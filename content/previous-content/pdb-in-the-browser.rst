pdb in the browser
##################
:date: 2008-05-16 12:03
:author: Ian Bicking
:tags: Python, Web

People have asked me a few times about `evalexception <https://ianbicking.org/ajaxy-exception-catching.html>`_ and `pdb <http://python.org/doc/current/lib/module-pdb.html>`_ -- they'd like to be able to use something like pdb through the browser, stepping through code.

The technique I used for tracebacks wouldn't really work for pdb.  For a traceback I saved all the information from the frames -- mostly just the local variables -- and then let the user interact with that through the browser.  But with pdb you pause the application part way through waiting for user input, and the routine only completes much later.

While writing `WaitForIt <http://pythonpaste.org/waitforit />`_ I played around with techniques to deal with very slow WSGI applications.  Not that hard, really -- you launch every request in a new thread, and you manage those requests in an application of its own.  So I started thinking about pdb again, and it started seeming feasible.  Whenever the app reads from stdin it goes into an interactive mode, showing you what comes out on stdout and letting you add input to stdin.  It's nothing specific to pdb really.

So, with a bit of hacking, I added it into `WebError <http://pypi.python.org/pypi/WebError />`_ (which is an extraction of the exception handling in `Paste <http://pythonpaste.org>`_).  To give the demo a try, do::

    hg clone http://knowledgetap.com/hg/weberror/
    cd weberror
    python setup.py develop
    # You need Paste trunk:
    easy_install Paste==dev
    python weberror/pdbcapture.py

What you'll see is not polished, it's just working, but since I mostly did it to see if I could do it, that's good enough for me.
