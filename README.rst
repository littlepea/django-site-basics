django-site-basics
========================

A reusable app to add favicon.ico, robots.txt, SEO tricks and 404/500 error pages handling for your site.

Installation
------------------------------------

Install "django-site-basics" using pip or easy_install::

    pip install django-site-basics

Add "site_basics" and optionally "sitemetrics" to your INSTALLED_APPS in settings.py::

      INSTALLED_APPS = (
          ...
          'sitemetrics', # (optional) for Google Analytics support
          'site_basics',
      )

Add site_basics URL patterns and handlers (if you want to  use them) to urls.py::

      handler404 = 'site_basics.views.page_404'
      handler500 = 'site_basics.views.page_500'

      urlpatterns = patterns('',
          ...
          url(r'^', include('site_basics.urls')),
      )

Replace Django's LocaleMiddleware with UpdatedLocaleMiddleware in your MIDDLEWARE_CLASSES::

    MIDDLEWARE_CLASSES = (
        ...
        #'django.middleware.locale.LocaleMiddleware', # disabled in favor of UpdatedLocaleMiddleware
        'site_basics.middleware.UpdatedLocaleMiddleware',
        ...
    )

Usage
------------------------------------

Favicon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Put favicon.ico into your STATIC_ROOT. and you good to go, /favicon.ico will automatically redirect to /static/favicon.ico if your STATIC_URL = '/static/'.

Otherwise you can set a custom path to your favicon using FAVICON_PATH setting. For example::

     FAVICON_PATH = STATIC_URL + 'images/favicon.png'

Robots.txt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

robots.txt will be working out-of-the-box but if you need to customize it put custom robots.txt file into your templates directory.
If you need to change template location use ROBOTS_TEMPLATE setting (robots.txt by default). Example::

    ROBOTS_TEMPLATE = 'myfolder/robots.txt'

UpdatedLocaleMiddleware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a fix of Django i18n_urlpatterns and SEO problem described in `Yawd's article`_.

.. _Yawd's article: http://blog.yawd.eu/2012/impact-django-page-redirects-seo/

It changes LocaleMiddleware i18n redirects from Temporary (302) to Permanent (301) which prevents search engines from indexing and ranking double links for the same page.

To activate it replace Django's LocaleMiddleware with UpdatedLocaleMiddleware in your MIDDLEWARE_CLASSES::

    MIDDLEWARE_CLASSES = (
        ...
        #'django.middleware.locale.LocaleMiddleware', # disabled in favor of UpdatedLocaleMiddleware
        'site_basics.middleware.UpdatedLocaleMiddleware',
        ...
    )

Error pages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Error pages work out-of-the-box providing you fancy themes from Annanta_ and Robotik_.

.. image:: http://www.designersdigest.co/wp-content/uploads/2010/03/404-Error-Template.jpg

.. image:: http://mogoolab.com/wp-content/uploads/2011/10/robotik_1-450x260.png

In development you can test these views by opening /test_page_404/ and /test_page_500/.

Annanta is default but you can switch to Robotik using setting::

    ERROR_PAGE_THEME = 'robotik' # default is 'annanta'

You can also set a color::

    ERROR_PAGE_THEME_COLOR = 'blue'

Available colors:

* blue
* green
* gray (Robotik only)
* grey (Annanta only)
* red (Annanta only)
* brown (Annanta only)

And if you're using Django CMS you can show links to your root pages by setting::

    ERROR_PAGE_CMS_LINKS = True

More configuration options below...

Google Analytics (sitemetrics)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Add 'sitemetrics' to 'INSTALLED_APPS' in your settings file (usually 'settings.py')
2. Add '{% load sitemetrics %}' tag to the top of a template (usually base template, e.g. 'base.html')

Then you have two options that add metrics client code to your page:

* Use so-called 'four arguments' sitemetrics tag notation::

    {% sitemetrics by google for "UA-000000-0" %}

Here: 'google' — provider alias; 'UA-000000-0' — keycode argument. That's how you put Google Analytics client code (with 'UA-000000-0' keycode) into page.

* Use so-called 'no arguments' sitemetrics tag notation::

    {% sitemetrics %}

That's how you put all client codes registered and active for the current site.

Client codes are registered with sites through Django Admin site interface.
'Admin site' and 'Sites' from Django contrib are required for this option to work.

