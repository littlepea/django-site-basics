django-site-basics
========================

A reusable app to add favicon.ico and robots.txt handling for your site.

Installation
------------------------------------

Install "django-site-basics" using pip or easy_install::

    pip install django-site-basics

Add "favicon" to your INSTALLED_APPS in settings.py::

      INSTALLED_APPS = (
          ...
          'site_basics',
      )

Add site_basics URL patterns to urls.py::

      urlpatterns = patterns('',
          ...
          url(r'^', include('site_basics.urls')),
      )

Usage
------------------------------------

Put favicon.ico into your STATIC_ROOT. and you good to go, /favicon.ico will automatically redirect to /static/favicon.ico if your STATIC_URL = '/static/'.

Otherwise you can set a custom path to your favicon using FAVICON_PATH setting. For example::

     FAVICON_PATH = STATIC_URL + 'images/favicon.png'

robots.txt will be working out of the box but if you need to customize it put custom robots.txt file into your templates directory.
If you need to change template location use ROBOTS_TEMPLATE setting (robots.txt by default). Example::

    ROBOTS_TEMPLATE = 'myfolder/robots.txt'

Running the Tests
------------------------------------

You can run the tests with via::

    python setup.py test

or::

    python runtests.py

TODO
------------------------------------

* 404 and 500 pages
* Google Analytics
* Sitemaps support

Credits
------------------------------------

* Developed and maintained under supervision of `Evgeny Demchenko`_
* Uses django-favicon_ for favicon.ico handling
* Uses django-robots-txt_ for robots.txt handling

.. _Evgeny Demchenko: https://github.com/littlepea
.. _django-favicon: https://github.com/littlepea/django-favicon
.. _django-robots-txt: https://github.com/nkuttler/django-robots-txt