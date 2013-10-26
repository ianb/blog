A Few Corrections To "On Packaging"
###################################
:date: 2008-12-14 15:53
:author: Ian Bicking
:tags: Packaging, Python

`James Bennett recently wrote an article on Python packaging and installation <http://www.b-list.org/weblog/2008/dec/14/packaging />`_, and Setuptools.  There's a lot of issues, and writing up my thoughts could take a long time, but I thought at least I should correct some errors, specifically category errors.  Figuring out where all the pieces in Setuptools (and pip and virtualenv) fit *is* difficult, so I don't blame James for making some mistakes, but in the interest of clarifying the discussion...

I will start with a kind of glossary:

Distribution:
    This is something-with-a-setup.py.  A tarball, zip, a checkout, etc.  Distributions have names; this is the name in ``setup(name="...")`` in the setup.py file.  They have some other metadata too (description, version, etc), and Setuptools adds to that metadata some.  Distutils doesn't make it very easy to add to the metadata -- it'll whine a little about things it doesn't know, but won't do anything with that extra data.  Fixing this problem in Distutils is an important aspect of Setuptools, and part of what Distutils itself unsuitable as a basis for good library management.

package/module:
    This is something you import.  It is not the same as a distribution, though usually a distribution will have the same name as a package.  In my own libraries I try to name the distribution with mixed case (like Paste) and the package with lower case (like paste).  Keeping the terminology straight here is *very* difficult; and usually it doesn't matter, but sometimes it does.

Setuptools The Distribution:
    This is what you install when you install Setuptools.  It includes several pieces that Phillip Eby wrote, that work together but are not strictly a single thing.

setuptools The Package:
    This is what you get when you do ``import setuptools``.  Setuptools largely works by monkeypatching distutils, so simply importing setuptools activates its functionality from then on.  This package is entirely focused on installation and package management, it is not something you should use at runtime (unless you are installing packages as your runtime, of course).

pkg_resources The Module:
    This is also included in Setuptools The Distribution, and is for use at runtime.  This is a single module that provides the ability to query what distributions are installed, metadata about those distributions, information about the location where they are installed.  It also allows distributions to be "activated".  A *distribution* can be available but not activated.  Activating a distribution means adding its location to ``sys.path``, and probably you've noticed how long sys.path is when you use easy_install.  Almost everything that allows different libraries to be installed, or allows different versions of libraries, does it through some management of sys.path.  pkg_resources also allows for generic access to "resources" (i.e., non-code files), and let's those resources be in zip files.  pkg_resources is safe to use, it doesn't do any of the funny stuff that people get annoyed with.

easy_install:
    This is also in Setuptools The Distribution.  The basic functionality it provides is that given a name, it can search for package with that distribution name, and also satisfying a version requirement.  It then downloads the package, installs it (using ``setup.py install``, but with the setuptools monkeypatches in place).  After that, it checks the newly installed distribution to see if it requires any other libraries that aren't yet installed, and if so it installs them.

Eggs the Distribution Format:
    These are zip files that Setuptools creates when you run ``python setup.py bdist_egg``.  Unlike a tarball, these can be binary packages, containing compiled modules, and generally contain .pyc files (which are portable across platforms, but not Python versions).  This format only includes files that will actually be installed; as a result it does not include doc files or ``setup.py`` itself.  All the metadata from ``setup.py`` that is needed for installation is put in files in a directory ``EGG-INFO``.

Eggs the Installation Format:
    Eggs the Distribution Format are a subset of the Installation Format.  That is, if you put an Egg zip file on the path, it is installed, no other process is necessary.  But the Installation Format is more general.  To have an egg installed, you either need something like ``DistroName-X.Y.egg/`` on the path, and then an ``EGG-INFO/`` directory under that with the metadata, or a path like ``DistroName.egg-info/`` with the metadata directly in that directory.  This metadata can exist anywhere, and doesn't have to be directly alongside the actual Python code.  Egg directories are required for pkg_resources to activate and deactivate distributions, but otherwise they aren't necessary.

