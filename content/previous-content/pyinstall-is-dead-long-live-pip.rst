pyinstall is dead, long live pip!
#################################
:date: 2008-10-28 11:59
:author: Ian Bicking
:tags: Programming

I've finished renaming pyinstall to its new name: **pip**.  The name pip is a acronym and declaration: *pip installs packages*.

I've also added a small feature intended for Google App Engine users, allowing you to zip and unzip packages in an environment.  For instance::

    $ pip zip --list
    In ./lib/python2.5/site-packages:
      No zipped packages.
      Unzipped packages:
        paste  (98 files)
        pygments  (64 files)
        tempita  (7 files)
        weberror  (31 files)
        webob  (22 files)
        webtest  (9 files)
        nose  (43 files)
        setuptools-0.6c9-py2.5.egg  (43 files)
        simplejson  (28 files)
    $ pip zip webob
    Zip webob (in ./lib/python2.5/site-packages/webob)

Right now this doesn't work well with egg directories (i.e., packages installed with ``easy_install``), though that shouldn't be too hard to resolve.  ``pip install`` itself does not install packages into egg directories (it *does* install eggs, which is to say it installs all the egg metadata and works fine with `pkg_resources <http://peak.telecommunity.com/DevCenter/PkgResources>`_).

I don't really use `buildout <http://pypi.python.org/pypi/zc.buildout>`_ myself, but I would like to throw it out there that I think someone should create a pip recipe as an alternative to `zc.recipe.egg <http://pypi.python.org/pypi/zc.recipe.egg>`_.  There's not really a stable programmatic API in pip at this point, but with no consumers of the API it feels like premature design to settle on something now -- integrate with pip and we can figure out what that stable API should be.  If you integrate buildout, probably another useful feature would be an option have to ``pip freeze`` write the packages out to a setting in your ``buildout.cfg``.
