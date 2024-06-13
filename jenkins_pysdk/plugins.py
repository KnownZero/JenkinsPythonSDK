from typing import (
    List,
    Union,
    Dict,
    BinaryIO,
    Generator
)

import orjson
from pydantic import HttpUrl

from jenkins_pysdk.objects import JenkinsActionObject
from jenkins_pysdk.exceptions import JenkinsGeneralException, JenkinsNotFound
from jenkins_pysdk.consts import Endpoints, XML_POST_HEADER


__all__ = ["Plugins", "Plugin", "PluginGroup", "UpdateCenter", "Site", "Installed"]


class Site:
    """
    Represents a site in Jenkins.

    :param jenkins: The Jenkins instance this site belongs to.
    :type jenkins: jenkins_pysdk.jenkins.Jenkins
    :param site_id: The ID of the site.
    :type site_id: str
    """
    def __init__(self, jenkins, site_id: str):
        self._jenkins = jenkins
        self._id = site_id
        self._raw = self._get_raw()

    def _get_raw(self) -> orjson.loads:
        url = self._jenkins._build_url(Endpoints.UpdateCenter.Site.format(site=self.id), suffix=Endpoints.Instance.Standard)
        req_obj, resp_obj = self._jenkins._send_http(url=url, params={"depth": 1})

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"Failed to get site ({self.id}) information.")

        data = orjson.loads(resp_obj.content)

        return data

    @property
    def id(self) -> str:
        """
       The ID of the site.

       :return: The ID of the site.
       :rtype: str
       """
        return str(self._id)

    @property
    def url(self) -> HttpUrl:
        """
       The URL of the site.

       :return: The URL of the site.
       :rtype: HttpUrl
       """
        return HttpUrl(self._raw['url'])

    @property
    def has_updates(self) -> bool:
        """
        Indicates whether the site has updates available.

        :return: True if updates are available, False otherwise.
        :rtype: bool
        """
        return bool(self._raw['hasUpdates'])

    @property
    def suggested_plugins_url(self) -> HttpUrl:
        """
        The URL for suggested plugins for the site.

        :return: The URL for suggested plugins.
        :rtype: HttpUrl
        """
        return HttpUrl(self._raw['suggestedPluginsUrl'])

    @property
    def connection_check_url(self) -> HttpUrl:
        """
        The URL for checking the connection of the site.

        :return: The URL for connection check.
        :rtype: HttpUrl
        """
        return HttpUrl(self._raw['connectionCheckUrl'])

    @property
    def timestamp(self) -> int:
        """
       The timestamp of the site data.

       :return: The timestamp of the site data.
       :rtype: int
       """
        return int(self._raw['dataTimestamp'])


class UpdateCenter:
    """
    Represents the update center in Jenkins.

    :param jenkins: The Jenkins instance this update center belongs to.
    :type jenkins: jenkins_pysdk.jenkins.Jenkins
    """
    def __init__(self, jenkins):
        self._jenkins = jenkins

    def search(self, name: str) -> Site:
        """
        Search for a site by name.

        :param name: The name of the site to search for.
        :type name: str
        :return: The Site object if found, otherwise raise an exception.
        :rtype: :class:`jenkins_pysdk.plugins.Site`
        :raises JenkinsNotFound: If the site with the specified name is not found.
        """
        for site in self.iter():
            if name == site.id:
                return site

        raise JenkinsNotFound(f"Site ({name}) was not found.")

    def iter(self) -> Generator[Site, None, None]:
        """
        Iterate over the sites in the update center.

        :return: A generator yielding Site objects.
        :rtype: Generator[:class:`jenkins_pysdk.plugins.Site`]
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Plugins.UpdateCenter, suffix=Endpoints.Instance.Standard)
        params = {"tree": Endpoints.UpdateCenter.Iter}
        req_obj, resp_obj = self._jenkins._send_http(url=url, params=params)

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException("Failed to get sites information.")

        data = orjson.loads(resp_obj.content)

        for site in data.get('sites', []):
            yield Site(self._jenkins, site['id'])

    def list(self) -> List[Site]:
        """
        Get a list of all sites in the update center.

        :return: A list of Site objects.
        :rtype: List[:class:`jenkins_pysdk.plugins.Site`]
        """
        return [site for site in self.iter()]

    def create(self, site_url: str or HttpUrl) -> JenkinsActionObject:
        """
        Create a new site in the update center.

        :return: JenkinsActionObject representing the create update center operation.
        :rtype: jenkins_pysdk.objects.JenkinsActionObject
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.UpdateCenter.Create)
        params = {"site": site_url}
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, params=params)

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to add update center ({site_url}).")

        msg = f"[{resp_obj.status_code}] Successfully added update center ({site_url})."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw

        return obj


