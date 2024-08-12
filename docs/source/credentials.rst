Credentials
========

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
