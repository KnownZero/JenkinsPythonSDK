import re
import time
import json
import threading
from typing import Optional

import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from jenkins_pysdk.core import Core
from jenkins_pysdk.consts import (
    Endpoints,
    FORM_HEADER_DEFAULT,
    Class
)
from jenkins_pysdk.exceptions import (
    JenkinsConnectionException,
    JenkinsUnauthorisedException,
    JenkinsRestartFailed,
    JenkinsActionFailed,
    JenkinsGeneralException
)
from jenkins_pysdk.objects import JenkinsConnectObject, JenkinsActionObject
from jenkins_pysdk.objects import Views as r_views, Jobs as r_jobs, Folders as r_folders
from jenkins_pysdk.jobs import Jobs, Folders
from jenkins_pysdk.views import Views
from jenkins_pysdk.users import Users, User
from jenkins_pysdk.credentials import Credentials
from jenkins_pysdk.plugins import Plugins
from jenkins_pysdk.nodes import Nodes
from jenkins_pysdk.queues import Queue

__all__ = ["Jenkins"]


class Jenkins(Core):
    """
    This is the main class for interacting with your Jenkins instance.

    :param host: The hostname/IP/DNS of the Jenkins instance.
    :type host: str
    :param username: The username for authentication. Defaults to None.
    :type username: str, optional
    :param passw: The password for authentication. Defaults to None.
    :type passw: str, optional
    :param token: The API token for authentication. Defaults to None.
    :type token: str, optional
    :param verify: Enable or disable SSL verification. Defaults to True.
    :type verify: bool, optional
    :param proxies: Specify a proxy for routing requests. Supports both HTTP and HTTPS. Defaults to None.
    :type proxies: dict, optional
    :param port: The port number for connecting to the Jenkins instance. Defaults to 443.
    :type port: int, optional
    :param timeout: Specify the connection timeout in seconds. Defaults to 30.
    :type timeout: int, optional
    """

    def __init__(self, *,
                 host: str,
                 username: Optional[str] = None,
                 passw: Optional[str] = None,
                 token: Optional[str] = None,
                 verify: Optional[bool] = True,
                 proxies: dict = None,
                 port: int = 443,
                 timeout: int = 30):
        self.host = host
        self.username = username
        self.passw = passw
        self.token = token
        self.verify = verify
        self.proxies = proxies
        self.port = port
        self.timeout = timeout

        self.host = re.sub(r":\d+", f":{port}", host)
        if not self.host.endswith(f":{port}"):
            self.host += f":{port}"

        # Extend functionality
        self._jobs = Jobs(self)
        self._folders = Folders(self)
        self._views = Views(self)
        self._credentials = Credentials(self)
        self._plugins = Plugins(self)
        self._nodes = Nodes(self)
        self._queue = Queue(self)
        self._users = Users(self)  # Define Users last as it requires Plugins

        # Test connection
        self.connect()

    @property
    def jobs(self) -> Jobs:
        """
        Retrieve information about jobs.

        :return: A Jobs object representing the jobs on the system.
        :rtype: :class:`jenkins_pysdk.jobs.Jobs`
        """
        return self._jobs

    @property
    def folders(self) -> Folders:
        """
        Retrieve information about folders.

        :return: A Folders object representing the folders on the system.
        :rtype: :class:`jenkins_pysdk.jobs.Folders`
        """
        return self._folders

    @property
    def views(self) -> Views:
        """
        Retrieve information about views.

        :return: A Views object representing the views on the system.
        :rtype: :class:`jenkins_pysdk.views.Views`
        """
        return self._views

    @property
    def credentials(self) -> Credentials:
        """
        Retrieve information about credentials.

        :return: A Credentials object representing the credentials on the system.
        :rtype: :class:`jenkins_pysdk.credentials.Credentials`
        """
        return self._credentials

    def api(self, query: str):
        """
        Run a custom query and return the relevant data objects.

        :return: Data objects representing the resource requested.
        """
        # TODO: Allow the user to enter their own query parameters
        raise NotImplementedError

    @property
    def ListView(self) -> r_views:
        """
        Flag used to create a ListView View in Views.create() method.

        :return: Flag for creating a ListView View
        :rtype: :class:`jenkins_pysdk.objects.Flags.Views`
        """
        return r_views(value=Class.ListView)

    @property
    def MyView(self) -> r_views:
        """
        Flag used to create a MyView View in Views.create() method.

        :return: Flag for creating a MyView View
        :rtype: :class:`jenkins_pysdk.objects.Flags.Views`
        """
        return r_views(value=Class.MyView)

    @property
    def FreeStyle(self) -> r_jobs:
        """
        Flag used to create FreeStyle jobs in Jobs.create() method.

        :return: Flag for creating FreeStyle jobs
        :rtype: :class:`jenkins_pysdk.objects.Flags.Jobs`
        """
        return r_jobs(value=Class.Freestyle)

    @property
    def Pipeline(self) -> r_jobs:
        """
        Flag used to create Pipeline jobs in Jobs.create() method.

        :return: Flag for creating Pipeline jobs
        :rtype: :class:`jenkins_pysdk.objects.Flags.Jobs`
        """
        return r_jobs(value=Class.Pipeline)

    @property
    def MultiBranchPipeline(self) -> r_jobs:
        """
        Flag used to create MultiBranchPipeline jobs in Jobs.create() method.

        :return: Flag for creating MultiBranchPipeline jobs
        :rtype: :class:`jenkins_pysdk.objects.Flags.Jobs`
        """
        return r_jobs(value=Class.MultiBranchPipeline)

    @property
    def MultiConfigurationProject(self) -> r_jobs:
        """
        Flag used to create multi-configuration project jobs in Jobs.create() method.

        :return: Flag for creating multi-configuration project jobs
        :rtype: :class:`jenkins_pysdk.objects.Flags.Jobs`
        """
        return r_jobs(value=Class.MultiConfigurationProject)

    @property
    def Folder(self) -> r_folders:
        """
        Flag used to create Folder in Folders.create() or Folder.create() method.

        :return: Flag for creating Folder
        :rtype: :class:`jenkins_pysdk.objects.Flags.Jobs`
        """
        return r_folders(value=Class.Folder)

    @property
    def OrganizationFolder(self) -> r_folders:
        """
        Flag used to create OrganizationFolder in Folders.create() or Folder.create() method.

        :return: Flag for creating OrganizationFolder
        :rtype: :class:`jenkins_pysdk.objects.Flags.Jobs`
        """
        return r_folders(value=Class.OrganizationFolder)

    def connect(self) -> JenkinsConnectObject:
        """
        Test the connection to the Jenkins instance.

        :return: Object containing connection information.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsConnectObject`
        :raises JenkinsConnectionException: If a connection exception occurs.
        :raises JenkinsUnauthorisedException: If the credentials aren't valid.
        """
        url = self._build_url(Endpoints.Instance.Connect)
        req_obj, response_obj = self._send_http(url=url)
        code = int(response_obj.status_code)

        if code == 200:
            return self._create_return_object(req_obj, response_obj, f"[{code}] Successfully connected to {self.host}.")

        if code == 400:
            return self._handle_failed_connection(req_obj, response_obj, f"[{code}] Failed to connect to host.")

        if code == 401:
            self._handle_unauthorised_exception(code)

        if code >= 500:
            return self._handle_failed_connection(req_obj, response_obj, f"[{code}] Server error.")

        raise JenkinsConnectionException(response_obj.text)

    @staticmethod
    def _create_return_object(req_obj, response_obj, msg):
        return_object = JenkinsConnectObject(
            request=req_obj,
            response=response_obj,
            content=str(msg),
            status_code=response_obj.status_code
        )
        return_object._raw = response_obj.content

        return return_object

    def _handle_failed_connection(self, req_obj, response_obj, msg):
        return self._create_return_object(req_obj, response_obj, JenkinsConnectionException(msg))

    def _handle_unauthorised_exception(self, code):
        msg = f"[{code}] Unauthorised. "
        if self.username and self.passw:
            msg += "Wrong credentials supplied."
        elif not self.username:
            msg += "No username supplied."
        elif not self.passw and not self.token:
            msg += "No password supplied."
        else:
            msg += "No credentials supplied."

        raise JenkinsUnauthorisedException(msg)

    @property
    def tree(self):
        """
        View all jobs in a pretty tree-like structure.

        :return: Tree-like structure of all jobs.
        """
        raise NotImplemented

    @property
    def users(self) -> Users:
        """
        Retrieve information about users.

        :return: A Users object representing the users on the system.
        :rtype: :class:`jenkins_pysdk.users.Users`
        """
        return self._users

    @property
    def me(self) -> User:
        """
        Retrieve information about the authenticated user.

        :return: Information about the authenticated user
        :rtype: :class:`jenkins_pysdk.users.User`
        """
        url = self._build_url(Endpoints.User.Me)
        return User(self, url)

    @property
    def plugins(self) -> Plugins:
        """
        Retrieve information about plugins.

        :return: A Plugins object representing the plugins on the system.
        :rtype: :class:`jenkins_pysdk.plugins.Plugins`
        """
        return self._plugins

    @property
    def nodes(self) -> Nodes:
        """
        Retrieve information about nodes.

        :return: A Nodes object representing the nodes on the system.
        :rtype: :class:`jenkins_pysdk.nodes.Nodes`
        """
        return self._nodes

    @property
    def queue(self) -> Queue:
        """
        Retrieve information about the queue.

        :return: A Queue object representing the queue on the system.
        :rtype: :class:`jenkins_pysdk.queues.Queue`
        """
        return self._queue

    @property
    def version(self) -> str:
        """
        Get the version information of the Jenkins instance.

        :return: Version information of the Jenkins instance
        :rtype: str
        """
        # TODO: Finish me
        url = self._build_url(Endpoints.Instance.Connect)
        req_obj, resp_obj = self._send_http(url=url)

        return resp_obj.headers['x-jenkins']

    @property
    def available_executors(self) -> int:
        """
        View the number of available executors on the instance.

        :return: Number of available executors
        :rtype: int
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        # TODO: FIX CODE COPY & PASTE BELOW... maybe singledispatch
        url = self._build_url(Endpoints.Instance.OverallLoad, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._send_http(url=url)
        data = json.loads(resp_obj.content)
        content = data['availableExecutors']

        if not content:
            raise JenkinsGeneralException("No executors are available.")

        return content

    @property
    def executors_in_use(self) -> str:
        """
        View the executors that are currently being used on the instance.

        :return: Information about the executors in use
        :rtype: str
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._build_url(Endpoints.Instance.OverallLoad, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._send_http(url=url)
        data = json.loads(resp_obj.content)
        content = data['busyExecutors']

        if not content:
            raise JenkinsGeneralException("No executors are in-use.")

        return content

    @property
    def pending_executors(self) -> int:
        """
        View the number of executors that are about to run on the instance.

        :return: Number of pending executors
        :rtype: int
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._build_url(Endpoints.Instance.OverallLoad, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._send_http(url=url)
        data = json.loads(resp_obj.content)
        content = data['connectingExecutors']

        if not content:
            raise JenkinsGeneralException("No executors are connecting.")

        return content

    @property
    def executor_info(self) -> str:
        """
        View information about the setup executors on the instance.

        :return: Information about the setup executors
        :rtype: str
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._build_url(Endpoints.Instance.OverallLoad, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._send_http(url=url)
        data = json.loads(resp_obj.content)
        content = data['definedExecutors']

        if not content:
            raise JenkinsGeneralException("No executors are defined.")

        return content

    @property
    def idle_executors(self) -> int:
        """
        View the number of idle executors on the instance.

        :return: Number of idle executors
        :rtype: int
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._build_url(Endpoints.Instance.OverallLoad, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._send_http(url=url)
        data = json.loads(resp_obj.content)
        content = data['idleExecutors']

        if not content:
            raise JenkinsGeneralException("No executors are idle.")

        return content

    @property
    def online_executors(self) -> int:
        """
        View the number of executors that are currently online on the instance.

        :return: Number of online executors
        :rtype: int
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._build_url(Endpoints.Instance.OverallLoad, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._send_http(url=url)
        data = json.loads(resp_obj.content)
        content = data['onlineExecutors']

        if not content:
            raise JenkinsGeneralException("No executors are online.")

        return content

    @property
    def queue_size(self) -> int:
        """
        View the current queue size on the instance.

        :return: Current queue size
        :rtype: int
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._build_url(Endpoints.Instance.OverallLoad, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._send_http(url=url)
        data = json.loads(resp_obj.content)
        content = data['queueLength']

        if not content:
            raise JenkinsGeneralException("No work in the queue.")

        return content

    @property
    def max_executors(self) -> int:
        """
        View the total number of executors on the instance.

        :return: Total number of executors
        :rtype: int
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._build_url(Endpoints.Instance.OverallLoad, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._send_http(url=url)
        data = json.loads(resp_obj.content)
        content = data['totalExecutors']

        if not content:
            raise JenkinsGeneralException("No executors are setup.")

        return content

    @property
    def max_queue_size(self) -> int:
        """
        View the maximum queue size on the instance.

        :return: Maximum queue size
        :rtype: int
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        # TODO: Fix endpoitn remove api json
        url = self._build_url(Endpoints.Instance.OverallLoad, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._send_http(url=url)
        data = json.loads(resp_obj.content)
        content = data['totalQueueLength']

        if not content:
            raise JenkinsGeneralException("No executors are setup.")

        return content

    def restart(self, graceful: bool = False) -> JenkinsActionObject:
        """
        Restart the Jenkins instance.

        :param graceful: (optional) If True, restart after all jobs have finished, defaults to False
        :type graceful: bool
        :return: Restart status
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        # TODO: Unit Test
        # TODO: Add restart message
        url = self._build_url(Endpoints.Maintenance.Restart)

        if graceful:
            url = self._build_url(Endpoints.Maintenance.SafeRestart)

        req_obj, resp_obj = self._send_http(method="POST", url=url)
        code = resp_obj.status_code

        # TODO: Fix mess
        if code == 503:
            if re.search(r"Please wait while Jenkins is restarting", str(resp_obj.content)):  # TODO: Unreliable method
                msg = f"[200] Restarting the Jenkins instance... please wait..."
                code = 200
            else:
                msg = JenkinsRestartFailed(f"[{code}] Failed to restart Jenkins.")
        elif code != 200:
            msg = JenkinsRestartFailed(f"[{code}] Failed to restart Jenkins.")
        else:
            msg = f"[{code}] Restarting the Jenkins instance... please wait..."

        restart_obj = JenkinsActionObject(request=req_obj, content=msg, status_code=code)

        return restart_obj

    def _enable_quiet_mode(self) -> JenkinsActionObject:
        """
        Enable Quiet Mode on the Jenkins instance.

        :return: Result of the request to enable Quiet Mode
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        url = self._build_url(Endpoints.Maintenance.QuietDown)
        req_obj, resp_obj = self._send_http(method="POST", url=url, headers=FORM_HEADER_DEFAULT)
        code = resp_obj.status_code

        if code != 200:
            msg = JenkinsActionFailed(f"[{code}] Failed to enable Quiet Mode.")
        else:
            msg = f"[{code}] Successfully enabled Quiet Mode."

        quiet_obj = JenkinsActionObject(request=req_obj, content=msg, status_code=code)

        return quiet_obj

    def _disable_quiet_mode(self, wait_time: int = 0) -> JenkinsActionObject:
        """
        Disable Quiet Mode on the Jenkins instance.

        :param wait_time: (optional) Time to wait before disabling Quiet Mode, in seconds (default is 0)
        :type wait_time: int
        :return: Result of the request to disable Quiet Mode
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        time.sleep(wait_time)
        url = self._build_url(Endpoints.Maintenance.NoQuietDown)
        req_obj, resp_obj = self._send_http(method="POST", url=url, headers=FORM_HEADER_DEFAULT)
        code = resp_obj.status_code

        if code != 200:
            msg = JenkinsActionFailed(f"[{code}] Failed to disable Quiet Mode.")
        else:
            msg = f"[{code}] Successfully disabled Quiet Mode."

        quiet_obj = JenkinsActionObject(request=req_obj, content=msg, status_code=code)

        return quiet_obj

    def quiet_mode(self, duration: int = None, disable: bool = False) -> JenkinsActionObject:
        """
        Enable or disable Quiet Mode on the Jenkins instance.

        :param duration: (optional) Enable Quiet Mode for X seconds
        :type duration: int
        :param disable: (optional) If True, disable Quiet Mode, defaults to False
        :type disable: bool
        :return: Result of the request to enable or disable Quiet Mode
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        # TODO: Fix 403 error
        # TODO: Unit Test
        # TODO: Add banner message param
        if duration and disable:
            raise JenkinsGeneralException("You can't enable and disable at the same time.")

        if disable:
            return self._disable_quiet_mode()

        quiet_obj = self._enable_quiet_mode()

        if not quiet_obj.status_code == 200:
            return quiet_obj

        if duration:
            try:
                t_thread = threading.Thread(target=self._disable_quiet_mode, args=(duration,))
                t_thread.start()
                quiet_obj.content = f"[{quiet_obj.status_code}] Successfully enabled Quiet Mode for {duration} seconds."
            except:
                quiet_obj = self._disable_quiet_mode()
                # TODO: Add log message or something....

        return quiet_obj

    def shutdown(self, graceful: bool = False) -> JenkinsActionObject:
        """
        Terminate the user's session.

        :param graceful: (Default: False) If True, pause new jobs and wait for all jobs to complete.
        :type graceful: bool
        :return: Result of the shutdown request
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        url = self._build_url(Endpoints.Maintenance.Shutdown)

        if graceful:
            url = self._build_url(Endpoints.Maintenance.SafeShutdown)

        req_obj, resp_obj = self._send_http(method="POST", url=url)

        if resp_obj.status_code == 200:
            msg = f"[{resp_obj.status_code}] Shutting down..."
        else:
            msg = f"[{resp_obj.status_code}] Failed to shutdown application."

        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)

        return obj

    def logout(self, boot: bool = False) -> JenkinsActionObject:
        """
        Terminate the user's session.

        :param boot: (Default: False) If True, terminate all the users' sessions. (Caution if it's a service account!)
        :type boot: bool
        :return: Result of the logout request
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        url = self._build_url(Endpoints.User.Logout)

        if boot:
            url = self._build_url(Endpoints.User.Boot.format(user=self.username))

        req_obj, resp_obj = self._send_http(method="POST", url=url)

        if resp_obj.status_code == 200:
            msg = f"[{resp_obj.status_code}] Successfully logged out."
        else:
            msg = f"[{resp_obj.status_code}] Failed to logout."

        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)

        return obj

    def reload(self) -> JenkinsActionObject:
        """
        Reload configuration from disk.

        :return: Result of request
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        url = self._build_url(Endpoints.Manage.Reload)
        req_obj, resp_obj = self._send_http(method="POST", url=url)
        msg = f"[{resp_obj.status_code}] Successfully reloaded configuration."

        if resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to reload configuration from disk."

        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)

        return obj

    def script_console(self, commands: str) -> str:
        url = self._build_url(Endpoints.Instance.Console)
        req_obj, resp_obj = self._send_http(method="POST", url=url, data={"script": commands}, headers=dict())

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to send commands to the script console.")

        return resp_obj.text
