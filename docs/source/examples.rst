Examples
========


System
-----------

.. _system:

Connect to the application


.. autofunction:: jenkins.Jenkins.connect()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.connect())
    
The above code will output:

::

    request=<Request object at 1718212996176> content='[200] Successfully connected to JenkinsDNS.' status_code=200

Get the Jenkins version

.. autofunction:: jenkins.Jenkins.version()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.version)

The above code will output:

::

    2.448

Restart the application

.. autofunction:: jenkins.Jenkins.restart()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.restart(graceful=True))

The above code will output:

::

    request=<Request object at 2603665289872> content='[200] Restarting the Jenkins instance... please wait...' status_code=200

Enable Quiet Mode

.. autofunction:: jenkins.Jenkins.quiet_mode()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.quiet_mode(duration=30))

The above code will output:

::

    request=<Request object at 1938732315280> content='[200] Successfully enabled Quiet Mode for 30 seconds.' status_code=200

Shutdown the application

.. autofunction:: jenkins.Jenkins.shutdown()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.shutdown())

The above code will output:

::

    request=<Request object at 2613641997152> content='[200] Shutting down...' status_code=200

Logout

.. autofunction:: jenkins.Jenkins.logout()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.logout())

The above code will output:

::

    request=<Request object at 2453417290592> content='[200] Successfully logged out.' status_code=200

Reload config from disk

.. autofunction:: jenkins.Jenkins.reload()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.reload())

The above code will output:

::

    request=<Request object at 2741687462992> content='[200] Successfully reloaded configuration.' status_code=200

Get the available executors

.. autofunction:: jenkins.Jenkins.available_executors()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.available_executors)

The above code will output:

::

    No executors are available.

Execute commands in the script console

.. autofunction:: jenkins.Jenkins.script_console()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS",
                      username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    import pathlib
    file = pathlib.Path("C:\\Users\\UnknownUser\\Desktop\\commands.groovy")
    commands = file.read_text()
    print(f"Running commands:\n{commands}")

    print(jenkins.script_console(commands))

The above code will output:

::

    Running commands:
    println("Hello from Jenkins Script Console!")

    Hello from Jenkins Script Console!


Folders
-----------

.. _folders:

Interact with a folder

.. autofunction:: jobs.Folders.search()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.folders.search("my_new_folder_name"))

The above code will output:

::

    <jenkins_pysdk.jobs.Folder object at 0x00000295B24B4AF0>

List all folders

.. autofunction:: jobs.Folders.list()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    for folder in jenkins.folders.list():
        print(folder.path, folder.url)

The above code will output:

::

    builder_1 https://JenkinsDNS/job/builder_1/
    builder_2 https://JenkinsDNS/job/builder_2/
    builder_4 https://JenkinsDNS/job/builder_4/
    builder_d https://JenkinsDNS/job/builder_d/
    builder_e https://JenkinsDNS/job/builder_e/
    builder_folder https://JenkinsDNS/job/builder_folder/
    builder_w https://JenkinsDNS/job/builder_w/
    new_folder/new_job23 https://JenkinsDNS/job/new_folder/job/new_job23/
    new_folder/test_folder https://JenkinsDNS/job/new_folder/job/test_folder/

Iterate all folders

.. autofunction:: jobs.Folders.iter()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    for folder in jenkins.folders.iter():
        print(folder.path, folder.url)

The above code will output:

::

    builder_1 https://JenkinsDNS/job/builder_1/
    builder_2 https://JenkinsDNS/job/builder_2/
    builder_4 https://JenkinsDNS/job/builder_4/
    builder_d https://JenkinsDNS/job/builder_d/
    builder_e https://JenkinsDNS/job/builder_e/
    builder_folder https://JenkinsDNS/job/builder_folder/
    builder_w https://JenkinsDNS/job/builder_w/
    new_folder/new_job23 https://JenkinsDNS/job/new_folder/job/new_job23/
    new_folder/test_folder https://JenkinsDNS/job/new_folder/job/test_folder/

