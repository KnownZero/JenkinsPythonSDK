Examples
========

System
-----------

.. _system:

Connect to the application


.. autofunction:: jenkins.Jenkins.connect()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.connect())
request=<HTTPRequestObject object at 1718212996176> response=<HTTPResponseObject object at 1718223889776> content='[200] Successfully connected to JenkinsDNS.' status_code=200

Get the Jenkins version


.. autofunction:: jenkins.Jenkins.version()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.version)
2.448

Restart the application


.. autofunction:: jenkins.Jenkins.restart()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.restart(graceful=True))
request=<HTTPRequestObject object at 2603665289872> content='[200] Restarting the Jenkins instance... please wait...' status_code=200

Enable Quiet Mode


.. autofunction:: jenkins.Jenkins.quiet_mode()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.quiet_mode(duration=30))
request=<HTTPRequestObject object at 1938732315280> content='[200] Successfully enabled Quiet Mode for 30 seconds.' status_code=200

Shutdown the application


.. autofunction:: jenkins.Jenkins.shutdown()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.shutdown())
request=<HTTPRequestObject object at 2613641997152> content='[200] Shutting down...' status_code=200

Logout


.. autofunction:: jenkins.Jenkins.logout()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.logout())
request=<HTTPRequestObject object at 2453417290592> content='[200] Successfully logged out.' status_code=200

Reload config from disk


.. autofunction:: jenkins.Jenkins.reload()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.reload)
request=<HTTPRequestObject object at 2741687462992> content='[200] Successfully reloaded configuration.' status_code=200

Get the available executors


.. autofunction:: jenkins.Jenkins.available_executors()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.available_executors)
No executors are available.


Folders
-----------

.. _folders:

Interact with a folder


.. autofunction:: jobs.Folders.search()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.folders.search("my_new_folder_name"))
<jenkins_pysdk.jobs.Folder object at 0x00000295B24B4AF0>

List all folders


.. autofunction:: jobs.Folders.list()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> for folder in jenkins.folders.list():
>>>     print(folder.path, folder.url)
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

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> for folder in jenkins.folders.iter():
>>>     print(folder.path, folder.url)
builder_1 https://JenkinsDNS/job/builder_1/
builder_2 https://JenkinsDNS/job/builder_2/
builder_4 https://JenkinsDNS/job/builder_4/
builder_d https://JenkinsDNS/job/builder_d/
builder_e https://JenkinsDNS/job/builder_e/
builder_folder https://JenkinsDNS/job/builder_folder/
builder_w https://JenkinsDNS/job/builder_w/
new_folder/new_job23 https://JenkinsDNS/job/new_folder/job/new_job23/
new_folder/test_folder https://JenkinsDNS/job/new_folder/job/test_folder/

Create a new folder


.. autofunction:: builders.Builder.Folder()
.. autofunction:: jobs.Folders.create()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> from builders import Builder
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_folder = Builder.Folder(name="my_new_folder_name", description="my description is pretty simple.")
>>> print(jenkins.folders.create("my_new_folder_name", my_folder))
request=<HTTPRequestObject object at 1935978150336> content='[200] Successfully created my_new_folder_name.' status_code=200


Check if the path is a folder


.. autofunction:: jobs.Folders.is_folder()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.folders.is_folder("folder3/sub_folder"))
True

Folder
-----------

.. _folder:

Reconfigure a folder


.. autofunction:: jobs.Folder.reconfig()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> from builders.builder import Builder
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> new_folder = Builder.Folder(name="my_new_folder_name", description="Reconfigured")
>>> print(jenkins.folders.search("my_new_folder_name").reconfig(new_folder))
request=<HTTPRequestObject object at 2282610093216> content='[200] Successfully reconfigured my_new_folder_name.' status_code=200


Get the first folder URL


.. autofunction:: jobs.Folder.url()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> from builders.builder import Builder
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.folders.list()[0].url)
https://JenkinsDNS/job/builder_1/

Get the first folder Path


.. autofunction:: jobs.Folder.path()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.folders.list()[0].path)
builder_1

Copy a folder

