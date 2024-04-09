from __future__ import annotations

import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

import re
import time

import pprint
from typing import Optional
import threading

from jenkins_pysdk.core import Core
from jenkins_pysdk.consts import Endpoints, FORM_HEADER_DEFAULT, Class
from jenkins_pysdk.jenkins_exceptions import JenkinsConnectionException, JenkinsUnauthorisedException, JenkinsRestartFailed, \
    JenkinsActionFailed
from jenkins_pysdk.response_objects import JenkinsConnectObject, JenkinsDataObject, JenkinsActionObject, \
    HTTPSessionResponseObject, Views as r_views, Jobs as r_jobs
from jenkins_pysdk.jobs import Jobs, Folders, Job, Folder
from jenkins_pysdk.views import Views, View
from jenkins_pysdk.users import Users, User
from credentials import Credentials

import orjson


__all__ = ["Jenkins"]


import logging
logging.basicConfig(handlers=[logging.StreamHandler()], format="func=%(funcName)s line=%(lineno)d | %(message)s")


class Jenkins(Core):
    Enable_Logging = 0

    def __init__(self, /, *,
                 host: str,
                 username: Optional[str] = None,
                 passw: Optional[str] = None,
                 token: Optional[str] = None,
                 verify: Optional[bool] = True,
                 proxy: dict = None,
                 port: int = 443,
                 timeout: int = 30):
        """

        :param host:
        :param username:
        :param passw:
        :param token:
        :param verify:
        :param timeout:
        """
        self.host = host
        self.username = username
        self.passw = passw
        self.token = token
        self.verify = verify
        self.proxy = proxy
        self.port = port
        self.timeout = timeout

        # Extend functionality
        self._jobs = Jobs(self)
        self._folders = Folders(self)
        self._views = Views(self)
        self._credentials = Credentials(self)
        self._users = Users(self)

        # Test connection
        self.connect()

    @property
    def jobs(self) -> (Jobs, Job):
        return self._jobs

    @property
    def folders(self) -> (Folders, Folder):
        return self._folders

    @property
    def views(self) -> (Views, View):
        return self._views

    @property
    def credentials(self):
        return self._credentials

    def ApiRaw(self, query: str):
        # TODO: Allow the user to enter their own query parameters
        raise NotImplementedError

    @property
    def ListView(self) -> r_views:
        return r_views(value=Class.ListView)

    @property
    def MyView(self) -> r_views:
        return r_views(value=Class.MyView)

    @property
    def FreeStyle(self) -> r_jobs:
        return r_jobs(value=Class.Freestyle)

    @property
    def enable_logging(self):
        return self.Enable_Logging

    @enable_logging.setter
    def enable_logging(self, value: int or bool):
        # TODO: Add logging and enhance with logger per component/more levels etc etc
        self.Enable_Logging = value

    def connect(self) -> JenkinsConnectObject or JenkinsConnectionException:
        """
        Connect to the Jenkins instance.
        :return:
        """
        # TODO: Fix PORTING MAYBE?
        url = self._build_url(Endpoints.Instance.Connect)
        req_obj, response_obj = self._send_http(url=url)
        code = int(response_obj.status_code)
        if code == 200:
            msg = f"[{response_obj.status_code}] Successfully connected to {self.host}."
            return_object = JenkinsConnectObject(request=req_obj, response=response_obj, content=msg,
                                                 status_code=response_obj.status_code)
            return_object._raw = response_obj._raw
            return return_object
        elif code == 400:
            msg = JenkinsConnectionException(f"[{response_obj.status_code}] Failed to connect to host.")
            return_object = JenkinsConnectObject(request=req_obj, response=response_obj, content=msg,
                                                 status_code=response_obj.status_code)
            return_object._raw = response_obj._raw
            return return_object
        elif code == 401:
            if self.username and self.passw:
                msg = JenkinsUnauthorisedException(
                    f"[{response_obj.status_code}] Wrong credentials supplied.")
            elif not self.username:
                msg = JenkinsUnauthorisedException(
                    f"[{response_obj.status_code}] Unauthorised. No username supplied.")
            elif not self.passw and not self.token:
                msg = JenkinsUnauthorisedException(
                    f"[{response_obj.status_code}] Unauthorised. No password supplied.")
            else:
                msg = JenkinsUnauthorisedException(
                    f"[{response_obj.status_code}] Unauthorised. No credentials supplied.")
            return_object = JenkinsConnectObject(request=req_obj, response=response_obj, content=msg,
                                                 status_code=response_obj.status_code)
            return_object._raw = response_obj._raw
            return return_object
        elif code == 500:
            # TODO: FIX THIS DUPLICATE CODE MESS
            msg = JenkinsConnectionException(f"[{response_obj.status_code}] Server error.")
            return_object = JenkinsConnectObject(request=req_obj, response=response_obj, content=msg,
                                                 status_code=response_obj.status_code)
            return_object._raw = response_obj._raw
            return return_object
        msg = "Unhandled response. See _raw field if request failed."
        if response_obj.status_code not in [200, 201]:
            raise JenkinsConnectionException(msg)

    def use_crumb(self) -> HTTPSessionResponseObject:
        """
        Spawns a session with the crumb included.
        Note: Crumbs are auto-applied to any requests that don't use an API token.
        :return:
        """
        url = self._build_url(Endpoints.Instance.Crumb)
        req_obj, resp_obj = self._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        add_crumb_header = {data['crumbRequestField']: data['crumb']}
        resp_obj.session.headers.update(add_crumb_header)
        raise NotImplementedError

    @property
    def tree(self):
        """
        View all jobs in a pretty tree-like structure.
        :return:
        """
        raise NotImplemented

    @property
    def users(self) -> Users:
        return self._users

    @property
    def me(self):
        """
        Return the authenticated users' information.
        """
        url = self._build_url(Endpoints.User.Me)
        return User(self, url)

    @property
    def version(self):
        # TODO: Finish me
        url = self._build_url(Endpoints.Instance.Crumb)
        req_obj, resp_obj = self._send_http(url)
        print(resp_obj.content)
        raise NotImplemented

    @property
    def plugins(self):
        """
        Returns a list of all plugins on the Jenkins instance.
        :return:
        """
        raise NotImplemented

    @property
    def available_executors(self) -> JenkinsDataObject:
        """
        View the available executors on the instance.
        :return:
        """
        # TODO: FIX CODE COPY & PASTE BELOW... maybe singledispatch
        _fields = ['_class', 'availableExecutors']
        url = self._build_url(Endpoints.Instance.OverallLoad)
        req_obj, resp_obj = self._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        content = data['availableExecutors']
        if not content:
            content = "No executors are available."
        obj = JenkinsDataObject(request=req_obj, content=content)
        obj._class = data['_class']
        raw_data = {k: v for k, v in data.items() if k in _fields}
        obj._raw = raw_data
        return obj

    @property
    def executors_in_use(self) -> JenkinsDataObject:
        """
        View the executors that are currently being used on the instance.
        :return:
        """
        _fields = ['_class', 'busyExecutors']
        url = self._build_url(Endpoints.Instance.OverallLoad)
        req_obj, resp_obj = self._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        content = data['busyExecutors']
        if not content:
            content = "No executors are in-use."
        obj = JenkinsDataObject(request=req_obj, content=content)
        obj._class = data['_class']
        raw_data = {k: v for k, v in data.items() if k in _fields}
        obj._raw = raw_data
        return obj

    @property
    def pending_executors(self) -> JenkinsDataObject:
        """
        View the executors that are about to run on the instance.
        :return:
        """
        _fields = ['_class', 'connectingExecutors']
        url = self._build_url(Endpoints.Instance.OverallLoad)
        req_obj, resp_obj = self._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        content = data['connectingExecutors']
        if not content:
            content = "No executors are connecting."
        obj = JenkinsDataObject(request=req_obj, content=content)
        obj._class = data['_class']
        raw_data = {k: v for k, v in data.items() if k in _fields}
        obj._raw = raw_data
        return obj

    @property
    def executor_info(self) -> JenkinsDataObject:
        """
        View the setup executors on the instance.
        :return:
        """
        _fields = ['_class', 'definedExecutors']
        url = self._build_url(Endpoints.Instance.OverallLoad)
        req_obj, resp_obj = self._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        content = data['definedExecutors']
        if not content:
            content = "No executors are defined."
        obj = JenkinsDataObject(request=req_obj, content=content)
        obj._class = data['_class']
        raw_data = {k: v for k, v in data.items() if k in _fields}
        obj._raw = raw_data
        return obj

    @property
    def idle_executors(self) -> JenkinsDataObject:
        """
        View the idle executors on the instance.
        :return:
        """
        _fields = ['_class', 'idleExecutors']
        url = self._build_url(Endpoints.Instance.OverallLoad)
        req_obj, resp_obj = self._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        content = data['idleExecutors']
        if not content:
            content = "No executors are idle."
        obj = JenkinsDataObject(request=req_obj, content=content)
        obj._class = data['_class']
        raw_data = {k: v for k, v in data.items() if k in _fields}
        obj._raw = raw_data
        return obj

    @property
    def online_executors(self) -> JenkinsDataObject:
        """
        View the executors that are online, on the instance.
        :return:
        """
        _fields = ['_class', 'onlineExecutors']
        url = self._build_url(Endpoints.Instance.OverallLoad)
        req_obj, resp_obj = self._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        content = data['onlineExecutors']
        if not content:
            content = "No executors are online."
        obj = JenkinsDataObject(request=req_obj, content=content)
        obj._class = data['_class']
        raw_data = {k: v for k, v in data.items() if k in _fields}
        obj._raw = raw_data
        return obj

    @property
    def queue_size(self) -> JenkinsDataObject:
        """
        View the current queue size on the instance.
        :return:
        """
        _fields = ['_class', 'queueLength']
        url = self._build_url(Endpoints.Instance.OverallLoad)
        req_obj, resp_obj = self._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        content = data['queueLength']
        if not content:
            content = "No work in the queue."
        obj = JenkinsDataObject(request=req_obj, content=content)
        obj._class = data['_class']
        raw_data = {k: v for k, v in data.items() if k in _fields}
        obj._raw = raw_data
        return obj

    @property
    def max_executors(self) -> JenkinsDataObject:
        """
        View the total number of executors on the instance.
        :return:
        """
        _fields = ['_class', 'totalExecutors']
        url = self._build_url(Endpoints.Instance.OverallLoad)
        req_obj, resp_obj = self._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        content = data['totalExecutors']
        if not content:
            content = "No executors are setup."
        obj = JenkinsDataObject(request=req_obj, content=content)
        obj._class = data['_class']
        raw_data = {k: v for k, v in data.items() if k in _fields}
        obj._raw = raw_data
        return obj

    @property
    def max_queue_size(self) -> JenkinsDataObject:
        """
        View the max queue size on the instance.
        :return:
        """
        _fields = ['_class', 'totalQueueLength']
        url = self._build_url(Endpoints.Instance.OverallLoad)
        req_obj, resp_obj = self._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        content = data['totalQueueLength']
        if not content:
            content = "No executors are setup."
        obj = JenkinsDataObject(request=req_obj, content=content)
        obj._class = data['_class']
        raw_data = {k: v for k, v in data.items() if k in _fields}
        obj._raw = raw_data
        return obj

    def restart(self, graceful: bool = False) -> JenkinsActionObject:
        """
        Restart the Jenkins instance.
        :param graceful: Restart after all jobs have finished.
        :return: Request outcome.
        """
        # TODO: Unit Test
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
        restart_obj._raw = resp_obj._raw
        return restart_obj

    def _enable_quiet_mode(self) -> JenkinsActionObject:
        url = self._build_url(Endpoints.Maintenance.QuietDown)
        req_obj, resp_obj = self._send_http(method="POST", url=url, headers=FORM_HEADER_DEFAULT)
        code = resp_obj.status_code
        if code != 200:
            msg = JenkinsActionFailed(f"[{code}] Failed to enable Quiet Mode.")
        else:
            msg = f"[{code}] Successfully enabled Quiet Mode."
        quiet_obj = JenkinsActionObject(request=req_obj, content=msg, status_code=code)
        quiet_obj._raw = resp_obj._raw
        return quiet_obj

    def _disable_quiet_mode(self, wait_time: int = 0) -> JenkinsActionObject:
        time.sleep(wait_time)
        url = self._build_url(Endpoints.Maintenance.NoQuietDown)
        req_obj, resp_obj = self._send_http(method="POST", url=url, headers=FORM_HEADER_DEFAULT)
        code = resp_obj.status_code
        if code != 200:
            msg = JenkinsActionFailed(f"[{code}] Failed to disable Quiet Mode.")
        else:
            msg = f"[{code}] Successfully disabled Quiet Mode."

        quiet_obj = JenkinsActionObject(request=req_obj, content=msg, status_code=code)
        quiet_obj._raw = resp_obj._raw
        return quiet_obj

    def quiet_mode(self, duration: int = None, disable: bool = False) -> JenkinsActionObject:
        """
        Enable Quiet Mode on the Jenkins instance.
        :param duration: (Optional) Enable Quiet Mode for X seconds
        :param disable: Disable Quiet Mode
        :return: Request outcome.
        """
        # TODO: Fix 403 error
        # TODO: Run second thread to enable quiet mode for x time
        # TODO: Unit Test
        # TODO: Add banner message
        if disable:
            return self._disable_quiet_mode()

        quiet_obj = self._enable_quiet_mode()
        if not quiet_obj.status_code == 200:
            return quiet_obj

        if duration:
            try:
                t_thread = threading.Thread(target=self._disable_quiet_mode, args=(duration,))
                t_thread.start()
                t_thread.join()
                quiet_obj.content = f"[{quiet_obj.status_code}] Successfully enabled Quiet Mode for {duration} seconds."
            except:
                quiet_obj = self._disable_quiet_mode()
                # TODO: Add log message or something....
        return quiet_obj

    def shutdown(self, graceful=False) -> JenkinsActionObject:
        url = self._build_url(Endpoints.Maintenance.Shutdown)
        if graceful:
            url = self._build_url(Endpoints.Maintenance.SafeShutdown)

        req_obj, resp_obj = self._send_http(method="POST", url=url)
        if resp_obj.status_code == 200:
            msg = f"[{resp_obj.status_code}] Shutting down..."
        else:
            msg = f"[{resp_obj.status_code}] Failed to shutdown application."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    @property
    def logout(self) -> JenkinsActionObject:
        """
        Logout of your session.
        """
        url = self._build_url(Endpoints.User.Logout)
        req_obj, resp_obj = self._send_http(method="POST", url=url)
        if resp_obj.status_code == 200:
            msg = f"[{resp_obj.status_code}] Successfully logged out."
        else:
            msg = f"[{resp_obj.status_code}] Failed to logout."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    @property
    def reload(self) -> JenkinsActionObject:
        """
        Reload configuration from disk.
        """
        url = self._build_url(Endpoints.Manage.Reload)
        req_obj, resp_obj = self._send_http(method="POST", url=url)
        msg = f"[{resp_obj.status_code}] Successfully reloaded configuration."
        if resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to reload configuration from disk."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    class Plugins:
        pass

if __name__ == "__main__":
    jenkins = Jenkins(host="http://c0ea-90-194-113-56.ngrok-free.app", username="admin", passw="jenkins")
    print(jenkins.version)
