Fast CGI that isn't FastCGI
###########################
:date: 2007-08-03 15:33
:author: Ian Bicking
:tags: Programming, Web

There's a bunch of techniques for doing deployments of long-running processes (Zope, Python server, Rails, etc).  A pretty good technique is to do HTTP proxying.  There's some details and conventions I'd like to `see for HTTP <https://ianbicking.org/http-proxying-questions.html>`_, but that's not my concern here.

HTTP proxying isn't great for commodity hosting.  Mostly you need to set up a new long-running process, and commodity hosts don't make that easy or reliable.  `FastCGI <http://www.fastcgi.com />`_ offers one solution to that, essentially putting the process management into Apache or whatever web server you are using.

The problem with FastCGI is that it is finicky.  There's lots of configuration parameters, lots of parts don't work right, and there seems to be a golden path where things actually work but it's hard to know exactly what that is.

Another technique that has been used in the past instead of FastCGI is a very small CGI script.  One example in `SCGI <http://python.ca/scgi />`_ is called `cgi2scgi <http://quixote.python.ca/scgi.dev/cgi2scgi.c>`_.  This small script is fast to run (it compiles to 12kb), and all it does is take the CGI request and turn it into a SCGI request to a long-running server.

This is a nice start, and easy to deploy, except it doesn't handle long-running processes.  A great feature to add to something like this would be simple process management.  I imagine something where if the socket (named or a port) that the ``cgi2scgi`` script connects to isn't up or working, it runs a script that will start the server.  If another request comes in while the server is starting up, it shouldn't try to start the server twice.  If the server is randomly killed (as is common on commodity hosters) then the next request will try to bring the server up.

Unlike FastCGI, this won't try to handle different process models or anything fancy.  It's up to the startup script to set everything up properly, start multiple worker processes if necessary, etc.  There's probably some tricky details I haven't thought of, and it's slightly annoying to write all this in C (but necessary, since it's part of the CGI script, which must be small).  But I think it can be done better than existing in-the-wild FastCGI implementations.

And when we're done, I think we could have something that would be a really good basis for commodity hosting of a whole bunch of non-PHP frameworks.  You can distribute the Linux binaries, as all the Commodity Hosts That Matter can run those (even the BSD ones should be fine).  Easy application installation practically falls right out of that.
