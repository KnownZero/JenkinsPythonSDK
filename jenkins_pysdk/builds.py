import re
from collections.abc import Generator
from typing import List, Optional

import orjson
from pydantic import HttpUrl

from jenkins_pysdk.objects import JenkinsActionObject
from jenkins_pysdk.exceptions import JenkinsGeneralException, JenkinsNotFound
from jenkins_pysdk.consts import Endpoints, FORM_HEADER_DEFAULT


__all__ = ["Builds", "Build"]


class Build:
    def __init__(self, jenkins, build_url: HttpUrl):
        """
        Initialize a Build object.

        :param jenkins: The Jenkins instance associated with the build.
        :type jenkins: jenkins_pysdk.jenkins.Jenkins
        :param build_url: The URL of the build.
        :type build_url: HttpUrl
        """
        self._jenkins = jenkins
        self._build_url = build_url
        self._raw = self._get_raw()

    def _get_raw(self) -> orjson.loads:
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=self._build_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to get build information.")
        return orjson.loads(resp_obj.content)

    @property
    def number(self) -> int:
        """
        Get the build number.

        :return: The build number.
        :rtype: int
        """
        return int(self._raw['number'])

    @property
    def timestamp(self) -> int:
        """
        Get the build timestamp.

        :return: The build timestamp.
        :rtype: int
        """
        return int(self._raw['timestamp'])

    @property
    def description(self) -> str:
        """
        Get the build description.

        :return: The build description.
        :rtype: str
        """
        return str(self._raw['description'])

    def console(self, progressive=False, html=False) -> str:
        """
        Retrieve the console output of the build.

        :param progressive: Whether to retrieve progressive console output.
        :type progressive: bool, optional
        :param html: Whether to retrieve HTML-formatted console output.
        :type html: bool, optional
        :return: The console output of the build.
        :rtype: str
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        # TODO: Implement params
        url = self._jenkins._build_url(Endpoints.Builds.BuildConsoleText, prefix=self._build_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to fetch build logs.")
        return resp_obj.content

    def delete(self) -> JenkinsActionObject:
        """
        Delete the build.

        :return: Result of the delete request.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        url = self._jenkins._build_url(Endpoints.Builds.Delete, prefix=self._build_url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url)
        msg = f"[{resp_obj.status_code}] Successfully deleted build ({self.number})."
        if resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to delete build ({self.number})."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    @property
    def changes(self) -> str:
        """
        Get the changes associated with the build.

        :return: The changes associated with the build.
        :rtype: str
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        # TODO: Change this junk XML output
        url = self._jenkins._build_url(Endpoints.Builds.Changes, prefix=self._build_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to fetch build changes.")
        return resp_obj.content

    def rebuild(self) -> JenkinsActionObject:
        """
        Rebuild the build.

        :return: The result of the rebuild operation.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        try:
            enabled = self._jenkins.plugins.installed.search("rebuild")._plugin_info['enabled']
            if not enabled:
                raise JenkinsGeneralException(f"You must enable the rebuild plugin first!\n"
                                              f"https://plugins.jenkins.io/rebuild/")
        except JenkinsNotFound:
            raise JenkinsGeneralException(f"Operation not available. You are missing the rebuild plugin.\n"
                                          f"https://plugins.jenkins.io/rebuild/")
        url = self._jenkins._build_url(Endpoints.Builds.RebuildCurrent, prefix=self._build_url, suffix="/")
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=FORM_HEADER_DEFAULT)
        if resp_obj.status_code in [200, 201]:
            msg = f"[{resp_obj.status_code}] Successfully triggered a rebuild of this build ({self.number})."
            obj = JenkinsActionObject(request=req_obj, response=resp_obj, content=msg, status_code=resp_obj.status_code)
            obj._raw = resp_obj._raw
            return obj
        raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to trigger a rebuild of this build ({self.number}).")

    # @property
    # def timings(self):
    #     """
    #     Get the timings information of the build.
    #
    #     :return: Timings information of the build.
    #     :rtype: dict
    #     """
    #     # TODO: Whatever this is going to be
    #     raise NotImplemented

    @property
    def next(self) -> ...:
        """
        Get the next build in the build queue.

        :return: The next build in the build queue.
        :rtype: :class:`jenkins_pysdk.builds.Build`
        """
        build_number = re.search(r"(\d+)/$", str(self._build_url)).group(1)
        job_url = re.search(r'^(.*?)(?=/\d+/)', str(self._build_url)).group(1)
        return Builds(self._jenkins, job_url).search(int(build_number) + 1)

    @property
    def previous(self) -> ...:
        """
        Get the previous build in the build history.

        :return: The previous build in the build history.
        :rtype: :class:`jenkins_pysdk.builds.Build`
        """
        build_number = re.search(r"(\d+)/$", str(self._build_url)).group(1)
        job_url = re.search(r'^(.*?)(?=/\d+/)', str(self._build_url)).group(1)
        return Builds(self._jenkins, job_url).search(int(build_number) - 1)

    @property
    def url(self) -> str:
        """
        Get the URL of the build.

        :return: The URL of the build.
        :rtype: str
        """
        return str(self._build_url)

    @property
    def result(self) -> str:
        """
        Get the result of the build.

        :return: The result of the build.
        :rtype: str
        """
        return str(self._raw['result'])

    @property
    def duration(self) -> int:
        """
        Get the duration of the build.

        :return: The duration of the build in milliseconds.
        :rtype: int
        """
        return int(self._raw['duration'])

    @property
    def done(self) -> bool:
        """
        Check if the build has completed.

        :return: True if the build has completed, False otherwise.
        :rtype: bool
        """
        if bool(self._raw['inProgress']):
            return False
        return True

    @property
    def artifacts(self):
        """
        Get the artifacts of the build.

        :return: A list of artifacts associated with the build.
        :rtype: List[Artifact]
        """
        # TODO: Change rtype to class when ready
        raise NotImplementedError


