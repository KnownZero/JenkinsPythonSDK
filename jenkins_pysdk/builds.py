import re
from collections.abc import Generator
from typing import List, Optional
import orjson
import pprint

from pydantic import HttpUrl

from jenkins_pysdk.response_objects import JenkinsActionObject
from jenkins_pysdk.jenkins_exceptions import JenkinsGeneralException
from jenkins_pysdk.consts import Endpoints


__all__ = ["Builds", "Build"]


class Build:
    def __init__(self, jenkins, build_url: HttpUrl):
        self._jenkins = jenkins
        self._build_url = build_url
        self._raw = self._get_raw()

    def _get_raw(self) -> orjson.loads:
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=self._build_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            pass  # TODO: Something here
        return orjson.loads(resp_obj.content)

    @property
    def number(self) -> int:
        return int(self._raw['number'])

    def console(self, progressive=False, html=False) -> str or Exception:
        url = self._jenkins._build_url(Endpoints.Builds.BuildConsoleText, prefix=self._build_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            return JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to fetch build logs.")
        return resp_obj.content

    @property
    def delete(self) -> JenkinsActionObject:
        url = self._jenkins._build_url(Endpoints.Builds.Delete, prefix=self._build_url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url)
        msg = f"[{resp_obj.status_code}] Successfully deleted build ({self.number})."
        if resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to delete build ({self.number})."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    @property
    def changes(self) -> str or Exception:
        # TODO: Change this junk XML output
        url = self._jenkins._build_url(Endpoints.Builds.Changes, prefix=self._build_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            return JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to fetch build changes.")
        return resp_obj.content

    def rebuild(self):
        # TODO: Check for plugin and rebuild
        raise NotImplemented

    @property
    def timings(self):
        # TODO: Whatever this is going to be
        raise NotImplemented

    @property
    def next(self):
        # TODO: Return next build
        # next_url = re.sub(r"")
        # yield Build(self._jenkins, next_url)
        raise NotImplemented

    @property
    def previous(self):
        # TODO: Return previous build
        raise NotImplemented

    @property
    def url(self):
        return self._build_url

    @property
    def result(self) -> str:
        return str(self._raw['result'])

    @property
    def duration(self) -> int:
        return int(self._raw['duration'])

    @property
    def done(self) -> bool:
        if bool(self._raw['inProgress']):
            return False
        return True

    @property
    def description(self) -> str:
        return str(self._raw['description'])

    @property
    def artifacts(self):
        raise NotImplementedError


class Builds:
    def __init__(self, jenkins, job_url: HttpUrl):
        self._jenkins = jenkins
        self._job_url = job_url

    def search(self, build_number: int) -> Build:
        """
        Fetch a build from build history.
        """
        return self._fetch_build(build_number)

    @property
    def total(self) -> int or Exception:
        """
        Get total number of saved builds.
        """
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=self._job_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            return JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to fetch job information.")

        data = orjson.loads(resp_obj.content)
        return len(data.get('builds', []))

    def iter(self) -> Generator[Build]:
        url = self._jenkins._build_url(Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        code = resp_obj.status_code
        if code != 200:
            return JenkinsGeneralException(f"[{code}] Failed to fetch job information.")

        data = orjson.loads(resp_obj.content)
        for build in data.get('builds', []):
            yield Build(self._jenkins, build['url'])

    def list(self) -> List[Build]:
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
        return Build(self._jenkins, data['builds'][index]['url'])

    @property
    def latest(self) -> Build:
        """
        Return the last build.
        """
        # TODO: Add filtering for success=False, failed=False
        return self._fetch_build(0)

    @property
    def oldest(self) -> Build:
        """
        Return the oldest saved build.
        """
        # TODO: Add filtering for success=False, failed=False
        return self._fetch_build(-1)

    def build(self, parameters: Optional[dict] = None) -> JenkinsActionObject:
        """
        Trigger a new build
        """
        if parameters:
            pass
        url = self._jenkins._build_url(Endpoints.Builds.Build, prefix=self._job_url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, data=parameters)
        if resp_obj.status_code in [200, 201]:
            msg = f"[{resp_obj.status_code}] Successfully triggered a new build."
            obj = JenkinsActionObject(request=req_obj, response=resp_obj, content=msg, status_code=resp_obj.status_code)
            obj._raw = resp_obj._raw
            return obj
        raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to trigger a new build.")