class Plugin:
    """
    Represents a plugin in Jenkins.

    :param jenkins: The Jenkins instance this plugin belongs to.
    :type jenkins: jenkins_pysdk.jenkins.Jenkins
    :param plugin_info: Information about the plugin.
    :type plugin_info: dict
    """
    def __init__(self, jenkins, plugin_info):
        self._jenkins = jenkins
        self._plugin_info = plugin_info

    @property
    def name(self) -> str:
        """
        The name of the plugin.

        :return: The name of the plugin.
        :rtype: str
        """
        return str(self._plugin_info['name'])

    @property
    def version(self) -> str:
        """
        The version of the plugin.

        :return: The version of the plugin.
        :rtype: str
        """
        return str(self._plugin_info['version'])

    @property
    def url(self) -> HttpUrl:
        """
        The URL of the plugin.

        :return: The URL of the plugin.
        :rtype: HttpUrl
        """
        return HttpUrl(self._plugin_info['url'])

    @property
    def compatible(self) -> bool:
        """
        Indicates whether the plugin is compatible.

        :return: True if the plugin is compatible, False otherwise.
        :rtype: bool
        """
        return bool(self._plugin_info['compatible'])

    @property
    def dependencies(self) -> List[dict]:
        """
        The dependencies of the plugin.

        :return: A list of dictionaries representing the dependencies,
                 where each dictionary contains the dependency name as key
                 and the dependency version as value.
        :rtype: List[dict]
        """
        return [{n: v} for n, v in self._plugin_info['dependencies'].items()]

    @property
    def requires(self) -> str:
        """
        The required core version for the plugin.

        :return: The required core version for the plugin.
        :rtype: str
        """
        return str(self._plugin_info['requiredCore'])

    @property
    def docs(self) -> HttpUrl:
        """
        The documentation URL for the plugin.

        :return: The documentation URL for the plugin.
        :rtype: HttpUrl
        """
        return HttpUrl(self._plugin_info['wiki'])

    @property
    def site(self) -> Site:
        """
        The site associated with the plugin.

        :return: The Site object representing the site associated with the plugin.
        :rtype: Site
        """
        return Site(self._jenkins, str(self._plugin_info['sourceId']))


class Installed:
    """
    Represents an installed plugin in Jenkins.

    :param jenkins: The Jenkins instance this installed plugin belongs to.
    :type jenkins: Jenkins
    :param plugin_info: Information about the installed plugin.
    :type plugin_info: dict
    """
    def __init__(self, jenkins, plugin_info):
        self._jenkins = jenkins
        self._plugin_info = plugin_info

    @property
    def name(self) -> str:
        """
        The name of the installed plugin.

        :return: The name of the installed plugin.
        :rtype: str
        """
        return str(self._plugin_info['shortName'])

    @property
    def active(self) -> bool:
        """
        Indicates whether the plugin is active.

        :return: True if the plugin is active, False otherwise.
        :rtype: bool
        """
        return bool(self._plugin_info['active'])

    def enable(self) -> JenkinsActionObject:
        """
        Enable the installed plugin.

        :return: JenkinsActionObject representing the enable action.
        :rtype: jenkins_pysdk.objects.JenkinsActionObject
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Plugins.PluginManager,
                                       suffix=Endpoints.Plugins.Enable.format(plugin=self.name))
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url)

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to enable plugin ({self.name}).")

        msg = f"[{resp_obj.status_code}] Successfully enabled plugin ({self.name})."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw

        return obj

    def disable(self) -> JenkinsActionObject:
        """
        Disable the installed plugin.

        :return: JenkinsActionObject representing the disable action.
        :rtype: jenkins_pysdk.objects.JenkinsActionObject
        :raises JenkinsGeneralException: If a general exception occurs.
        """

        url = self._jenkins._build_url(Endpoints.Plugins.PluginManager,
                                       suffix=Endpoints.Plugins.Disable.format(plugin=self.name))
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url)

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to disable plugin ({self.name}).")

        msg = f"[{resp_obj.status_code}] Successfully disabled plugin ({self.name})."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw

        return obj

    @property
    def version(self) -> str:
        """
        The version of the installed plugin.

        :return: The version of the installed plugin.
        :rtype: str
        """
        return str(self._plugin_info['version'])

    @property
    def url(self) -> HttpUrl:
        """
        The URL of the installed plugin.

        :return: The URL of the installed plugin.
        :rtype: HttpUrl
        """
        return HttpUrl(self._plugin_info['url'])

    @property
    def dependencies(self) -> List[Dict]:
        """
        The dependencies of the installed plugin.

        :return: A list of dictionaries representing the dependencies,
                 where each dictionary contains the dependency name as key
                 and the dependency version as value.
        :rtype: List[Dict]
        """
        return self._plugin_info['dependencies']

    @property
    def requires(self) -> str:
        """
        The required core version for the installed plugin.

        :return: The required core version for the installed plugin.
        :rtype: str
        """
        return str(self._plugin_info['requiredCoreVersion'])

    @property
    def pinned(self) -> bool:
        """
        Indicates whether the installed plugin is pinned.

        :return: True if the plugin is pinned, False otherwise.
        :rtype: bool
        """
        return bool(self._plugin_info['pinned'])

    def delete(self) -> JenkinsActionObject:
        """
        Delete the plugin from the Jenkins instance.

        :return: JenkinsActionObject representing the delete action.
        :rtype: jenkins_pysdk.objects.JenkinsActionObject
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        url = self._jenkins._build_url(Endpoints.Plugins.PluginManager,
                                       suffix=Endpoints.Plugins.Uninstall.format(plugin=self.name))
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url)

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to uninstall plugin ({self.name}).")

        msg = f"[{resp_obj.status_code}] Successfully uninstalled plugin ({self.name})."
        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw

        return obj


