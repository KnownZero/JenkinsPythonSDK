Builds
========

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

.. autofunction:: builds.Build.next()
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

.. autofunction:: builds.Build.previous()
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

