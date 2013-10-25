What PHP Deployment Gets Right
##############################
:date: 2008-01-12 13:16
:author: Ian Bicking
:tags: Programming, Python, Ruby, Web

With the recent talk on the blogosphere about `deployment <http://blog.dreamhost.com/2008/01/07/how-ruby-on-rails-could-be-much-better />`_ (and `for Django <http://www.b-list.org/weblog/2008/jan/10/hosts />`_, and lots of other posts too), people are thinking about `PHP <http://comments.deasil.com/2008/01/11/lessons-to-be-learned-from-php />`_ a bit more analytically.  I think people mostly get it wrong.

There are several different process models for the web:

1. CGI, where every request creates a new process, and the process handles only one request.  (You could also fork a new process each request with mostly the same result.)

2. Worker processes, where a process handles one request at a time, but the process is long-lived and will handle another request after finishing the first.

3. Threaded, where a process handles multiple requests, each in its own thread.  Threads may or may not be reused (depending on whether you use a thread pool), and that's kind of like the difference between CGI and worker processes.  But it's not a big difference because either way the process is long lived, including all your objects.

4. Asynchronous, where a process handles multiple requests without threads.  Typically your code is event driven: a request is an event, but so are things like "database results returned", or "file read from disk".  Code takes the form of short snippets between these events.

What people don't realize is that PHP is effectively a CGI model of execution.  People don't appreciate this because PHP is implemented with mod_php, an Apache module.  There are many other modules like mod_perl (the first of these mod_language modules), mod_python, mod_ruby, etc.  None of these other modules are like mod_php.  This has led `many a commentator astray <http://www.rubyinside.com/no-true-mod_ruby-is-damaging-rubys-viability-on-the-web-693.html>`_ because they don't get this.  This is because the PHP language *was written for* mod_php.  Perl, Python, Ruby -- none of them were written to be used as an Apache module.  You can't take one of these existing languages and just retrofit it to be like PHP or like mod_php.

Why is it important that PHP has a CGI like model?  Mostly because it lets two groups separate their work: system administration types (including hosting companies) set up the environment, and developer types use the environment, and they don't have to interact much.  The developers are empowered, and the administrators are not bothered.

Some details:

* PHP processes can leak memory like crazy.  It doesn't matter because they only leak memory for one request.

* PHP processes can be easily killed if they act badly (sucking up too much memory or if they get caught in an infinite loop).

* PHP code has no global state.  It has lots of global variables, but since they only live for one request they are relatively harmless.  (Not entirely harmless, but what's a major sin in another language is only a minor sin in PHP.)  The process cannot become corrupted.

* There's no global set of installed libraries (besides what PHP is compiled with).  If you want to include a library you include files, typically relative paths.  You won't include someone else's library accidentally.  (This has changed in PHP, but the search path remains largely unused.)

* Most of the language is implemented in C, in a shared library.  In comparison Python has "batteries included", but those batteries are largely written in Python.  Python code is not shareable, and can take time to load up.  So while a single Python CGI script might be small, it probably imports lots of code which would have to be loaded each request.  PHP scripts actually are small.  (Stuff like `PEAR <http://pear.php.net />`_ changes this by adding substantial libraries written in PHP, but also seriously effects PHP performance.)

* What few system-dependent libraries and C extensions that are required are compiled into PHP, and hosting companies have kind of figured out a consistent set of these libraries (stuff like database drivers, an image processing library, and XML parsing).  Individual developers write only PHP (and that's all they are typically allowed to write).

These features are all contrary to the design of these other languages, and even more contrary to the *conventions* in other language communities.  Python programmers *could* write all their libraries in C and start to make CGI scripts feasible, but they don't and they won't.

Focusing on mod_php is a goose chase.  You have to focus on the features it provides.

Here's the features I think are important:

* The failure cases are isolated.  Processes never get wedged.  One user doesn't take out another user's application.  Even one bad page in an application won't take out the entire application.

* File-based deployment.  There isn't a build process for deploying a PHP application.  You put the files in the right place and they are deployed.  (Configuration in PHP is fuzzy, but PHP is not perfect.)

* Minimal global dependencies.  If you use libraries then you package those libraries with your application.  You don't worry about the administrator upgrading something on the system and breaking your application.  (At least not much, there still things like upgrading mod_php that can break your application, or changing settings in php.ini.  PHP is not perfect.)

* It's pretty easy to do multiple deployments for development.  You just drop another copy of the files somewhere else and change your database settings.

And of course the high-level features:

* Working applications stay working.  (Even half-working applications at least stay half-working.)

* Administrators aren't being hassled to make little changes and fixes all the time.

* Developers can do what they need to do without going through the administrators.

People or organizations that are hybrid developer/administrators `don't care about this so much <http://www.loudthinking.com/posts/21-the-deal-with-shared-hosts>`_. And that makes sense; this is all about separating those two roles.  Though even developer/administrators would benefit from a better story here because it would let them concentrate more on being developers and the administration part will start taking care of itself.

Solving this is all the harder because of how it interacts with the language itself.  But it's not impossible.  Process model 2 -- worker processes -- are feasible for most languages.  You just need a really good process manager (including process setup for isolation, and process monitoring to mitigate problems).  Apache *alone* is not this manager.  `mod_fastcgi <http://www.fastcgi.com />`_ *could* be this manager, but it's not.  Maybe `mod_wsgi <http://www.modwsgi.org />`_ will become this manager for Python.
