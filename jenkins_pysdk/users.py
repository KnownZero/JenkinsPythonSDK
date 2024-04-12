from collections.abc import Generator
from typing import List
import orjson
import pprint

from pydantic import HttpUrl

from jenkins_pysdk.objects import JenkinsActionObject
from jenkins_pysdk.exceptions import JenkinsGeneralException, JenkinsNotFound
from jenkins_pysdk.consts import Endpoints, XML_POST_HEADER
from jenkins_pysdk.objects import Builder
from jenkins_pysdk.views import View as v_view
from jenkins_pysdk.credentials import Domain as c_domain


__all__ = ["Users", "User"]


class User:
    def __init__(self, jenkins, user_url: HttpUrl):
        """
        Interact with a user on the Jenkins instance.

        :param jenkins: Connection to the Jenkins instance.
        :param user_url: URL of the user.
        """
        self._jenkins = jenkins
        self._user_url = user_url
        self._raw = self._get_raw()

    @property
    def url(self) -> HttpUrl:
        """
        Get the URL of the user.

        :return: The URL of the user.
        :rtype: HttpUrl
        """
        return self._user_url

    def _get_raw(self) -> orjson.loads:
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=self._user_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            pass  # TODO: Something here
        return orjson.loads(resp_obj.content)

    @property
    def description(self) -> str:
        """
        Get the description of the user.

        :return: The description of the user.
        :rtype: str
        """
        return str(self._raw['description'])

    @property
    def name(self) -> str:
        """
        Get the name of the user.

        :return: The name of the user.
        :rtype: str
        """
        return str(self._raw['fullName'])

    def credentials(self, domain="_") -> c_domain:
        """
        Search the user's personal credential safe.

        :param domain: The domain to search for credentials (default is "_").
        :type domain: str, optional
        :return: A domain object representing the user's personal credential safe.
        :rtype: :class:`credentials.Domain`
        :raises: JenkinsNotFound: If the users credentials were not found.
        """
        # TODO: Replace with Domain
        endpoint = Endpoints.User.Credentials.format(domain=domain)
        url = self._jenkins._build_url(endpoint, prefix=self._user_url, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url, params={"depth": 1})
        if resp_obj.status_code == 404:
            raise JenkinsNotFound(f"No credentials found for {self.name}, or you don't have permission to view them.")
        return c_domain(jenkins=self._jenkins, url=url)

    @property
    def views(self) -> List[v_view]:
        """
        Get a list of views associated with the user.

        :return: A list of view objects associated with the user.
        :rtype: List[v_view]
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.User.Views, prefix=self._user_url, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to get users' views.")
        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)
        return [v_view(jenkins=self._jenkins,
                       name=job['name'],
                       url=job['url']) for job in data.get('jobs', [])]

    @property
    def builds(self):
        """
        Get a list of builds associated with the user.

        :return: A list of build objects associated with the user.
        :rtype: List[Build]
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        import time
        # TODO: Something about this...
        print(Warning("No REST endpoint available... returning HTML response for the moment..."))
        time.sleep(1)
        url = self._jenkins._build_url(Endpoints.User.Builds, prefix=self._user_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        code = resp_obj.status_code
        if code != 200:
            raise JenkinsGeneralException(f"[{code}] Failed to get users' builds.")
        return resp_obj.content

    @property
    def delete(self) -> JenkinsActionObject:
        """
        Delete the user.

        :return: Action object representing the result of the deletion operation.
        :rtype: JenkinsActionObject
        """
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
        """
        Interact with users on the Jenkins instance.

        :param jenkins: Connection to the Jenkins instance.
        """
        self._jenkins = jenkins

    def search(self, username: str) -> User:
        """
        Search for a user by username.

        :param username: The username of the user to search for.
        :type username: str
        :return: User object corresponding to the username.
        :rtype: User
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Users.User.format(username=username), suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code == 404:
            raise JenkinsGeneralException(f"User {username} was not found.")
        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)
        return User(self._jenkins, data.get('absoluteUrl', url))

    def iter(self) -> Generator[User]:
        """
        Iterate over all users.

        :return: Generator yielding User objects.
        :rtype: Generator[User]
        """
        url = self._jenkins._build_url(Endpoints.Users.List, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)
        for user in data['users']:
            user = user['user']  # Bit odd...
            yield User(self._jenkins, user['absoluteUrl'])

    def list(self) -> List[User]:
        """
        Get a list of all users.

        :return: List of User objects.
        :rtype: List[User]
        """
        return [user for user in self.iter()]

    @property
    def total(self) -> int:
        """
        Get the total number of users.

        :return: Total number of users.
        :rtype: int
        """
        return len(self.list())

    def create(self, user: str or Builder.User):
        """
        Create a new user.

        :param user: The user to be created.
        :type user: Builder.User
        """
        url = self._jenkins._build_url(Endpoints.Users.Create)
        print(url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_POST_HEADER, data=str(user))
        print(resp_obj.status_code)
        raise NotImplemented
