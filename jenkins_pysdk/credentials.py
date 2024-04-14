from collections.abc import Generator
from typing import List, Optional
import orjson

from pydantic import HttpUrl

from jenkins_pysdk.objects import JenkinsActionObject
from jenkins_pysdk.exceptions import JenkinsGeneralException, JenkinsNotFound, JenkinsAlreadyExists
from jenkins_pysdk.consts import Endpoints, XML_HEADER_DEFAULT, XML_POST_HEADER, FORM_HEADER_DEFAULT
from jenkins_pysdk.builders import Builder


__all__ = ["Credentials", "Credential", "Domain"]


class Credential:
    def __init__(self, *, jenkins, cred_id: str, domain_url: HttpUrl):
        """
        Initialize a Credential object representing a Jenkins credential.

        :param jenkins: The Jenkins instance associated with the credential.
        :type jenkins: Jenkins
        :param cred_id: The ID of the credential.
        :type cred_id: str
        :param domain_url: The URL of the domain associated with the credential.
        :type domain_url: HttpUrl
        """
        self._jenkins = jenkins
        self._cred_id = cred_id
        self.domain_url = domain_url

    @property
    def id(self) -> str:
        """
        Get the ID of the credential.

        :return: The ID of the credential.
        :rtype: str
        """
        return str(self._cred_id)

    @property
    def config(self) -> JenkinsActionObject:
        """
        Get the configuration of the credential.

        :return: The configuration of the credential.
        :rtype: :class:`objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Credential.Get.format(cred_id=self._cred_id),
                                       prefix=self.domain_url, suffix=Endpoints.Jobs.Xml)
        req_obj, resp_obj = self._jenkins._send_http(url=url, headers=XML_HEADER_DEFAULT)
        code = resp_obj.status_code
        if code != 200:
            raise JenkinsGeneralException(f"[{code}] Failed to download credential XML.")
        return resp_obj.content

    @property
    def delete(self) -> JenkinsActionObject:
        """
        Delete the credential.

        :return: Result of the deletion operation.
        :rtype: :class:`objects.JenkinsActionObject`
        """
        url = self._jenkins._build_url(Endpoints.Credential.Get.format(cred_id=self._cred_id),
                                       prefix=self.domain_url, suffix=Endpoints.Jobs.Xml)
        req_obj, resp_obj = self._jenkins._send_http(method="DELETE", url=url)
        msg = f"[{resp_obj.status_code}] Successfully deleted credential."
        if resp_obj.status_code != 204:
            msg = f"[{resp_obj.status_code}] Failed to delete credential."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def reconfig(self, xml: str or Builder.Credentials) -> JenkinsActionObject:
        """
        Reconfigure the credential with new XML content or using a Credentials builder.

        :param xml: The new XML content or a Credentials builder.
        :type xml: str or Builder.Credentials
        :return: Result of the reconfiguration operation.
        :rtype: :class:`objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Credential.Get.format(cred_id=self._cred_id),
                                       prefix=self.domain_url, suffix=Endpoints.Jobs.Xml)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_POST_HEADER, data=str(xml))
        msg = f"[{resp_obj.status_code}] Successfully reconfigured {self._cred_id}."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to reconfigure {self._cred_id}."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def move(self, dest: str) -> JenkinsActionObject:
        """
        Move the credential to another domain.

        :return: Result of the move operation.
        :rtype: :class:`objects.JenkinsActionObject`
        """
        url = self._jenkins._build_url(Endpoints.Credential.Get.format(cred_id=self._cred_id),
                                       prefix=self.domain_url, suffix=Endpoints.Credential.Move)
        data = {"destination": dest}
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=FORM_HEADER_DEFAULT, data=data)
        msg = f"[{resp_obj.status_code}] Successfully moved {self._cred_id} to {dest}."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to move {self._cred_id} to {dest}."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj


class Domain:
    def __init__(self, *, jenkins, url: HttpUrl):
        """
        Initialize a Domain object.

        :param jenkins: The Jenkins instance.
        :type jenkins: Jenkins
        :param url: The URL of the domain.
        :type url: HttpUrl
        """
        self._jenkins = jenkins
        self.domain_url = url
        self._raw = self._get_raw()

    @property
    def name(self) -> str:
        return str(self._raw['urlName'])

    @property
    def url(self) -> HttpUrl:
        return self.domain_url

    def _get_raw(self) -> orjson.loads:
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=self.domain_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        data = orjson.loads(resp_obj.content)
        return data

    def search(self, cred_id: str) -> Credential:
        """
        Search for a credential within the domain.

        :param cred_id: The ID of the credential to search for.
        :type cred_id: str
        :return: The credential matching the provided ID.
        :rtype: :class:`Credential`
        """
        for cred in self.iter():
            if cred.id == cred_id:
                return Credential(jenkins=self._jenkins, cred_id=cred.id, domain_url=self.domain_url)
        else:
            raise JenkinsNotFound(f"Credential ({cred_id}) was not found in domain ({self.name}).")

    def iter(self) -> Generator[Credential]:
        """
        Iterate over credentials within the domain.

        :return: A generator yielding credentials within the specified domain.
        :rtype: Generator[:class:`Credential`]
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=self.domain_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url, params={"depth": 1})

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to fetch credentials in domain ({self.name}).")

        data = orjson.loads(resp_obj.content)
        for cred in data.get('credentials', []):
            domain_url = str(self.domain_url).strip(Endpoints.Instance.Standard)
            yield Credential(jenkins=self._jenkins, cred_id=cred['id'], domain_url=domain_url)

    def list(self) -> List[Credential]:
        """
        List credentials within the domain.

        :return: A list of credentials within the specified domain.
        :rtype: List[:class:`Credential`]
        """
        return [cred for cred in self.iter()]

    def create(self, name: str, cred: str or Builder.Credentials) -> JenkinsActionObject:
        """
        Create a new credential.

        :param name: The name of the domain
        :type name: str
        :param cred: The credential object to create.
        :type cred: str or Builder.Credentials
        :return: Result of the deletion operation.
        :rtype: :class:`objects.JenkinsActionObject`
        """
        url = self._jenkins._build_url(Endpoints.Credentials.Domain.format(domain=self.name),
                                       suffix=Endpoints.Credential.Create)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_HEADER_DEFAULT, data=str(cred))
        if resp_obj.status_code == 409:
            raise JenkinsAlreadyExists(f"[{resp_obj.status_code}] Credential ({name}) already exists.)")
        elif resp_obj.status_code > 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to create credential ({name}).")
        msg = f"[{resp_obj.status_code}] Successfully created credential ({name})."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj


class Credentials:
    def __init__(self, jenkins):
        """
        Interact with Credentials on the Jenkins instance.

        :param jenkins: The Jenkins instance.
        :type jenkins: Jenkins
        """
        self._jenkins = jenkins

    def search_domains(self, domain: Optional[str] = None) -> Domain:
        """
        Search for domains on the Jenkins instance.

        :param domain: The name of the domain to search for. If None, returns all domains.
        :type domain: str, optional
        :return: The Domain object representing the found domain.
        :rtype: :class:`Domain`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        if not domain:
            domain = "_"
        url = self._jenkins._build_url(Endpoints.Credentials.Domain.format(domain=domain))
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code == 404:
            raise JenkinsGeneralException(f"Couldn't find {domain} or you don't have permission to view it.")
        return Domain(jenkins=self._jenkins, url=url)

    def iter_domains(self) -> Generator[Domain]:
        """
        Iterate over domains on the Jenkins instance.

        :return: A generator yielding Domain objects.
        :rtype: Generator[:class:`Domain`]
        :raises JenkinsGeneralException: If a general exception occurs.
        """
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
        """
        List all domains on the Jenkins instance.

        :return: List of Domain objects.
        :rtype: List[:class:`Domain`]
        """
        return [domain for domain in self.iter_domains()]

    def create_domain(self, name: str, cred: str or Builder.Credentials.Domain) -> JenkinsActionObject:
        """
        Create a new domain.

        :param name: The name of the domain
        :type name: str
        :param cred: The credentials to associate with the domain.
        :type cred: :class:`Builder.Credentials.Domain`
        :return: Outcome of the domain creation request.
        :rtype: :class:`objects.JenkinsActionObject`
        :raises JenkinsAlreadyExists: If the domain already exists.
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Credentials.CreateDomain)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_HEADER_DEFAULT, data=str(cred))
        if resp_obj.status_code == 409:
            raise JenkinsAlreadyExists(f"[{resp_obj.status_code}] Domain ({name}) already exists.)")
        elif resp_obj.status_code > 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to create domain ({name}).")
        msg = f"[{resp_obj.status_code}] Successfully created domain ({name})."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

