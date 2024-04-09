from __future__ import annotations

from typing import Any, Optional, List
from pydantic import BaseModel, HttpUrl, PrivateAttr


__all__ = ["HTTPRequestObject", "JenkinsConnectObject", "HTTPResponseObject", "JenkinsDataObject", "JenkinsDataObjects",
           "JenkinsJobObject", "JenkinsJobObjects", "JenkinsActionObject", "Parameter", "Filter",
           "Flags", "JenkinsViewObject", "JenkinsViewObjects", "Setting", "JenkinsBuildObject", "JenkinsBuildObjects",
           "JenkinsValidateJob", "HTTPSessionResponseObject", "HTTPSessionRequestObject"]


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


###########################################
#   DATA
###########################################

class JenkinsDataObject(JenkinsSafe):
    request: Any
    content: Any
    _class: Any = PrivateAttr()
    _raw: Any = PrivateAttr()


class JenkinsBuildObject(JenkinsSafe):
    _class: str = PrivateAttr()
    artifacts: Any = None  # TODO: make artifacts object
    building_status: bool  # TODO: Improve to object response
    name: str
    timestamp: int
    content: Any
    url: HttpUrl
    _raw: Any = PrivateAttr()


class JenkinsBuildObjects(JenkinsSafe):
    objects: List[JenkinsBuildObject]

    def list(self) -> List[JenkinsBuildObject]:
        return self.objects

    def iter(self) -> JenkinsBuildObject:
        for obj in self.objects:
            yield obj

    def items(self):
        for obj in self.objects:
            yield obj._as_dict()

    def append(self, obj: JenkinsBuildObject):
        self.objects.append(obj)


class JenkinsValidateJob(JenkinsSafe):
    is_valid: bool
    url: HttpUrl
    _raw: PrivateAttr


class JenkinsJobObject(JenkinsSafe):
    _class: str = PrivateAttr()
    name: str
    path: str
    url: HttpUrl
    content: Any = None
    _raw: Any = PrivateAttr()


class JenkinsJobObjects(JenkinsSafe):
    objects: List[JenkinsJobObject]

    def list(self) -> List[JenkinsJobObject]:
        for obj in self.objects:
            yield obj

    def enumerate(self) -> (int, JenkinsJobObject):
        for obj in enumerate(self.objects):
            yield obj

    def items(self) -> dict:
        for obj in self.objects:
            # TODO: fix this
            yield obj._as_dict()

    def append(self, obj: JenkinsJobObject):
        self.objects.append(obj)


class JenkinsViewObject(JenkinsSafe):
    _class: str = PrivateAttr()
    name: str
    url: HttpUrl
    config: Any
    jobs: JenkinsJobObjects
    _raw: Any = PrivateAttr()


class JenkinsViewObjects(JenkinsSafe):
    objects: List[JenkinsViewObject]

    def list(self) -> List[JenkinsViewObject]:
        for obj in self.objects:
            yield obj

    def enumerate(self) -> (int, JenkinsViewObject):
        for obj in enumerate(self.objects):
            yield obj

    def items(self):
        for obj in self.objects:
            yield obj._as_dict()

    def append(self, obj: JenkinsViewObject):
        self.objects.append(obj)


class JenkinsDataObjects(JenkinsSafe):
    objects: List[JenkinsDataObject|JenkinsViewObjects|JenkinsJobObjects]  # TODO: Fix hardcode

    def list(self) -> JenkinsDataObject|JenkinsViewObject|JenkinsJobObject:
        for obj in self.objects:
            if not isinstance(obj, JenkinsDataObject):
                yield from obj.list()
            else:
                yield obj

    def enumerate(self) -> (int, JenkinsDataObject):
        for obj in enumerate(self.objects):
            yield obj

    def items(self):
        for obj in self.objects:
            yield obj._as_dict()

    def append(self, obj: JenkinsDataObject|JenkinsViewObjects|JenkinsJobObjects): # TODO: Fix hardcode
        self.objects.append(obj)


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
    value: str | bool


class Builder(Flags):
    class User:
        value: dict