class PluginGroup:
    """
    Represents a group of plugins in Jenkins.

    :param jenkins: The Jenkins instance this plugin group belongs to.
    :type jenkins: jenkins_pysdk.jenkins.Jenkins
    :param p_type: The type of the plugin group.
    :type p_type: str
    """
    def __init__(self, jenkins, p_type: str):
        self._jenkins = jenkins
        self.type = p_type

    def search(self, id: str, site: str = "default", _paginate=500) -> Union[Plugin, Installed]:
        """
        Search for a plugin or an installed plugin within the plugin group.

        :param id: The ID of the plugin to search for.
        :type id: str
        :param site: The site to search for the plugin. Default is "default".
        :type site: str, optional
        :param _paginate: The number of items to paginate. Default is 500.
        :type _paginate: int, optional
        :return: A Plugin or Installed object representing the found plugin.
        :rtype: Union[jenkins_pysdk.plugins.Plugin, jenkins_pysdk.plugins.Installed]
        :raises JenkinsNotFound: If the plugin with the specified name is not found.
        """
        for plugin in self.iter(site=site, _paginate=_paginate):
            if plugin.name == id:
                return plugin

        raise JenkinsNotFound(f"Plugin ({id}) was not found in {self.type}.")

    def iter(self, site: str = "default", _paginate: int = 0) -> Generator[Union[Plugin, Installed], None, None]:
        """
        Iterate over the plugins or installed plugins within the plugin group.

        :param site: The site to iterate over. Default is "default".
        :type site: str, optional
        :param _paginate: The number of items to paginate. Default is 0.
        :type _paginate: int, optional
        :return: A generator that yields Plugin or Installed objects.
        :rtype: Generator[Union[jenkins_pysdk.plugins.Plugin, jenkins_pysdk.plugins.Installed]]
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        endpoint = Endpoints.Plugins.PluginManager if self.type == "plugins" else Endpoints.Plugins.UpdateCenter
        url = self._jenkins._build_url(endpoint, suffix=Endpoints.Instance.Standard)

        start = 0
        while True:
            limit = start + _paginate if _paginate > 0 else ""
            paginate = f"{{{start},{limit}}}"
            param = Endpoints.Plugins.PluginManagerIter.format(p_type=self.type, paginate=paginate) \
                if self.type == "plugins" else Endpoints.Plugins.UpdateCenterIter.format(p_type=self.type, paginate=paginate)
            params = {"tree": param}
            req_obj, resp_obj = self._jenkins._send_http(url=url, params=params)

            if resp_obj.status_code > 200 and start > 0:
                break  # Pagination finished, Jenkins doesn't return a nice response
            elif resp_obj.status_code != 200:
                raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to get plugin information.")

            data = orjson.loads(resp_obj.content)
            # This will make type hints annoying
            if self.type == "plugins":
                for plugin in data.get(self.type, []):
                    yield Installed(self._jenkins, plugin)
            else:
                for site_name in data['sites']:
                    for plugin in site_name.get(self.type, []):
                        if plugin['sourceId'] != site:
                            break
                        elif plugin['sourceId'] == site:
                            for plugin in site_name.get(self.type, []):
                                yield Plugin(self._jenkins, plugin)
                            break
                    break
                else:
                    raise JenkinsNotFound(f"Site ({site}) was not found.")

            if _paginate > 0:
                start += _paginate + 1
            elif _paginate == 0:
                break

    def list(self, _paginate: int = 0) -> List[Union[Plugin, Installed]]:
        """
        List the plugins or installed plugins within the plugin group.

        :param _paginate: The number of items to paginate. Default is 0.
        :type _paginate: int, optional
        :return: A list of Plugin or Installed objects.
        :rtype: List[Union[jenkins_pysdk.plugins.Plugin, jenkins_pysdk.plugins.Installed]]
        """
        return [plugin for plugin in self.iter(_paginate=_paginate)]


class Plugins:
    """
    Represents a collection of plugins in Jenkins.

    :param jenkins: The Jenkins instance containing the plugins.
    :type jenkins: jenkins_pysdk.jenkins.Jenkins
    """
    def __init__(self, jenkins):
        self._jenkins = jenkins

    @property
    def availables(self) -> PluginGroup:
        """
        Represents a group of available plugins in Jenkins.

        :return: A PluginGroup instance representing the available plugins.
        :rtype: jenkins_pysdk.plugins.PluginGroup
        """
        return PluginGroup(self._jenkins, p_type="availables")

    @property
    def updates(self) -> PluginGroup:
        """
        Represents a group of plugins with available updates in Jenkins.

        :return: A PluginGroup instance representing the plugins with available updates.
        :rtype: jenkins_pysdk.plugins.PluginGroup
        """
        return PluginGroup(self._jenkins, p_type="updates")

    @property
    def installed(self) -> PluginGroup:
        """
        Represents a group of installed plugins in Jenkins.

        :return: A PluginGroup instance representing the installed plugins.
        :rtype: jenkins_pysdk.plugins.PluginGroup
        """
        return PluginGroup(self._jenkins, p_type="plugins")

    def upload(self, filename: str, file_content: BinaryIO or bytes) -> JenkinsActionObject:
        """
        Uploads a plugin to Jenkins.

        :param filename: The name of the plugin file.
        :type filename: str
        :param file_content: The content of the plugin file as bytes.
        :type file_content: bytes or BinaryIO
        :return: A JenkinsActionObject representing the upload action.
        :rtype: jenkins_pysdk.objects.JenkinsActionObject
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        # Solution: https://issues.jenkins.io/browse/JENKINS-68443
        # Make it a form submission ^
        if isinstance(file_content, BinaryIO):
            file_content = file_content.read()

        url = self._jenkins._build_url(Endpoints.Plugins.Upload)
        file = {"file": (filename, file_content, "application/java-archive"), "submit": ""}
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=dict(), files=file)
        msg = f"[{resp_obj.status_code}] Successfully uploaded plugin ({filename})."

        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to upload plugin ({filename})."

        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw

        return obj

    def install(self, name: str, version: str or int or float = "latest", restart: bool = False) -> JenkinsActionObject:
        """
        Installs a plugin in Jenkins.

        :param name: The name of the plugin to install.
        :type name: str
        :param version: The version of the plugin to install. Default is "latest".
        :type version: Union[str, int, float], optional
        :param restart: Whether to restart Jenkins after installation. Default is False.
        :type restart: bool, optional
        :return: A JenkinsActionObject representing the installation action.
        :rtype: jenkins_pysdk.objects.JenkinsActionObject
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        try:
            plugin = self.installed.search(name)
            if plugin.version == version:
                raise JenkinsGeneralException(f"Plugin ({name}@{version}) is already installed.")
        except JenkinsNotFound:
            pass

        url = self._jenkins._build_url(Endpoints.Plugins.PluginManager, suffix=Endpoints.Plugins.Install)
        data = f"<jenkins><install plugin=\"{name}@{version}\"/></jenkins>"
        req_obj, resp_obj = self._jenkins._send_http(method="POST", url=url, headers=XML_POST_HEADER, data=data)

        if resp_obj.status_code != 200:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to install plugin ({name}).")

        try:
            self.installed.search(name)
        except JenkinsNotFound:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Received successful operation but plugin ({name}) "
                                          f"was not found. Consider restarting Jenkins.")

        msg = f"[{resp_obj.status_code}] Successfully installed plugin ({name})."

        if restart:
            self._jenkins.restart(graceful=True)
            msg = f"[{resp_obj.status_code}] Successfully installed plugin ({name}) and restarted Jenkins."

        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw

        return obj

    @property
    def sites(self) -> UpdateCenter:
        """
        Represents the update centers for managing plugin sites in Jenkins.

        :return: An UpdateCenter instance representing the update centers.
        :rtype: jenkins_pysdk.plugins.UpdateCenter
        """
        return UpdateCenter(self._jenkins)
