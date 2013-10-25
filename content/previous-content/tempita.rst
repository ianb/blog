Tempita
#######
:date: 2007-08-06 16:50
:author: Ian Bicking
:tags: Programming, Python

I mentioned a templating language I put into Paste `a while ago <http://blog.ianbicking.org/what-im-up-to-jun07.html>`_, but since then I extracted it into a separate package called `Tempita <http://pythonpaste.org/tempita />`_.  I think the documentation is fairly complete (it's a small language), but I'll describe it shortly here.

I wanted a text-substitution language, because I wanted something to be used to generate Python files, config files, etc.  I also didn't want a complex API, with search paths and components or something that interacts with import machinery, or any of that.  `string.Template <http://python.org/doc/current/lib/node40.html>`_ is *almost* good enough, but not quite.

I started with the idea of something vaguely like `Django Templates <http://www.djangoproject.com/documentation/templates />`_, though since I didn't care about more advanced templating features like blocks that didn't apply to my use cases.  You do variable substitution with ``{{var|filter}}``, and there's no escape character, and that's about where the similarity ends.

I realized there was no real reason to use anything but ``{{...}}``, so it's just ``{{if expr}}``, ``{{endif}}``, etc.  There's an escape for arbitrary Python, similar to how Kid does it -- you can have blocks of Python code, but the Python code can only prepare variables and functions, it can't write anything.  I think this gives a nice escape for complex logic (for times when you can't put the logic in a ``.py`` file), without the jumbled mish-mash of languages like PHP where you can trully mix functions and output.

Because it allows Python expressions everywhere, special tags don't seem so necessary.  Instead you can just provide functions to do whatever you need.  I wrote `a couple little ones <http://pythonpaste.org/tempita/#bunch-and-looper>`_ as a start.  There's a few things that are awkward still, because there's no way to define a block of template as a function, or pass the output of a block to a function.  I haven't actually needed these yet, but I can *imagine* needing this (e.g., when creating nested structures).

I wouldn't suggest using this templating language in a web application, but I think it can be quite helpful for all the cases where you have to generate text and you *aren't* writing a web application (e.g., a `Framework Component <http://www.groovie.org/articles/2007/02/11/wsgi-middleware-isnt-middleware-time-for-better-language>`_).  In my experience the web templating languages tend to be complex to invoke and understand in these contexts (and `Buffet <http://projects.dowski.com/projects/buffet>`_ unfortunately doesn't help in my mind, as it's loading system is so vague).  
