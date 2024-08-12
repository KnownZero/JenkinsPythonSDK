Views
========

Views
-----------

.. _views:

Search for a view

.. autofunction:: views.Views.search()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.views.search("All"))

The above code will output:

::

    <jenkins_pysdk.views.View object at 0x0000026497A93820>


Iterate all views

.. autofunction:: views.Views.iter()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    for view in jenkins.views.iter():
        print(view.name)

The above code will output:

::

    all
    m
    my

List all views

.. autofunction:: views.Views.list()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.views.list())

The above code will output:

::

    [<jenkins_pysdk.views.View object at 0x0000013439AA9E10>, <jenkins_pysdk.views.View object at 0x0000013439AA9DE0>, <jenkins_pysdk.views.View object at 0x0000013439AA9DB0>]

Create a view

.. autofunction:: views.Views.create()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    xml = """
       <hudson.model.ListView>
         <name>my_view</name>
         <mode>hudson.model.ListView</mode>
         <description>Your view description</description>
         <jobNames>
           <comparator class="hudson.util.CaseInsensitiveComparator"/>
           <string>new_freestyle</string>
         </jobNames>
         <columns>
           <hudson.views.StatusColumn/>
           <hudson.views.WeatherColumn/>
           <hudson.views.JobColumn/>
         </columns>
         <recurse>true</recurse>
       </hudson.model.ListView>
       """
    print(jenkins.views.create("my_view", xml))

The above code will output:

::

    request=<Request object at 2275566295520> content='[200] Successfully created my_view.' status_code=200


View
-----------

.. _view:

Get the view name

.. autofunction:: views.View.name()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.views.search("All").name)

The above code will output:

::

    All

Get the view URL

.. autofunction:: views.View.url()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.views.search("All").url)

The above code will output:

::

    http://JenkinsDNS/view/All

Reconfigure the view
(Job order must be the same as the order in the application, otherwise you will get dodgy results)
E.g.
builder_e is higher up in the list of jobs so it goes above builder_folder, which is underneath it in the list :)

.. autofunction:: views.View.reconfig()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    xml = """
       <hudson.model.ListView>
         <name>my_view</name>
         <description>Your view description</description>
         <filterExecutors>false</filterExecutors>
         <filterQueue>false</filterQueue>
         <properties class="hudson.model.View$PropertyList"/>
         <jobNames>
           <comparator class="hudson.util.CaseInsensitiveComparator"/>
           <string>builder_e</string>
           <string>builder_folder</string>
           <string>builder_w</string>
           <string>new_freestyle</string>
         </jobNames>
         <jobFilters/>
         <columns>
           <hudson.views.StatusColumn/>
           <hudson.views.WeatherColumn/>
           <hudson.views.JobColumn/>
         </columns>
         <recurse>true</recurse>
       </hudson.model.ListView>
      """
      print(jenkins.views.search("my_view").reconfig(xml))

The above code will output:

::

    request=<Request object at 2153302882832> content='[200] Successfully reconfigured view (my_view).' status_code=200

Delete the view

.. autofunction:: views.View.delete()
.. code-block:: python

    from jenkins_pysdk.jenkins import Jenkins
    jenkins = Jenkins(host="JenkinsDNS", username="admin", token="11e8e294cee85ee88b60d99328284d7608")
    print(jenkins.views.search("YourViewName").delete())

The above code will output:

::

    request=<Request object at 2246812676752> content='[200] Successfully deleted view (YourViewName).' status_code=200
