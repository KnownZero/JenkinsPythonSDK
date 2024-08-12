Nodes
======

Nodes
-----------

.. _nodes:

Search for a node

.. autofunction:: nodes.Nodes.search()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.nodes.search("sdk_test").url)

The above code will output:

::

    https://JenkinsDNS/computer/sdk_test

Create a node

.. autofunction:: nodes.Nodes.create()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")

    from jenkins_pysdk.builders import Builder
    config = Builder.Node(description="test 2", remote_fs="/jen")
    print(jenkins.nodes.create("docs_node", config))

The above code will output:

::

    request=<Request object at 1660092329280> content='[200] Successfully created node (docs_node).' status_code=200

Iterate all nodes

.. autofunction:: nodes.Nodes.iter()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    for node in jenkins.nodes.iter():
       print(node.url)

The above code will output:

::

    https://JenkinsDNS/computer/(built-in)
    https://JenkinsDNS/computer/docs_node
    https://JenkinsDNS/computer/sdk_test
    https://JenkinsDNS/computer/te-st
    https://JenkinsDNS/computer/testing

List all nodes

.. autofunction:: nodes.Nodes.list()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.nodes.list())

The above code will output:

::

    [<jenkins_pysdk.nodes.Node object at 0x000002000BC05D20>, <jenkins_pysdk.nodes.Node object at 0x000002000BC05BD0>, <truncated...>]

Get total nodes

.. autofunction:: nodes.Nodes.total()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.nodes.total)

The above code will output:

::

    5


Node
-----------

.. _node:

Get the node name

.. autofunction:: nodes.Node.name()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.nodes.search("sdk_test").name)

The above code will output:

::

    sdk_test

Get the node URL

.. autofunction:: nodes.Node.url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.nodes.search("sdk_test").url)

The above code will output:

::

    https://JenkinsDNS/computer/sdk_test

Check if the node is idle

.. autofunction:: nodes.Node.idle()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    node = jenkins.nodes.search("sdk_test")
    print(node.idle)

The above code will output:

::

    True

Get the node config

.. autofunction:: nodes.Node.config()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    node = jenkins.nodes.search("sdk_test")
    print(node.config)

The above code will output:

::

    <?xml version="1.1" encoding="UTF-8"?>
    <slave>
      <name>sdk_test</name>
      <description>test 2</description>
      <remoteFS>/jen</remoteFS>
      <numExecutors>1</numExecutors>
      <mode>NORMAL</mode>
      <retentionStrategy class="hudson.slaves.RetentionStrategy$Always"/>
      <launcher class="hudson.slaves.JNLPLauncher">
        <workDirSettings>
          <disabled>false</disabled>
          <internalDir>remoting</internalDir>
          <failIfWorkDirIsMissing>false</failIfWorkDirIsMissing>
        </workDirSettings>
        <webSocket>false</webSocket>
      </launcher>
      <label></label>
      <nodeProperties/>
    </slave>

Reconfigure the node

.. autofunction:: nodes.Node.reconfig()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    node = jenkins.nodes.search("sdk_test")
    config = """
       <slave>
         <name>sdk_test</name>
         <description>my new description</description>
         <remoteFS>/jenkins/new</remoteFS>
         <numExecutors>1</numExecutors>
         <mode>NORMAL</mode>
         <retentionStrategy class="hudson.slaves.RetentionStrategy$Always"/>
         <launcher class="hudson.slaves.JNLPLauncher">
           <workDirSettings>
             <disabled>false</disabled>
             <internalDir>remoting</internalDir>
             <failIfWorkDirIsMissing>false</failIfWorkDirIsMissing>
           </workDirSettings>
           <webSocket>false</webSocket>
         </launcher>
         <label></label>
         <nodeProperties/>
       </slave>
       """
    print(jenkins.nodes.search("sdk_test").reconfig(config))

The above code will output:

::

    request=<Request object at 1423581162816> content='[200] Successfully reconfigured sdk_test.' status_code=200

Disable the node

.. autofunction:: nodes.Node.disable()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.nodes.search("sdk_test").disable("disabling for test"))

The above code will output:

::

    request=<Request object at 2424196147344> content='[200] Successfully marked node (sdk_test) as offline.' status_code=200

Enable the node

.. autofunction:: nodes.Node.enable()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.nodes.search("sdk_test").enable())

The above code will output:

::

    request=<Request object at 2289828053616> content='[200] Successfully marked node (sdk_test) as online.' status_code=200

Delete the node

.. autofunction:: nodes.Node.delete()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.nodes.search("sdk_test").delete())

The above code will output:

::

    request=<Request object at 2401019053696> content='[200] Successfully deleted node (sdk_test).' status_code=200
