import json
from typing import List, Generator

from jenkins_pysdk.objects import JenkinsActionObject
from jenkins_pysdk.exceptions import JenkinsGeneralException, JenkinsNotFound
from jenkins_pysdk.consts import Endpoints, FORM_HEADER_DEFAULT
from jenkins_pysdk.objects import Builder
from jenkins_pysdk.views import View as v_view
from jenkins_pysdk.credentials import Domain as c_domain


__all__ = ["Users", "User"]


class User:
    def __init__(self, jenkins, user_url: str):
        """
        Interact with a user on the Jenkins instance.

        :param jenkins: Connection to the Jenkins instance.
        :type jenkins: jenkins_pysdk.jenkins.Jenkins
        :param user_url: URL of the user.
        :type user_url: str
        """
        self._jenkins = jenkins
        self._user_url = user_url
        self._raw = self._get_raw()

    @property
    def url(self) -> str:
        """
        Get the URL of the user.

        :return: The URL of the user.
        :rtype: str
        """
        return self._user_url

    def _get_raw(self) -> json.loads:
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=self._user_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to get user information.")

        return json.loads(resp_obj.content)

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
        Search the users' personal credential safe.

        :param domain: The domain to search for credentials (default is "_").
        :type domain: str, optional
        :return: A domain object representing the user's personal credential safe.
        :rtype: :class:`jenkins_pysdk.credentials.Domain`
        :raises: JenkinsNotFound: If the users credentials were not found.
        """
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
        :rtype: List[jenkins_pysdk.views.View]
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.User.Views, prefix=self._user_url, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url)

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to get users' views.")

        data = json.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)

        return [v_view(jenkins=self._jenkins,
                       name=job['name'],
                       url=job['url']) for job in data.get('jobs', [])]

    @property
    def builds(self):
        """
        Get a list of builds associated with the user.

        :return: A list of build objects associated with the user.
        :rtype: List[jenkins_pysdk.builds.Build]
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.User.Builds, prefix=self._user_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        code = resp_obj.status_code

        if code != 200:
            raise JenkinsGeneralException(f"[{code}] Failed to get users' builds.")

        return resp_obj.content

    def delete(self) -> JenkinsActionObject:
        """
        Delete the user.

        :return: Action object representing the result of the deletion operation.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
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

        return obj

    def logout(self) -> JenkinsActionObject:
        """
        Terminate the user's session.

        :return: Result of the logout request
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        url = self._jenkins._build_url(Endpoints.User.Boot.format(user=self.name))
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url)

        if resp_obj.status_code == 200:
            msg = f"[{resp_obj.status_code}] Successfully logged out."
        else:
            msg = f"[{resp_obj.status_code}] Failed to logout."

        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)

        return obj


class Users:
    def __init__(self, jenkins):
        """
        Interact with users on the Jenkins instance.

        :param jenkins: Connection to the Jenkins instance.
        :type jenkins: jenkins_pysdk.jenkins.Jenkins
        """
        self._jenkins = jenkins

        self._check_version()

    def _check_version(self):
        # Handling v2.452 change
        # https://issues.jenkins.io/browse/JENKINS-18884
        version = self._jenkins.version
        version = tuple(map(int, version.split(".")))
        new_version = tuple(map(int, "2.452".split(".")))
        if version >= new_version:
            try:
                found = self._jenkins.plugins.installed.search("people-view")
                if not found.active:
                    print(Warning(f"Your people-view plugin is not enabled."))
            except JenkinsNotFound:
                # TODO: Fix this print
                print(Warning(
                    f"Your Jenkins version ({version}) requires the people-view plugin but you haven't installed it."))

    def search(self, username: str) -> User:
        """
        Search for a user by username.

        :param username: The username of the user to search for.
        :type username: str
        :return: User object corresponding to the username.
        :rtype: :class:`jenkins_pysdk.users.User`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Users.User.format(username=username), suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url)

        if resp_obj.status_code == 404:
            raise JenkinsGeneralException(f"User {username} was not found.")

        data = json.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)

        return User(self._jenkins, data.get('absoluteUrl', url))

    def iter(self) -> Generator[User, None, None]:
        """
        Iterate over all users.

        :return: Generator yielding User objects.
        :rtype: Generator[:class:`jenkins_pysdk.usersUser`]
        """
        url = self._jenkins._build_url(Endpoints.Users.List, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url)

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to retrieve users.")

        data = json.loads(resp_obj.content)
        data = self._jenkins._validate_url_returned_from_instance(data)

        for user in data['users']:
            user = user['user']  # Bit odd...
            yield User(self._jenkins, user['absoluteUrl'])

    def list(self) -> List[User]:
        """
        Get a list of all users.

        :return: List of User objects.
        :rtype: List[:class:`jenkins_pysdk.users.User`]
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

    def create(self, config: Builder.User) -> JenkinsActionObject:
        """
         Create a new user.

        :param config: The user to be created.
        :type config: :class:`jenkins_pysdk.builders.Builder`
        :return: An object representing the action performed in Jenkins.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        username = config['username']
        url = self._jenkins._build_url(Endpoints.Users.CreateByAdmin)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=FORM_HEADER_DEFAULT, data=config)

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to create user ({username}).")

        msg = f"[{resp_obj.status_code}] Successfully created user ({username})."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)

        return obj
