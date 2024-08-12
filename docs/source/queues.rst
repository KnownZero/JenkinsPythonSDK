Queues
========

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