.. autofunction:: builders.Builder.Folder()
.. autofunction:: jobs.Folders.create()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    from jenkins_pysdk.builders import Builder
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_folder = Builder.Folder(name="my_new_folder_name", description="my description is pretty simple.")
    print(jenkins.folders.create("my_new_folder_name", my_folder))

The above code will output:

::

    request=<Request object at 1935978150336> content='[200] Successfully created my_new_folder_name.' status_code=200


Check if the path is a folder

.. autofunction:: jobs.Folders.is_folder()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.folders.is_folder("folder3/sub_folder"))

The above code will output:

::

    True

Folder
-----------

.. _folder:

Reconfigure a folder

.. autofunction:: jobs.Folder.reconfig()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    from builders.builder import Builder
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    new_folder = Builder.Folder(name="my_new_folder_name", description="Reconfigured")
    print(jenkins.folders.search("my_new_folder_name").reconfig(new_folder))

The above code will output:

::

    request=<Request object at 2282610093216> content='[200] Successfully reconfigured my_new_folder_name.' status_code=200

Get the first folder URL

.. autofunction:: jobs.Folder.url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    from builders.builder import Builder
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.folders.list()[0].url)

The above code will output:

::

    https://JenkinsDNS/job/builder_1/

Get the first folder Path

.. autofunction:: jobs.Folder.path()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.folders.list()[0].path)

The above code will output:

::

    builder_1

Copy a folder
(You are interacting with a specific folder location, so you can't copy a folder up a level)

.. autofunction:: jobs.Folder.copy()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_folder = jenkins.folders.search("folder3")
    print(my_folder.copy(new_job_name="another_sub_folder")

The above code will output:

::

    request=<Request object at 1480728865872> content='[200] Successfully copied sub_folder to another_sub_folder.' status_code=200

Delete the current folder

.. autofunction:: jobs.Folder.delete()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.folders.search("folder3/another_sub_folder").delete())

The above code will output:

::

    request=<Request object at 2309917207952> content='[204] Successfully deleted folder.' status_code=204

Create a folder
(You are interacting with a specific folder location, so you can only create sub-folders)

.. autofunction:: jobs.Folder.create()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    from jenkins_pysdk.builders import Builder
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_folder = Builder.Folder(name="my_new_folder_name", description="my description is pretty simple.")
    print(jenkins.folders.search("folder3/sub_folder").create("another_sub_folder", my_folder))

The above code will output:

::

    request=<Request object at 1660448175456> content='[200] Successfully created another_sub_folder.' status_code=200

Get the folder config

.. autofunction:: jobs.Folder.config()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.folders.search("folder3/another_sub_folder").config)

The above code will output:

::

    <?xml version='1.1' encoding='UTF-8'?>
    <com.cloudbees.hudson.plugins.folder.Folder plugin="cloudbees-folder@6.928.v7c780211d66e">
      <description></description>
      <properties/>
      <folderViews class="com.cloudbees.hudson.plugins.folder.views.DefaultFolderViewHolder">
        <views>
          <hudson.model.AllView>
            <owner class="com.cloudbees.hudson.plugins.folder.Folder" reference="../../../.."/>
            <name>All</name>
            <filterExecutors>false</filterExecutors>
            <filterQueue>false</filterQueue>
            <properties class="hudson.model.View$PropertyList"/>
          </hudson.model.AllView>
        </views>
        <tabBar class="hudson.views.DefaultViewsTabBar"/>
      </folderViews>
      <healthMetrics/>
      <icon class="com.cloudbees.hudson.plugins.folder.icons.StockFolderIcon"/>
    </com.cloudbees.hudson.plugins.folder.Folder>


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


Builds
-----------
.. _builds:

Search for a build

