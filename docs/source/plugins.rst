Plugins
========

Plugins
-----------

.. _plugins:

Install a plugin

.. autofunction:: plugins.Plugins.install()

Example plugin: https://plugins.jenkins.io/pipeline-stage-view/

.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.plugins.install("pipeline-stage-view", 2.18))

The above code will output:

::

    request=<Request object at 2898119135520> content='[200] Successfully installed plugin (pipeline-stage-view).' status_code=200

Upload a plugin

.. autofunction:: plugins.Plugins.upload()

Example plugin: https://plugins.jenkins.io/chucknorris/

.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    filename = "chucknorris.hpi"
    with open(f"C:\\Users\\UnknownUser\\Downloads\\{filename}", "rb") as file:
        print(jenkins.plugins.upload(filename, file))

The above code will output:

::

    request=<Request object at 2188075571200> content='[200] Successfully uploaded plugin (chucknorris.hpi).' status_code=200


Available
~~~~~~~~~~~~

Search for an available plugin
(A plugin that is not already installed)

The plugin ID/Name is found in the plugin docs 'ID' field
In the below link you will see ID: blueocean-rest
https://plugins.jenkins.io/blueocean-rest/

.. autofunction:: plugins.PluginGroup.search()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.plugins.available.search("blueocean-rest"))

The above code will output:

::

    <jenkins_pysdk.plugins.Plugin object at 0x000001AB664C0370>

Iterate all available plugins

.. autofunction:: plugins.PluginGroup.iter()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    for plugin in jenkins.plugins.available.iter(_paginate=500):
        print(plugin.name, plugin.version)

The above code will output:

::

    pipeline-rest-api 2.34
    pipeline-stage-view 2.34
    jdk-tool 73.vddf737284550
    command-launcher 107.v773860566e2e
    jsch 0.2.16-86.v42e010d9484b_
    sshd 3.322.v159e91f6a_550
    authentication-tokens 1.53.v1c90fd9191a_b_
    javadoc 243.vb_b_503b_b_45537
    <truncated...>

List all available plugins

.. autofunction:: plugins.PluginGroup.list()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.plugins.available.list(_paginate=1000))

The above code will output:

::

    [<jenkins_pysdk.plugins.Plugin object at 0x000002316EB50520>, <jenkins_pysdk.plugins.Plugin object at 0x000002316EB50130>, <jenkins_pysdk.plugins.Plugin object at 0x000002316EB50160>, <truncated...>]


Updates
~~~~~~~~~~~~

Search for a plugin needing an update

The plugin ID/Name is found in the plugin docs 'ID' field
In the below link you will see ID: ssh-credentials
https://plugins.jenkins.io/ssh-credentials/

.. autofunction:: plugins.PluginGroup.search()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.plugins.updates.search("ssh-credentials").name)

The above code will output:

::

    ssh-credentials

Iterate all plugins needing an updates

.. autofunction:: plugins.PluginGroup.iter()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    for plugin in jenkins.plugins.updates.iter(_paginate=500):
        print(plugin.name, plugin.version, plugin.url)

The above code will output:

::

    checks-api 2.2.0 https://updates.jenkins.io/download/plugins/checks-api/2.2.0/checks-api.hpi
    github-branch-source 1787.v8b_8cd49a_f8f1 https://updates.jenkins.io/download/plugins/github-branch-source/1787.v8b_8cd49a_f8f1/github-branch-source.hpi
    gradle 2.11 https://updates.jenkins.io/download/plugins/gradle/2.11/gradle.hpi
    ionicons-api 70.v2959a_b_74e3cf https://updates.jenkins.io/download/plugins/ionicons-api/70.v2959a_b_74e3cf/ionicons-api.hpi
    jackson2-api 2.17.0-379.v02de8ec9f64c https://updates.jenkins.io/download/plugins/jackson2-api/2.17.0-379.v02de8ec9f64c/jackson2-api.hpi
    <truncated...>

List all plugins needing an updates

.. autofunction:: plugins.PluginGroup.list()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.plugins.updates.list(_paginate=500))

The above code will output:

::

    [<jenkins_pysdk.plugins.Plugin object at 0x000001CF357C4B20>, <truncated...>]


Installed
~~~~~~~~~~~~

Search for an installed plugin

The plugin ID/Name is found in the plugin docs 'ID' field
In the below link you will see ID: ssh-credentials
https://plugins.jenkins.io/ssh-credentials/

.. autofunction:: plugins.PluginGroup.search()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.plugins.installed.search("ant").version)

The above code will output:

::

    497.v94e7d9fffa_b_9

Iterate all installed plugins

.. autofunction:: plugins.PluginGroup.iter()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    for plugin in jenkins.plugins.installed.iter(_paginate=500):
        print(plugin.name, plugin.active)

The above code will output:

::

    ant True
    antisamy-markup-formatter True
    apache-httpcomponents-client-4-api True
    bootstrap5-api True
    bouncycastle-api True
    <truncated...>

List all installed plugins