(You are interacting with a specific folder location, so you can't copy a folder up a level)

.. autofunction:: jobs.Folder.copy()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_folder = jenkins.folders.search("folder3")
>>> print(my_folder.copy(new_job_name="another_sub_folder", copy_job_name="sub_folder"))
request=<HTTPRequestObject object at 1480728865872> content='[200] Successfully copied sub_folder to another_sub_folder.' status_code=200

Delete the current folder


.. autofunction:: jobs.Folder.delete()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.folders.search("folder3/another_sub_folder").delete)
request=<HTTPRequestObject object at 2309917207952> content='[204] Successfully deleted folder.' status_code=204

Create a folder

(You are interacting with a specific folder location, so you can only create sub-folders)

.. autofunction:: jobs.Folder.create()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> from builders import Builder
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_folder = Builder.Folder(name="my_new_folder_name", description="my description is pretty simple.")
>>> print(jenkins.folders.search("folder3/sub_folder").create("another_sub_folder", my_folder))
request=<HTTPRequestObject object at 1660448175456> content='[200] Successfully created another_sub_folder.' status_code=200

Get the folder config


.. autofunction:: jobs.Folder.config()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.folders.search("folder3/another_sub_folder").config)
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

Interact with a job


.. autofunction:: jobs.Jobs.search()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("new_freestyle"))
<jenkins_pysdk.jobs.Job object at 0x000001E515CD4A90>

List all jobs


.. autofunction:: jobs.Jobs.list()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.list())
[<jenkins_pysdk.jobs.Job object at 0x000002B4E528A710>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5119780>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5118580>, <jenkins_pysdk.jobs.Job object at 0x000002B4E511BC10>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5119870>]

Iterate all jobs

.. autofunction:: jobs.Jobs.iter()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.iter())
[<jenkins_pysdk.jobs.Job object at 0x000002B4E528A710>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5119780>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5118580>, <jenkins_pysdk.jobs.Job object at 0x000002B4E511BC10>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5119870>]

Create a freestyle job


.. autofunction:: jobs.Jobs.create()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> freestyle = """<project>
>>>                 <description>My description goes here</description>
>>>                 <keepDependencies>false</keepDependencies>
>>>                 <properties/>
>>>                 <scm class="hudson.scm.NullSCM"/>
>>>                 <canRoam>true</canRoam>
>>>                 <disabled>false</disabled>
>>>                 <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
>>>                 <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
>>>                 <triggers/>
>>>                 <concurrentBuild>false</concurrentBuild>
>>>                 <builders/>
>>>                 <publishers/>
>>>                 <buildWrappers/>
>>>                </project>"""
>>> print(jenkins.jobs.create("freestyle_created", freestyle, jenkins.FreeStyle))
request=<HTTPRequestObject object at 2205281481040> content='[200] Successfully created freestyle_created.' status_code=200

Check if the path is a job


.. autofunction:: jobs.Jobs.is_job()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.is_job("folder3/freestyle_4"))
True


Job
-----------

Disable a job


.. autofunction:: jobs.Job.disable()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("folder3/freestyle_4").disable)
request=<HTTPRequestObject object at 2523890810240> content='[200] Successfully disabled folder3/freestyle_4.' status_code=200

Get a job URL


.. autofunction:: jobs.Job.url()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("folder3/freestyle_4").url)
https://JenkinsDNS/job/folder3/job/freestyle_4

Get a job path


.. autofunction:: jobs.Job.path()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("folder3/freestyle_4").path)
folder3/freestyle_4


Get job URL


.. autofunction:: jobs.Job.enable()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("folder3/freestyle_4").enable)
request=<HTTPRequestObject object at 1986068844192> content='[200] Successfully enabled folder3/freestyle_4.' status_code=200

Reconfigure a job


.. autofunction:: jobs.Job.reconfig()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> from jenkins_pysdk.builders import Builder
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> config = Builder._Templates.Freestyle.format(description="New desc", disabled=True)
>>> print(jenkins.jobs.search("freestyle_created").reconfig(config))
request=<HTTPRequestObject object at 1772165197280> content='[200] Successfully reconfigured freestyle_created.' status_code=200

Delete a job


