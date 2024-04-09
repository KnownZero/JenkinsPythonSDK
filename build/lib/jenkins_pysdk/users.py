from collections.abc import Generator
from typing import List
import orjson
import pprint

from pydantic import HttpUrl

from jenkins_pysdk.response_objects import JenkinsActionObject
from jenkins_pysdk.jenkins_exceptions import JenkinsGeneralException, JenkinsNotFound
from jenkins_pysdk.consts import Endpoints, XML_POST_HEADER
from jenkins_pysdk.response_objects import Builder
from jenkins_pysdk.views import View as v_view
from jenkins_pysdk.credentials import Domain as c_domain


__all__ = ["Users", "User"]


class User:
    def __init__(self, jenkins, user_url: HttpUrl):
        self._jenkins = jenkins
        self._user_url = user_url
        self._raw = self._get_raw()

    @property
    def url(self):
        return self._user_url

    def _get_raw(self) -> orjson.loads:
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=self._user_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            pass  # TODO: Something here
        return orjson.loads(resp_obj.content)

    @property
    def description(self) -> str:
        return str(self._raw['description'])

    @property
    def name(self):
        return str(self._raw['fullName'])

    def credentials(self, domain="_") -> c_domain:
        """
        Search users personal credential safe.
        """
        # TODO: Replace with Domain
        endpoint = Endpoints.User.Credentials.format(domain=domain)
        url = self._jenkins._build_url(endpoint, prefix=self._user_url, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url, params={"depth": 1})
        if resp_obj.status_code == 404:
            raise JenkinsNotFound(f"No credentials found for {self.name}, or you don't have permission to view them.")
        return c_domain(jenkins=self._jenkins, url=url)

    @property
    def views(self) -> List[v_view] or JenkinsGeneralException:
        url = self._jenkins._build_url(Endpoints.User.Views, prefix=self._user_url, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            return JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to get users' views.")
        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)
        return [v_view(jenkins=self._jenkins,
                       name=job['name'],
                       url=job['url']) for job in data.get('jobs', [])]

    @property
    def builds(self):
        import time
        # TODO: Something about this...
        print(Warning("No REST endpoint available... returning HTML response for the moment..."))
        time.sleep(1)
        url = self._jenkins._build_url(Endpoints.User.Builds, prefix=self._user_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        code = resp_obj.status_code
        if code != 200:
            return JenkinsGeneralException(f"[{code}] Failed to get users' builds.")
        return resp_obj.content

    @property
    def delete(self) -> JenkinsActionObject:
        url = self._jenkins._build_url("/", prefix=self._user_url, suffix=Endpoints.User.Delete)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url)
        if resp_obj.status_code == 404:
            # confirm as 404 doesn't seem reliable
            try:
                Users(self._jenkins).search(self.name)
                msg = f"[400] Failed to delete user ({self.name})."
            except JenkinsNotFound:
                msg = f"[200] Successfully deleted user ({self.name})."
        else:
            msg = f"[400] Failed to delete user ({self.name})."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    # def __str__(self):
    #     return f"<{self.name} object at {id(self)}>"


class Users:
    def __init__(self, jenkins):
        self._jenkins = jenkins

    def search(self, username: str) -> Generator[User] or JenkinsNotFound:
        url = self._jenkins._build_url(Endpoints.Users.User.format(username=username), suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code == 404:
            raise JenkinsNotFound(f"User {username} was not found.")
        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)
        return User(self._jenkins, data.get('absoluteUrl', url))

    def iter(self) -> Generator[User]:
        url = self._jenkins._build_url(Endpoints.Users.List, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)
        for user in data['users']:
            user = user['user']  # Bit odd...
            yield User(self._jenkins, user['absoluteUrl'])

    def list(self) -> List[User]:
        return [user for user in self.iter()]

    @property
    def total(self) -> int:
        """
        Get the total number of users on the instance.
        """
        return len(self.list())

    def create(self, user: Builder.User):
        url = self._jenkins._build_url(Endpoints.Users.Create)
        print(url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_POST_HEADER, data=str(user))
        print(resp_obj.status_code)
        raise NotImplemented
