from collections.abc import Generator
from typing import List

import orjson
from pydantic import HttpUrl

from jenkins_pysdk.objects import JenkinsValidateJob, JenkinsActionObject, Jobs as r_jobs
from jenkins_pysdk.exceptions import JenkinsJobNotFound, JenkinsFolderNotFound, JenkinsGeneralException
from jenkins_pysdk.consts import Endpoints, Class, XML_HEADER_DEFAULT, XML_POST_HEADER
from jenkins_pysdk.builders import Builder
from jenkins_pysdk.builds import Builds

__all__ = ["Jobs", "Folders", "Job", "Folder"]


class Job:
    """
    Represents a job in Jenkins.

    :param jenkins: The Jenkins instance associated with the job.
    :type jenkins: Jenkins
    :param job_path: The path of the job.
    :type job_path: str
    :param job_url: The URL of the job.
    :type job_url: str
    """

    def __init__(self, *, jenkins, job_path, job_url):
        self._job_path = job_path
        self._job_url = job_url
        self._jenkins = jenkins

    def disable(self) -> JenkinsActionObject:
        """
        Disable the job.

        :return: Result of the request to disable the job.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Jobs.Disable, prefix=self._job_url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url)
        msg = f"[{resp_obj.status_code}] Successfully disabled {self._job_path}."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to disable {self._job_path}."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    @property
    def url(self) -> HttpUrl:
        """
        Get the URL of the job.

        :return: The URL of the job.
        :rtype: :class:`HttpUrl`
        """
        return HttpUrl(self._job_url)

    @property
    def path(self) -> str:
        """
        Get the path of the job.

        :return: The path of the job.
        :rtype: str
        """
        return self._job_path

    def enable(self) -> JenkinsActionObject:
        """
        Enable the job.

        :return: The outcome of enabling the job.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Jobs.Enable, prefix=self._job_url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url)
        msg = f"[{resp_obj.status_code}] Successfully enabled {self._job_path}."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to enable {self._job_path}."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def reconfig(self, xml: str or Builder = None) -> JenkinsActionObject:
        """
        Reconfigure the job.

        :param xml: The XML configuration to use for reconfiguration.
        :type xml: str, optional
        :return: The outcome of reconfiguring the job.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Jobs.Xml, prefix=self._job_url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_POST_HEADER,
                                                     data=str(xml))
        msg = f"[{resp_obj.status_code}] Successfully reconfigured {self._job_path}."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to reconfigure {self._job_path}."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def delete(self) -> JenkinsActionObject:
        """
        Delete the folder.

        :return: Result of the delete operation.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        url = self._jenkins._build_url("/", prefix=self._job_url)
        req_obj, resp_obj = self._jenkins._send_http(method="DELETE", url=url)
        msg = f"[{resp_obj.status_code}] Successfully deleted job."
        if resp_obj.status_code != 204:
            msg = f"[{resp_obj.status_code}] Failed to delete job."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    @property
    def config(self) -> str:
        """
        Get the XML configuration of the job.

        :return: The XML configuration of the job.
        :rtype: str
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Jobs.Xml, prefix=self._job_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url, headers=XML_HEADER_DEFAULT)
        code = resp_obj.status_code
        if code != 200:
            raise JenkinsGeneralException(f"[{code}] Failed to download job XML.")
        return resp_obj.content

    @property
    def builds(self) -> Builds:
        """
        Access the builds associated with this job.

        :return: Builds associated with this job.
        :rtype: :class:`builds.Builds`
        """
        return Builds(self._jenkins, self._job_url)


class Jobs:
    def __init__(self, jenkins):
        """
        Interact with Jobs on the Jenkins instance.

        :param jenkins: Connection to Jenkins instance.
        :type jenkins: Jenkins
        """
        self._jenkins = jenkins

    def search(self, job_path: str) -> Job:
        """
        Search for a job within Jenkins.

        :param job_path: The path of the job to search for.
        :type job_path: str
        :return: The job object.
        :rtype: :class:`Job`
        :raises: JenkinsJobNotFound: If the job wasn't found.
        """
        validated = self._validate_job(job_path)
        if not validated.is_valid:
            raise JenkinsJobNotFound(f"Could not retrieve {job_path} because it doesn't exist.")
        return Job(jenkins=self._jenkins, job_path=job_path, job_url=validated.url)

    def is_job(self, path: str) -> bool:
        """
        Checks if the path corresponds to a job in Jenkins.

        :param path: The path of the job to check.
        :type path: str
        :return: True if the path corresponds to a job, False otherwise.
        :rtype: bool
        :raises JenkinsGeneralException: If a general exception occurs.
        :raises JenkinsJobNotFound: If the job is not found.
        """
        built = self._jenkins._build_job_http_path(path)
        endpoint = f"{built}/{Endpoints.Instance.Standard}"
        url = self._jenkins._build_url(endpoint)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code == 404:
            raise JenkinsJobNotFound(f"[{resp_obj.status_code}] {path} not found.")
        else:
            data = orjson.loads(resp_obj.content)
            if data['_class'] != Class.Folder:
                return True
            return False

    def _validate_job(self, job_path: str) -> JenkinsValidateJob or JenkinsGeneralException:
        job = self._jenkins._build_job_http_path(job_path)
        url = self._jenkins._build_url(job)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code == 200:
            validated = True
        elif resp_obj.status_code in (400, 404):
            validated = False
        else:
            validated = None
        if not self.is_job(job_path):
            raise JenkinsGeneralException(f"{job_path} is a folder. Please use folders.")

        obj = JenkinsValidateJob(url=url, is_valid=validated)
        obj._raw = resp_obj
        return obj

    def _create_job(self, job_name: str, xml, mode: r_jobs, folder_path: HttpUrl = None) \
            -> JenkinsActionObject or JenkinsFolderNotFound:
        create_endpoint = Endpoints.Jobs.Create
        endpoint = f"{folder_path}/{create_endpoint}" if folder_path else create_endpoint
        url = self._jenkins._build_url(endpoint)
        params = {"name": job_name, "mode": mode}
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_HEADER_DEFAULT,
                                                     params=params, data=xml)
        if resp_obj.status_code == 404:
            raise JenkinsFolderNotFound(f"Parent path {str(folder_path)} not found.")
        elif resp_obj.status_code == 200:
            msg = f"[{resp_obj.status_code}] Successfully created {job_name}."
        else:
            msg = f"[{resp_obj.status_code}] Failed to create job {job_name}."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def create(self, job_path: str, xml: str, *args: r_jobs) -> JenkinsActionObject or JenkinsGeneralException:
        """
        Create a job on the Jenkins instance.

        :param job_path: The path where the job should be created.
        :type job_path: str
        :param xml: XML configuration for the job.
        :type xml: str
        :param args: Additional parameters for job creation.
        :type args: :class:`objects.Jobs` (Default: Freestyle)
        :return: Object representing the result of the creation action.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        try:
            self.is_job(job_path)
            raise JenkinsGeneralException(f"{job_path} already exists.")
        except JenkinsJobNotFound:
            pass

        # TODO: Add all other jobs types
        mode = args[0].value if args else Class.Freestyle
        job_name, job_parent = self._jenkins._get_folder_parent(job_path)
        built = self._jenkins._build_job_http_path(job_parent)
        created = self._create_job(job_name, xml, mode, built)
        return created

    def iter(self, folder=None, _paginate=0) -> Generator[Job]:
        """
        Iterate through jobs in the Jenkins instance.

        :param folder: The folder to iterate through. If None, iterate through all jobs.
        :type folder: str, optional
        :param _paginate: Pagination flag. Defaults to 0 (disabled).
        :type _paginate: int, optional
        :return: Generator yielding Job objects.
        :rtype: Generator[:class:`Job`]
        """
        if folder:
            path = self._jenkins._build_job_http_path(folder)
            url = self._jenkins._build_url(path + "/")
            yield from self._fetch_job_iter(url)
        else:
            start = 0

            while True:
                limit = _paginate + start
                job_param = Endpoints.Jobs.Iter
                if _paginate > 0:
                    job_param = f"{job_param}{{{start},{limit}}}"
                params = {"tree": job_param}
                url = self._jenkins._build_url(Endpoints.Instance.Standard)

                req_obj, resp_obj = self._jenkins._send_http(url=url, params=params)
                if resp_obj.status_code > 200 and start > 0:
                    break  # Pagination finished, Jenkins doesn't return a nice response
                elif resp_obj.status_code != 200:
                    raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to get job information.")

                data = orjson.loads(resp_obj.content)
                data = self._jenkins._validate_url_returned_from_instance(data)

                jobs = data.get('jobs', [])
                for item in jobs:
                    if item['_class'] == Class.Folder:
                        yield from self._fetch_job_iter(item['url'])
                    elif item['_class'] != Class.Folder:
                        yield from self._fetch_job(item['url'])

                if not jobs:
                    break

                if _paginate > 0:
                    start += _paginate + 1
                elif _paginate == 0:
                    break

    def _fetch_job_iter(self, job_url) -> Generator[Job]:
        # Pagination not needed here because function repeats itself if needed
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=job_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)

        try:
            if data['_class'] != Class.Folder:
                yield Job(jenkins=self._jenkins, job_path=data['fullName'], job_url=data['url'])
            elif data['_class'] == Class.Folder:
                for item in data.get('jobs', []):
                    yield from self._fetch_job_iter(item['url'])
        except Exception as error:
            print(error)

    def _fetch_job(self, job_url) -> Generator[Job]:
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=job_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)
        yield Job(jenkins=self._jenkins, job_path=data['fullName'], job_url=data['url'])

    def list(self, folder=None, _paginate=0) -> List[Job]:
        """
        Retrieve a list of jobs from Jenkins.

        :param folder: (Optional) The folder from which to retrieve jobs.
        :type folder: str or None
        :param _paginate: (Optional) The number of jobs to retrieve per paginated request.
            Set to 0 to disable pagination.
        :type _paginate: int
        :return: A list of Job objects representing the jobs in the specified folder.
        :rtype: List[:class:`Job`]
        """
        return [item for item in self.iter(folder=folder, _paginate=_paginate)]

    @property
    def tree(self):
        """
        View all jobs in a pretty tree-like structure.

        :return: Tree-like structure of all jobs.
        """
        raise NotImplemented

    def api(self):
        """
        Run your own query and return jobs data objects.

        :return: Jobs data objects.
        """
        raise NotImplemented


