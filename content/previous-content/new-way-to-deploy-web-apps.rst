A new way to deploy web applications
####################################
:date: 2010-01-29 14:21
:author: Ian Bicking
:tags: Packaging, Programming, Python, Silver Lining, Web

Deployment is one of the things I like least about development, and yet without deployment the development doesn't really matter.

I've tried a few things (e.g. `fassembler <http://blog.ianbicking.org/2008/06/19/my-experience-writing-a-build-system />`_), built a few things (`virtualenv <http://virtualenv.openplans.org>`_, `pip <http://pip.openplans.org>`_), but deployment just sucked *less* as a result.  Then I got excited about `App Engine <http://appengine.google.com>`_; everyone else was getting excited about "scaling", but really I was `excited about an accessible deployment process <http://blog.ianbicking.org/2008/04/09/app-engine-and-open-source />`_.  When it comes to deployment App Engine is the first thing that has really felt good to me.

**But** I can't actually *use* App Engine.  I was able to come to terms with the idea of writing an application to the platform, but there are limits... and with App Engine there were simply too many limits.  Geo stuff on App Engine is at best a crippled hack, I miss `lxml <http://codespeak.net/lxml />`_ terribly, I never hated relational databases, and almost nothing large works without some degree of rewriting.  Sometimes you can work around it, but you can never be sure you won't hit some wall later.  And frankly working around the platform is tiring and not very rewarding.

----------

So... App Engine seemed neat, but I couldn't use it, and deployment was still a problem.

What I like about App Engine: an application is just files.  There's no build process, no fancy copying of things in weird locations, nothing like that; you upload files, and uploading files *just works*.  Also, you can check *everything* into version control.  Not just your application code, but every library you use, the exact files that you installed.  I really wanted a system like that.

At the same time, I started looking into "the cloud".  It took me a while to get a handle on what "cloud computing" really means.  What I learned: don't overthink it.  It's not magic.  It's just virtual private servers that can be requisitioned automatically via an API, and are billed on a short time cycle.  You can expand or change the definition a bit, but this definition is the one that matters to *me*.  (I've also realized that I cannot get excited about complicated solutions; only once I realized how simple cloud computing is could I really get excited about the idea.)

Given the modest functionality of cloud computing, why does it matter? Because with a cloud computing system you can actually *test* the full deployment stack.  You can create a brand-new server, identical to all servers you will create in the future; you can set this server up; you can deploy to it.  You get it wrong, you throw away that virtual server and start over from the beginning, fixing things until you get it right.  Billing is important here too; with hourly billing you pay cents for these tests, and you don't need a pool of ready servers because the cloud service basically manages that pool of ready servers for you.

Without "cloud computing" we each too easily find ourselves in a situation where deployments are ad hoc, server installations develop over time, and servers and applications are inconsistent in their configuration.  Cloud computing makes servers disposable, which means we can treat them in consistent ways, testing our work as we go.  It makes it easy to treat operations with the same discipline as software.

Given the idea from App Engine, and the easy-to-use infrastructure of a cloud service, I started to script together something to manage the servers and start up applications.  I didn't know what exactly I wanted to do to start, and I'm not completely sure where I'm going with this.  But on the whole this feels pretty right.  So I present the provisionally-named: `toppcloud <http://toppcloud.colorstudy.com>`_ (**Update**: this has been renamed Silver Cloud).

----------

