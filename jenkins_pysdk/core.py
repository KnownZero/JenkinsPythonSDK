from typing import Union, Tuple

import orjson
from pydantic import HttpUrl

from jenkins_pysdk.consts import Endpoints
from jenkins_pysdk.utils import interact_http, interact_http_session
from jenkins_pysdk.consts import HTTP_HEADER_DEFAULT
from jenkins_pysdk.objects import HTTPSessionRequestObject, HTTPSessionResponseObject, \
    HTTPRequestObject, HTTPResponseObject
from jenkins_pysdk.exceptions import JenkinsConnectionException
from jenkins_pysdk.version import version, python_name

__all__ = ["Core"]


# noinspection PyUnresolvedReferences
class Core:  # TODO: Revise these messy methods
    def _set_schema(self, url):
        raise NotImplemented

    def _build_url(self, endpoint: str, prefix: str = None, suffix: str = None) -> HttpUrl:
        if not self.host.startswith("http://") and not self.host.startswith("https://"):
            host = f"http://{self.host}"
        else:
            host = self.host
        host = host.replace("http://", "https://") if self.verify else host
        if prefix:
            prefix = str(prefix).replace("http://", "https://") if self.verify else str(prefix)
            endpoint = f"{prefix.rstrip('/')}/{endpoint.replace('//', '/')}"
        else:
            endpoint = f"{host.rstrip('/')}/{endpoint.replace('//', '/')}"
        if suffix:
            endpoint = f"{endpoint.rstrip('/')}/{suffix.replace('//', '/')}"
        return HttpUrl(endpoint)

    def _validate_url_returned_from_instance(self, data: orjson):
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
                   url: HttpUrl,
                   method: str = "GET",
                   headers: dict = HTTP_HEADER_DEFAULT,
                   params: dict = None,
                   data: dict = None,
                   username: str = None,
                   passw_or_token: str = None,
                   timeout: int = None,
                   _session: HTTPSessionResponseObject = None,
                   ) -> Union[Tuple[HTTPRequestObject, HTTPResponseObject],
                              Tuple[HTTPSessionRequestObject, HTTPSessionResponseObject]]:
        """
        Some HTTP interaction function...
        :param url: The url to hit
        :param method: HTTP method
        :param headers: request headers
        :param params: request parameters
        :param data: request data
        :param username: user where authentication is needed
        :param passw_or_token: password or API token for authentication
        :param timeout: request timeout
        :return:
        """
        headers.update({"User-Agent": f"{python_name}/{version}"})
        # TODO: Unit Test
        if self.token:
            request_obj = HTTPRequestObject(method=method, url=url, headers=headers, params=params, data=data,
                                            username=username if username else self.username,
                                            passw_or_token=self.token if self.token else self.passw,
                                            verify=self.verify,
                                            proxy=self.proxy,
                                            timeout=timeout if timeout else self.timeout)
            req, resp = request_obj, interact_http(request_obj)
            if isinstance(resp._raw, Exception):
                raise JenkinsConnectionException(resp._raw)
            return req, resp
        else:
            crumbed_session_req = HTTPSessionRequestObject(
                method="GET", url=self._build_url(Endpoints.Instance.Crumb), headers=headers,
                username=username if username else self.username,
                passw_or_token=passw_or_token if passw_or_token else self.passw,
                verify=self.verify,
                proxy=self.proxy,
                timeout=timeout if timeout else self.timeout,
                keep_session=True
            )
            crumbed_session = interact_http_session(crumbed_session_req)
            if isinstance(crumbed_session._raw, Exception):
                raise JenkinsConnectionException(crumbed_session._raw)
            crumbed_data = orjson.loads(crumbed_session.content)
            headers.update({crumbed_data['crumbRequestField']: crumbed_data['crumb']})
            request_obj = HTTPSessionRequestObject(method=method, url=url, headers=headers, params=params, data=data,
                                                   username=username if username else self.username,
                                                   passw_or_token=passw_or_token if passw_or_token else self.passw,
                                                   verify=self.verify,
                                                   proxy=self.proxy,
                                                   timeout=timeout if timeout else self.timeout,
                                                   session=crumbed_session.session)
            return request_obj, interact_http_session(request_obj)


# class Interact(ABC):
#     def __init__(self, jenkins):
#         self._jenkins = jenkins
#
#     @property
#     def config(self):
#         return
