My Experience Writing a Build System
####################################
:date: 2008-06-19 22:41
:author: Ian Bicking
:tags: Programming, Python, Web

Lately there's been some interest in build processes among various people -- `Vellum <http://www.zedshaw.com/projects/vellum />`_ was announced a while back, `Ben has been looking for a tool <http://groovie.org/2008/04/09/wheres-the-capistrano-knock-off-for-us-python-web-devs>`_ and looking at `Fabric <https://savannah.nongnu.org/projects/fab />`_, and `Kevin announced Paver <http://www.blueskyonmars.com/projects/paver />`_.  At the same time `zc.buildout <http://pypi.python.org/pypi/zc.buildout>`_ is starting to gain some users outside of the Zope world, and I noticed `Minitage <http://www.minitage.org/doc/rst />`_ as an abstraction on top of zc.buildout.

A while ago I started working on a build project for `Open Plans <http://topp.openplans.org>`_ called `fassembler <https://svn.openplans.org/svn/fassembler/trunk>`_.  I think the result has been fairly successful and maintainable, and I thought I'd share some of my own reflections on that tool.

**Update:** what we were trying to accomplish
-------------------------------------------------------

I didn't make it clear in the post just what we were trying to do, and what this build system would accomplish.

Our site (`openplans.org <http://openplans.org>`_) is made up of several separate servers with an HTML-rewriting proxy on the front end.  We have a Zope server running a custom application, Apache running WordPress MU, and some servers running Pylons or other Python web applications for portions of our site.  We needed a way to consistently reproduce this entire stack, all the pieces, plugged together so that the site would actually work.  Two equally important places where we had to reproduce the stack are for developer rigs and the production site.

Our code is primarily Python and we use a *lot* of libraries, developed both internally and externally.  Setting up the site is primarily a matter of installing the right libraries and configuration and setting up any databases (both a `ZODB <http://www.zope.org/Products/StandaloneZODB>`_ databases and several MySQL databases).  We use a few libraries written in C, but `distutils <http://python.org/doc/current/lib/module-distutils.html>`_ handles the compilation of those pretty transparently.

For this case we really don't care about build tools that focus on compilation.  We don't care about careful dependency tracking because we are compiling very little software.

make doesn't make sense
-----------------------

**Update 2**: If you think the make model makes lots of sense, read the preceding section -- it makes sense for a different problem set than what we're doing.

We initially had a system based on `BuildIt <http://agendaless.com/Members/chrism/software/buildit>`_, which is kind of like `make <http://en.wikipedia.org/wiki/Make_(software)>`_ with Python as the control code.  It wasn't really a good basis for our build tool, and I think it added a lot of confusion, compounded by the fact that we weren't quite sure what we wanted our build to do.  Ultimately I think the make model of building doesn't make sense.

The make model is based on the idea that you **really** want to save work.  So you detect changes and remake things only as necessary.  For compilation this might make sense, because you edit code and recompile a lot and it's tedious to wait.  But we are building a website, and installing software, and none of that style of efficiency matters.  make-style detection of work to be done doesn't even save any time.  But it does make the build more fragile (e.g., if you define a dependency incorrectly) and much harder to understand, and you constantly find yourself wiping the build and starting from scratch because you don't trust the system.

The metaphor for the new build system was much simpler: do a list of things, top to bottom.  There's no effort into detecting changes in the build, or changes in the settings, or anything else.  

Do things carefully
-------------------

In the build system almost all actions go through the `filemaker <https://svn.openplans.org/svn/fassembler/trunk/fassembler/filemaker.py>`_ module.  This is *kind of* a file abstraction library.  But the goals are entirely different than convenience: the goal is transparency and safety.  In contrast Paver uses `path.py <http://www.jorendorff.com/articles/python/path />`_ for convenience, but I'm not sure what the win would be if we used a model like that.

``filemaker`` itself is heavily tied to the framework that it's written for, specifically user interaction and logging.  Most tasks just *do* things, and rely on filemaker to detect problems and ask the user questions.  For example, every time a file is written, it checks if the file exists, and if it has the same content.  If it exists with other content, it asks the user about what to do.  It doesn't overwrites files without asking (at least by default).  I think this makes the tool more humane as the default behavior for a build is to be careful and transparent.  The build author has to go out of their way to make things difficult.

