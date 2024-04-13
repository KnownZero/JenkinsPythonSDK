Examples
========

System
====

.. _system:

Connect to the application
----------------

.. autofunction:: jenkins.Jenkins.connect()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.connect())
request=<HTTPRequestObject object at 1718212996176> response=<HTTPResponseObject object at 1718223889776> content='[200] Successfully connected to JenkinsDNS.' status_code=200

Get the Jenkins version
----------------

.. autofunction:: jenkins.Jenkins.version()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.version)

Get the available executors
----------------

.. autofunction:: jenkins.Jenkins.available_executors()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.available_executors)
No executors are available.

Restart the application
----------------

.. autofunction:: jenkins.Jenkins.restart()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.restart(graceful=True))
request=<HTTPRequestObject object at 2603665289872> content='[200] Restarting the Jenkins instance... please wait...' status_code=200

Enable Quiet Mode
----------------

.. autofunction:: jenkins.Jenkins.quiet_mode()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.quiet_mode(duration=30))
request=<HTTPRequestObject object at 1938732315280> content='[200] Successfully enabled Quiet Mode for 30 seconds.' status_code=200

Shutdown the application
----------------

.. autofunction:: jenkins.Jenkins.shutdown()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.shutdown())
request=<HTTPRequestObject object at 2613641997152> content='[200] Shutting down...' status_code=200

Logout
----------------

.. autofunction:: jenkins.Jenkins.logout()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.logout())
request=<HTTPRequestObject object at 2453417290592> content='[200] Successfully logged out.' status_code=200

Reload config from disk
----------------

.. autofunction:: jenkins.Jenkins.reload()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.reload)
request=<HTTPRequestObject object at 2741687462992> content='[200] Successfully reloaded configuration.' status_code=200


Folders
====

.. _folders:

Interact with a folder
----------------

.. autofunction:: jobs.Folders.search()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.folders.search("my_new_folder_name"))
<jenkins_pysdk.jobs.Folder object at 0x00000295B24B4AF0>

List all folders
----------------

.. autofunction:: jobs.Folders.list()

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
----------------

.. autofunction:: jobs.Folders.iter()

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

Create a new folders
----------------

.. autofunction:: builders.Builder.Folder()
.. autofunction:: jobs.Folders.create()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> from builders import Builder
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_folder = Builder.Folder(name="my_new_folder_name", description="my description is pretty simple.")
>>> print(jenkins.folders.create("my_new_folder_name", my_folder))
request=<HTTPRequestObject object at 1935978150336> content='[200] Successfully created my_new_folder_name.' status_code=200


Check if the path is a folder
----------------

.. autofunction:: jobs.Folders.is_folder()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.folders.is_folder("folder3/sub_folder"))
True

Folder
====

.. _folder:

Reconfigure a folder
----------------

.. autofunction:: jobs.Folder.reconfig()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> from builders.builder import Builder
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> new_folder = Builder.Folder(name="my_new_folder_name", description="Reconfigured")
>>> print(jenkins.folders.search("my_new_folder_name").reconfig(new_folder))
request=<HTTPRequestObject object at 2282610093216> content='[200] Successfully reconfigured my_new_folder_name.' status_code=200


Get the first folder URL
----------------

.. autofunction:: jobs.Folder.url()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> from builders.builder import Builder
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.folders.list()[0].url)
https://JenkinsDNS/job/builder_1/

Get the first folder Path
----------------

.. autofunction:: jobs.Folder.url()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.folders.list()[0].path)
builder_1

Copy a folder
----------------
(You are interacting with a specific folder location, so you can't copy a folder up a level)

.. autofunction:: jobs.Folder.copy()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_folder = jenkins.folders.search("folder3")
>>> print(my_folder.copy(new_job_name="another_sub_folder", copy_job_name="sub_folder"))
request=<HTTPRequestObject object at 1480728865872> content='[200] Successfully copied sub_folder to another_sub_folder.' status_code=200

Delete the current folder
----------------

.. autofunction:: jobs.Folder.delete()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.folders.search("folder3/another_sub_folder").delete)
request=<HTTPRequestObject object at 2309917207952> content='[204] Successfully deleted folder.' status_code=204

Create a folder
----------------
(You are interacting with a specific folder location, so you can only create sub-folders)

