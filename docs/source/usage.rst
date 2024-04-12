Usage
=====

.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (venv) $ pip install jenkins-pysdk

Test Connection
----------------

To retrieve a list of random ingredients,
You can explicity run ``jenkins.connect()`` function:

.. autofunction:: jenkins.connect

For example (using an API token):

>>> import jenkins_pysdk.jenkins
>>> conn = jenkins.Jenkins(host="JenkinsDNS", username="admin",
                      token="11e8e294cee85ee88b60d99328284d7608")
>>> print(conn.connect())
request=<HTTPRequestObject object at 2430739526048> response=<HTTPResponseObject object at 2430750139600> content='[200] Successfully connected to JenkinsDNS.' status_code=200