Many zc.buildout recipes will blithely overwrite all sorts of files which always made me very uncomfortable with the product.  It's the *recipes* in zc.buildout which do this, not the buildout framework itself, but because buildout made overwriting the easy thing to do, and didn't start with humane conventions or tools, this behavior is the norm.

What I think filemaker most accomplished was the ability to do file operations while also asserting the expected state of the system, and so makes build bugs noticeable earlier instead of getting a build process that finishes successfully but creates a buggy build, or having an exception show up far from where the error was originally introduced.

Also, because it won't overwrite your work in progress this has saved the build from engendering deep feelings of hatred in cases when it might overwrite your work in progress.  It's hard to detect this absence of hatred, but I know that I've felt it with other systems.

**Update:** a corollary: ignore no errors
-----------------------------------------

One question you might wonder about: why not a shell script?  We did prototype some things as shell scripts, but we've consistently moved to Python at some point, even things that seemed really trivial.  The problem with shell scripts is they have horribly bad behavior with respect to errors.  Ignoring errors is really really easy, noticing errors is really hard.

This is absolutely unacceptable for builds.  Builds must not ignore errors.  The build may mostly work despite an error.  It might be totally broken, but the error message is lost in all sorts of useless output.  The error message probably makes no sense.  The context is lost.  No suggestion is given to the user.

When builds work, that's great.  Build *do not* always work.  They always fail sometimes, and some poor sucker (usually in some hot potato-like arrangement) has to figure out what went wrong.  You have to plan for these problems.

Everything in the build tries to be careful about errors.  All places where it is not, it is a bug.  The resolution isn't to see something appear to work, but create a broken build, and say "oh, you forgot to set X".  The resolution is to make sure when you forget to set X it gives you an error that tells you to set X.

This is one of the more important and more often ignored principles of a good build/deployment system.  Maybe it's gotten better, but when I first used zc.buildout (*very* early in its development) the poor handling of errors was by far the biggest problem and it left me with a bad taste in my mouth.  easy_install and setuptools in general is also very flawed in this respect.

Log interesting things
----------------------

I tried to make a compromise between logging very verbosely, and being too quiet.  As a user, I want to see everything *interesting* and leave out everything *boring*.  Determining interesting and boring can be a bit difficult, but really just require some attention and tweaking.

To make it possible to visually parse the output of the tool I found both indentation and color to be very useful.  Indentation is used to represent subtasks, and color to make sections and warnings stand out.

The default verbosity setting is not to be completely quiet.  Silence is a Unix convention that just doesn't work for build tools.  Silence gets you interactions like this::

    $ build-something target-directory/
    (much time passes)
    Error: cannot write /home/ianb/builds/20080426/target-directory/products/AuxInput/auxinput/config/configuration.xml

Why did it want to write that file?  Why can't it write that file?  Is the build buggy?  Did I misconfigure it?  Does the directory exist?

The typical way of handling this is either to run the build again with logging setup or otherwise make it more verbose, or to get in the habit of always running it verbose.

Mixing code and configuration
-----------------------------

BuildIt, which we were using before, had the ability to put variables in settings, and you could read an option from another section with something like ``${section/option}``.  It was limited to simple (but recursive) variable substitution, and had some clever but very confusing rules that created a kind of inheritance.

I liked the ability to do substitution, but wasn't happy with the compromise BuildIt made.  I wasted a *lot* of time trying to figure out the context of substitutions.  So, I saw two directions.  One was to remove the cleverness and just do simple substitution.  This is the choice zc.buildout made.  The other was to go whole-hog.  With a bit of trepidation I decided to to go for it, and I made the choice to treat all configuration settings as `Tempita <http://pythonpaste.org/tempita />`_ templates.  All configuration is generally accessed via ``config.setting_name``, and that lazily interpolates the setting (it took me quite a while to figure out how to avoid infinite loops of substitution).  Because evaluation is done lazily settings can depend on each other and be overridden and have lots of code in defaults (e.g., a default that is calculated based on the value of another setting), and it works out okay.  Most settings just ended up having a smart default, and as a result very little tweaking of the configuration is necessary.