.. autofunction:: jobs.Folder.create()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> from builders import Builder
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_folder = Builder.Folder(name="my_new_folder_name", description="my description is pretty simple.")
>>> print(jenkins.folders.search("folder3/sub_folder").create("another_sub_folder", my_folder))
request=<HTTPRequestObject object at 1660448175456> content='[200] Successfully created another_sub_folder.' status_code=200

Get the folder config
----------------

.. autofunction:: jobs.Folder.config()

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
====

.. _jobs:

Interact with a job
----------------

.. autofunction:: jobs.Jobs.search()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("new_freestyle"))
<jenkins_pysdk.jobs.Job object at 0x000001E515CD4A90>

List all jobs
----------------

.. autofunction:: jobs.Jobs.list()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.list())
[<jenkins_pysdk.jobs.Job object at 0x000002B4E528A710>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5119780>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5118580>, <jenkins_pysdk.jobs.Job object at 0x000002B4E511BC10>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5119870>]

Iterate all jobs
----------------

.. autofunction:: jobs.Jobs.iter()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.iter())
[<jenkins_pysdk.jobs.Job object at 0x000002B4E528A710>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5119780>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5118580>, <jenkins_pysdk.jobs.Job object at 0x000002B4E511BC10>, <jenkins_pysdk.jobs.Job object at 0x000002B4E5119870>]

Create a freestyle job
----------------

.. autofunction:: jobs.Jobs.create()

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
----------------

.. autofunction:: jobs.Jobs.is_job()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.is_job("folder3/freestyle_4"))
True


Job
====

Disable a job
----------------

.. autofunction:: jobs.Job.disable()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("folder3/freestyle_4").disable)
request=<HTTPRequestObject object at 2523890810240> content='[200] Successfully disabled folder3/freestyle_4.' status_code=200

Get a job URL
----------------

.. autofunction:: jobs.Job.url()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("folder3/freestyle_4").url)
https://JenkinsDNS/job/folder3/job/freestyle_4

Get a job path
----------------

.. autofunction:: jobs.Job.path()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("folder3/freestyle_4").path)
folder3/freestyle_4


Get job URL
----------------

.. autofunction:: jobs.Job.enable()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("folder3/freestyle_4").enable)
request=<HTTPRequestObject object at 1986068844192> content='[200] Successfully enabled folder3/freestyle_4.' status_code=200

Reconfigure a job
----------------

.. autofunction:: jobs.Job.reconfig())

>>> from jenkins_pysdk.jenkins import Jenkins
>>> from jenkins_pysdk.builders import Builder
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> config = Builder._Templates.Freestyle.format(description="New desc", disabled=True)
>>> print(jenkins.jobs.search("freestyle_created").reconfig(config))
request=<HTTPRequestObject object at 1772165197280> content='[200] Successfully reconfigured freestyle_created.' status_code=200

Delete a job
----------------

.. autofunction:: jobs.Job.delete()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("freestyle_created").delete)
request=<HTTPRequestObject object at 1721615969440> content='[204] Successfully deleted job.' status_code=204

Get job config
----------------

.. autofunction:: jobs.Job.config()

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
----------------

.. autofunction:: jobs.Job.builds()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.jobs.search("new_freestyle").builds)
<jenkins_pysdk.builds.Builds object at 0x000001EF9C34A860>


Builds
====

Search for a build
----------------

.. autofunction:: builds.Builds.search()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job = jenkins.jobs.search("new_freestyle")
>>> print(my_job.builds.search(10))
<jenkins_pysdk.builds.Build object at 0x0000025270CDFD00>

Interact with a job's builds
----------------

.. autofunction:: builds.Builds.search()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job = jenkins.jobs.search("new_freestyle")
>>> print(my_job.builds)
<jenkins_pysdk.builds.Builds object at 0x0000025EF50AA890>

Get the total build history of a job
----------------

.. autofunction:: builds.Builds.total()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job = jenkins.jobs.search("new_freestyle")
>>> print(my_job.builds.total)
6

Iterate all job's builds
----------------

.. autofunction:: builds.Builds.iter()

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
----------------

.. autofunction:: builds.Builds.list()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job = jenkins.jobs.search("new_freestyle")
>>> print(my_job.builds.list())
[<jenkins_pysdk.builds.Build object at 0x00000131E097FD00>, <jenkins_pysdk.builds.Build object at 0x00000131E097FAF0>, <jenkins_pysdk.builds.Build object at 0x00000131E097FE20>, <jenkins_pysdk.builds.Build object at 0x00000131E097FBB0>, <jenkins_pysdk.builds.Build object at 0x00000131E097F850>, <jenkins_pysdk.builds.Build object at 0x00000131E08BC4C0>]


