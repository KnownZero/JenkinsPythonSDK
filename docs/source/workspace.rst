Workspace
==========

.. _workspace:

Download the workspace files

.. autofunction:: workspace.Workspace.download()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("new_freestyle").workspace.download("C:/Users/UnknownUser/Desktop/workspace.zip"))

The above code will output:

::

    request=<Request object at 2314487495104> content='[200] Successfully Downloaded workspace files for new_freestyle.' status_code=200

Download a workspace file

.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    ws = jenkins.jobs.search("new_freestyle").workspace
    print(ws.download("C:/Users/UnknownUser/Desktop/useSocket.ts", workspace_file="apps/native/hooks/useSocket.ts"))

The above code will output:

::

    request=<Request object at 2207675860768> content='[200] Successfully downloaded workspace files for new_freestyle.' status_code=200

Wipe the workspace

.. autofunction:: workspace.Workspace.wipe()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("new_freestyle").workspace.wipe())

The above code will output:

::

    request=<Request object at 2300540877328> content='[200] Successfully wiped workspace for new_freestyle.' status_code=200