class Builds:
    def __init__(self, jenkins, job_url: HttpUrl):
        """
        Initializes a Builds object.

        :param jenkins: The Jenkins instance.
        :type jenkins: jenkins_pysdk.jenkins.Jenkins
        :param job_url: The URL of the job.
        :type job_url: HttpUrl
        """
        self._jenkins = jenkins
        self._job_url = job_url

    def search(self, build_number: int) -> Build:
        """
        Fetches a specific build from the build history of the job.

        :param build_number: The number of the build to fetch.
        :type build_number: int
        :return: The Build object representing the requested build.
        :rtype: :class:`jenkins_pysdk.builds.Build`
        """
        return self._fetch_build(build_number)

    @property
    def total(self) -> int:
        """
        Get the total number of saved builds for the job.

        :return: The total number of saved builds.
        :rtype: int
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=self._job_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to fetch job information.")

        data = orjson.loads(resp_obj.content)
        return len(data.get('builds', []))

    def iter(self) -> Generator[Build]:
        """
        Iterate over builds in the build history of the job.

        :yield: A Build object representing each build in the build history.
        :rtype: Generator[:class:`jenkins_pysdk.builds.Build`]
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=self._job_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to fetch job information.")

        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)
        for build in data.get('builds', []):
            yield Build(self._jenkins, build['url'])

    def list(self) -> List[Build]:
        """
        Get a list of all builds in the build history of the job.

        :return: A list of Build objects representing each build in the build history.
        :rtype: List[:class:`jenkins_pysdk.builds.Build`]
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        return [b for b in self.iter()]

    def _fetch_build(self, index: int) -> Build:
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=self._job_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to fetch last job.")

        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)
        if not data.get('builds', []):
            raise JenkinsGeneralException("This job has no builds.")
        for build in data.get('builds', []):
            if int(build['number']) == index:
                return Build(self._jenkins, build['url'])
        else:
            raise JenkinsGeneralException(f"Build ({index}) was not found.")

    @property
    def latest(self) -> Build:
        """
        Retrieve the last build in the build history of the job.

        :return: The Build object representing the last build.
        :rtype: :class:`jenkins_pysdk.builds.Build`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        # TODO: Add filtering for success=False, failed=False
        try:
            return self.list()[0]
        except IndexError:
            raise JenkinsGeneralException("No builds")

    @property
    def oldest(self) -> Build:
        """
        Retrieve the oldest saved build in the build history of the job.

        :return: The Build object representing the oldest saved build.
        :rtype: :class:`jenkins_pysdk.builds.Build`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        # TODO: Add filtering for success=False, failed=False
        try:
            return self.list()[-1]
        except IndexError:
            raise JenkinsGeneralException("No builds.")

    def build(self, parameters: Optional[dict] = None, delay: int = 0) -> JenkinsActionObject:
        """
        Trigger a new build for the job with optional parameters.

        :param parameters: (Optional) parameters to be passed to the build.
        :type parameters: dict, optional
        :param delay: (Default: 0) Delay the build by X seconds
        :type delay: int
        :return: Result of the build trigger request.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        params = {"delay": f"{delay}sec"}
        endpoint = Endpoints.Builds.buildWithParameters if parameters else Endpoints.Builds.Build
        url = self._jenkins._build_url(endpoint, prefix=self._job_url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=FORM_HEADER_DEFAULT,
                                                     params=params, data=parameters)
        if resp_obj.status_code in [200, 201]:
            msg = f"[{resp_obj.status_code}] Successfully triggered a new build."
            obj = JenkinsActionObject(request=req_obj, response=resp_obj, content=msg, status_code=resp_obj.status_code)
            obj._raw = resp_obj._raw
            return obj
        raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to trigger a new build.")

    def rebuild_last(self) -> JenkinsActionObject:
        """
        Trigger a rebuild of the last build of the job.

        :return: Result of the rebuild operation.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        try:
            enabled = self._jenkins.plugins.installed.search("rebuild")._plugin_info['enabled']
            if not enabled:
                raise JenkinsGeneralException(f"You must enable the rebuild plugin first!\n"
                                              f"https://plugins.jenkins.io/rebuild/")
        except JenkinsNotFound:
            raise JenkinsGeneralException(f"Operation not available. You are missing the rebuild plugin.\n"
                                          f"https://plugins.jenkins.io/rebuild/")
        url = self._jenkins._build_url(Endpoints.Builds.RebuildLast, prefix=self._job_url, suffix="/")
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=FORM_HEADER_DEFAULT)
        if resp_obj.status_code in [200, 201]:
            msg = f"[{resp_obj.status_code}] Successfully triggered a rebuild of the last build."
            obj = JenkinsActionObject(request=req_obj, response=resp_obj, content=msg, status_code=resp_obj.status_code)
            obj._raw = resp_obj._raw
            return obj
        raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to trigger a rebuild of the last build.")