Somewhat ironically the result was a kind of atrophying of the settings, because no one actually *set* them, instead we just tweaked the defaults to get it right.  Now I'm not entirely sure what exactly the "settings" are setting, or who they should really belong to.  To the build?  To the tasks?  While this is conceptually confusing, in practice it isn't so bad.  This mixing of code and configuration has been distinctly useful, and not *nearly* as problematic to debug as I worried it would be.   In some ways it was a way of building ``lambda`` into every string, and the lazy evaluation of those strings has been really important.  But it's not clear if they are really settings.

Would normal string interpolation have been enough (e.g., with `string.Template <http://python.org/doc/current/lib/node40.html>`_)?  I'm pretty sure it wouldn't have been.  The ability to do a little math or use functions that read things from the environment has been very important.

Managing Python libraries
-------------------------

fassembler uses `virtualenv <http://pypi.python.org/pypi/virtualenv>`_ for building each piece of the stack.  Generally it creates several environments and installs things into them -- it doesn't run inside the environments itself.  This works fine.

zc.buildout in comparison does some fancy stuff to scripts where specific eggs are enabled when you run a script.  Each script has a list of *all* the eggs to enable.  You can't install things or manage anything manually, even to test -- you always have to go through buildout, and it will regenerate the scripts for you.  zc.buildout was implemented at the same time as workingenv (the predecessor to virtualenv), and I actually finished virtualenv with fassembler in mind, so I can't blame zc.buildout for not using virtualenv.  That said, I don't think the zc.buildout system makes any sense.  And it's really complicated and has to access all sorts of not-really-public parts of easy_install to work.

Isolation is only the start.  easy_install makes sure each library's claimed dependencies are satisfied.  You might then think easy_install would do all the work to make the stack work.  It is nowhere close to making the stack work.  ``setup.py`` files can/should contain the bare minimum that is known to be necessary to make a package work.  But they can't predict future incompatibilities, and they can't predict interactions.  And you don't want all your packages changing versions arbitrarily.  If you work with a lot of libraries you *need* those libraries to be pinned, and only update them when you *want* to update them, not just because an update has been released.

So for each piece of the stack we have a set of "requirements".  This is a flat files that indicates all the packages to install.  They can have explicit versions, far more restrictive than anything you should put in ``setup.py``.  It also can check out from svn, including pinning to revisions.  This installation plan can go in svn, you can do diffs on it, you can branch and copy and do whatever.  Maybe at some point we could use it to keep cached copies of the libraries.  For now it mostly uses ``easy_install`` (and ``python setup.py develop`` for checkouts).  

In parallel we have a command-line program for just installing packages using files like this, called `PoachEggs <https://svn.openplans.org/svn/PoachEggs/trunk>`_.  I want to make this better, and have fassembler use it, but I mostly note it because it implements a feature that can "freeze" all your packages to a requirements file.  You take a working build and freeze its requirements, giving explicit (``==``) versions for packages, and pin all the svn checkouts to a revision, so that the frozen requirements file will install exactly the packages you know work.

An alternative to this is what the `Repoze <http://repoze.org />`_ guys are doing, which is to create a custom index that only includes the versions of libraries that you want.  You then tell easy_install to use this instead of `PyPI <http://pypi.python.org/pypi>`_.  It works with zc.buildout (and anything that uses easy_install), but I can't get excited about it compared to a simple text file.  I also want svn checkouts instead of create tarballs of the checkout -- I like an editable environment, because the build is just as much to support developers as to support deployment.

The structure
-------------

A big part of the development of fassembler was nailing down the structure of our site, and moving to use tools like `supervisor <http://supervisord.org />`_ to manage our processes.  A lot of these expectations are built into the builds and fassembler itself.  This is part of what makes the build Work -- the pieces all conform to a common structure with some basic standards.  But this isn't the build tool itself, it's just a set of conventions.

