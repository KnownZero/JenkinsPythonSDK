Users
========

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
