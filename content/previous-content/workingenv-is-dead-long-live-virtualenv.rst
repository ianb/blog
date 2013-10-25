Workingenv is dead, long live Virtualenv!
#########################################
:date: 2007-10-10 10:00
:author: Ian Bicking
:tags: Python

A lot of people have found `workingenv <http://cheeseshop.python.org/pypi/workingenv.py>`_ useful, but it's always been a bit fragile.  If you've seen the ``.../site.py is not a setuptools-generated site.py; please remove it.`` message, you know what I mean.

For a while I tried to refactor and improve workingenv, but it didn't go very well.  So I decided to ditch it completely and revisit the ideas of `virtual-python.py <http://peak.telecommunity.com/DevCenter/EasyInstall#creating-a-virtual-python>`_. That script works by copying the Python executable, and in doing so change sys.prefix -- it's pretty consistent that all other paths in Python derive from sys.prefix.

The result is `virtualenv <http://pypi.python.org/pypi/virtualenv>`_, which I think is now featureful enough for general use.  It might still be buggy, but it's worked well for some of us, and I expect the bugs to all be much *easier* than they were in workingenv.

Unlike virtual-python.py, virtualenv works on Windows and in the latest release also Mac framework builds.  It also handles site-packages better, so you can manage some of your packages using packages from your OS distribution (e.g., debs or rpms), while also installing environment-local packages.

So, in summary: use virtualenv, don't use workingenv.  And if you were using the ``--requirements`` option to workingenv, the package `PoachEggs <https://svn.openplans.org/svn/PoachEggs/trunk>`_ lets you do a similar batch installation after you've created the environment.