.. autofunction:: jobs.Job.delete()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("freestyle_created").delete)
request=<HTTPRequestObject object at 1721615969440> content='[204] Successfully deleted job.' status_code=204

Get job config


.. autofunction:: jobs.Job.config()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("new_freestyle").config)
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

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("new_freestyle").builds)
<jenkins_pysdk.builds.Builds object at 0x000001EF9C34A860>


Builds
-----------

Search for a build


.. autofunction:: builds.Builds.search()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job = jenkins.jobs.search("new_freestyle")
>>> print(my_job.builds.search(10))
<jenkins_pysdk.builds.Build object at 0x0000025270CDFD00>


Get the total build history of a job


.. autofunction:: builds.Builds.total()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job = jenkins.jobs.search("new_freestyle")
>>> print(my_job.builds.total)
6

Iterate all job's builds


.. autofunction:: builds.Builds.iter()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job = jenkins.jobs.search("new_freestyle")
>>> for build in my_job.builds.iter():
>>>     print(build.number)
10
9
8
7
2
1

List all job's builds


.. autofunction:: builds.Builds.list()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job = jenkins.jobs.search("new_freestyle")
>>> print(my_job.builds.list())
[<jenkins_pysdk.builds.Build object at 0x00000131E097FD00>, <jenkins_pysdk.builds.Build object at 0x00000131E097FAF0>, <jenkins_pysdk.builds.Build object at 0x00000131E097FE20>, <jenkins_pysdk.builds.Build object at 0x00000131E097FBB0>, <jenkins_pysdk.builds.Build object at 0x00000131E097F850>, <jenkins_pysdk.builds.Build object at 0x00000131E08BC4C0>]


Get the latest saved build


.. autofunction:: builds.Builds.latest()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job = jenkins.jobs.search("new_freestyle")
>>> print(my_job.builds.latest.url)
https://JenkinsDNS/job/new_freestyle/10/

Get the oldest saved build


.. autofunction:: builds.Builds.oldest()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job = jenkins.jobs.search("new_freestyle")
>>> print(my_job.builds.latest.url)
https://JenkinsDNS/job/new_freestyle/1/

Trigger a new build


.. autofunction:: builds.Builds.build()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("new_freestyle").builds.build({"choises": "A", "a_bool": False}, delay=10))
request=<HTTPRequestObject object at 1874065655344> content='[201] Successfully triggered a new build.' status_code=201


Rebuild the last build


.. autofunction:: builds.Builds.rebuild_last()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("new_freestyle").builds.rebuild_last)
request=<HTTPRequestObject object at 2881680762624> content='[200] Successfully triggered a rebuild of the last build.' status_code=200


Build
-----------

Get the build number


.. autofunction:: builds.Build.number()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_10 = jenkins.jobs.search("new_freestyle").builds.search(10)
>>> print(my_job_build_10.number)
10

Get the build URL


.. autofunction:: builds.Build.url()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
>>> print(my_job_build_2.url)
https://JenkinsDNS/job/new_freestyle/2/

Get the build result


.. autofunction:: builds.Build.result()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
>>> print(my_job_build_2.result)
SUCCESS

Get the build timestamp


.. autofunction:: builds.Build.timestamp()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("new_freestyle").builds.latest.timestamp)
1711475427971


Get the build description


.. autofunction:: builds.Build.description()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("new_freestyle").builds.latest.description)
None

Check if the build is done


.. autofunction:: builds.Build.done()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
>>> print(my_job_build_2.done)
True

Get the build duration


.. autofunction:: builds.Build.duration()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
>>> print(my_job_build_2.duration)
15

Get the build console logs


.. autofunction:: builds.Build.console()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_10 = jenkins.jobs.search("new_freestyle").builds.search(10)
>>> print(my_job_build_10.console())
Started by user admin
Running as SYSTEM
Building in workspace /var/lib/jenkins/workspace/new_freestyle
Finished: SUCCESS

Delete the build


.. autofunction:: builds.Build.delete()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_10 = jenkins.jobs.search("new_freestyle").builds.search(10)
>>> print(my_job_build_10.delete)
request=<HTTPRequestObject object at 2286772207216> content='[200] Successfully deleted build (10).' status_code=200

Get the build changes


