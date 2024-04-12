from collections.abc import Generator
from typing import List
import orjson

from pydantic import HttpUrl

from jenkins_pysdk.objects import JenkinsValidateJob, JenkinsActionObject, Views as r_views
from jenkins_pysdk.exceptions import JenkinsViewNotFound, JenkinsGeneralException
from jenkins_pysdk.consts import Endpoints, Class, XML_HEADER_DEFAULT, XML_POST_HEADER
from jenkins_pysdk.builders import Builder

__all__ = ["Views"]


class View:
    def __init__(self, /, *, jenkins, name, url):
        """
        Interact with Views on the Jenkins instance.

        :param jenkins: Connection to Jenkins instance.
        :type jenkins: Jenkins
        :param name: The name of the view.
        :type name: str
        :param url: The URL of the view.
        :type url: HttpUrl
        """
        self._jenkins = jenkins
        self._view_name = name
        self._view_url = url

    @property
    def url(self) -> HttpUrl:
        """
        Get the URL of the view.

        :return: The URL of the view.
        :rtype: HttpUrl
        """
        return HttpUrl(self._view_url)

    @property
    def name(self) -> str:
        """
        Get the name of the view.

        :return: The name of the view.
        :rtype: str
        """
        return self._view_name

    def reconfig(self, xml: str = None, builder: Builder.View = None) -> JenkinsActionObject:
        """
        Reconfigure the view with XML configuration or a builder.

        :param xml: The XML configuration of the view, defaults to None.
        :type xml: str, optional
        :param builder: The builder object to build the view, defaults to None.
        :type builder: Builder.View, optional
        :return: Jenkins action object indicating the reconfiguration status.
        :rtype: JenkinsActionObject
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        if not xml and not builder:
            raise JenkinsGeneralException("Missing view configuration.")
        url = self._jenkins._build_url(Endpoints.Jobs.Xml, prefix=self._view_url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_POST_HEADER,
                                                     data=xml)
        msg = f"[{resp_obj.status_code}] Successfully reconfigured {self._view_name}."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to reconfigure {self._view_name}."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    @property
    def delete(self) -> JenkinsActionObject:
        """
        Delete the view.

        :return: Jenkins action object indicating the delete status.
        :rtype: JenkinsActionObject
        """
        url = self._jenkins._build_url("/", prefix=self._view_url)
        req_obj, resp_obj = self._jenkins._send_http(method="DELETE", url=url)
        msg = f"[{resp_obj.status_code}] Successfully deleted view."
        if resp_obj.status_code != 204:
            msg = f"[{resp_obj.status_code}] Failed to delete view."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    @property
    def config(self) -> str:
        """
        Get the XML configuration of the view.

        :return: The XML configuration of the view.
        :rtype: str
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Jobs.Xml, prefix=self._view_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url, headers=XML_HEADER_DEFAULT)
        code = resp_obj.status_code
        if code != 200:
            raise JenkinsGeneralException(f"[{code}] Failed to download view XML.")
        return resp_obj.content


