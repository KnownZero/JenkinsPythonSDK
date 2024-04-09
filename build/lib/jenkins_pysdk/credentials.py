from collections.abc import Generator
from typing import List
import orjson
import pprint

from pydantic import HttpUrl

from jenkins_pysdk.response_objects import JenkinsActionObject
from jenkins_pysdk.jenkins_exceptions import JenkinsGeneralException, JenkinsNotFound
from jenkins_pysdk.consts import Endpoints, XML_HEADER_DEFAULT, FORM_HEADER_DEFAULT, XML_POST_HEADER
from jenkins_pysdk.builders import Builder


__all__ = ["Credentials", "Credential"]


class Credential:
    def __init__(self, /, *, jenkins, cred_id: str, domain_url: HttpUrl):
        self._jenkins = jenkins
        self._cred_id = cred_id
        self.domain_url = domain_url

    @property
    def id(self) -> str:
        return str(self._cred_id)

    @property
    def config(self):
        url = self._jenkins._build_url(f"/credential/{self._cred_id}", prefix=self.domain_url, suffix=Endpoints.Jobs.Xml)
        req_obj, resp_obj = self._jenkins._send_http(url=url, headers=XML_HEADER_DEFAULT)
        code = resp_obj.status_code
        if code != 200:
            return JenkinsGeneralException(f"[{code}] Failed to download credential XML.")
        return resp_obj.content

    @property
    def delete(self):
        url = self._jenkins._build_url(f"/credential/{self._cred_id}", prefix=self.domain_url, suffix=Endpoints.Jobs.Xml)
        req_obj, resp_obj = self._jenkins._send_http(method="DELETE", url=url)
        msg = f"[{resp_obj.status_code}] Successfully deleted credential."
        if resp_obj.status_code != 204:
            msg = f"[{resp_obj.status_code}] Failed to delete credential."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def reconfig(self, xml: str or Builder.Credentials):
        url = self._jenkins._build_url(f"/credential/{self._cred_id}", prefix=self.domain_url, suffix=Endpoints.Jobs.Xml)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_POST_HEADER,
                                                     data=xml)
        msg = f"[{resp_obj.status_code}] Successfully reconfigured {self._cred_id}."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to reconfigure {self._cred_id}."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def move(self):
        # TODO: This
        raise NotImplemented


class Domain:
    def __init__(self, /, *, jenkins, url: HttpUrl):
        self._jenkins = jenkins
        self.domain_url = url

    def search(self, cred_id: str):
        pass

    def iter(self, domain="_") -> Generator[Credential]:
        req_obj, resp_obj = self._jenkins._send_http(url=self.domain_url, params={"depth": 1})

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to fetch credentials in domain ({domain}).")

        data = orjson.loads(resp_obj.content)
        for cred in data.get('credentials', []):
            domain_url = str(self.domain_url).strip(Endpoints.Instance.Standard)
            yield Credential(jenkins=self._jenkins, cred_id=cred['id'], domain_url=domain_url)

    def list(self, domain="_", _paginate=0) -> List[Credential]:
        return [cred for cred in self.iter(domain=domain)]

    def create(self, cred: Builder.Credentials):
        url = self._jenkins._build_url(Endpoints.Users.Create)
        print(url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=FORM_HEADER_DEFAULT)
        print(resp_obj.status_code)
        raise NotImplemented


class Credentials:
    def __init__(self, jenkins):
        """
        Interact with Credentials on the Jenkins instance.
        """
        self._jenkins = jenkins

    def search_domains(self, domain=None) -> Domain:
        """
        Interact with your chosen domain.
        """
        if not domain:
            domain = "_"
        url = self._jenkins._build_url(Endpoints.Credentials.Domain.format(domain=domain))
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code == 404:
            raise JenkinsNotFound(f"Couldn't find {domain} or you don't have permission to view it.")
        return Domain(jenkins=self._jenkins, url=url)

    def iter_domains(self) -> Generator[Domain]:
        creds_url = self._jenkins._build_url(Endpoints.Manage.CredentialStore)
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=creds_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to fetch credential domains.")

        data = orjson.loads(resp_obj.content)
        for domain in data.get('domains'):
            url = self._jenkins._build_url(Endpoints.Credentials.Domain.format(domain=domain))
            yield Domain(jenkins=self._jenkins, url=url)

    def list_domains(self) -> List[Domain]:
        return [domain for domain in self.iter_domains()]

    def create_domain(self, cred: Builder.Credentials=None):
        # TODO: Create domain
        url = self._jenkins._build_url(Endpoints.Credentials.Create)
        print(url)
        data = {'name': "alex_test", 'description': "test", 'Submit': "Create"}
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=FORM_HEADER_DEFAULT, params=data)
        print(resp_obj.status_code)
        raise NotImplemented