.. autofunction:: builds.Builds.search()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    j = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(j.jobs.search("folder1").builds.search(1).number)
    print(j.jobs.search("folder1").builds.search(lastStableBuild=True).number)
    print(j.jobs.search("folder1").builds.search(lastSuccessfulBuild=True).number)
    print(j.jobs.search("folder1").builds.search(lastFailedBuild=True).number)
    print(j.jobs.search("folder1").builds.search(lastUnsuccessfulBuild=True).number)
    print(j.jobs.search("folder1").builds.search(lastCompletedBuild=True).number)

The above code will output:

::

    1
    55
    57
    56
    57
    57

Get the total build history of a job

.. autofunction:: builds.Builds.total()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job = jenkins.jobs.search("new_freestyle")
    print(my_job.builds.total)

The above code will output:

::

    6

Iterate all job's builds

.. autofunction:: builds.Builds.iter()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job = jenkins.jobs.search("new_freestyle")
    for build in my_job.builds.iter():
        print(build.number)

The above code will output:

::

    10
    9
    8
    7
    2
    1

List all jobs' builds

.. autofunction:: builds.Builds.list()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job = jenkins.jobs.search("new_freestyle")
    print(my_job.builds.list())

The above code will output:

::

    [<jenkins_pysdk.builds.Build object at 0x00000131E097FD00>, <jenkins_pysdk.builds.Build object at 0x00000131E097FAF0>, <jenkins_pysdk.builds.Build object at 0x00000131E097FE20>, <jenkins_pysdk.builds.Build object at 0x00000131E097FBB0>, <jenkins_pysdk.builds.Build object at 0x00000131E097F850>, <jenkins_pysdk.builds.Build object at 0x00000131E08BC4C0>]


Get the latest saved build

.. autofunction:: builds.Builds.latest()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job = jenkins.jobs.search("new_freestyle")
    print(my_job.builds.latest.url)

The above code will output:

::

    https://JenkinsDNS/job/new_freestyle/10/

Get the oldest saved build

.. autofunction:: builds.Builds.oldest()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job = jenkins.jobs.search("new_freestyle")
    print(my_job.builds.latest.url)

The above code will output:

::

    https://JenkinsDNS/job/new_freestyle/1/

Trigger a new build

.. autofunction:: builds.Builds.build()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("new_freestyle").builds.build({"choises": "A", "a_bool": False}, delay=10))

The above code will output:

::

    request=<Request object at 1874065655344> content='[201] Successfully triggered a new build.' status_code=201


Rebuild the last build

.. autofunction:: builds.Builds.rebuild_last()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("new_freestyle").builds.rebuild_last())

The above code will output:

::

    request=<Request object at 2881680762624> content='[200] Successfully triggered a rebuild of the last build.' status_code=200


Build
-----------
.. _build:

Get the build number

.. autofunction:: builds.Build.number()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job_build_10 = jenkins.jobs.search("new_freestyle").builds.search(10)
    print(my_job_build_10.number)

The above code will output:

::

    10

Get the build URL

.. autofunction:: builds.Build.url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
    print(my_job_build_2.url)

The above code will output:

::

    https://JenkinsDNS/job/new_freestyle/2/

Get the build result

.. autofunction:: builds.Build.result()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
    print(my_job_build_2.result)

The above code will output:

::

    SUCCESS

Get the build timestamp

.. autofunction:: builds.Build.timestamp()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("new_freestyle").builds.latest.timestamp)

The above code will output:

::

    1711475427971


Get the build description

.. autofunction:: builds.Build.description()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("new_freestyle").builds.latest.description)

The above code will output:

::

    None

Check if the build is done

.. autofunction:: builds.Build.done()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
    print(my_job_build_2.done)

The above code will output:

::

    True

Get the build duration

.. autofunction:: builds.Build.duration()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
    print(my_job_build_2.duration)

The above code will output:

::

    15

Get the build console logs

.. autofunction:: builds.Build.console()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job_build_10 = jenkins.jobs.search("new_freestyle").builds.search(10)
    print(my_job_build_10.console())

The above code will output:

::

    Started by user admin
    Running as SYSTEM
    Building in workspace /var/lib/jenkins/workspace/new_freestyle
    Finished: SUCCESS