.. autofunction:: builds.Build.changes()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
>>> print(my_job_build_2.changes)
<HTML output>

Get the next build
(Beta - if you delete some builds then ordering will be broken)


.. autofunction:: builds.Build.changes()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
>>> print(jenkins.jobs.search("new_freestyle").builds.oldest.next)
<jenkins_pysdk.builds.Build object at 0x000001FE5F797D30>

Get the previous build
(Beta - if you delete some builds then ordering will be broken)


.. autofunction:: builds.Build.changes()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
>>> print(jenkins.jobs.search("new_freestyle").builds.oldest.next)
<jenkins_pysdk.builds.Build object at 0x000001FE5F797D30>


Rebuild current build


.. autofunction:: builds.Build.rebuild()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("new_freestyle").builds.search(9).rebuild)
request=<HTTPRequestObject object at 1582937378384> content='[200] Successfully triggered a rebuild of this build (9).' status_code=200


Credentials
-----------

Search for a system domain


.. autofunction:: credentials.Credentials.search_domains()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.credentials.search_domains("domain2"))
<jenkins_pysdk.credentials.Domain object at 0x0000023E2488CCD0>

Iterate all domains


.. autofunction:: credentials.Credentials.iter_domains()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> for domain in jenkins.credentials.iter_domains():
>>>     print(domain.name)
Global credentials (unrestricted)
domain2
test_domain

Iterate all domains


.. autofunction:: credentials.Credentials.list_domains()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print([domain.name for domain in jenkins.credentials.list_domains()])
['Global credentials (unrestricted)', 'domain2', 'test_domain']

Create a domain


.. autofunction:: credentials.Credentials.create_domain()
.. code-block:: python

>>> jenkins = Jenkins(host="https://JenkinsDNS", username="admin",
>>>                   passw="11e8e294cee85ee88b60d99328284d7608")
>>> from builders import Builder
>>> new_user = Builder.Credentials.Domain(name="global2", description="new global domain")
>>> print(jenkins.credentials.create_domain("global2", new_user))
request=<HTTPSessionRequestObject object at 1593952704992> content='[200] Successfully created domain (global2).' status_code=200


Domain
-----------

Get the domain name


.. autofunction:: credentials.Domain.name()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> domain = jenkins.credentials.search_domains()
>>> print(domain.name)
Global credentials (unrestricted)

Get the domain URL


.. autofunction:: credentials.Domain.url()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> domain = jenkins.credentials.search_domains()
>>> print(domain.url)
https://JenkinsDNS/manage/credentials/store/system/domain/_

Search for a credential in the domain


.. autofunction:: credentials.Domain.search()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> github_pat = jenkins.credentials.search_domains("domain2").search("Github_PAT")
>>>    print(github_pat)
<jenkins_pysdk.credentials.Credential object at 0x000002B2AD79BD60>


Iterate credentials in the domain


.. autofunction:: credentials.Domain.iter()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> domain = jenkins.credentials.search_domains()  # Defaults to Global domain
>>> for cred in domain.iter():
>>>     print(cred.id)
3f2ba384-a1bc-4785-86d0-1c82d4e8be03
95b47fec-c078-4821-b05b-c7149f549429

List credentials in the domain


.. autofunction:: credentials.Domain.list()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> domain = jenkins.credentials.search_domains()  # Defaults to Global domain
>>> print([cred.id for cred in domain.list()])
['3f2ba384-a1bc-4785-86d0-1c82d4e8be03', '95b47fec-c078-4821-b05b-c7149f549429']

Create a credential in the domain


.. autofunction:: credentials.Domain.create()
.. code-block:: python

>>> jenkins = Jenkins(host="https://JenkinsDNS", username="admin",
>>>                   passw="11e8e294cee85ee88b60d99328284d7608")
>>> from builders import Builder
>>>
>>> new_cred = Builder.Credentials.UsernamePassword(cred_id="gitlab_login", username="new_username", password="new_pasw")
>>> print(new_cred)
>>> print(jenkins.credentials.search_domains("global2").create("new_cred", new_cred))
<com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
    <scope>GLOBAL</scope>
    <id>gitlab_login</id>
    <username>new_username</username>
    <password>new_pasw</password>
