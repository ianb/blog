2 Python Environment Experiments
################################
:date: 2007-09-16 18:32
:author: Ian Bicking
:tags: Programming, Python

two experiments in the Python environment.  The first is `virtualenv <http://pypi.python.org/pypi/virtualenv>`_, which is a rethinking of `virtual-python.py <http://peak.telecommunity.com/DevCenter/EasyInstall#creating-a-virtual-python>`_, and my attempt to move away from `workingenv <http://pypi.python.org/pypi/workingenv.py>`_.  It works mostly like ``virtual-python.py``, and on systems where it works (not Windows, nor Framework Mac Python) I think it works considerably better than workingenv.  No more ``not a setuptools' site.py``, in particular. The basic technique is that it creates/copies a new ``python`` executable, and anything that uses that executable (including a script that references that executable with ``#!``) will use that environment.

On the systems where it doesn't work, I'm not quite sure what to do. The problem with the Mac is that ``sys.prefix`` is not determined by the location of the ``python`` executable, it's hard-coded in some fashion.  I `asked about it on distutils-sig <http://mail.python.org/pipermail/distutils-sig/2007-September/008265.html>`_ and got some response, but haven't figured out any solution yet.

On Windows similarly ``sys.prefix`` is not determined by the executable location.  What it's determined by there I don't know -- the location of ``python25.dll``, something in the registry?  If I could figure it out, perhaps this could work there too -- the existance of symlinks isn't as important as it was with ``virtual-python.py``.

If I can get these figured out, I think this will be a much happier experience than ``workingenv``, and a somewhat friendlier experience than ``virtual-python.py``.  On non-Mac posix systems it works well right now.

The other experiment is in `buildutils <https://www.knowledgetap.com/hg/buildutils>`_ (downloadable with `Mercurial <http://www.selenic.com/mercurial/wiki />`_): a new command ``python setup.py bundle``, run in the application package you want to bundle.  This creates a directory with all the dependencies of the application, and scripts that load up the appropriate dependencies. You can then ship the entire thing in a zip file as a runnable application that doesn't require any installation except for unpacking.

Actually creating the bundle can be a little finicky, because ``easy_install`` has a tendency to prefer things on the local machine even though it shouldn't.  Probably it would be best to run this inside a virtualenv; when you are done you can also feel more confident that you've actually included all the dependencies (if you use ``--no-site-packages`` when creating the virtualenv).

Anyway, while both of these are a little incomplete I'm feeling optimistic about them, and I'm hoping intrepid souls can give feedback on how they work.

**Update:** virtualenv 0.8.2 is out, featuring Better Error Messages (and nothing else).  Still doesn't work on Mac Framework Pythons, or Windows.  You'll have to keep using workingenv there -- but patches extremely welcome!  Contact me if you are interested in supporting these platforms.  It will involve some digging, but maybe we can just do the digging once for everyone.

**Update 2:** virtualenv 0.8.3 is out, featuring Windows!