Building with html
.. autofunction:: builds.Build.console()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    builds = jenkins.jobs.search("folder1").builds
    builds.build()
    for chunk in builds.latest.console(html=True):
        print(chunk)

The above code will output:

::

    Started by user <a href='/user/admin' class='jenkins-table__link model-link model-link--float'>admin</a>
    Running as SYSTEM
    Building on the built-in node in workspace /var/lib/jenkins/workspace/folder1
    The recommended git tool is: NONE
    No credentials specified
     &gt; git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/folder1/.git # timeout=10
    Fetching changes from the remote Git repository
     &gt; git config remote.origin.url <a href='https://github.com/KnownZero/JenkinsPythonSDK.git'>https://github.com/KnownZero/JenkinsPythonSDK.git</a> # timeout=10
    Fetching upstream changes from <a href='https://github.com/KnownZero/JenkinsPythonSDK.git'>https://github.com/KnownZero/JenkinsPythonSDK.git</a>
     &gt; git --version # timeout=10
     &gt; git --version # 'git version 2.31.1'
     &gt; git fetch --tags --force --progress -- <a href='https://github.com/KnownZero/JenkinsPythonSDK.git'>https://github.com/KnownZero/JenkinsPythonSDK.git</a> +refs/heads/*:refs/remotes/origin/* # timeout=10
     &gt; git rev-parse origin/dev^{commit} # timeout=10
    Checking out Revision d525e7e6633eac266239438520cf27b37e751794 (origin/dev)
     &gt; git config core.sparsecheckout # timeout=10
     &gt; git checkout -f d525e7e6633eac266239438520cf27b37e751794 # timeout=10
    Commit message: "release 1.3.5"
     &gt; git rev-list --no-walk d525e7e6633eac266239438520cf27b37e751794 # timeout=10
    [Checks API] No suitable checks publisher found.
    [folder1] $ /bin/sh -xe /tmp/jenkins5873370620277880285.sh
    + echo text
    text
    + sleep 1
    + echo 'last line'
    last line
    [Checks API] No suitable checks publisher found.
    Finished: SUCCESS

Delete the build

.. autofunction:: builds.Build.delete()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job_build_10 = jenkins.jobs.search("new_freestyle").builds.search(10)
    print(my_job_build_10.delete())

The above code will output:

::

    request=<Request object at 2286772207216> content='[200] Successfully deleted build (10).' status_code=200

Get the build changes

.. autofunction:: builds.Build.changes()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
    print(my_job_build_2.changes)

The above code will output:

::

    <HTML output>

Get the next build
(Beta - if you delete some builds then ordering will be broken)

.. autofunction:: builds.Build.changes()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
    print(jenkins.jobs.search("new_freestyle").builds.oldest.next)

The above code will output:

::

    <jenkins_pysdk.builds.Build object at 0x000001FE5F797D30>

Get the previous build
(Beta - if you delete some builds then ordering will be broken)

.. autofunction:: builds.Build.changes()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
    print(jenkins.jobs.search("new_freestyle").builds.oldest.next)

The above code will output:

::

    <jenkins_pysdk.builds.Build object at 0x000001FE5F797D30>


Rebuild current build

.. autofunction:: builds.Build.rebuild()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.jobs.search("new_freestyle").builds.search(9).rebuild())

The above code will output:

::

    request=<Request object at 1582937378384> content='[200] Successfully triggered a rebuild of this build (9).' status_code=200


Workspace
-----------
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


Queue
-----------
.. _queue:

Iterate all queue items

.. autofunction:: queues.Queue.iter()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    for item in jenkins.queue.iter():
        print(item.number, item.job.path)

The above code will output:

::

    52 new_freestyle
    54 folder1

List all queue items

.. autofunction:: queues.Queue.list()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.queue.list())

The above code will output:

::

    [<jenkins_pysdk.queues.QueueItem object at 0x00000221F99323B0>, <jenkins_pysdk.queues.QueueItem object at 0x00000221F9932350>]