</com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
request=<HTTPSessionRequestObject object at 2307040044480> content='[200] Successfully created credential (new_cred).' status_code=200


Credential
-----------

Get the credential ID


.. autofunction:: credentials.Credential.id()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> github_pat = jenkins.credentials.search_domains("domain2").search("Github_PAT")
>>> print(github_pat.id)
Github_PAT

Get the credential config


.. autofunction:: credentials.Credential.config()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> github_pat = jenkins.credentials.search_domains("domain2").search("Github_PAT")
>>> print(github_pat.config)
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

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> github_pat = jenkins.credentials.search_domains("domain2").search("Github_PAT")
>>> new_password = """<org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl plugin="plain-credentials@179.vc5cb_98f6db_38">
>>>                     <scope>GLOBAL</scope>
>>>                     <id>Github_PAT</id>
>>>                     <description/>
>>>                    <secret>
>>>                     new_password
>>>                     </secret>
>>>                 </org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl>"""
request=<HTTPRequestObject object at 2336431155744> content='[200] Successfully reconfigured Github_PAT.' status_code=200

Move a credential to another domain
(You can't move from System to User/Local)


.. autofunction:: credentials.Credential.move()
.. code-block:: python

>>> jenkins = Jenkins(host="https://JenkinsDNS", username="admin",
>>>                   passw="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.credentials.search_domains("global2").search("gitlab_login").move("system/test_domain"))
request=<HTTPSessionRequestObject object at 1999299504192> content='[200] Successfully moved gitlab_login to system/test_domain.' status_code=200


Users
-----------

Search for a user


.. autofunction:: users.Users.search()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.users.search("test"))
<jenkins_pysdk.users.User object at 0x000001BEEBF3CD30>

Get total users


.. autofunction:: users.Users.total()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.users.search("test"))
3

Iterate all users


.. autofunction:: users.Users.iter()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>>     for user in jenkins.users.iter():
>>>        print(user.name)
admin
new
test

List all users


.. autofunction:: users.Users.list()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.users.list())
[<jenkins_pysdk.users.User object at 0x00000207B731CE50>, <jenkins_pysdk.users.User object at 0x00000207B73DD210>, <jenkins_pysdk.users.User object at 0x00000207B73DD960>]


Create a new user (as admin)

.. autofunction:: users.Users.create()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> from builders import Builder
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> new_user = Builder.User(username="my_new_user", password="my_new_pass", fullname="jamesJ", email="jamesj@j.com")
>>> print(jenkins.users.create(new_user)
request=<HTTPSessionRequestObject object at 1868709648224> content='[200] Successfully created user (my_new_user).' status_code=200



User
-----------

Get the user name


.. autofunction:: users.User.name()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("test")
>>> print(user.name)
test

Get the user URL


.. autofunction:: users.User.url()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("test")
>>> print(user.url)
https://JenkinsDNS/user/test

Get the user description


.. autofunction:: users.User.description()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("test")
>>> print(user.description)
This user is using for testing automation.

Get the user's credentials


.. autofunction:: users.User.credentials()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("admin")
>>> print([cred.id for cred in user.credentials(domain="my_creds_store").list()])
['my_pypi_password']

Get the user's views


.. autofunction:: users.User.views()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("test")
>>> print(user.views)
[<jenkins_pysdk.views.View object at 0x000002AF1883DDB0>, <jenkins_pysdk.views.View object at 0x000002AF1883CCD0>, <jenkins_pysdk.views.View object at 0x000002AF1883C6A0>, <jenkins_pysdk.views.View object at 0x000002AF1883C8B0>, <jenkins_pysdk.views.View object at 0x000002AF1883D0C0>]

Get the user's builds


.. autofunction:: users.User.builds()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("admin")
>>> print(user.builds)
No REST endpoint available... returning HTML response for the moment...
<HTML Output>

Delete the user


.. autofunction:: users.User.delete()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("test")
>>> print(user.delete)
request=<HTTPRequestObject object at 2813768495920> content='[400] Failed to delete user (test).' status_code=200

Terminate a users' sessions


.. autofunction:: users.User.logout()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("test")
>>> print(user.logout)
request=<HTTPRequestObject object at 2073057402192> content='[200] Successfully logged out.' status_code=200


Me
-----------

Get my username


.. autofunction:: users.User.name()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.me.name)
admin

