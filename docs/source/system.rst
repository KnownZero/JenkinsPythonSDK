System
========

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