Get the newest item in the queue

.. autofunction:: queues.Queue.newest()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    newest = jenkins.queue.newest
    print(newest.job.path, newest.number)

The above code will output:

::

    new_freestyle 52

Get the oldest item in the queue

.. autofunction:: queues.Queue.oldest()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    oldest = jenkins.queue.oldest
    print(oldest.job.path, oldest.number)

The above code will output:

::

    folder1 54

Get total queue items

.. autofunction:: queues.Queue.total()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.queue.total)

The above code will output:

::

    1


QueueItem
-----------
.. _queueitem:

Get the item queue ID

.. autofunction:: queues.QueueItem.id()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.queue.oldest.id)

The above code will output:

::

    56

Get the item build number

.. autofunction:: queues.QueueItem.number()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.queue.oldest.number)

The above code will output:

::

    50

Get the item scheduled time

.. autofunction:: queues.QueueItem.scheduled()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.queue.oldest.scheduled)

The above code will output:

::

    1713706848264

Get the item blocked status

.. autofunction:: queues.QueueItem.blocked()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.queue.oldest.blocked)

The above code will output:

::

    True

Get the item stuck status

.. autofunction:: queues.QueueItem.stuck()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.queue.oldest.stuck)

The above code will output:

::

    False

Get the item queue reason

.. autofunction:: queues.QueueItem.reason()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.queue.oldest.reason)

The above code will output:

::

    Build #49 is already in progress (ETA: 3 min 48 sec)

Get the item job type

.. autofunction:: queues.QueueItem.type()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.queue.oldest.type)

The above code will output:

::

    hudson.model.FreeStyleProject

Interact with the item Build

.. autofunction:: queues.QueueItem.build()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.queue.oldest.build.console())

The above code will output:

::

    http://JenkinsDNS/job/new_freestyle/50

Interact with the item Job

.. autofunction:: queues.QueueItem.job()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.queue.oldest.job.delete())

The above code will output:

::

    request=<Request object at 2191625717376> content='[204] Successfully deleted job.' status_code=204


Credentials
-----------
.. _credentials:

Search for a system domain

.. autofunction:: credentials.Credentials.search_domains()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.credentials.search_domains("domain2"))

The above code will output:

::

    <jenkins_pysdk.credentials.Domain object at 0x0000023E2488CCD0>

Iterate all domains

.. autofunction:: credentials.Credentials.iter_domains()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    for domain in jenkins.credentials.iter_domains():
        print(domain.name)

The above code will output:

::

    Global credentials (unrestricted)
    domain2
    test_domain

Iterate all domains

.. autofunction:: credentials.Credentials.list_domains()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print([domain.name for domain in jenkins.credentials.list_domains()])

The above code will output:

::

    ['Global credentials (unrestricted)', 'domain2', 'test_domain']

Create a domain

.. autofunction:: credentials.Credentials.create_domain()
.. code-block:: python

    jenkins = Jenkins(host="https://JenkinsDNS", username="admin", passw="11e8e294cee85ee88b60d99328284d7608")
    from jenkins_pysdk.builders import Builder
    new_user = Builder.Credentials.Domain(name="global2", description="new global domain")
    print(jenkins.credentials.create_domain("global2", new_user))

The above code will output:

::

    request=<HTTPSessionRequestObject object at 1593952704992> content='[200] Successfully created domain (global2).' status_code=200


Domain
-----------
.. _domain:

Get the domain name

.. autofunction:: credentials.Domain.name()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    domain = jenkins.credentials.search_domains()
    print(domain.name)

The above code will output:

::

    Global credentials (unrestricted)

Get the domain URL

.. autofunction:: credentials.Domain.url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    domain = jenkins.credentials.search_domains()
    print(domain.url)

The above code will output:

::

    https://JenkinsDNS/manage/credentials/store/system/domain/_

Search for a credential in the domain

