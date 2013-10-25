Doctest for Ruby
################
:date: 2007-08-23 11:10
:author: Ian Bicking
:tags: Javascript, Programming, Python, Ruby

Finally, `someone wrote a version of doctest for Ruby <http://clintonforbes.blogspot.com/2007/08/doctest-for-ruby-and-rails.html>`_.

Recently I've been writing most of my tests using `stand-alone doctest files <http://python.org/doc/current/lib/doctest-simple-testfile.html>`_.  It's a great way to do TDD -- mostly because the cognitive load is so low.  Also, I write my examples but don't write my output, then copy the output after visually confirming it is correct.  So the basic pattern is:

* Figure out *what* I want to do
* Figure out *how* I want to test it
* Automate my conditions
* Manually inspect whether the output is correct (i.e., implement and debug)
* Copy the output so that in the future the manual process is automated (`doctest-mode <http://www.cis.upenn.edu/~edloper/projects/doctestmode />`_ for Emacs makes this particularly easy)

The result is a really good balance of manual and automated testing, I think giving you the benefit of both processes -- the ease of manual testing, and the robustness of automated testing.

Another good thing about doctest is it doesn't let you hide any boilerplate and setup.  If it's easy to use doctest, it's probably easy to use the library.

There's nothing Python-specific about doctest (e.g., `doctestjs <http://svn.colorstudy.com/doctestjs/trunk/docs/index.html>`_), so it's good to see it moving to other languages.  Even if the language doesn't have a `REPL <http://en.wikipedia.org/wiki/REPL>`_, IMHO it's worth inventing it just for this.  
