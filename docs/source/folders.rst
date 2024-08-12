Folders
========


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