.. autofunction:: credentials.Domain.search()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    github_pat = jenkins.credentials.search_domains("domain2").search("Github_PAT")
       print(github_pat)

The above code will output:

::

    <jenkins_pysdk.credentials.Credential object at 0x000002B2AD79BD60>

Iterate credentials in the domain

.. autofunction:: credentials.Domain.iter()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    domain = jenkins.credentials.search_domains()  # Defaults to Global domain
    for cred in domain.iter():
        print(cred.id)

The above code will output:

::

    3f2ba384-a1bc-4785-86d0-1c82d4e8be03
    95b47fec-c078-4821-b05b-c7149f549429

List credentials in the domain

.. autofunction:: credentials.Domain.list()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    domain = jenkins.credentials.search_domains()  # Defaults to Global domain
    print([cred.id for cred in domain.list()])

The above code will output:

::

    ['3f2ba384-a1bc-4785-86d0-1c82d4e8be03', '95b47fec-c078-4821-b05b-c7149f549429']

Create a credential in the domain

.. autofunction:: credentials.Domain.create()
.. code-block:: python

    jenkins = Jenkins(host="https://JenkinsDNS", username="admin", passw="11e8e294cee85ee88b60d99328284d7608")
    from jenkins_pysdk.builders import Builder

    new_cred = Builder.Credentials.UsernamePassword(cred_id="gitlab_login", username="new_username", password="new_pasw")
    print(new_cred)
    print(jenkins.credentials.search_domains("global2").create("new_cred", new_cred))

The above code will output:

::

    <com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
        <scope>GLOBAL</scope>
        <id>gitlab_login</id>
        <username>new_username</username>
        <password>new_pasw</password>
    </com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
    request=<HTTPSessionRequestObject object at 2307040044480> content='[200] Successfully created credential (new_cred).' status_code=200


Credential
-----------
.. _credential:

Get the credential ID

.. autofunction:: credentials.Credential.id()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    github_pat = jenkins.credentials.search_domains("domain2").search("Github_PAT")
    print(github_pat.id)

The above code will output:

::

    Github_PAT

Get the credential config

.. autofunction:: credentials.Credential.config()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    github_pat = jenkins.credentials.search_domains("domain2").search("Github_PAT")
    print(github_pat.config)

The above code will output:

::

    <org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl plugin="plain-credentials@179.vc5cb_98f6db_38">
      <scope>GLOBAL</scope>
      <id>Github_PAT</id>
      <description></description>
      <secret>
        <secret-redacted/>
      </secret>
    </org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl>

Reconfigure the credential

.. autofunction:: credentials.Credential.reconfig()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    github_pat = jenkins.credentials.search_domains("domain2").search("Github_PAT")
    new_password = """<org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl plugin="plain-credentials@179.vc5cb_98f6db_38">
                        <scope>GLOBAL</scope>
                        <id>Github_PAT</id>
                        <description/>
                       <secret>
                        new_password
                        </secret>
                    </org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl>"""

The above code will output:

::

    request=<Request object at 2336431155744> content='[200] Successfully reconfigured Github_PAT.' status_code=200

Move a credential to another domain
(You can't move from System to User/Local)

.. autofunction:: credentials.Credential.move()
.. code-block:: python

    jenkins = Jenkins(host="https://JenkinsDNS", username="admin",
                      passw="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.credentials.search_domains("global2").search("gitlab_login").move("system/test_domain"))

The above code will output:

::

    request=<HTTPSessionRequestObject object at 1999299504192> content='[200] Successfully moved gitlab_login to system/test_domain.' status_code=200

Delete the credential

.. autofunction:: credentials.Credential.delete()
.. code-block:: python

    jenkins = Jenkins(host="https://JenkinsDNS", username="admin",
                      passw="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.credentials.search_domains("test_domain").search("gitlab_login").delete())

The above code will output:

::

    request=<Request object at 2398624629840> content='[200] Failed to delete credential.' status_code=200


Users
-----------
.. _users:

Search for a user

.. autofunction:: users.Users.search()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.users.search("test"))

The above code will output:

::

    <jenkins_pysdk.users.User object at 0x000001BEEBF3CD30>

Get total users

.. autofunction:: users.Users.total()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.users.search("test"))

The above code will output:

::

    3

Iterate all users

.. autofunction:: users.Users.iter()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
        for user in jenkins.users.iter():
           print(user.name)

The above code will output:

::

    admin
    new
    test

List all users

.. autofunction:: users.Users.list()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.users.list())