I don't know quite what to make of this.  Extracting the conventions from the builds leads to a situation where you can more easily misconfigure things, and the installation process ends up being more documentation-based instead of code-based.  We do *not* want to rely on documentation, because documentation is generally because of a flaw in the build process that needs explaining.  It's faster for everyone if the code is just right.  Maybe these conventions could be put into code, separate from the build.  The abstraction worries me, though -- too much to keep track of?

What we don't get right
-----------------------

The biggest problem is that fassembler is our own system and no one else uses it.  If someone wants to use just a piece of our stack they either have to build it manually or they have to use our system which is meant to build all our pieces together with our conventions.  There's some pressure to use zc.buildout to make pieces more accessible to other Zope users.  We've also found things that build with zc.buildout that we'd like to use (e.g., setups for `varnish <http://varnish.projects.linpro.no />`_).

We haven't figured out how to separate the code for building *our* stuff from the build software itself.  There's a bootstrapping problem: you need to get the build code to build a project, and so it can't be part of the project you are building.  zc.buildout uses configuration files (that aren't code, so they lack the bootstrap problem) and it uses `recipes <http://pypi.python.org/pypi/zc.buildout#id1>`_ (a kind of plugin) and has gone to quite a bit of effort to bootstrap everything.  virtualenv also supports a kind of `bootstrap <http://pypi.python.org/pypi/virtualenv#bootstrap-example>`_ which we use to do the initial setup of the environment, but it doesn't support code organization in the style of zc.buildout.

Builds are also fairly tedious to write.  They aren't horrible, but they feel much longer than they should be.  Part of their length, though, is that over time we put in more code to guard against environment differences or build errors, and more code to detect the environment.  But compared to zc.buildout's configuration files, it doesn't feel quite as nice, and if it's not as nice sometimes people are lazy and do ad hoc setups.

The future
----------

We haven't really decided, but as you might have noticed zc.buildout gets a lot of attention here.  There's quite a few things I don't like about it, but a lot of these have to do with the recipes available.  We don't *have* to use the standard zc.buildout egg installation recipe.  In fact that would be first on the chopping block, replaced with something much simpler that assumes you are running inside a virtualenv environment, and probably something that uses requirement files.

Also, we could extract filemaker into a library and recipes could use that.  Possibly logging could be handled the same way (the `logging <http://python.org/doc/current/lib/module-logging.html>`_ module just isn't designed for an interactive experience like a build tool).  Then if we used other people's recipes we might feel grumpy, since they'd use neither filemaker or our logging, but it would still work.  And our recipes would be full of awesome.  The one thing I don't think we could do is introduce the template-based configuration.  Or, if we did, it would be hard.

That said, there is a very different direction we could go, one inspired more by `App Engine <http://code.google.com/appengine />`_.  In that model we build files under a directory, and that directory is the build.  Wherever you build, you get the same files, period.  All paths would be relative.  All environmental detection would happen in code at runtime.  Things that aren't "files" exactly would simply be standard scripts.  E.g., database setup would not be done by the build, but would be a script put in a standard location.

This second file-based model of building is very much different than the principles behind zc.buildout.  zc.buildout requires rebuilding when anything changes, and does so without apology.  It requires rebuilding to move the directories, or to move to different machines.  Using a file-based model requires a lot of push-back into the products themselves.  Applications have to be patched to accept smart relative paths.  They have to manage themselves a lot more, detect their environment, handle any conflicts or ambiguities, being graceful about stuff like databases, because the files have to be universal.  In an extreme case I could imagine going so far as to only keep a template for a configuration file, and write the real configuration file to a temporary location before starting a server (if the server cannot be patched to accept runtime location information).

So this is the choice ahead.  I'm not sure *when* we'll make this choice (if ever!) -- build systems are dull and somewhat annoying, but they are no more dull and annoying than dealing with a poor build system.  Actually, they are *definitely* less dull than working with a build system that isn't good enough or powerful enough, or one that simply lacks the TLC necessary to keep builds working.  So no choice is a choice too, and maybe a bad choice.