.. autofunction:: plugins.PluginGroup.list()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.plugins.updates.list(_paginate=500))

The above code will output:

::

    [<jenkins_pysdk.plugins.Installed object at 0x0000021DBB290A30>, <truncated...>]


UpdateCenter
~~~~~~~~~~~~

Search for a site

.. autofunction:: plugins.UpdateCenter.search()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.plugins.sites.search("default"))

The above code will output:

::

    <jenkins_pysdk.plugins.Site object at 0x00000230D4BD1D20>

Iterate all sites

.. autofunction:: plugins.UpdateCenter.iter()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    for site in jenkins.plugins.sites.iter():
        print(site.id)

The above code will output:

::

    default

List all sites

.. autofunction:: plugins.UpdateCenter.list()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.plugins.sites.search("default"))

The above code will output:

::

    [<jenkins_pysdk.plugins.Site object at 0x0000027AA7115D20>]

Add a new update center

List all sites

.. autofunction:: plugins.UpdateCenter.create()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.plugins.sites.create("https://www.google.com/update-center.json"))

The above code will output:

::

    request=<Request object at 1985835210512> content='[200] Successfully added update center (https://www.google.com/update-center.json).' status_code=200


Plugin
-----------

.. _plugin:

Available
~~~~~~~~~~~~

Get the available plugin name

.. autofunction:: plugins.Plugin.name()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    av = jenkins.plugins.availables.search("pipeline-stage-view")
    print(av.name)

The above code will output:

::

    pipeline-stage-view

Get the available plugin version

.. autofunction:: plugins.Plugin.version()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    av = jenkins.plugins.availables.search("pipeline-stage-view")
    print(av.version)

The above code will output:

::

    2.34

Get the available plugin URL

.. autofunction:: plugins.Plugin.url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    av = jenkins.plugins.availables.search("pipeline-stage-view")
    print(av.url)

The above code will output:

::

    https://updates.jenkins.io/download/plugins/pipeline-stage-view/2.34/pipeline-stage-view.hpi

Check if the available plugin is compatible

.. autofunction:: plugins.Plugin.compatible()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    av = jenkins.plugins.availables.search("pipeline-stage-view")
    print(av.compatible)

The above code will output:

::

    True

Get the available plugin dependencies

.. autofunction:: plugins.Plugin.dependencies()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    av = jenkins.plugins.availables.search("pipeline-stage-view")
    print(av.dependencies)

The above code will output:

::

    [{'workflow-api': '1213.v646def1087f9'}, {'pipeline-rest-api': '2.34'}, {'workflow-job': '1295.v395eb_7400005'}]

Get the available plugin required core version

.. autofunction:: plugins.Plugin.requires()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    av = jenkins.plugins.availables.search("pipeline-stage-view")
    print(av.requires)

The above code will output:

::

    2.361.4

Get the available plugin docs page

.. autofunction:: plugins.Plugin.docs()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    av = jenkins.plugins.availables.search("pipeline-stage-view")
    print(av.docs)

The above code will output:

::

    https://plugins.jenkins.io/pipeline-stage-view

Get the update centre of the available plugin

.. autofunction:: plugins.Plugin.site()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    av = jenkins.plugins.availables.search("pipeline-stage-view")
    print(av.site.url)

The above code will output:

::

    https://updates.jenkins.io/update-center.json


Installed
~~~~~~~~~~~~

Get the installed plugin name

.. autofunction:: plugins.Installed.name()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    ins = jenkins.plugins.installed.search("maven-plugin")
    print(ins.name)

The above code will output:

::

    maven-plugin

Get the active status of the installed plugin

.. autofunction:: plugins.Installed.active()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    ins = jenkins.plugins.installed.search("maven-plugin")
    print(ins.active)

The above code will output:

::

    True

Enable the installed plugin

.. autofunction:: plugins.Installed.enable()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    ins = jenkins.plugins.installed.search("maven-plugin")
    print(ins.enable())

The above code will output:

::

    request=<Request object at 1991094649216> content='[200] Successfully enabled plugin (maven-plugin).' status_code=200

Disable the installed plugin

.. autofunction:: plugins.Installed.disable()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    ins = jenkins.plugins.installed.search("maven-plugin")
    print(ins.disable())

The above code will output:

::

    request=<Request object at 2529251115152> content='[200] Successfully disabled plugin (maven-plugin).' status_code=200

Get the installed plugin version

.. autofunction:: plugins.Installed.version()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    ins = jenkins.plugins.installed.search("maven-plugin")
    print(ins.version)

The above code will output:

::

    3.23

Get the installed plugin URL

.. autofunction:: plugins.Installed.url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    ins = jenkins.plugins.installed.search("maven-plugin")
    print(ins.url)

The above code will output:

::

    https://plugins.jenkins.io/maven-plugin

Get the installed plugin dependencies

.. autofunction:: plugins.Installed.dependencies()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    ins = jenkins.plugins.installed.search("maven-plugin")
    print(ins.dependencies)

The above code will output:

::

    [{'optional': False, 'shortName': 'commons-lang3-api', 'version': '3.12.0-36.vd97de6465d5b_'}, {'optional': False, 'shortName': 'apache-httpcomponents-client-4-api', 'version': '4.5.14-150.v7a_b_9d17134a_5'}, {'optional': False, 'shortName': 'javadoc', 'version': '233.vdc1a_ec702cff'}, {'optional': False, 'shortName': 'jsch', 'version': '0.2.8-65.v052c39de79b_2'}, {'optional': False, 'shortName': 'junit', 'version': '1207.va_09d5100410f'}, {'optional': False, 'shortName': 'mailer', 'version': '457.v3f72cb_e015e5'}, {'optional': True, 'shortName': 'token-macro', 'version': '359.vb_cde11682e0c'}]


Get the installed plugin required core version

.. autofunction:: plugins.Installed.requires()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    ins = jenkins.plugins.installed.search("maven-plugin")
    print(ins.requires)

The above code will output:

::

    2.387.3

Get the installed plugin pinned status

.. autofunction:: plugins.Installed.pinned()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    ins = jenkins.plugins.installed.search("maven-plugin")
    print(ins.requires)

The above code will output:

::

    False

Delete the installed plugin

.. autofunction:: plugins.Installed.delete()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    ins = jenkins.plugins.installed.search("maven-plugin")
    print(ins.delete())

The above code will output:

::

    request=<Request object at 2148244816416> content='[200] Successfully uninstalled plugin (maven-plugin).' status_code=200


Updates
~~~~~~~~~~~~

Get the update plugin name

.. autofunction:: plugins.Plugin.name()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    up = jenkins.plugins.updates.search("checks-api")
    print(up.name)

The above code will output:

::

    checks-api

Get the update plugin version

.. autofunction:: plugins.Plugin.version()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    up = jenkins.plugins.updates.search("checks-api")
    print(up.version)

The above code will output:

::

    2.2.0

Get the update plugin URL

.. autofunction:: plugins.Plugin.url()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    up = jenkins.plugins.updates.search("checks-api")
    print(up.url)

The above code will output:

::

    https://updates.jenkins.io/download/plugins/checks-api/2.2.0/checks-api.hpi

Get the update plugin compatible status

.. autofunction:: plugins.Plugin.compatible()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    up = jenkins.plugins.updates.search("checks-api")
    print(up.compatible)

The above code will output:

::

    True

Get the update plugin dependencies

.. autofunction:: plugins.Plugin.dependencies()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    up = jenkins.plugins.updates.search("checks-api")
    print(up.dependencies)

The above code will output:

::

    [{'workflow-support': '865.v43e78cc44e0d'}, {'workflow-step-api': '657.v03b_e8115821b_'}, {'commons-lang3-api': '3.13.0-62.v7d18e55f51e2'}, {'commons-text-api': '1.11.0-95.v22a_d30ee5d36'}, {'plugin-util-api': '4.1.0'}, {'display-url-api': '2.200.vb_9327d658781'}]

Get the update plugin required core version

.. autofunction:: plugins.Plugin.requires()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    up = jenkins.plugins.updates.search("checks-api")
    print(up.requires)

The above code will output:

::

    2.426.3

Get the update plugin docs page

.. autofunction:: plugins.Plugin.docs()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    up = jenkins.plugins.updates.search("checks-api")
    print(up.docs)

The above code will output:

::

    https://plugins.jenkins.io/checks-api

Get the update plugin update centre site

.. autofunction:: plugins.Plugin.site()
   :noindex:
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    up = jenkins.plugins.updates.search("checks-api")
    print(up.site.url)

The above code will output:

::

    https://updates.jenkins.io/update-center.json


Site
~~~~~~~~~~~~

Get the update centre site ID

.. autofunction:: plugins.Site.id()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    site = jenkins.plugins.sites.search("default")
    print(site.id)

The above code will output:

::

    default

Get the update centre site URL

.. autofunction:: plugins.Site.url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    site = jenkins.plugins.sites.search("default")
    print(site.url)

The above code will output:

::

    https://updates.jenkins.io/update-center.json

Check if the update centre has updates

.. autofunction:: plugins.Site.has_updates()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    site = jenkins.plugins.sites.search("default")
    print(site.has_updates)

The above code will output:

::

    True

Get the plugin suggested url from the site

.. autofunction:: plugins.Site.suggested_plugins_url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    site = jenkins.plugins.sites.search("default")
    print(site.suggested_plugins_url)

The above code will output:

::

    https://updates.jenkins.io/platform-plugins.json

Get the connection check url for the site

.. autofunction:: plugins.Site.connection_check_url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    site = jenkins.plugins.sites.search("default")
    print(site.connection_check_url)

The above code will output:

::

    https://www.google.com/

Get the site data timestamp

.. autofunction:: plugins.Site.timestamp()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    site = jenkins.plugins.sites.search("default")
    print(site.timestamp)

The above code will output:

::

    1713633892889