class Views:
    def __init__(self, jenkins):
        """
        Interact with Views on the Jenkins instance.

        :param jenkins: Connection to the Jenkins instance.
        """
        self._jenkins = jenkins

    def search(self, view_path: str) -> View:
        """
        Search for a view within Jenkins.

        :param view_path: The path of the view to search for.
        :type view_path: str
        :return: The View object representing the found view.
        :rtype: View
        :raises JenkinsViewNotFound: If the view was not found.
        """
        # TODO: Get view_name from API as results are won't be consistent with User Views
        validated = self._validate_view(view_path)
        if not validated.is_valid:
            raise JenkinsViewNotFound(f"Could not retrieve {view_path} because it doesn't exist.")
        return View(jenkins=self._jenkins, name=view_path, url=validated.url)

    def is_view(self, path: str) -> bool:
        """
        Check if the specified path corresponds to a view in Jenkins.

        :param path: The path to check.
        :type path: str
        :return: True if the path corresponds to a view, False otherwise.
        :rtype: bool
        """
        built = self._jenkins._build_view_http_path(path)
        endpoint = f"{built}/{Endpoints.Instance.Standard}"
        url = self._jenkins._build_url(endpoint)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code == 404:
            raise JenkinsViewNotFound(f"[{resp_obj.status_code}] {path} not found.")
        else:
            data = orjson.loads(resp_obj.content)
            if data['_class'] != Class.Folder:
                return True
            return False

    def _validate_view(self, view_path) -> JenkinsValidateJob:  # TODO: Review what the heck this is doing?
        job = self._jenkins._build_view_http_path(view_path)
        url = self._jenkins._build_url(job)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code == 200:
            validated = True
        elif resp_obj.status_code in (400, 404):
            validated = False
        else:
            validated = None
        if not self.is_view(view_path):
            raise JenkinsGeneralException(f"{view_path} is not a view.")

        obj = JenkinsValidateJob(url=url, is_valid=validated)
        obj._raw = resp_obj
        return obj

    def _create_view(self, view_name: str, xml, mode: r_views) -> JenkinsActionObject:
        # TODO: Add mode with params
        params = {"mode": mode}
        url = self._jenkins._build_url(f"/{view_name}")

        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_POST_HEADER,
                                                     params=params, data=xml)
        if resp_obj.status_code == 200:
            msg = f"[{resp_obj.status_code}] Successfully created {view_name}."
        else:
            msg = f"[{resp_obj.status_code}] Failed to create view {view_name}."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def create(self, name: str, xml: str or Builder.View, *args: r_views) -> JenkinsActionObject:
        """
        Create a new view.

        :param name: The name of the new view.
        :type name: str
        :param xml: The XML configuration or Builder.View object for the new view.
        :type xml: str or Builder.View
        :param args: Additional parameters for the view creation.
        :type args: r_views
        :return: JenkinsActionObject indicating the result of the creation.
        :rtype: JenkinsActionObject
        """
        try:
            self.is_view(name)
            raise JenkinsGeneralException(f"{name} already exists.")
        except JenkinsViewNotFound:
            pass

        mode = args[0].value if args else Class.ListView
        created = self._create_view(name, xml, mode)
        return created

    def iter(self, /, folder=None, _paginate=0) -> Generator[View]:
        """
        Iterate through views.

        :param folder: Folder to iterate through. Default is None.
        :type folder: Any, optional
        :param _paginate: Pagination option. Default is 0 (no pagination).
        :type _paginate: int, optional
        :return: A generator yielding View objects.
        :rtype: Generator[View]
        """
        if folder:
            path = self._jenkins._build_job_http_path(folder)
            url = self._jenkins._build_url(path + "/")
            yield from self._fetch_view_iter(url)
        else:
            url = self._jenkins._build_url("")  # TODO: Remove copy & paste
            start = 0

            while True:
                limit = _paginate + start
                job_param = f"views[fullName,url,jobs[fullName,url,jobs]]"  # TODO: Remove hardcode
                tree_param = f"{job_param}{{{start},{limit}}}"
                params = {"tree": tree_param}
                url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=url)

                req_obj, resp_obj = self._jenkins._send_http(url=url, params=params)
                if resp_obj.status_code > 200 and start > 0:
                    break  # Pagination finished, Jenkins doesn't return a nice response

                data = orjson.loads(resp_obj.content)
                data = self._jenkins._validate_url_returned_from_instance(data)

                jobs = data.get('jobs', [])
                for item in jobs:
                    if item['_class'] == Class.Folder:
                        yield from self._fetch_view_iter(item['url'])
                    elif item['_class'] != Class.Folder:
                        yield from self._fetch_view(item['url'])

                if not jobs:
                    break

                if _paginate > 0:
                    start += _paginate

    def _fetch_view_iter(self, job_url) -> Generator[View]:
        # Pagination not needed here because function repeats itself if needed
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=job_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)

        try:
            if data['_class'] != Class.Folder:
                yield View(jenkins=self._jenkins, name=data['fullName'], url=data['url'])
            elif data['_class'] == Class.Folder:
                for item in data.get('jobs', []):
                    yield from self._fetch_view_iter(item['url'])
        except Exception as error:
            print(error)

    def _fetch_view(self, view_url) -> Generator[View]:
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=view_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)
        yield View(jenkins=self._jenkins, name=data['fullName'], url=data['url'])

    def list(self, folder=None, _paginate=0) -> List[View]:
        return [item for item in self.iter(folder=folder, _paginate=_paginate)]

    @property
    def tree(self):
        """
        View all views in a pretty tree-like structure.

        :return: None
        :rtype: None
        """
        raise NotImplemented

    def api(self):
        """
        Run your own query and return views data objects.

        :return: None
        :rtype: None
        """
        raise NotImplemented