Get the latest saved build
----------------

.. autofunction:: builds.Builds.latest()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job = jenkins.jobs.search("new_freestyle")
>>> print(my_job.builds.latest.url)
https://JenkinsDNS/job/new_freestyle/10/

Get the oldest saved build
----------------

.. autofunction:: builds.Builds.oldest()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job = jenkins.jobs.search("new_freestyle")
>>> print(my_job.builds.latest.url)
https://JenkinsDNS/job/new_freestyle/1/

Trigger a new build
----------------

.. autofunction:: builds.Builds.latest()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job = jenkins.jobs.search("new_freestyle")
>>> params = {}  # For build parameters
>>> print(my_job.builds.build())
request=<HTTPRequestObject object at 2421026107968> content='[201] Successfully triggered a new build.' status_code=201


Build
====

Get the build number
----------------

.. autofunction:: builds.Build.number()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_10 = jenkins.jobs.search("new_freestyle").builds.search(10)
>>> print(my_job_build_10.number)
10

Get the build URL
----------------

.. autofunction:: builds.Build.url()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
>>> print(my_job_build_2.url)
https://JenkinsDNS/job/new_freestyle/2/

Get the build result
----------------

.. autofunction:: builds.Build.result()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
>>> print(my_job_build_2.result)
SUCCESS

Get the build description
----------------

.. autofunction:: builds.Build.description()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
>>> print(my_job_build_2.description)
None

Check if the build is done
----------------

.. autofunction:: builds.Build.done()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
>>> print(my_job_build_2.done)
True

Get the build duration
----------------

.. autofunction:: builds.Build.duration()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
>>> print(my_job_build_2.duration)
15

Get the build console logs
----------------

.. autofunction:: builds.Build.console()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_10 = jenkins.jobs.search("new_freestyle").builds.search(10)
>>> print(my_job_build_10.console())
Started by user admin
Running as SYSTEM
Building in workspace /var/lib/jenkins/workspace/new_freestyle
Finished: SUCCESS

Delete the build
----------------

.. autofunction:: builds.Build.delete()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_10 = jenkins.jobs.search("new_freestyle").builds.search(10)
>>> print(my_job_build_10.delete)
request=<HTTPRequestObject object at 2286772207216> content='[200] Successfully deleted build (10).' status_code=200

Get the build changes
----------------

.. autofunction:: builds.Build.changes()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> my_job_build_2 = jenkins.jobs.search("new_freestyle").builds.search(2)
>>> print(my_job_build_2.changes)
<HTML output>


Credentials
====

Search for a system domain
----------------

.. autofunction:: credentials.Credentials.search_domains()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.credentials.search_domains("domain2"))
<jenkins_pysdk.credentials.Domain object at 0x0000023E2488CCD0>

Iterate all domains
----------------

.. autofunction:: credentials.Credentials.iter_domains()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> for domain in jenkins.credentials.iter_domains():
>>>     print(domain.name)
Global credentials (unrestricted)
domain2
test_domain

Iterate all domains
----------------

.. autofunction:: credentials.Credentials.list_domains()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print([domain.name for domain in jenkins.credentials.list_domains()])
['Global credentials (unrestricted)', 'domain2', 'test_domain']

Domain
====

Get the domain name
----------------

.. autofunction:: credentials.Domain.name()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> domain = jenkins.credentials.search_domains()
>>> print(domain.name)
Global credentials (unrestricted)

Get the domain URL
----------------

.. autofunction:: credentials.Domain.url()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> domain = jenkins.credentials.search_domains()
>>> print(domain.url)
https://JenkinsDNS/manage/credentials/store/system/domain/_

Search for a credential in the domain
----------------

.. autofunction:: credentials.Domain.search()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> github_pat = jenkins.credentials.search_domains("domain2").search("Github_PAT")
>>>    print(github_pat)
<jenkins_pysdk.credentials.Credential object at 0x000002B2AD79BD60>


Iterate credentials in the domain
----------------

.. autofunction:: credentials.Domain.iter()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> domain = jenkins.credentials.search_domains()  # Defaults to Global domain
>>> for cred in domain.iter():
>>>     print(cred.id)
3f2ba384-a1bc-4785-86d0-1c82d4e8be03
95b47fec-c078-4821-b05b-c7149f549429