Get my user URL


.. autofunction:: users.User.url()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.me.url)
https://JenkinsDNS/me


Get my user description


.. autofunction:: users.User.description()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.me.description)
None

Get my user credentials


.. autofunction:: users.User.credentials()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print([passw.id for passw in jenkins.me.credentials(domain="admin_domain").list()])
['my_pypi_password']


Get my user views


.. autofunction:: users.User.views()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print([view.name for view in jenkins.me.views])
['builder_1', 'builder_2', 'builder_4', 'builder_d', 'builder_e', 'builder_folder', 'builder_w', 'folder1', 'folder3', 'my_new_folder_name', 'new_folder', 'new_freestyle']


Get my user builds


.. autofunction:: users.User.builds()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.me.builds)
No REST endpoint available... returning HTML response for the moment...
<HTML Output>

Terminate my session


.. autofunction:: users.User.logout()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>>  print(jenkins.me.logout)
request=<HTTPRequestObject object at 2012346268496> content='[200] Successfully logged out.' status_code=200


Views
-----------

Search for a view


.. autofunction:: views.Views.search()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.views.search("All"))

Iterate all views


.. autofunction:: views.Views.iter()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> for view in jenkins.views.iter():
>>>     print(view.name)
all
m
my

List all views


.. autofunction:: views.Views.list()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.views.list())
[<jenkins_pysdk.views.View object at 0x0000013439AA9E10>, <jenkins_pysdk.views.View object at 0x0000013439AA9DE0>, <jenkins_pysdk.views.View object at 0x0000013439AA9DB0>]

Create a view


.. autofunction:: views.Views.create()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> xml = """
>>>    <hudson.model.ListView>
>>>      <name>my_view</name>
>>>      <mode>hudson.model.ListView</mode>
>>>      <description>Your view description</description>
>>>      <jobNames>
>>>        <comparator class="hudson.util.CaseInsensitiveComparator"/>
>>>        <string>new_freestyle</string>
>>>      </jobNames>
>>>      <columns>
>>>        <hudson.views.StatusColumn/>
>>>        <hudson.views.WeatherColumn/>
>>>        <hudson.views.JobColumn/>
>>>      </columns>
>>>      <recurse>true</recurse>
>>>    </hudson.model.ListView>
>>>    """
>>> print(jenkins.views.create("my_view", xml))
request=<HTTPRequestObject object at 2275566295520> content='[200] Successfully created my_view.' status_code=200


View
-----------

Get the view name


.. autofunction:: views.View.name()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.views.search("All").name)
All

Get the view URL


.. autofunction:: views.View.url()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.views.search("All").url)
http://JenkinsDNS/view/All

Reconfigure the view
(Job order must be the same as the order in the application, otherwise you will get dodgy results)
E.g.
builder_e is higher up in the list of jobs so it goes above builder_folder, which is underneath it in the list :)

.. autofunction:: views.View.reconfig()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> xml = """
>>>    <hudson.model.ListView>
>>>      <name>my_view</name>
>>>      <description>Your view description</description>
>>>      <filterExecutors>false</filterExecutors>
>>>      <filterQueue>false</filterQueue>
>>>      <properties class="hudson.model.View$PropertyList"/>
>>>      <jobNames>
>>>        <comparator class="hudson.util.CaseInsensitiveComparator"/>
>>>        <string>builder_e</string>
>>>        <string>builder_folder</string>
>>>        <string>builder_w</string>
>>>        <string>new_freestyle</string>
>>>      </jobNames>
>>>      <jobFilters/>
>>>      <columns>
>>>        <hudson.views.StatusColumn/>
>>>        <hudson.views.WeatherColumn/>
>>>        <hudson.views.JobColumn/>
>>>      </columns>
>>>      <recurse>true</recurse>
>>>    </hudson.model.ListView>
>>>   """
>>>   print(jenkins.views.search("my_view").reconfig(xml))
request=<HTTPRequestObject object at 2153302882832> content='[200] Successfully reconfigured view (my_view).' status_code=200


