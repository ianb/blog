toppcloud (Silver Lining) and Django
####################################
:date: 2010-02-05 02:50
:author: Ian Bicking
:tags: Programming, Python, Silver Lining, Web

I wrote up instructions on using `toppcloud <http://blog.ianbicking.org/2010/01/29/new-way-to-deploy-web-apps />`_ (**update**: renamed Silver Lining) with Django.  They are `up on the site <http://toppcloud.colorstudy.com/django-quickstart.html>`_ (where they will be updated in the future), but I'll drop them here too...

Creating a Layout
-----------------

First thing you have to do (after installing toppcloud of course) is create an environment for your new application.  Do that like::

    $ toppcloud init sampleapp

This creates a directory ``sampleapp/`` with a basic layout.  The first thing we'll do is set up version control for our project. For the sake of documentation, imagine you go to `bitbucket <http://bitbucket.org>`_ and create two new repositories, one called ``sampleapp`` and another called ``sampleapp-lib`` (and for the examples we'll use the username ``USER``).

We'll go into our new environment and use these::

    $ cd sampleapp
    $ hg clone http://bitbucket.org/USER/sampleapp src/sampleapp
    $ rm -r lib/python/
    $ hg clone http://bitbucket.org/USER/sampleapp-lib lib/python
    $ mkdir lib/python/bin/
    $ echo "syntax: glob
    bin/python*
    bin/activate
    bin/activate_this.py
    bin/pip
    bin/easy_install*
    " > lib/python/.hgignore
    $ mv bin/* lib/python/bin/
    $ rmdir bin/
    $ ln -s lib/python/bin bin

Now there is a basic layout setup, with all your libraries going into the ``sampleapp-lib`` repository, and your main application in the ``sampleapp`` repository.

Next we'll install Django::

    $ source bin/activate
    $ pip install Django

Then we'll set up a standard Django site::

    $ cd src/sampleapp
    $ django-admin.py sampleapp

Also we'd like to be able to import this file.  It'd be nice if there was a ``setup.py`` file, and we could run ``pip -e src/sampleapp``, but ``django-admin.py`` doesn't create that itself.  Instead we'll get that on the import path more manually with a ``.pth`` file::

    $ echo "../../src/sampleapp" > lib/python/sampleapp.pth

Also there's the tricky ``$DJANGO_SETTINGS_MODULE`` that you might have had problems with before.  We'll use the file ``lib/python/toppcustomize.py`` (which is imported everytime Python is started) to make sure that is always set::

    $ echo "import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'sampleapp.settings'
    " > lib/python/toppcustomize.py

Also we have a file ``src/sampleapp/sampleapp/manage.py``, and that file doesn't work *quite* how we'd like.  Instead we'll put a file into ``bin/manage.py`` that does the same thing::

    $ rm sampleapp/manage.py
    $ cd ../..
    $ echo '#!/usr/bin/env python
    from django.core.management import execute_manager
    from sampleapp import settings
    if __name__ == "__main__":
        execute_manager(settings)
    ' > bin/manage.py
    $ chmod +x bin/manage.py

Now, if you were just using plain Django you'd do something like run ``python manage.py runserver``.  But we'll be using ``toppcloud serve`` instead, which means we have to set up the two other files toppcloud needs: ``app.ini`` and the runner.  Here's a simple ``app.ini``::

    $ echo '[production]
    app_name = sampleapp
    version = 1
    runner = src/sampleapp/toppcloud-runner.py
    ' > src/sampleapp/toppcloud-app.ini
    $ rm app.ini
    $ ln -s src/sampleapp/toppcloud-app.ini app.ini

The file *must* be in the "root" of your application, and named ``app.ini``, but it's good to keep it in version control, so we set it up with a symlink.

It also refers to a "runner", which is the Python file that loads up the WSGI application.  This looks about the same for any Django application, and we'll put it in ``src/sampleapp/toppcloud-runner.py``::

    $ echo 'import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()
    ' > src/sampleapp/toppcloud-runner.py

Now if you want to run the application, you can::

    $ toppcloud serve .

This will load it up on ``http://localhost:8080``, and serve up a boring page.  To do something interesting we'll want to use a database.

Setting Up A Database
---------------------

At the moment the only good database to use is PostgreSQL with the PostGIS extensions.  Add this line to ``app.ini``::

    service.postgis =

This makes the database "available" to the application.  For development you still have to set it up yourself.  You should create a database ``sampleapp`` on your computer.

Next, we'll need to change ``settings.py`` to use the new database configuration.  Here's the lines that you'll see::

    DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    DATABASE_NAME = ''             # Or path to database file if using sqlite3.
    DATABASE_USER = ''             # Not used with sqlite3.
    DATABASE_PASSWORD = ''         # Not used with sqlite3.
    DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
    DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

First add this to the top of the file::

    import os

Then you'll change those lines to::

    DATABASE_ENGINE = 'postgresql_psycopg2'
    DATABASE_NAME = os.environ['CONFIG_PG_DBNAME']
    DATABASE_USER = os.environ['CONFIG_PG_USER']
    DATABASE_PASSWORD = os.environ['CONFIG_PG_PASSWORD']
    DATABASE_HOST = os.environ['CONFIG_PG_HOST']
    DATABASE_PORT = ''

Now we can create all the default tables::

    $ manage.py syncdb
    Creating table auth_permission
    Creating table auth_group
    Creating table auth_user
    Creating table auth_message
    Creating table django_content_type
    Creating table django_session
    Creating table django_site
    ...

Now we have an empty project that doesn't do anything.  Let's make it do a little something (this is all really based on `the Django tutorial <http://docs.djangoproject.com/en/dev/intro/tutorial01 />`_).

::

    $ manage.py startapp polls

Django magically knows to put the code in ``src/sampleapp/sampleapp/polls/`` -- we'll setup the model in ``src/sampleapp/sampleapp/polls/models.py``::

    from django.db import models

    class Poll(models.Model):
        question = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')

    class Choice(models.Model):
        poll = models.ForeignKey(Poll)
        choice = models.CharField(max_length=200)
        votes = models.IntegerField()

And activate the application by adding ``'sampleapp.polls'`` to ``INSTALLED_APPS`` in ``src/sampleapp/sampleapp/settings.py``.  Also add ``'django.contrib.admin'`` to get the admin app in place.  Run ``manage.py syncdb`` to get the tables in place.

You can try ``toppcloud serve .`` and go to ``/admin/`` to login and see your tables.  You might notice all the CSS is broken.  

toppcloud serves static files out of the ``static/`` directory.  You don't actually put ``static`` in the URLs, these files are available at the top-level (unless you create a ``static/static/`` directory). The best way to put files in there is generally symbolic links.  

For Django admin, do this::

    $ cd static
    $ ln -s ../lib/python/django/contrib/admin/media admin-media

Now edit ``src/sampleapp/sampleapp/settings.py`` and change ``ADMIN_MEDIA_PREFIX`` to ``'/admin-media'``.

(Probably some other links should be added.)

One *last* little thing you might want to do; replace this line in
settings::

    SECRET_KEY = 'ASF#@$@#JFAS#@'

With this::

    from tcsupport.secret import get_secret
    SECRET_KEY = get_secret()

Then you don't have to worry about checking a secret into version control.

You still don't really have an application, but the rest is mere "programming" so have at it!
