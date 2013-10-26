pyinstall pybundles
###################
:date: 2008-10-01 13:14
:author: Ian Bicking
:tags: Python

**Update**: pyinstall has been renamed to `pip <http://pip.openplans.org>`_ (per the suggestions in the comments to this post)    

I added `pybundles <http://pyinstall.openplans.org/#bundles>`_ to `pyinstall <http://pyinstall.openplans.org>`_ very shortly before I `announced pyinstall <http://www.openplans.org/projects/topp-engineering/blog/2008/09/24/pyinstall-a-new-hope />`_.  I hadn't actually tried it out that much.  Since then I've made three more minor releases of pyinstall, and I think the bundle support is working pretty decently.

A ``.pybundle`` file is just a bunch of source code, all the source code you need to install some package(s).  For instance, for `Deliverance <http://deliverance.openplans.org>`_ I've created a bundle file so you can do::

    $ easy_install pyinstall virtualenv
    $ pyinstall.py -E DeliveranceTest/ \\
    >   http://deliverance.openplans.org/dist/Deliverance-snapshot-latest.pybundle

This creates a virtualenv environment in ``DeliveranceTest/``, unpacks all the source from the bundle, and installs all of it.  It's not magical -- it still has to compile the source and move the files around -- but it does mean just a single download, and the versions of everything that is installed aren't going to change unless that bundle file is regenerated.

I've been thinking about some other features for pybundles, like post installation scripts.  All of this has raised a problem though: pyinstall needs to be a two-level command, with commands like:

``pyinstall.py install X``
``pyinstall.py bundle Y``
``pyinstall.py freeze req.txt``
and of course the not-yet-implemented:
``pyinstall.py remove Z``

But ``pyinstall.py install`` does not read well.  It's not too late to rename the package (yet again), or just rename the script.  Ideas?