How it works: first you have a directory of files that defines your application.  This probably includes a checkout of your "application" (let's say in ``src/mynewapp/``), and I find it also useful to use source control on the libraries (which are put in ``lib/python/``).  There's a file in ``app.ini`` that defines some details of the application (very similar to ``app.yaml``).

While app.ini is a (`very minimal <http://toppcloud.colorstudy.com/appconfig.html>`_) description of the *application*, there is no description of the environment.  You do not specify database connection details, for instance.  Instead your application *requests* access to a database service.  For instance, one of these services is a PostgreSQL/PostGIS database (which you get if you put ``service.postgis`` in your app.ini file).  If you ask for that then there will be evironmental variables, ``CONFIG_PG_DBNAME`` etc., that will tell your application how to connect to the database.  (For local development you can provide your own configuration, based on how you have PostgreSQL or some other service installed.)

The standard setup is also a `virtualenv <http://virtualenv.openplans.org>`_ environment.  It is setup so *every time* you start that virtualenv environment you'll get those configuration-related environmental variables.  This means your application configuration is always present, your services always available.  It's available in tests just like it is during a request.  Django accomplishes something similar with the (much maligned) ``$DJANGO_SETTINGS_MODULE`` but toppcloud builds it into the virtualenv environment instead of the shell environment.

And how is the server setup?  Much like with App Engine that is merely an implementation detail.  Unlike App Engine that's an implementation detail you can actually *look* at and change (by changing toppcloud), but it's not something you are supposed to concern yourself with during regular application development.

The basic lifecycle using toppcloud looks like:

``toppcloud create-node``
    Create a new virtual server; you can create any kind of supported server, but only Ubuntu Jaunty or Karmic are supported (and Jaunty should probably be dropped).  This step is where the "cloud" part actually ends.  If you want to install a bare Ubuntu onto an existing physical machine that's fine too -- after ``toppcloud create-node`` the "cloud" part of the process is pretty much done.  Just don't go using some old Ubuntu install; this tool is for clean systems that are used only for toppcloud.

``toppcloud setup-node``
    Take that bare Ubuntu server and set it up (or update it) for use with toppcloud.  This installs all the basic standard stuff (things like Apache, mod_wsgi, Varnish) and some management script that toppcloud runs.  This is written to be safe to run over and over, so upgrading and setting up a machine are the same.  It needs to be a bare server, but 

``toppcloud init path/to/app/``
    Setup a basic virtualenv environment with some toppcloud customizations.

``toppcloud serve path/to/app``
    Serve up the application locally.

``toppcloud update --host=test.example.com path/to/app/``
    This creates or updates an application at the given host.  It edits ``/etc/hosts`` so that the domain is locally viewable.

``toppcloud run test.example.com script.py``
    Run a script (from ``bin/``) on a remote server.  This allows you to run things like ``django-admin.py syncdb``.

There's a few other things -- stuff to manage the servers and change around hostnames or the active version of applications.  It's growing to fit a variety of workflows, but I don't think its growth is unbounded.

----------

So... this is what toppcloud.  From the outside it doen't do a lot.  From the inside it's not actually that complicated either.  I've included a lot of constraints in the tool but I think it offers an excellent balance.  The constraints are workable for applications (insignificant for many applications), while still exposing a simple and consistent system that's easier to reason about than a big-ball-of-server.

Some of the constraints:

1. Binary packages are supported via Ubuntu packages; you only upload portable files.  If you need a library like lxml, you need to request that package (``python-lxml``) to be installed in your app.ini.  If you need a version of a binary library that is not yet packaged, I think creating a new deb is reasonable.

2. There is no Linux distribution abstraction, but I don't care.  

3. There is no option for the way your application is run -- there's one way applications are run, because I believe there is a best practice.  I might have gotten the best practice wrong, but that should be resolved inside toppcloud, not inside applications. Is Varnish a terrible cache?  Probably not, but if it is we should all be able to agree on that and replace it.  If there are genuinely different needs then maybe additional application or deployment configuration will be called for -- but we shouldn't add configuration just because someone *says* there is a better practice (and a better practice that is not universally better); there must be justifications.  

4. By abstracting out services and persistence some additional code is required for each such service, and that code is centralized in toppcloud, but it means we can also start to add consistent tools usable across a wide set of applications and backends.  

5. All file paths have to be relative, because files get moved around.  I know of some particularly problematic files (e.g., ``.pth`` files), and toppcloud fixes these automatically.  Mostly this isn't so hard to do.

These particular compromises are ones I have not seen in many systems (and `I've started to look more <http://toppcloud.colorstudy.com/comparisons.html>`_).  App Engine I think goes too far with its constraints.  `Heroku <http://heroku.com />`_ is close, but closed source.  

This is different than a strict everything-must-be-a-package strategy.  This deployment system is light and simple and takes into account reasonable web development workflows.  The pieces of an application that move around a lot are all well-greased and agile.  The parts of an application that are better to Do Right And Then Leave Alone (like Apache configuration) are static.

Unlike generalized systems like buildout this system avoids "building" entirely, making deployment a simpler and lower risk action, leaning on system packages for the things they do best.  Other open source tools emphasize a greater degree of flexibility than I think is necessary, allowing people to encode exploratory service integration into what *appears* to be an encapsulated build (I'm looking at you buildout).  

Unlike `requirement sets <http://pip.openplans.org/requirement-format.html>`_ and packaging and versioning libraries, this makes all the Python libraries (typically the most volatile libraries) explicit and controlled, and can better ensure that small updates really are small.  It doesn't invalidate installers and versioning, but it makes that process even more explicit and encourages greater thoughtfulness.

Unlike many production-oriented systems (what I've seen in a lot of "cloud" tools) this encorporates both the development environment and production environment; but unlike some developer-oriented systems this does not try to normalize everyone's environment and instead relies on developers to set up their systems however is appropriate.  And unlike platform-neutral systems this can ensure an amount of reliability and predictability through extremely hard requirements (it is deployed on Ubuntu Jaunty/Karmic *only*).

But it's not all constraints.  Toppcloud is solidly web framework neutral.  It's even `slightly language neutral <http://toppcloud.colorstudy.com/php.html>`_.  Though it does require support code for each persistence technique, it is fairly easy to do, and there are no requirements for "scalable systems"; I think unscalable systems are a perfectly reasonable implementation choice for many problems.  I believe a more scalable system could be built on this, but as a deployment and development option, not a starting requirement.

So far I've done some deployments using toppcloud; not a lot, but some.  And I can say that it feels really good; lots of rough edges still, but the core concept feels really right.   I've made a lot of sideways attacks on deployment, and a few direct attacks... sometimes I write things that I think are useful, and sometimes I write things that I think are right.  Toppcloud is at the moment maybe more right than useful.  But I genuinely believe this is (in theory) a universally appropriate deployment tool.

----------

Alright, so now you think maybe you should look more at toppcloud...

Well, I can offer you `a fair amount of documentation <http://toppcloud.colorstudy.com>`_.  A lot of that documentation refers to design, and a bit of it to examples.  There's also a couple projects you can look at; they are all small, but :

* `Frank <http://bitbucket.org/geraldmc/frank-src/src/tip/build-fs-layout>`_ (will be interactivesomerville.org) which is another similar Django/Pinax project (Pinax was a bit tricky).  This is probably the largest project.  It's a Django/Pinax volunteer-written application for collecting community feedback the Boston Greenline project, if that sounds interesting to you might want to chip in on the development (if so `check out the wiki <https://projects.openplans.org/greenline>`_).

* `Neighborly <http://github.com/ianb/neighborly/blob/master/INSTALL.txt>`_, with minimal functionality (we need to run more sprints) but an installation story.

* `bbdocs <http://bitbucket.org/ianb/bbdocs/src/tip/create-layout.sh>`_ which is a very simple bitbucket document generator, that makes the toppcloud site.

* `geodns <http://bitbucket.org/ianb/geodns>`_ which is another simple no-framework PostGIS project.

----------

Now, the letdown.  One thing I cannot offer you is support.  **THERE IS NO SUPPORT**.  I cannot now, and I might never really be able to support this tool.  This tool is appropriate for collaborators, for people who like the idea and are ready to build on it.  If it grows well I hope that it can grow a community, I hope people can support each other.  I'd like to help that happen.  But I can't do that by bootstrapping it through unending support, because I'm not good at it and I'm not consistent and it's unrealistic and unsustainable.  This is not a open source dead drop.  But it's also not My Future; I'm not going to build a company around it, and I'm not going to use all my free time supporting it.  It's a tool I want to exist.  I **very much** want it to exist.  But even very much wanting something is not the same as being an undying champion, and I am not an undying champion.  If you want to tell me what my process *should* be, please do!

----------

    If you want to see me get philosophical about packaging and deployment and other stuff like that, see my upcoming talk at `PyCon <http://us.pycon.org />`_.
