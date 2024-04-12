from __future__ import annotations


from typing import Any, Optional
from pydantic import BaseModel, HttpUrl, PrivateAttr


__all__ = ["HTTPRequestObject", "JenkinsConnectObject", "HTTPResponseObject", "JenkinsActionObject", "Parameter",
           "Filter", "Flags", "Setting", "HTTPSessionResponseObject", "HTTPSessionRequestObject", "JenkinsValidateJob",
           "Views"]


class JenkinsSafe(BaseModel):
    def __repr__(self):
        return f"<{self.__class__.__name__} object at {id(self)}>"

    def _as_dict(self):
        return self.model_dump_json()


###########################################
#   HTTP
###########################################

class HTTPRequestObject(JenkinsSafe):
    url: HttpUrl
    method: str = "GET"
    headers: Optional[dict] = None
    params: Optional[dict] = None
    data: Optional[Any] = None
    username: str
    passw_or_token: str  # TODO: MASK
    verify: bool
    proxy: Optional[dict] = None
    timeout: int = 30


class HTTPResponseObject(JenkinsSafe):
    request: Any
    content: Any
    status_code: int
    _raw: Any = PrivateAttr()


class HTTPSessionRequestObject(HTTPRequestObject):
    session: Any = None
    keep_session: bool = False


class HTTPSessionResponseObject(HTTPResponseObject):
    session: Any


class JenkinsValidateJob(JenkinsSafe):
    is_valid: bool
    url: HttpUrl
    _raw: PrivateAttr


###########################################
#   ACTION
###########################################

class JenkinsConnectObject(JenkinsSafe):
    request: HTTPRequestObject
    response: HTTPResponseObject
    content: str
    status_code: int
    _raw: Any = PrivateAttr()


class JenkinsActionObject(JenkinsSafe):
    request: Any
    content: Any
    status_code: int
    _raw: Any = PrivateAttr()


###########################################
#   FLAGS
###########################################

class Flags(BaseModel):
    value: Any

    def _as_dict(self):
        yield self.model_dump_json()


class Views(Flags):
    value: str


class Jobs(Flags):
    value: str


class Parameter(Flags):
    value: str


class BaseParameter(Flags):
    value: str


class Builds(BaseParameter):
    value: str


class Actions(Builds):
    value: str


class Filter(Flags):
    value: str


class Setting(Flags):
    value: str or bool


class Builder(Flags):
    class User:
        value: dict
