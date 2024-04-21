Quick Start
=====

.. _installation:

Installation
------------

To use this Python Jenkins SDK, first install it using pip:

.. code-block:: console

   (venv) $ pip install jenkins-pysdk

Next, test the connection to your application:

.. _test_connection:

To retrieve a list of random ingredients,
You can explicitly run ``jenkins.connect()`` function:

.. autofunction:: jenkins.Jenkins.connect()

For example (using an API token):

.. code-block:: python

    import jenkins_pysdk.jenkins as jenkins
    conn = jenkins.Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(conn.connect())
The above code will output:

::

    request=<HTTPRequestObject object at 2430739526048> response=<HTTPResponseObject object at 2430750139600> content='[200] Successfully connected to JenkinsDNS.' status_code=200
