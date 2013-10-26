Using pip Requirements
######################
:date: 2008-12-16 19:30
:author: Ian Bicking
:tags: Packaging, Python

Following onto a set of recent posts (from `James <http://www.b-list.org/weblog/2008/dec/14/packaging />`_, `me <http://blog.ianbicking.org/2008/12/14/a-few-corrections-to-on-packaging />`_, then `James again <http://www.b-list.org/weblog/2008/dec/15/pip />`_), Martijn Faassen `wrote a description of Grok's version management <http://faassen.n--tree.net/blog/view/weblog/2008/12/16/0>`_.  Our ideas are pretty close, but he's using buildout, and I'll describe out to do the same things with pip.

Here's a kind of development workflow that I think works well:

* A framework release is prepared.  Ideally there's a buildbot that has been running (as `Pylons has <http://pylonshq.com:8010 />`_, for example), so the integration has been running for a while.

* People make sure there are released versions of all the important components.  If there are known conflicts between pieces, libraries and the framework update their ``install_requires`` in their ``setup.py`` files to make sure people don't use conflicting pieces together.

* Once everything has been released, there is a known set of packages that work together.  Using a buildbot maybe future versions will also work together, but they won't necessarily work together with applications built on the framework.  And breakage can also occur regardless of a buildbot.

* Also, people may have versions of libraries already installed, but just because they've installed something doesn't mean they really mean to stay with an old version.  While known conflicts have been noted, there's going to be lots of unknown conflicts and future conflicts.

* When starting development with a framework, the developer would like to start with some known-good set, which is a set that can be developed by the framework developers, or potentially by any person.  For instance, if you extend a public framework with an internal framework (or even a public sub-framework like `Pinax <http://pinaxproject.com />`_) then the known-good set will be developed by a different set of people.

* As an application is developed, the developer will add on other libraries, or use some of their own libraries.  Development will probably occur at the trunk/tip of several libraries as they are developed together.

* A developer might upgrade the entire framework, or just upgrade one piece (for instance, to get a bug fix they are interested in, or follow a branch that has functionality they care about).  The developer doesn't necessarily have the same notion of "stable" and "released" as the core framework developers have.

* At the time of deployment the developer wants to make sure all the pieces are deployed together as they've tested them, and how they know them to work.  At any time, another developer may want to clone the same set of libraries.

* After initial deployment, the developer may want to upgrade a single component, if only to test that an upgrade works, or if it resolves a bug.  They may test out combinations only to throw them away, and they don't want to bump versions of libraries in order to deploy new combinations.

This is the kind of development pattern that requirement files are meant to assist with.  They can provide a known-good set of packages.  Or they can provide a starting point for an active line of development.  Or they can provide a historical record of how something was put together.

The easy way to start a requirement file for pip is just to put the packages you know you want to work with.  For instance, we'll call this ``project-start.txt``::

    Pylons
    -e svn+http://mycompany/svn/MyApp/trunk#egg=MyApp
    -e svn+http://mycompany/svn/MyLibrary/trunk#egg=MyLibrary

You can plug away for a while, and maybe you decide you want to freeze the file.  So you do::

    $ pip freeze -r project-start.txt project-frozen.txt

By using ``-r project-start.txt`` you give ``pip freeze`` a template for it to start with.  From that, you'll get ``project-frozen.txt`` that will look like::

    Pylons==0.9.7
    -e svn+http://mycompany/svn/MyApp/trunk@1045#egg=MyApp
    -e svn+http://mycompany/svn/MyLibrary/trunk@1058#egg=MyLibrary

    ## The following requirements were added by pip --freeze:
    Beaker==0.2.1
    WebHelpers==0.9.1
    nose==1.4
    # Installing as editable to satisfy requirement INITools==0.2.1dev-r3488:
    -e svn+http://svn.colorstudy.com/INITools/trunk@3488#egg=INITools-0.2.1dev_r3488
    
At that point you might decide that you don't care about the nose version, or you might have installed something from trunk when you could have used the last release.  So you go and adjust some things.

Martijn also asks: how do you have framework developers maintain one file, and then also have developers maintain their own lists for their projects?

You could start with a file like this for the framework itself.  Pylons for instance could ship with something like this.  To install Pylons you could then do::

    $ pip -E MyProject install \\
    >    -r http://pylonshq.com/0.9.7-requirements.txt

You can also download that file yourself, add some comments, rename the file and add your project to it, and use that.  When you freeze the order of the packages and any comments will be preserved, so you can keep track of what changed.  Also it should be ameniable to source control, and diffs would be sensible.

You could also use indirection, creating a file like this for your project::

    -r http://pylonshq.com/0.9.7-requirements.txt
    -e svn+http://mycompany/svn/MyApp/trunk#egg=MyApp
    -e svn+http://mycompany/svn/MyLibrary/trunk#egg=MyLibrary

That is, requirements files can refer to each other.  So if you want to maintain your own requirements file alongside the development of an upstream requirements file, you could do that.
