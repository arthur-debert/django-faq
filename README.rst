Django-FAQ
=================

This is a simple faq application for your Django powered site.
This app follows several "best practices" for reusable apps by
allowing for template overrides and extra_context arguments and such.

Features
===================

- Question Headers can be created that can be used to group related
  questions into sections ;

- Questions can be "protected" in which case they are only presented
  to authenticated users ;

- Questions are linked to the current locale of the user, so you can
  have multiple FAQs on your website ;

- For every question, five similar questions are calculated and cached (this feature still has to be reviewed) ;

- There is a SubmitFAQForm defined that you can use to allow site
  visitors to submit new questions and/or answers to the site
  administrator for consideration. All submitted questions are added as
  "inactive" and so it is up to the administrator to edit, activate or
  discard the question as well as set its' sort_order field and slug to
  reasonable values.


Installation
============

1. add 'faq' directory to your Python path.
2. Make sure you have the Localization middleware in your MIDDLEWARE_CLASSES::

    MIDDLEWARE_CLASSES = (
        ...
        'django.middleware.locale.LocaleMiddleware',
        ...
    )

2. add 'faq' to your INSTALLED_APPS tuple found in your settings file::

    INSTALLED_APPS = (
        ...
        'faq',
        ...
    )

3. Run ``./manage syncdb`` to create the tables

4. If you want to customize the templates then either create an 'faq'
   directory in your projects templates location, or you can also pass along
   custom 'template_name' arguments by creating your own view wrappers around
   the 'faq' app views. I show how to do the latter in the 'example' project
   included - look at the views.py file to see the details.

5. If you'd like to load some example data then execute ./manage.py loaddata example_data.json

Example Site
============

The example app now has a convenient home page that appears as the default
page. It has links to the available views.

There are some saved FAQs in a fixture named ``example_data.json`` that provide
the example apps with some questions to view when you bring them up for the
first time. These FAQs provide additional notes about installing and using
*django-faq*.

I included an example site in the ``./example_project`` directory. You should
be able to simply execute ``./manage.py syncdb`` and then
``./manage.py runserver`` and have the example site up and running. I assume
your system has sqlite3 available - it is set as the default database in
``settings.py``

There is a stand-alone example site in the projects/example directory. to try it out:

1. Install django-faq as per the Installation section above.

2. Execute ``./manage.py syncdb`` (This assumes that *sqlite3* is available as it is set as the default database with the ``DATABASE_NAME = 'django-faq.db'``.)

3. If you'd like to load some example data then execute ``./manage.py loaddata example_data.json``

4. Execute ``./manage.py runserver`` and you will have the example site up and running. The home page will have links to get to the available views as well as to the admin.

5. After logging into the admin you will notice an additional question appears in the FAQ. That question is "protected" and therefore not presented to non-authenticated users.

6. The capability to submit an FAQ is available and works whether or not you are a logged in user. Note that a staff member will have to use the admin and review any submitted FAQs and clean them up and set them to active before they are viewable by the end user views.
