Jobs
========


Jobs
-----------

.. _jobs:

Interact with a job

.. autofunction:: jobs.Jobs.search()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("new_freestyle"))

The above code will output:

::

    <jenkins_pysdk.jobs.Job object at 0x000001E515CD4A90>

List all jobs

.. autofunction:: jobs.Jobs.list()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.list())

The above code will output:

::

    [<jenkins_pysdk.jobs.Job object at 0x000002B4E528A710>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5119780>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5118580>, <jenkins_pysdk.jobs.Job object at 0x000002B4E511BC10>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5119870>]

Iterate all jobs

.. autofunction:: jobs.Jobs.iter()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.iter())

The above code will output:

::

    [<jenkins_pysdk.jobs.Job object at 0x000002B4E528A710>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5119780>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5118580>, <jenkins_pysdk.jobs.Job object at 0x000002B4E511BC10>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5119870>]

Create a freestyle job

.. autofunction:: jobs.Jobs.create()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    freestyle = """<project>
                    <description>My description goes here</description>
                    <keepDependencies>false</keepDependencies>
                    <properties/>
                    <scm class="hudson.scm.NullSCM"/>
                    <canRoam>true</canRoam>
                    <disabled>false</disabled>
                    <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
                    <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
                    <triggers/>
                    <concurrentBuild>false</concurrentBuild>
                    <builders/>
                    <publishers/>
                    <buildWrappers/>
                   </project>"""
    print(jenkins.jobs.create("freestyle_created", freestyle, jenkins.FreeStyle))

The above code will output:

::

    request=<Request object at 2205281481040> content='[200] Successfully created freestyle_created.' status_code=200

Check if the path is a job

.. autofunction:: jobs.Jobs.is_job()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.is_job("folder3/freestyle_4"))

The above code will output:

::

    True


Job
-----------

.. _job:

Disable a job

.. autofunction:: jobs.Job.disable()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("folder3/freestyle_4").disable())

The above code will output:

::

    request=<Request object at 2523890810240> content='[200] Successfully disabled folder3/freestyle_4.' status_code=200

Get a job URL

.. autofunction:: jobs.Job.url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("folder3/freestyle_4").url)

The above code will output:

::

    https://JenkinsDNS/job/folder3/job/freestyle_4

Get a job path

.. autofunction:: jobs.Job.path()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("folder3/freestyle_4").path)

The above code will output:

::

    folder3/freestyle_4


Get job URL

.. autofunction:: jobs.Job.enable()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("folder3/freestyle_4").enable())

The above code will output:

::

    request=<Request object at 1986068844192> content='[200] Successfully enabled folder3/freestyle_4.' status_code=200

Reconfigure a job

.. autofunction:: jobs.Job.reconfig()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    from jenkins_pysdk.builders import Builder
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    config = Builder._Templates.Freestyle.format(description="New desc", disabled=True)
    print(jenkins.jobs.search("freestyle_created").reconfig(config))

The above code will output:

::

    request=<Request object at 1772165197280> content='[200] Successfully reconfigured freestyle_created.' status_code=200

Delete a job

.. autofunction:: jobs.Job.delete()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("freestyle_created").delete())

The above code will output:

::

    request=<Request object at 1721615969440> content='[204] Successfully deleted job.' status_code=204

Get job config

.. autofunction:: jobs.Job.config()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("new_freestyle").config)

The above code will output:

::

    <?xml version='1.1' encoding='UTF-8'?>
    <project>
      <description></description>
      <keepDependencies>false</keepDependencies>
      <properties/>
      <scm class="hudson.scm.NullSCM"/>
      <canRoam>true</canRoam>
      <disabled>false</disabled>
      <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
      <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
      <triggers/>
      <concurrentBuild>false</concurrentBuild>
      <builders/>
      <publishers/>
      <buildWrappers/>
    </project>

Get a job's builds

.. autofunction:: jobs.Job.builds()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("new_freestyle").builds)

The above code will output:

::

    <jenkins_pysdk.builds.Builds object at 0x000001EF9C34A860>

Interact with the job workspace

.. autofunction:: jobs.Job.workspace()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("freestyle_created").workspace)

The above code will output:

::

    <jenkins_pysdk.workspace.Workspace object at 0x00000153D2E27580>