The above code will output:

::

    [<jenkins_pysdk.users.User object at 0x00000207B731CE50>, <jenkins_pysdk.users.User object at 0x00000207B73DD210>, <jenkins_pysdk.users.User object at 0x00000207B73DD960>]

Create a new user (as admin)

.. autofunction:: users.Users.create()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    from jenkins_pysdk.builders import Builder
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    new_user = Builder.User(username="my_new_user", password="my_new_pass", fullname="jamesJ", email="jamesj@j.com")
    print(jenkins.users.create(new_user)

The above code will output:

::

    request=<HTTPSessionRequestObject object at 1868709648224> content='[200] Successfully created user (my_new_user).' status_code=200


User
-----------
.. _user:

Get the user name

.. autofunction:: users.User.name()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    user = jenkins.users.search("test")
    print(user.name)

The above code will output:

::

    test

Get the user URL

.. autofunction:: users.User.url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    user = jenkins.users.search("test")
    print(user.url)

The above code will output:

::

    https://JenkinsDNS/user/test

Get the user description

.. autofunction:: users.User.description()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    user = jenkins.users.search("test")
    print(user.description)

The above code will output:

::

    This user is using for testing automation.

Get the user's credentials

.. autofunction:: users.User.credentials()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    user = jenkins.users.search("admin")
    print([cred.id for cred in user.credentials(domain="my_creds_store").list()])

The above code will output:

::

    ['my_pypi_password']

Get the user's views

.. autofunction:: users.User.views()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    user = jenkins.users.search("test")
    print(user.views)

The above code will output:

::

    [<jenkins_pysdk.views.View object at 0x000002AF1883DDB0>, <jenkins_pysdk.views.View object at 0x000002AF1883CCD0>, <jenkins_pysdk.views.View object at 0x000002AF1883C6A0>, <jenkins_pysdk.views.View object at 0x000002AF1883C8B0>, <jenkins_pysdk.views.View object at 0x000002AF1883D0C0>]

Get the user's builds

.. autofunction:: users.User.builds()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    user = jenkins.users.search("admin")
    print(user.builds)

The above code will output:

::

    <HTML Output>

Delete the user

.. autofunction:: users.User.delete()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    user = jenkins.users.search("test")
    print(user.delete())

The above code will output:

::

    request=<Request object at 2813768495920> content='[400] Failed to delete user (test).' status_code=200

Terminate a users' sessions

.. autofunction:: users.User.logout()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    user = jenkins.users.search("test")
    print(user.logout())

The above code will output:

::

    request=<Request object at 2073057402192> content='[200] Successfully logged out.' status_code=200


Me
-----------
.. _me:

Get my username

.. autofunction:: users.User.name()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.me.name)

The above code will output:

::

    admin

Get my user URL

.. autofunction:: users.User.url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.me.url)

The above code will output:

::

    https://JenkinsDNS/me

Get my user description

.. autofunction:: users.User.description()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.me.description)

The above code will output:

::

    None

Get my user credentials

.. autofunction:: users.User.credentials()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print([passw.id for passw in jenkins.me.credentials(domain="admin_domain").list()])

The above code will output:

::

    ['my_pypi_password']

Get my user views

.. autofunction:: users.User.views()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print([view.name for view in jenkins.me.views])

The above code will output:

::

    ['builder_1', 'builder_2', 'builder_4', 'builder_d', 'builder_e', 'builder_folder', 'builder_w', 'folder1', 'folder3', 'my_new_folder_name', 'new_folder', 'new_freestyle']

