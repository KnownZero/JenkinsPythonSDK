from typing import Any
from pydantic import (
    BaseModel,
    PrivateAttr,
)


__all__ = ["JenkinsConnectObject", "JenkinsActionObject", "Parameter",
           "Filter", "Flags", "Setting", "JenkinsValidateJob",
           "Views", "Jobs", "Folders", "Builder"]


class JenkinsSafe(BaseModel):
    def __repr__(self):
        return f"<{self.__class__.__name__} object at {id(self)}>"

    def _as_dict(self):
        return self.model_dump_json()


class JenkinsValidateJob(JenkinsSafe):
    is_valid: bool
    url: str
    _raw: PrivateAttr


###########################################
#   ACTION
###########################################

class JenkinsConnectObject(JenkinsSafe):
    request: Any
    response: Any
    content: str
    status_code: int
    _raw: Any = PrivateAttr()


class JenkinsActionObject(JenkinsSafe):
    request: Any
    content: Any
    status_code: int


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


class Folders(Flags):
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

    class Credential:
        value: str
