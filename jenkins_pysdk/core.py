import os
import json
import warnings
from typing import Tuple, Any

from httpx import (
    Client,
    Request,
    Response,
    HTTPError,
    TimeoutException
)

from jenkins_pysdk.consts import Endpoints
from jenkins_pysdk.consts import HTTP_HEADER_DEFAULT
from jenkins_pysdk.exceptions import JenkinsConnectionException
from jenkins_pysdk.version import version, python_name

__all__ = ["Core"]


# noinspection PyUnresolvedReferences
class Core:  # TODO: Revise these messy methods
    def _set_schema(self, url):
        raise NotImplemented

    def _build_url(self, endpoint: str, prefix: str = None, suffix: str = None) -> str:
        endpoint = str(endpoint)
        if not self.host.startswith("http://") and not self.host.startswith("https://"):
            host = f"http://{self.host}"
        else:
            host = self.host

        host = host.replace("http://", "https://") if self.verify else host

        if prefix:
            prefix = prefix.replace("http://", "https://") if self.verify else prefix
            endpoint = f"{prefix.rstrip('/')}/{endpoint.replace('//', '/')}"
        else:
            endpoint = f"{host.rstrip('/')}/{endpoint.replace('//', '/')}"

        if suffix:
            endpoint = f"{endpoint.rstrip('/')}/{suffix.replace('//', '/')}"

        return endpoint

    def _validate_url_returned_from_instance(self, data: json):
        """
        Handle returned endpoints when the Jenkins instance is not configured properly.
        :param data:
        :return:
        """
        if isinstance(data, dict):
            for key, value in data.items():
                if key in ['url', 'absoluteUrl'] and isinstance(value, str):
                    if self.verify:
                        value = value.replace("http://", "https://")
                    # TODO: Make this work for non 8080
                    value = value.replace("localhost:8080", self.host.lstrip("http://").lstrip("https://"))
                    data[key] = value
                else:
                    data[key] = self._validate_url_returned_from_instance(value)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                data[i] = self._validate_url_returned_from_instance(item)

        return data

    @staticmethod
    def _build_job_http_path(job_path: str, folder_path=None):
        import re

        if folder_path:
            job_path = f"{folder_path}/{job_path}".replace("//", "/")

        if not job_path.startswith("/"):
            job_path = "/" + job_path

        job_path = job_path.rstrip("/")
        job_path = re.sub(r"((/)?\bjob\b(/)?)+", "/", str(job_path))

        return job_path.replace("/", "/job/").replace("//", "/")

    @staticmethod
    def _build_view_http_path(view_path: str):
        import re

        if not view_path.startswith("/"):
            view_path = "/" + view_path

        view_path = view_path.rstrip("/")
        job_path = re.sub(r"((/)?\bjob\b(/)?)+", "/", str(view_path))

        return job_path.replace("/", "/view/").replace("//", "/").lstrip("/")

    @staticmethod
    def _get_folder_parent(folder_path: str) -> (str, str):
        if folder_path.startswith("/"):
            folder_path = folder_path[1:]

        if folder_path.endswith("/"):
            folder_path = folder_path[:-1]

        folder_name = folder_path.split("/")[-1]
        folder_path = "/".join(folder_path.split("/")[:-1])
        folder_path = folder_path if folder_path else ""

        return folder_name, folder_path

    @staticmethod
    def _get_job_level(path: str) -> int:
        levels = path.split('/')

        return len(levels)

    def _send_http(self, *,
                   url: str,
                   method: str = "GET",
                   headers: dict = HTTP_HEADER_DEFAULT,
                   params: dict = None,
                   data: Any = None,
                   files: dict = None,
                   username: str = None,
                   passw_or_token: str = None,
                   timeout: int = None
                   ) -> Tuple[Request, Response]:
        """
        Some HTTP interaction function...
        :param url: The url to hit
        :param method: HTTP method
        :param headers: request headers
        :param params: request parameters
        :param data: request data
        :param files: upload files
        :param username: user where authentication is needed
        :param passw_or_token: password or API token for authentication
        :param timeout: request timeout
        :return:
        """
        if not isinstance(headers, dict):
            headers = dict()

        headers.update({"User-Agent": f"{python_name}/{version}"})

        with Client(verify=self.verify,
                    proxies=self.proxies,
                    timeout=timeout if timeout else self.timeout,
                    follow_redirects=True,
                    auth=(username if username else self.username,
                          passw_or_token if passw_or_token else self.token if self.token else self.passw),
                    ) as session:

            if not self.token:
                try:
                    crumbed_session_req = Request(
                        method="GET",
                        url=self._build_url(Endpoints.Instance.Crumb, suffix=Endpoints.Instance.Standard),
                        headers=HTTP_HEADER_DEFAULT,
                    )
                    crumbed_session = session.send(crumbed_session_req)
                except (EnvironmentError, HTTPError, TimeoutException) as e:
                    raise JenkinsConnectionException(e)

                crumbed_data = json.loads(crumbed_session.content)
                headers.update({crumbed_data['crumbRequestField']: crumbed_data['crumb']})
                headers.update({"x-jenkins-session": crumbed_session.headers['x-jenkins-session']})

            try:
                with warnings.catch_warnings():
                    warnings.filterwarnings("ignore", category=DeprecationWarning)
                    request_obj = Request(method=method,
                                          url=url,
                                          headers=headers,
                                          params=params,
                                          data=data,
                                          files=files,
                                          cookies=crumbed_session.cookies)
                    resp = session.send(request_obj)
            except (EnvironmentError, HTTPError, TimeoutException) as e:
                raise JenkinsConnectionException(e)

            return request_obj, resp