pip:
    This is an alternative to easy_install.  It works *somewhat* differently than easy_install, but not much.  Mostly it is *better* than easy_install, in that it has some extra features and is easier to use.  Unlike easy_install, it downloads all distributions up-front, and generates the metadata to read distribution and version requirements.  It uses Setuptools to generate this metadata from a setup.py file, and uses pkg_resources to parse this metadata.  It then installs packages *with the setuptools monkeypatches applied*.  It just happens to use an option ``python setup.py --single-version-externally-managed``, which gets Setuptools to install packages in a more flat manner, with ``Distro.egg-info/`` directories alongside the package.  Pip installs eggs!  I've heard the many complaints about easy_install (and I've had many myself), but ultimately I think pip does well by just fixing a few small issues.  Pip is *not* a repudiation of Setuptools or the basic mechanisms that easy_install uses.  

PoachEggs:
    This is a defunct package that had some of the features of pip (particularly requirement files) but used easy_install for installation.  Don't bother with this, it was just a bridge to get to pip.

virtualenv:
    This is a little hack that creates isolated Python environments.  It's based on ``virtual-python.py``, which is something I wrote based on some documentation notes PJE wrote for Setuptools.  Basically virtualenv just creates a ``bin/python`` interpreter that has its own value of ``sys.prefix``, but uses the system Python and standard library.  It also installs Setuptools to make it easier to bootstrap the environment (because bootstrapping Setuptools is itself a bit tedious).  I'll add pip to it too sometime.  Using virtualenv you don't have to worry about different library versions, because for any one environment you will probably only need one version of a library.  On any one *machine* you probably need different versions, which is why installing packages system-wide is problematic for most libraries.  (I've been meaning to write a post on why I think using system packaging for libraries is counter-productive, but that'll wait for another time.)

----

So... there's the pieces involved, at least the ones I can remember now.  And I haven't really discussed .pth files, entry points, sys.path trickery, site.py, distutils.cfg... sadly this is a complex state of affairs, but it was also complex before Setuptools.

There are a few things that I think people really dislike about Setuptools.

First, zip files.  Setuptools prefers zip files, for reasons that won't mean much to you, and maybe are more historical than anything.  When a distribution doesn't indicate if it is zip-safe, Setuptools looks at the code and sees if it uses ``__file__``, an if not it presumes that the code is probably zip-safe.  The specific problem James cites is what appears to be a bug in Django, that Django looks for code and can't traverse into zip files in the same way that Python itself can.  Setuptools didn't itself add anything to Python to make it import zip files, that functionality was added to Python some time before.  The zipped eggs that Setuptools installs are using existing (standard!) Python functionality.

That said, I don't think zipping libraries up is all that useful, and while it *should* work, it doesn't always, and it makes code harder to inspect and understand.  So since it's not that useful, I've disabled it when pip installs packages.  I also have had it disabled on my own system for years now, by creating a ``distutils.cfg`` file with ``[easy_install] zip_ok = False`` in it.  Sadly App Engine is forcing me to use zip files again, because of its absurdly small file limits... but that's a different topic.  (There is an experimental ``pip zip`` command mostly intended for App Engine.)

Another pain point is version management with ``setup.py`` and Setuptools.  Indeed it is easy to get things messed up, and it is easy to piss people off by overspecifying, and sometimes things can get in a weird state for no good reason (often because of easy_install's rather naive leap-before-you-look installation order).  Pip fixes that last point, but it also tries to suggest more constructive and less painful ways to manage other pieces.

Pip requirement files are an assertion of **versions that work together**.  setup.py requirements (the Setuptools requirements) should contain two things: **1**: all the libraries used by the distribution (without which there's no way it'll work) and **2**: exclusions of the versions of those libraries that are **known not to work**.  setup.py requirements should not be viewed as an assertion that by satisfying those requirements everything *will* work, just that it *might* work.  Only the end developer, testing the system together, can figure out if it really works.  Then pip gives you a way to record that working set (using `pip freeze <http://pip.openplans.org/#freezing-requirements>`_), separate from any single distribution or library.

There's also a lot of conflicts between Setuptools and package maintainers.  This is kind of a proxy war between developers and sysadmins, who have very different motivations.  It deserves a post of its own, but the conflicts are about more than just how Setuptools is implemented.

I'd love if there was a language-neutral library installation and management tool that really worked.  Linux system package managers are absolutely not that tool; frankly it is absurd to even consider them as an alternative.  So for now we do our best in our respective language communities.  If we're going to move forward, we'll have to acknowledge what's come before, and the reasoning for it.
