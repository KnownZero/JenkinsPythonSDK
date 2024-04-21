from collections.abc import Generator
from typing import List

import orjson

from jenkins_pysdk.consts import Endpoints, XML_HEADER_DEFAULT, XML_POST_HEADER
from jenkins_pysdk.objects import JenkinsActionObject
from jenkins_pysdk.exceptions import JenkinsGeneralException, JenkinsNotFound
from jenkins_pysdk.builders import Builder

from pydantic import HttpUrl

__all__ = ["Nodes", "Node"]


class Node:
    """
    Represents a node in Jenkins.

    :param jenkins: The Jenkins instance this node belongs to.
    :type jenkins: jenkins_pysdk.jenkins.Jenkins
    :param name: The name of the node.
    :type name: str
    :param node_url: The URL of the node.
    :type node_url: HttpUrl
    """
    def __init__(self, jenkins, name: str, node_url: HttpUrl):
        self._jenkins = jenkins
        self._name = name
        self._node_url = node_url
        self._raw = self._get_raw()

    def _get_raw(self) -> orjson.loads:
        url = self._jenkins._build_url(Endpoints.Instance.Standard, prefix=self._node_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to get node ({self.name}) information.")

        data = orjson.loads(resp_obj.content)
        return data

    @property
    def name(self) -> str:
        """
        The name of the node.

        :return: The name of the node.
        :rtype: str
        """
        return str(self._name)

    @property
    def url(self) -> HttpUrl:
        """
        The URL of the node.

        :return: The URL of the node.
        :rtype: HttpUrl
        """
        return HttpUrl(self._node_url)

    @property
    def idle(self) -> int:
        """
       Whether the node is idle or not.

       :return: 1 if the node is idle, 0 otherwise.
       :rtype: int
       """
        return bool(self._raw['idle'])

    def delete(self) -> JenkinsActionObject:
        """
        Delete action for the node.

        :return: JenkinsActionObject representing the delete action.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        url = self._jenkins._build_url(Endpoints.Nodes.Delete, prefix=self._node_url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url)
        msg = f"[{resp_obj.status_code}] Successfully deleted node ({self.name})."
        if resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to delete node ({self.name})."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    @property
    def config(self) -> str:
        """
        Get the configuration of the node.

        :return: The configuration of the node as a string.
        :rtype: str
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Jobs.Xml, prefix=self._node_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url, headers=XML_HEADER_DEFAULT)
        code = resp_obj.status_code
        if code != 200:
            raise JenkinsGeneralException(f"[{code}] Failed to download node XML.")
        return resp_obj.content

    def reconfig(self, xml: str) -> JenkinsActionObject:
        """
        Reconfigure the node with the provided XML configuration.

        :param xml: The XML configuration to apply to the node.
        :type xml: str
        :return: JenkinsActionObject representing the reconfiguration action.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        url = self._jenkins._build_url(Endpoints.Jobs.Xml, prefix=self._node_url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_POST_HEADER, data=str(xml))
        msg = f"[{resp_obj.status_code}] Successfully reconfigured {self.name}."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to reconfigure {self.name}."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def disable(self, message: str) -> JenkinsActionObject:
        """
        Disable the node with an optional message.

        :param message: Optional message explaining the reason for disabling the node.
        :type message: str
        :return: JenkinsActionObject representing the disable action.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Nodes.Disable, prefix=self._node_url)
        msg = {"offlineMessage": message}
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, params=msg)
        msg = f"[{resp_obj.status_code}] Successfully marked node ({self.name}) as offline."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to mark ({self.name}) as offline."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def enable(self) -> JenkinsActionObject:
        """
        Enable action for the node.

        :return: JenkinsActionObject representing the delete action.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        _raw = self._get_raw()
        if bool(_raw['temporarilyOffline']) is False:
            raise JenkinsGeneralException(f"Node ({self.name}) is not marked as offline.")
        url = self._jenkins._build_url(Endpoints.Nodes.Disable, prefix=self._node_url)
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url)
        msg = f"[{resp_obj.status_code}] Successfully marked node ({self.name}) as online."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to mark ({self.name}) as online."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj


class Nodes:
    """
    Represents a collection of nodes in Jenkins.

    :param jenkins: The Jenkins instance managing the nodes.
    :type jenkins: Jenkins
    """
    def __init__(self, jenkins):
        self._jenkins = jenkins

    def search(self, name: str) -> Node:
        """
        Search for a node by name.

        :param name: The name of the node to search for.
        :type name: str
        :return: The Node object if found, otherwise raise an exception.
        :rtype: Node
        :raises JenkinsNotFound: If the node with the specified name is not found.
        """
        # TODO: Not efficient
        for node in self.iter():
            if node.name == name:
                return node
        else:
            raise JenkinsNotFound(f"Node ({name}) was not found.")

    def create(self, name: str, json: dict or orjson or Builder.Node) -> JenkinsActionObject:
        """
        Create a new node with the given name and configuration.

        :param name: The name of the node to create.
        :type name: str
        :param json: The JSON configuration of the node, either as a dictionary,
                     an orjson object, or a Builder.Node object.
        :type json: dict or orjson or Builder.Node
        :return: JenkinsActionObject representing the create action.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        try:
            self.search(name)
            raise JenkinsGeneralException(f"Node ({name}) already exists.")
        except JenkinsNotFound:
            pass

        url = self._jenkins._build_url(Endpoints.Nodes.Computer, suffix=Endpoints.Nodes.Create)
        data = {
            'name': name,
            'type': 'hudson.slaves.DumbSlave$DescriptorImpl',
            'json': json
        }
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, params=data)
        msg = f"[{resp_obj.status_code}] Successfully created node ({name})."
        if resp_obj.status_code == 400:
            msg = f"[{resp_obj.status_code}] Bad request for node ({name})."
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to create node ({name})."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    def iter(self) -> Generator[Node]:
        """
        Iterate over the nodes.

        :return: A generator yielding Node objects.
        :rtype: Generator[:class:`jenkins_pysdk.nodes.Node`]
        :raises JenkinsGeneralException: If a general exception occurs.

        """
        url = self._jenkins._build_url(Endpoints.Nodes.Computer, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url, params={"tree": "computer[assignedLabels[*]]"})
        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to get nodes information.")

        data = orjson.loads(resp_obj.content)
        for node in data.get('computer', []):
            name = node['assignedLabels'][-1]['name']  # Assuming last name is consistently correct
            url_name = name
            if name == "built-in":
                url_name = f"({name})"
            url = self._jenkins._build_url(Endpoints.Nodes.Node.format(name=url_name))
            yield Node(self._jenkins, name, url)

    def list(self) -> List[Node]:
        """
        Get a list of all nodes.

        :return: A list of Node objects.
        :rtype: List[:class:`jenkins_pysdk.nodes.Node`]
        """
        return [node for node in self.iter()]

    @property
    def total(self) -> int:
        """
        Get the total number of nodes.

        :return: The total number of nodes.
        :rtype: int
        """
        url = self._jenkins._build_url(Endpoints.Nodes.Computer, suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to get nodes information.")

        data = orjson.loads(resp_obj.content)
        return len(data['computer'])