class Folder:
    def __init__(self, *, jenkins, folder_path, folder_url):
        """
        Interact with Folders on the Jenkins instance.

        :param jenkins: Connection to Jenkins instance
        """
        self._folder_path = folder_path
        self._folder_url = folder_url
        self._jenkins = jenkins

    def reconfig(self, xml: str or Builder.Folder) -> JenkinsActionObject:
        """
        Reconfigure the folder.

        :param xml: The XML configuration or Builder.Folder object.
        :type xml: str or Builder.Folder
        :return: Action outcome
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Jobs.Xml, prefix=self._folder_url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_POST_HEADER,
                                                     data=xml)
        msg = f"[{resp_obj.status_code}] Successfully reconfigured {self._folder_path}."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to reconfigure {self._folder_path}."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    @property
    def url(self) -> HttpUrl:
        """
        Get the URL of the folder.

        :return: The URL of the folder.
        :rtype: HttpUrl
        """
        return HttpUrl(self._folder_url)

    @property
    def path(self) -> str:
        """
        Get the path of the folder.

        :return: The path of the folder.
        :rtype: str
        """
        return self._folder_path

    def copy(self, new_job_name: str, copy_job_name: str) -> JenkinsActionObject:
        """
        Copy an item into the existing path.

        :param new_job_name: The name of the new job.
        :type new_job_name: str
        :param copy_job_name: The name of the job to copy.
        :type copy_job_name: str
        :return: Result of the copy operation.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        import re
        params = {"name": new_job_name, "mode": "copy", "from": copy_job_name}
        url = self._jenkins._build_url(Endpoints.Jobs.Create, prefix=self._folder_url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, params=params)
        msg = f"[{resp_obj.status_code}] Successfully copied {copy_job_name} to {new_job_name}."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code == 400:
            if re.search(r"A job already exists with the name", str(resp_obj.content)):  # TODO: This is method unreliable
                raise JenkinsGeneralException(f"{new_job_name} already exists.")
            msg = f"[{resp_obj.status_code}] Failed to copy folder."
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to copy folder."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def delete(self) -> JenkinsActionObject:
        """
        Delete the folder.

        :return: Result of the delete operation.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url("/", prefix=self._folder_url)
        req_obj, resp_obj = self._jenkins._send_http(method="DELETE", url=url)
        msg = f"[{resp_obj.status_code}] Successfully deleted folder."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 204:
            msg = f"[{resp_obj.status_code}] Failed to delete folder."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def create(self, folder_name: str, xml: str or Builder.Folder) -> JenkinsActionObject:
        """
        Creates sub-folders in the current path.

        :param folder_name: The name of the folder to create.
        :type folder_name: str
        :param xml: The XML configuration for the folder. Can be a string or a Builder.Folder object.
        :type xml: str or Builder.Folder
        :return: The result of the action.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        try:
            return Folders(self._jenkins)._create_folder(folder_name, xml, self.path)
        except:
            raise

    @property
    def config(self) -> str:
        """
        Get the XML configuration of the folder.

        :return: The XML configuration of the folder.
        :rtype: str
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Jobs.Xml, prefix=self._folder_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url, headers=XML_HEADER_DEFAULT)
        code = resp_obj.status_code
        if code != 200:
            raise JenkinsGeneralException(f"[{code}] Failed to download job XML.")
        return resp_obj.content


class Folders:
    def __init__(self, jenkins):
        """
        Interact with Folders on the Jenkins instance.

        :param jenkins: Connection to Jenkins instance.
        """
        self._jenkins = jenkins

    def search(self, folder_path: str) -> Folder:
        """
        Search for a folder within the Jenkins instance.

        :param folder_path: The path of the folder to search for.
        :type folder_path: str
        :return: The folder object if found.
        :rtype: :class:`Folder`
        :raises JenkinsFolderNotFound: If the folder was not found.
        """
        validated = self._validate_job(folder_path)
        if not validated.is_valid:
            raise JenkinsFolderNotFound(f"Could not retrieve {folder_path} because it doesn't exist.")
        return Folder(jenkins=self._jenkins, folder_path=folder_path, folder_url=validated.url)

    def _validate_job(self, job_path) -> JenkinsValidateJob:
        job = self._jenkins._build_job_http_path(job_path)
        url = self._jenkins._build_url(job)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code == 200:
            validated = True
        elif resp_obj.status_code in (400, 404):
            validated = False
        else:
            validated = None
        if not self.is_folder(job_path):
            raise JenkinsGeneralException(f"{job_path} is not a folder. Please use jobs.")

        obj = JenkinsValidateJob(url=url, is_valid=validated)
        obj._raw = resp_obj
        return obj

    def is_folder(self, path: str) -> bool:
        """
        Checks if the path corresponds to a folder in Jenkins.

        :param path: The path to check.
        :type path: str
        :return: True if the path corresponds to a folder, False otherwise.
        :rtype: bool
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        built = self._jenkins._build_job_http_path(path)
        url = self._jenkins._build_url(built, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            raise JenkinsFolderNotFound(f"{path} not found.")
        data = orjson.loads(resp_obj.content)
        if data['_class'] == Class.Folder:
            return True
        return False

    def _create_folder(self, folder_name: str, xml, folder_path: str = None) -> JenkinsActionObject:
        endpoint = self._jenkins._build_job_http_path(folder_path)
        url = self._jenkins._build_url(endpoint, suffix=Endpoints.Jobs.Create)
        params = {"name": folder_name, "mode": Class.Folder}
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_HEADER_DEFAULT,
                                                     params=params, data=xml)
        if resp_obj.status_code == 404:
            raise JenkinsFolderNotFound(f"Parent path {str(folder_path)} not found.")
        elif resp_obj.status_code == 200:
            msg = f"[{resp_obj.status_code}] Successfully created {folder_name}."
        else:
            msg = f"[{resp_obj.status_code}] Failed to create folder {folder_name}."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def create(self, folder_path: str, xml: str or Builder.Folder) -> JenkinsActionObject:
        """
        Creates a folder at the specified path with the given XML configuration.

        :param folder_path: The path where the folder will be created.
        :type folder_path: str
        :param xml: The XML configuration for the folder.
        :type xml: str or Builder.Folder
        :return: The result of the folder creation operation.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsFolderNotFound: If the folder was not found.
        """
        folder_name, folder_parent = self._jenkins._get_folder_parent(folder_path)

        try:
            built_path = self._jenkins._build_job_http_path(folder_name, folder_parent)
            self.search(built_path)
            raise JenkinsGeneralException(f"{folder_path} already exists.")
        except JenkinsFolderNotFound:
            pass

        try:
            built_path = self._jenkins._build_job_http_path(folder_parent)
            return self._create_folder(folder_name, xml, built_path)
        except JenkinsFolderNotFound as error:
            if not self.is_folder(folder_parent):
                raise JenkinsFolderNotFound(f"Failed to create folder because parent path not found: {folder_parent}.")
            raise error

    def iter(self, folder: str = None, _paginate: int = 0) -> Generator[Folder]:
        """
        Iterate over folders within the specified folder.

        :param folder: The path of the parent folder. If None, iterate over all folders.
        :type folder: str, optional
        :param _paginate: Number of items to paginate. Default is 0 (no pagination).
        :type _paginate: int, optional
        :return: A generator yielding Folder objects.
        :rtype: Generator[:class:`Folder`]
        """
        if folder:
            path = self._jenkins._build_job_http_path(folder)
            url = self._jenkins._build_url(path + "/")
            yield from self._fetch_folder_iter(url)
        else:
            start = 0

            while True:
                limit = _paginate + start
                job_param = Endpoints.Jobs.Iter
                if _paginate > 0:
                    job_param = f"{job_param}{{{start},{limit}}}"
                params = {"tree": job_param}
                json_url = self._jenkins._build_url(Endpoints.Instance.Standard)

                req_obj, resp_obj = self._jenkins._send_http(url=json_url, params=params)
                if resp_obj.status_code > 200 and start > 0:
                    break  # Pagination finished, Jenkins doesn't return a nice response
                elif resp_obj.status_code != 200:
                    raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to get folder information.")

                data = orjson.loads(resp_obj.content)
                data = self._jenkins._validate_url_returned_from_instance(data)

                folders = data.get('jobs', [])
                for item in folders:
                    if item['_class'] == Class.Folder:
                        yield from self._fetch_folder_iter(item['url'])

                if not folders:
                    break

                if _paginate > 0:
                    start += _paginate + 1
                elif _paginate == 0:
                    break

    def _fetch_folder_iter(self, folder_url) -> Generator[Folder]:
        json_url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=folder_url)
        req_obj, resp_obj = self._jenkins._send_http(url=json_url)
        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)

        if data['_class'] == Class.Folder:
            folders = data.get('jobs', [])
            for item in folders:
                yield from self._fetch_folder_iter(item['url'])
            if not folders:
                yield from self._fetch_folder(data['url'])

    def _fetch_folder(self, folder_url) -> Generator[Folder]:
        json_url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=folder_url)
        req_obj, resp_obj = self._jenkins._send_http(url=json_url)
        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)
        yield Folder(jenkins=self._jenkins, folder_path=data['fullName'], folder_url=data['url'])

    def list(self, folder=None, _paginate=0) -> List[Folder]:
        """
        Retrieve a list of folder from Jenkins.

        :param folder: (Optional) The folder from which to retrieve jobs.
        :type folder: str or None
        :param _paginate: (Optional) The number of jobs to retrieve per paginated request.
            Set to 0 to disable pagination.
        :type _paginate: int
        :return: A list of Job objects representing the jobs in the specified folder.
        :rtype: List[:class:`Folder`]
        """
        return [item for item in self.iter(folder=folder, _paginate=_paginate)]

    @property
    def tree(self):
        """
        Get a hierarchical representation of all folders.

        :return: A tree-like structure representing all folders.
        """
        raise NotImplemented

    def api(self):
        """
        Run a custom query and return folder data objects.

        :return: Data objects representing folders.
        """
        raise NotImplemented