List credentials in the domain
----------------

.. autofunction:: credentials.Domain.list()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> domain = jenkins.credentials.search_domains()  # Defaults to Global domain
>>> print([cred.id for cred in domain.list()])
['3f2ba384-a1bc-4785-86d0-1c82d4e8be03', '95b47fec-c078-4821-b05b-c7149f549429']

Credential
====

Get the credential ID
----------------

.. autofunction:: credentials.Credential.id()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> github_pat = jenkins.credentials.search_domains("domain2").search("Github_PAT")
>>> print(github_pat.id)
Github_PAT

Get the credential config
----------------

.. autofunction:: credentials.Credential.config()

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
----------------

.. autofunction:: credentials.Credential.reconfig()

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

Users
====

Search for a user
----------------

.. autofunction:: users.Users.search()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.users.search("test"))
<jenkins_pysdk.users.User object at 0x000001BEEBF3CD30>

Get total users
----------------

.. autofunction:: users.Users.total()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.users.search("test"))
3

Iterate all users
----------------

.. autofunction:: users.Users.iter()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>>     for user in jenkins.users.iter():
>>>        print(user.name)
admin
new
test

List all users
----------------

.. autofunction:: users.Users.list()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.users.list())
[<jenkins_pysdk.users.User object at 0x00000207B731CE50>, <jenkins_pysdk.users.User object at 0x00000207B73DD210>, <jenkins_pysdk.users.User object at 0x00000207B73DD960>]


User
====

Get the user name
----------------

.. autofunction:: users.User.name()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("test")
>>> print(user.name)
test

Get the user URL
----------------

.. autofunction:: users.User.url()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("test")
>>> print(user.url)
https://JenkinsDNS/user/test

Get the user description
----------------

.. autofunction:: users.User.description()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("test")
>>> print(user.description)
This user is using for testing automation.

Get the user's credentials
----------------

.. autofunction:: users.User.credentials()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("admin")
>>> print([cred.id for cred in user.credentials(domain="my_creds_store").list()])
['my_pypi_password']

Get the user's views
----------------

.. autofunction:: users.User.views()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("test")
>>> print(user.views)
[<jenkins_pysdk.views.View object at 0x000002AF1883DDB0>, <jenkins_pysdk.views.View object at 0x000002AF1883CCD0>, <jenkins_pysdk.views.View object at 0x000002AF1883C6A0>, <jenkins_pysdk.views.View object at 0x000002AF1883C8B0>, <jenkins_pysdk.views.View object at 0x000002AF1883D0C0>]

Get the user's builds
----------------

.. autofunction:: users.User.builds()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("admin")
>>> print(user.builds)
No REST endpoint available... returning HTML response for the moment...
<HTML Output>

Delete the user
----------------

.. autofunction:: users.User.delete()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("test")
>>> print(user.delete)
request=<HTTPRequestObject object at 2813768495920> content='[400] Failed to delete user (test).' status_code=200

Terminate a users' sessions
----------------

.. autofunction:: users.User.logout()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> user = jenkins.users.search("test")
>>> print(user.logout)
request=<HTTPRequestObject object at 2073057402192> content='[200] Successfully logged out.' status_code=200

Views
====

Search for a view
----------------

.. autofunction:: views.Views.search()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.views.search("All"))

Iterate all views
----------------

.. autofunction:: views.Views.iter()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> for view in jenkins.views.iter():
>>>     print(view.name)
all
m
my

List all views
----------------

.. autofunction:: views.Views.list()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.views.list())
[<jenkins_pysdk.views.View object at 0x0000013439AA9E10>, <jenkins_pysdk.views.View object at 0x0000013439AA9DE0>, <jenkins_pysdk.views.View object at 0x0000013439AA9DB0>]

Create a view
----------------

.. autofunction:: views.Views.create()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.views.create())
###############################################################################################################################################


View
====

Get the view name
----------------

.. autofunction:: views.View.name()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.views.search("All").name)
All

Get the view URL
----------------

.. autofunction:: views.View.url()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.views.search("All").url)
http://JenkinsDNS/view/All

Reconfigure the view
----------------

.. autofunction:: views.View.reconfig()

>>> from jenkins_pysdk.jenkins import Jenkins
>>> jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
>>> print(jenkins.views.search("All").reconfig())
http://JenkinsDNS/view/All
