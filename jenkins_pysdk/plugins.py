from collections.abc import Generator
from typing import List, Union

import orjson
from pydantic import HttpUrl

from jenkins_pysdk.objects import JenkinsActionObject
from jenkins_pysdk.exceptions import JenkinsGeneralException, JenkinsNotFound
from jenkins_pysdk.consts import Endpoints


__all__ = ["Plugins", "Plugin", "PluginGroup", "UpdateCenter", "Site"]


class Site:
    def __init__(self):
        pass


class UpdateCenter:
    def __init__(self):
        pass

    def iter(self):
        pass

    def list(self):
        pass


class Plugin:
    def __init__(self, jenkins, plugin_info):
        self._jenkins = jenkins
        self._plugin_info = plugin_info

    @property
    def name(self) -> str:
        return str(self._plugin_info['name'])

    @property
    def active(self):
        return bool(self._plugin_info['active'])

    @property
    def version(self) -> str:
        return str(self._plugin_info['version'])

    @property
    def url(self) -> HttpUrl:
        return HttpUrl(self._plugin_info['url'])

    @property
    def compatible(self) -> bool:
        return bool(self._plugin_info['compatible'])

    @property
    def dependencies(self) -> List[dict]:
        return [{n: v} for n, v in self._plugin_info['dependencies'].items()]

    @property
    def requires(self):
        return str(self._plugin_info['requiredCore'])

    @property
    def docs(self) -> HttpUrl:
        return HttpUrl(self._plugin_info['wiki'])

    @property
    def site(self) -> Site:
        return Site()


# The data has different key names... what a mess :(
class Installed:
    def __init__(self, jenkins, plugin_info):
        self._jenkins = jenkins
        self._plugin_info = plugin_info

    @property
    def name(self) -> str:
        return str(self._plugin_info['shortName'])

    @property
    def active(self):
        return bool(self._plugin_info['active'])

    @property
    def enabled(self) -> bool:
        return bool(self._plugin_info['enabled'])

    @property
    def version(self) -> str:
        return str(self._plugin_info['version'])

    @property
    def url(self) -> HttpUrl:
        return HttpUrl(self._plugin_info['url'])

    @property
    def compatible(self) -> bool:
        return bool(self._plugin_info['compatible'])

    @property
    def dependencies(self) -> List[dict]:
        return [{n: v} for n, v in self._plugin_info['dependencies'].items()]

    @property
    def requires(self):
        return str(self._plugin_info['requiredCoreVersion'])

    @property
    def pinned(self) -> bool:
        return bool(self._plugin_info['pinned'])


class PluginGroup:
    def __init__(self, jenkins, p_type: str):
        self._jenkins = jenkins
        self.type = p_type

    def search(self, id: str, _paginate=200) -> Union[Plugin, Installed]:
        for plugin in self.iter(_paginate=_paginate):
            if plugin.name == id:
                return plugin
        else:
            raise JenkinsNotFound(f"Plugin ({id}) was not found.")

    def iter(self, _paginate: int = 0) -> Generator[Union[Plugin, Installed]]:
        endpoint = Endpoints.Plugins.PluginManager if self.type == "plugins" else Endpoints.Plugins.UpdateCenter
        url = self._jenkins._build_url(endpoint, suffix=Endpoints.Instance.Standard)

        start = 0
        while True:
            limit = start + _paginate if _paginate > 0 else ""
            paginate = f"{{{start},{limit}}}"
            param = Endpoints.Plugins.PluginManagerIter.format(p_type=self.type, paginate=paginate) \
                if self.type else Endpoints.Plugins.UpdateCenterIter.format(p_type=self.type, paginate=paginate)
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
                # TODO: Beta - the below won't work with multiple sites
                for plugin in data['sites'][0].get(self.type, []):
                    yield Plugin(self._jenkins, plugin)

            if _paginate > 0:
                start += _paginate + 1
            elif _paginate == 0:
                break

    def list(self, _paginate: int = 0) -> List[Union[Plugin, Installed]]:
        return [plugin for plugin in self.iter(_paginate=_paginate)]


class Plugins:
    def __init__(self, jenkins):
        self._jenkins = jenkins

    @property
    def available(self) -> PluginGroup:
        return PluginGroup(self._jenkins, p_type="availables")

    @property
    def updates(self) -> PluginGroup:
        return PluginGroup(self._jenkins, p_type="updates")

    @property
    def installed(self) -> PluginGroup:
        return PluginGroup(self._jenkins, p_type="plugins")

    def upload(self):
        pass

    @property
    def sites(self):
        return UpdateCenter()
