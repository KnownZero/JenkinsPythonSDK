from typing import Any
from dataclasses import dataclass, asdict

__all__ = ["JenkinsConnectObject", "JenkinsActionObject", "Parameter",
           "Filter", "Flags", "Setting", "JenkinsValidateJob",
           "Views", "Jobs", "Folders", "Builder"]


@dataclass
class Base:
    def __init__(self, **kws):
        for arg, val in kws.items():
            setattr(self, arg, val)

    def _as_dict(self):
        return asdict(self)


class JenkinsSafe(Base):
    def __repr__(self):
        return f"<{self.__class__.__name__} object at {id(self)}>"


class JenkinsValidateJob(JenkinsSafe):
    is_valid: bool
    url: str
    _raw: Any


###########################################
#   ACTION
###########################################

class JenkinsConnectObject(JenkinsSafe):
    request: Any
    response: Any
    content: str
    status_code: int
    _raw: Any


class JenkinsActionObject(JenkinsSafe):
    request: Any
    content: Any
    status_code: int


###########################################
#   FLAGS
###########################################

class Flags(Base):
    value: Any

    def _as_dict(self):
        yield super()._as_dict()


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