Plugins
-----------

Interact with available plugins


.. autofunction:: plugins.Plugins.available()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.plugins.available)
<jenkins_pysdk.plugins.PluginGroup object at 0x000001E53CD5B070>

Interact with update plugins


.. autofunction:: plugins.Plugins.updates()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.plugins.updates)
<jenkins_pysdk.plugins.PluginGroup object at 0x000001A3830FB070>

Upload a plugin


.. autofunction:: plugins.Plugins.upload()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>>


Interact with UpdateCenter


.. autofunction:: plugins.Plugins.sites()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>>


Available
-----------

Search for an available plugin
(A plugin that is not already installed)

The plugin ID/Name is found in the plugin docs 'ID' field
In the below link you will see ID: blueocean-rest
https://plugins.jenkins.io/blueocean-rest/

.. autofunction:: plugins.PluginGroup.search()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.plugins.available.search("blueocean-rest"))
<jenkins_pysdk.plugins.Plugin object at 0x000001AB664C0370>

Iterate all available plugins

.. autofunction:: plugins.PluginGroup.iter()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> for plugin in jenkins.plugins.available.iter(_paginate=500):
>>>     print(plugin.name, plugin.version)
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

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.plugins.available.list(_paginate=1000))
[<jenkins_pysdk.plugins.Plugin object at 0x000002316EB50520>, <jenkins_pysdk.plugins.Plugin object at 0x000002316EB50130>, <jenkins_pysdk.plugins.Plugin object at 0x000002316EB50160>, <truncated...>]


Updates
-----------

Search for a plugin needing an update

The plugin ID/Name is found in the plugin docs 'ID' field
In the below link you will see ID: ssh-credentials
https://plugins.jenkins.io/ssh-credentials/

.. autofunction:: plugins.PluginGroup.search()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.plugins.updates.search("ssh-credentials").name)
ssh-credentials

Iterate all plugins needing an updates

.. autofunction:: plugins.PluginGroup.iter()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> for plugin in jenkins.plugins.updates.iter(_paginate=500):
>>>     print(plugin.name, plugin.version, plugin.url)
checks-api 2.2.0 https://updates.jenkins.io/download/plugins/checks-api/2.2.0/checks-api.hpi
github-branch-source 1787.v8b_8cd49a_f8f1 https://updates.jenkins.io/download/plugins/github-branch-source/1787.v8b_8cd49a_f8f1/github-branch-source.hpi
gradle 2.11 https://updates.jenkins.io/download/plugins/gradle/2.11/gradle.hpi
ionicons-api 70.v2959a_b_74e3cf https://updates.jenkins.io/download/plugins/ionicons-api/70.v2959a_b_74e3cf/ionicons-api.hpi
jackson2-api 2.17.0-379.v02de8ec9f64c https://updates.jenkins.io/download/plugins/jackson2-api/2.17.0-379.v02de8ec9f64c/jackson2-api.hpi
<truncated...>

List all plugins needing an updates

.. autofunction:: plugins.PluginGroup.list()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.plugins.updates.list(_paginate=500))
[<jenkins_pysdk.plugins.Plugin object at 0x000001CF357C4B20>, <truncated...>]


Installed
-----------

Search for an installed plugin

The plugin ID/Name is found in the plugin docs 'ID' field
In the below link you will see ID: ssh-credentials
https://plugins.jenkins.io/ssh-credentials/

.. autofunction:: plugins.PluginGroup.search()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.plugins.installed.search("ant").version)
497.v94e7d9fffa_b_9

Iterate all installed plugins

.. autofunction:: plugins.PluginGroup.iter()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> for plugin in jenkins.plugins.installed.iter(_paginate=500):
>>>     print(plugin.name, plugin.active)
ant True
antisamy-markup-formatter True
apache-httpcomponents-client-4-api True
bootstrap5-api True
bouncycastle-api True
<truncated...>

List all installed plugins

.. autofunction:: plugins.PluginGroup.list()
.. code-block:: python

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.plugins.updates.list(_paginate=500))
[<jenkins_pysdk.plugins.Installed object at 0x0000021DBB290A30>, <truncated...>]