'./manage.py syncdb' is required just once for this option to work (it installs sitemetrics table into database).

Configuration
------------------------------------

ROBOTS_TEMPLATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a template for robots.txt handler ('robots.txt' by default). Example::

    ROBOTS_TEMPLATE = 'myforlder/myrobotstemplate.txt'

ERROR_PAGE_THEME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a theme for error pages ('annanta' or 'robotik', 'annanta' by default). Example::

    ERROR_PAGE_THEME = 'robotik'

ERROR_PAGE_THEME_COLOR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a color for error pages theme ('blue' by default). Example::

    ERROR_PAGE_THEME_COLOR = 'green'

ERROR_404_PAGE_TEMPLATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

404 template ('%s/404.html' % ERROR_PAGE_THEME by default). Example::

    ERROR_404_PAGE_TEMPLATE = 'myforlder/404.html'

ERROR_500_PAGE_TEMPLATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

500 template ('%s/500.html' % ERROR_PAGE_THEME by default). Example::

    ERROR_404_PAGE_TEMPLATE = 'myforlder/500.html'

ERROR_PAGE_LOGO_URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set it if you want to display your logo on the error pages (None by default). Example::

    ERROR_PAGE_LOGO_URL = '%simages/logo.png' % settings.STATIC_URL

ERROR_PAGE_CMS_LINKS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Allows you to show your root menu links on the error pages if you're using Django CMS (False by default). Example::

    ERROR_PAGE_CMS_LINKS = True

ERROR_PAGE_NAV_LINKS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Allows you to show your root menu links on the error pages if you're using Django CMS. Format is a tuple of tuples. Example::

    ERROR_PAGE_NAV_LINKS = (
        ('/', ugettext('Home')),
    ))

ERROR_PAGE_SOCIAL_LINKS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Allows you to show your social media links on the error pages. Format is a tuple of tuples (empty by default).

Allowed values (because  of the icons preloaded) are anything from the GoSocial_ icons pack.

Example::

    ERROR_PAGE_SOCIAL_LINKS = (
        ('twitter', 'http://twitter.com/YOURUSERNAME'),
        ('facebook', 'http://www.facebook.com/pages/YOURUSERNAME/YOURUSERID'),
        ('last.fm', 'http://www.last.fm/user/YOURUSERNAME'),
        ('flickr', 'http://www.flickr.com/photos/YOURUSERNAME'),
        ('vimeo', 'http://vimeo.com/YOURUSERID'),
        ('rss', '/rss/'),
    )


ERROR_PAGE_SEARCH_ACTION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Allows you to setup a search form on your error pages (None by default).

Additional settings:

* ERROR_PAGE_SEARCH_METHOD ('GET' by default)
* ERROR_PAGE_SEARCH_PARAM ('q' by default)

Example::

    ERROR_PAGE_SEARCH_ACTION = '/search/'
    ERROR_PAGE_SEARCH_METHOD = 'POST'
    ERROR_PAGE_SEARCH_PARAM = 'query'

Running the Tests
------------------------------------

You can run the tests with via::

    python setup.py test

or::

    python runtests.py

TODO
------------------------------------

* Add more templates
* Add locales and translations
* Sitemaps support

Credits
------------------------------------

* Developed and maintained under supervision of `Evgeny Demchenko`_
* Uses django-favicon_ for favicon.ico handling
* Uses django-robots-txt_ for robots.txt handling
* Uses django-sitemetrics_ for Google Analytics handling
* Uses Robotik_ 404 error page template
* Uses Annanta_ 404 error page template
* Uses GoSocial_ icons pack
* `Yawd's middleware code`_

.. _Evgeny Demchenko: https://github.com/littlepea
.. _django-favicon: https://github.com/littlepea/django-favicon
.. _django-robots-txt: https://github.com/nkuttler/django-robots-txt
.. _django-sitemetrics: https://github.com/idlesign/django-sitemetrics
.. _Annanta: http://www.designersdigest.co/archive/404-error-template/
.. _Robotik: http://mogoolab.com/portfolio/free-404-error-page-html-template/
.. _GoSocial: https://www.gosquared.com/blog/gosocial-a-free-social-media-icon-pack
.. _Yawd's middleware code: http://blog.yawd.eu/2012/impact-django-page-redirects-seo/