Get my user builds

.. autofunction:: users.User.builds()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.me.builds)

The above code will output:

::

    No REST endpoint available... returning HTML Request for the moment...
    <HTML Output>

Terminate my session

.. autofunction:: users.User.logout()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
     print(jenkins.me.logout())

The above code will output:

::

    request=<Request object at 2012346268496> content='[200] Successfully logged out.' status_code=200


Views
-----------
.. _views:

Search for a view

.. autofunction:: views.Views.search()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.views.search("All"))

The above code will output:

::

    <jenkins_pysdk.views.View object at 0x0000026497A93820>


Iterate all views

.. autofunction:: views.Views.iter()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    for view in jenkins.views.iter():
        print(view.name)

The above code will output:

::

    all
    m
    my

List all views

.. autofunction:: views.Views.list()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.views.list())

The above code will output:

::

    [<jenkins_pysdk.views.View object at 0x0000013439AA9E10>, <jenkins_pysdk.views.View object at 0x0000013439AA9DE0>, <jenkins_pysdk.views.View object at 0x0000013439AA9DB0>]

Create a view

.. autofunction:: views.Views.create()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    xml = """
       <hudson.model.ListView>
         <name>my_view</name>
         <mode>hudson.model.ListView</mode>
         <description>Your view description</description>
         <jobNames>
           <comparator class="hudson.util.CaseInsensitiveComparator"/>
           <string>new_freestyle</string>
         </jobNames>
         <columns>
           <hudson.views.StatusColumn/>
           <hudson.views.WeatherColumn/>
           <hudson.views.JobColumn/>
         </columns>
         <recurse>true</recurse>
       </hudson.model.ListView>
       """
    print(jenkins.views.create("my_view", xml))

The above code will output:

::

    request=<Request object at 2275566295520> content='[200] Successfully created my_view.' status_code=200


View
-----------
.. _view:

Get the view name

.. autofunction:: views.View.name()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.views.search("All").name)

The above code will output:

::

    All

Get the view URL

.. autofunction:: views.View.url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.views.search("All").url)

The above code will output:

::

    http://JenkinsDNS/view/All

Reconfigure the view
(Job order must be the same as the order in the application, otherwise you will get dodgy results)
E.g.
builder_e is higher up in the list of jobs so it goes above builder_folder, which is underneath it in the list :)

.. autofunction:: views.View.reconfig()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    xml = """
       <hudson.model.ListView>
         <name>my_view</name>
         <description>Your view description</description>
         <filterExecutors>false</filterExecutors>
         <filterQueue>false</filterQueue>
         <properties class="hudson.model.View$PropertyList"/>
         <jobNames>
           <comparator class="hudson.util.CaseInsensitiveComparator"/>
           <string>builder_e</string>
           <string>builder_folder</string>
           <string>builder_w</string>
           <string>new_freestyle</string>
         </jobNames>
         <jobFilters/>
         <columns>
           <hudson.views.StatusColumn/>
           <hudson.views.WeatherColumn/>
           <hudson.views.JobColumn/>
         </columns>
         <recurse>true</recurse>
       </hudson.model.ListView>
      """
      print(jenkins.views.search("my_view").reconfig(xml))

The above code will output:

::

    request=<Request object at 2153302882832> content='[200] Successfully reconfigured view (my_view).' status_code=200

Delete the view

.. autofunction:: views.View.delete()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.views.search("YourViewName").delete())

The above code will output:

::

    request=<Request object at 2246812676752> content='[200] Successfully deleted view (YourViewName).' status_code=200


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
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.plugins.updates.search("ssh-credentials").name)

The above code will output:

::

    ssh-credentials

Iterate all plugins needing an updates

.. autofunction:: plugins.PluginGroup.iter()
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
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.plugins.installed.search("ant").version)

The above code will output:

::

    497.v94e7d9fffa_b_9

Iterate all installed plugins

.. autofunction:: plugins.PluginGroup.iter()
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
