from collections.abc import Generator
from typing import List
import orjson
import pprint

from pydantic import HttpUrl

from jenkins_pysdk.response_objects import JenkinsValidateJob, JenkinsActionObject, Views as r_views
from jenkins_pysdk.jenkins_exceptions import JenkinsViewNotFound, JenkinsGeneralException
from jenkins_pysdk.consts import Endpoints, Class, XML_HEADER_DEFAULT, XML_POST_HEADER
from jenkins_pysdk.builders import Builder

__all__ = ["Views"]


class View:
    def __init__(self, /, *, jenkins, name, url):
        self._jenkins = jenkins
        self._view_name = name
        self._view_url = url

    @property
    def url(self) -> HttpUrl:
        return HttpUrl(self._view_url)

    @property
    def name(self) -> str:
        return self._view_name

    def reconfig(self, xml: str = None, builder: Builder.View = None) -> JenkinsActionObject:
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
    def delete(self):
        url = self._jenkins._build_url("/", prefix=self._view_url)
        req_obj, resp_obj = self._jenkins._send_http(method="DELETE", url=url)
        msg = f"[{resp_obj.status_code}] Successfully deleted view."
        if resp_obj.status_code != 204:
            msg = f"[{resp_obj.status_code}] Failed to delete view."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    @property
    def config(self):
        url = f"{self._view_url}/{Endpoints.Jobs.Xml}"  # TODO: Fix this
        req_obj, resp_obj = self._jenkins._send_http(url=url, headers=XML_HEADER_DEFAULT)
        code = resp_obj.status_code
        if code != 200:
            return JenkinsGeneralException(f"[{code}] Failed to download view XML.")
        return resp_obj.content


class Views:
    def __init__(self, jenkins):
        """
        Interact with Jobs on the Jenkins instance.
        :param jenkins: Connection to Jenkins instance
        """
        self._jenkins = jenkins

    def search(self, view_path: str) -> View:
        # TODO: Get view_name from API as resutls are won't be consistent with User Views
        validated = self._validate_view(view_path)
        if not validated.is_valid:
            raise JenkinsViewNotFound(f"Could not retrieve {view_path} because it doesn't exist.")
        return View(jenkins=self._jenkins, name=view_path, url=validated.url)

    def is_view(self, path: str) -> bool:
        """
        Checks if the path is a Folder.
        :param path: The job path
        :return:
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

        # url = self._jenkins._build_url(Endpoints.Views.Create)
        # params = {"name": view_name, "mode": mode}
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
        try:
            self.is_view(name)
            raise JenkinsGeneralException(f"{name} already exists.")
        except JenkinsViewNotFound:
            pass

        mode = args[0].value if args else Class.ListView
        created = self._create_view(name, xml, mode)
        return created

    def iter(self, /, folder=None, _paginate=0) -> Generator[View]:
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
        View all jobs in a pretty tree-like structure.
        :return:
        """
        raise NotImplemented

    def api(self):
        """
        Run your own query and return jobs data objects.
        :return:
        """
        raise NotImplemented
