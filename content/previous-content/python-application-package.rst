Python Application Package
##########################
:date: 2012-02-29 18:12
:author: Admin
:tags: Packaging, Python, Silver Lining, Web

I've been thinking some more about deployment of Python web applications, and deployment in general (in part leading up to the `Web Summit <https://us.pycon.org/2012/community/WebDevSummit />`_). And I've got an idea.

I `wrote about this about a year ago <https://ianbicking.org/2011/03/31/python-webapp-package />`_ and `recently revised some notes on a proposal <https://github.com/ianb/pywebapp/blob/master/docs/spec.txt>`_ but I've been thinking about something a bit more basic: a way to simply ship server applications, bundles of code.  Web applications are just one use case for this.

For now lets call this a "Python application package".  It has these features:

1. There is an *application description*: this tells the *environment* about the application.  (This is sometimes called "configuration" but that term is very confusing and overloaded; I think "description" is much clearer.)

2. Given the description, you can create an execution environment to run code from the application and acquire objects from the application.  So there would be a specific way to setup ``sys.path``, and a way to indicate any libraries that are required but not bundled directly with the application.

3. The environment can inject information into the application.  (Also this sort of thing is sometimes called "configuration", but let's not do that either.)  This is where the environment could indicate, for instance, what database the application should connect to (host, username, etc).

4. There would be a way to run commands and get objects from the application.  The environment would look in the application description to get the names of commands or objects, and use them in some specific manner depending on the purpose of the application.  For instance, WSGI web applications would point the environment to an application object.  A Tornado application might simply have a command to start itself (with the environment indicating what port to use through its injection).

There's a lot of things you can build from these pieces, and in a sophisticated application you might use a bunch of them at once.  You might have some WSGI, maybe a seperate non-WSGI server to handle Web Sockets, something for a Celery queue, a way to accept incoming email, etc.  In pretty much all cases I think basic application lifecycle is needed: commands to run when an application is first installed, something to verify the environment is acceptable, when you want to back up its data, when you want to uninstall it.

There's also some things that all environments should setup the same or inject into the application.  E.g., ``$TMPDIR`` should point to a place where the application can keep its temporary files.  Or, every application should have a directory (perhaps specified in another environmental variable) where it can write log files.

Details?
--------

To get more concrete, here's what I can imagine from a small application description; probably YAML would be a good format::

    platform: python, wsgi
    require:
      os: posix
      python: <3
      rpm: m2crypto
      deb: python-m2crypto
      pip: requirements.txt
    python:
      paths: vendor/
    wsgi:
      app: myapp.wsgiapp:application

I imagine ``platform`` as kind of a series of mixins.  This system doesn't really need to be Python-specific; when creating something similar for `Silver Lining <http://cloudsilverlining.org>`_ I found PHP support relatively easy to add (handling languages that aren't naturally portable, like Go, might be more of a stretch).  So ``python`` is one of the features this application uses.  You can imagine lots of modularization for other features, but it would be easy and unproductive to get distracted by that.

The application has certain requirements of its environment, like the version of Python and the general OS type.  The application might also require libraries, ideally one libraries that are not portable (M2Crypto being an example).  Modern package management works pretty nicely for this stuff, so relying on system packages as a first try I believe is best (I'd offer ``requirements.txt`` as a fallback, not as the primary way to handle dependencies).

I think it's much more reliable if applications primarily rely on bundling their dependencies directly (i.e., using a vendor directory). The tool support for this is a bit spotty, but I believe this package format could clarify the problems and solutions.  `Here is an example <https://gist.github.com/1368649>`_ of how you might set up a virtualenv environment for *managing* vendor libraries (you then do not need virtualenv to *use* those same libraries), and do so in a way where you can check the results into source control.  It's kind of complicated, but works (well, almost works - ``bin/`` files need fixing up).  It's a start at least.

Support Library
---------------

On the environment side we need a good support library.  `pywebapp <https://github.com/ianb/pywebapp />`_ has some of the basic features, though it is quite incomplete. I imagine a library looking something like this::

    from apppackage import AppPackage
    app = AppPackage('/var/apps/app1.2012.02.11')
    # Maybe a little Debian support directly:
    subprocess.call(['apt-get', 'install'] +
                    app.config['require']['deb'])
    # Or fall back of virtualenv/pip
    app.create_virtualenv('/var/app/venvs/app1.2012.02.11')
    app.install_pip_requirements()
    wsgi_app = app.load_object(app.config['wsgi']['app'])

You can imagine building hosting services on this sort of thing, or setting up continuous integration servers (``app.run_command(app.config['unit_test'])``), and so forth.

Local Development
-----------------

If designed properly, I think this format is as usable for local development as it is for deployment.  It should be able to run directly from a checkout, with the "development environment" being an environment just like any other.

This rules out, or at least makes less exciting, the use of zip files or tarballs as a package format.  The only justification I see for using such archives is that they are easy to move around; but we live in the FUTURE and there are many ways to move directories around and we don't need to cater to silly old fashions.  If that means a script that creates a tarball, FTPs it to another computer, and there it is unzipped, then fine - this format *should not* specify anything about how you actually deliver the files.  But let's not worry about copying `WARs <http://en.wikipedia.org/wiki/WAR_file_format_%28Sun%29>`_.
