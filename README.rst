cookiecutter-django-essentials
==============================

.. image:: https://requires.io/github/wldcordeiro/cookiecutter-django-essentials/requirements.svg?branch=master
     :target: https://requires.io/github/wldcordeiro/cookiecutter-django-essentials/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://circleci.com/gh/wldcordeiro/cookiecutter-django-essentials.svg?style=svg
    :target: https://circleci.com/gh/wldcordeiro/cookiecutter-django-essentials
    :alt: CircleCI Build Status

A cookiecutter_ template for Django.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Features
---------
* For Django 1.7

Management Features
^^^^^^^^^^^^^^^^^^^

* Settings management via django-configurations_
* Database configuration via dj-database-url_
* Security checking via django-secure_
* Internationalization support via django-localflavor_
* Improved Admin experience via django-grappelli_

Utility Features
^^^^^^^^^^^^^^^^

* Useful mixins via django-braces_
* Better forms via django-floppyforms_
* Useful model tools via django-model-utils_
* Model version management via django-reversion_
* Markdown support via django-markdown_

Development Features
^^^^^^^^^^^^^^^^^^^^

* Improved shell experience via ipython_
* Further improved shell experience via ptpython_
* Helpers and improved development server via django-extensions_
* Debug easily with the django-debug-toolbar_
* Verify your test coverage with coverage_
* Insure your code is PEP8 compliant with flake8_
* Grunt build for compass, uglify, imagemin and livereload

User Management Features
^^^^^^^^^^^^^^^^^^^^^^^^

* Registration via django-allauth_
* User avatars via django-avatar_

REST Features
^^^^^^^^^^^^^

* REST API Creation support via django-rest-framework_
* REST powered authentication and registration via django-rest-auth_

Production Features
^^^^^^^^^^^^^^^^^^^
* Procfile_ for deploying to Heroku
* Heroku optimized requirements
* Basic caching setup
* Basic e-mail configurations for send emails via SendGrid_

.. _django-configurations: https://github.com/jezdez/django-configurations
.. _dj-database-url: https://github.com/kennethreitz/dj-database-url
.. _django-secure: https://pypi.python.org/pypi/django-secure
.. _django-localflavor: https://github.com/django/django-localflavor
.. _django-grappelli: https://github.com/sehmaschine/django-grappelli
.. _django-braces: https://github.com/brack3t/django-braces
.. _django-floppyforms: https://github.com/gregmuellegger/django-floppyforms
.. _django-model-utils: https://github.com/carljm/django-model-utils
.. _django-reversion: https://github.com/etianen/django-reversion
.. _django-markdown: https://github.com/klen/django_markdown
.. _ipython: http://ipython.org/
.. _ptpython: https://github.com/jonathanslenders/ptpython
.. _django-extensions: https://github.com/django-extensions/django-extensions
.. _django-debug-toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar/
.. _coverage: https://pypi.python.org/pypi/coverage/3.7.1
.. _flake8: https://pypi.python.org/pypi/flake8
.. _django-allauth: https://github.com/pennersr/django-allauth
.. _django-avatar: https://github.com/jezdez/django-avatar/
.. _django-rest-framework: https://github.com/tomchristie/django-rest-framework
.. _django-rest-auth: https://github.com/Tivix/django-rest-auth
.. _Procfile: https://devcenter.heroku.com/articles/procfile
.. _SendGrid: https://sendgrid.com/




Constraints
-----------

* Only maintained 3rd party libraries are used.
* PostgreSQL everywhere
* Environment variables for configuration (This won't work with Apache/mod_wsgi).


Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get cookiecutter. Trust me, it's awesome::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/wldcordeiro/cookiecutter-django-essentials.git

You'll be prompted for some questions, answer them, then it will create a Django project for you.


**Warning**: After this point, change 'Wellington Cordeiro', 'wldcordeiro', etc to your own information.

It prompts you for questions. Answer them::

    Cloning into 'cookiecutter-django-essentials'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name (default is "project_name is the title of the project")? Reddit Clone
    repo_name (default is "repo_name")? redditclone
    repo_url (default is "repo_url is the url for your repo, minus '.git'")? http://github.com/foo/redditclone
    author_name (default is "Your Name")? Wellington Cordeiro
    author_github_username (default is "@yourusername") @wldcordeiro
    email (default is "Your email")? wellington@wellingtoncordeiro.com
    description (default is "A short description of the project.")? A reddit clone.
    year (default is "Current year")? 2015
    domain_name (default is "Domain name")? redditclone.org
    version (default is "0.1.0")? 1.0.0
    now (default is "2015/01/05")? 2015/01/10
    time_zone (default is "America/Denver")? America/Denver
    port (default is "8080")? 8082
    database_name (default is "database")? testdb
    database_user (default is "dbuser")? testuser
    database_password (default is"password")? awesomepassword


Enter the project and take a look around::

    $ cd redditclone/
    $ ls

Create a GitHub repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:pydanny/redditclone.git
    $ git push -u origin master

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv
* PostgreSQL

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements/local.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Then, create a PostgreSQL database and add the database configuration using the  ``dj-database-url`` app pattern: ``postgres://db_owner:password@dbserver_ip:port/db_name`` either:

* in the ``config.local.py`` setting file,
* or in the env variable ``DATABASE_URL`` in production.



You can now run the usual Django ``migrate`` and ``runserver`` command (replace ``yourapp`` with the name of the directory containing the Django project)::

    $ python yourapp/manage.py migrate

    $ python yourapp/manage.py runserver

Though it's better if you run::

    $ grunt serve

Since this will run the server and minify your Javascript, compile your SCSS and minify your images.

The base app will run but you'll need to create your super user::

    $ python yourapp/manage.py createsuperuser

**Live reloading and Sass CSS compilation**

If you'd like to take advantage of live reloading and Sass / Compass CSS compilation you can do so with the included Grunt task.

Make sure that nodejs_ is installed. Then in the project root run::

    $ npm install

.. _nodejs: http://nodejs.org/download/

Now you just need::

    $ grunt serve

The base app will now run as it would with the usual ``manage.py runserver_plus`` but with live reloading and Sass compilation enabled.

To get live reloading to work you'll probably need to install an `appropriate browser extension`_

.. _appropriate browser extension: http://feedback.livereload.com/knowledgebase/articles/86242-how-do-i-install-and-use-the-browser-extensions-

It's time to write the code!!!

"Your Stuff"
-------------

Scattered throughout the Python and HTML of this project are places marked with "your stuff". This is where third-party libraries are to be integrated with your project.

Releases
--------

Want a stable release? You can find them at https://github.com/wldcordeiro/cookiecutter-django-essentials/releases


Not Exactly What You Want?
---------------------------

This is what I want. *It might not be what you want.* Don't worry, you have options:

Fork This
~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this to create your own version.
Once you have your fork working, let me know and I'll add it to a '*Similar Cookiecutter Templates*' list here.
It's up to you whether or not to rename your fork.

If you do rename your fork, I encourage you to submit it to the following places:

* cookiecutter_ so it gets listed in the README as a template.
* The cookiecutter grid_ on Django Packages.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _grid: https://www.djangopackages.com/grids/g/cookiecutter/

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they make my own project development
experience better.
