A Python Web Application Package and Format (we should make one)
################################################################
:date: 2011-03-31 10:01
:author: Admin
:tags: Packaging, Programming, Python, Web

At PyCon there was an open space about deployment, and the idea of drop-in applications (Java-WAR-style).

I generally get pessimistic about 80% solutions, and dropping in a WAR file feels like an 80% solution to me. I've used the Hudson/Jenkins installer (which I think is *specifically* a project that got WARs on people's minds), and in a lot of ways that installer is nice, but it's also kind of wonky, it makes configuration unclear, it's not always clear when it installs or configures itself through the web, and when you have to do this at the system level, nor is it clear where it puts files and data, etc. So a great initial experience doesn't feel like a great ongoing experience to me -- and *it doesn't have to be that way*. If those were *necessary* compromises, sure, but they aren't. And because we *don't have* WAR files, if we're proposing to make something new, then we have every opportunity to make things better.

So the question then is what we're trying to make. To me: we want applications that are easy to install, that are self-describing, self-configuring (or at least guide you through configuration), reliable with respect to their environment (not dependent on system tweaking), upgradable, and respectful of persistence (the data that outlives the application install). A lot of this can be done by the "container" (to use Java parlance; or "environment") -- if you just have the app packaged in a nice way, the container (server environment, hosting service, etc) can handle all the system-specific things to make the application actually work.

At which point I am of course reminded of my `Silver Lining <http://cloudsilverlining.org>`_ project, which defines something very much like this. Silver Lining isn't *just* an application format, and things aren't fully extracted along these lines, but it's pretty close and it addresses a lot of important issues in the lifecycle of an application. To be clear: Silver Lining is an application packaging format, a server configuration library, a cloud server management tool, a persistence management tool, and a tool to manage the application with respect to all these services over time. It is a bunch of things, maybe too many things, so it is not unreasonable to pick out a smaller subset to focus on. Maybe an easy place to start (and good for Silver Lining itself) would be to separate at least the application format (and tools to manage applications in that state, e.g., installing new libraries) from the tools that make use of such applications (deploy, etc).

Some opinions I have on this format, exemplified in Silver Lining:

* It's not zipped or a single file, unlike WARs. Uploading zip files is not a great API. Geez. I know there's this desire to "just drop in a file"; but there's no getting around the fact that "dropping a file" becomes a *deployment protocol* **and** *it's an incredibly impoverished protocol*. The format is also not subtly git-based (ala Heroku) because ``git push`` is not a good deployment protocol.

* But of course there isn't really any deployment protocol inferred by a format anyway, so maybe I'm getting ahead of myself ;) I'm saying a tool that deploys should take as an argument a directory, not a single file. (If the tool then zips it up and uploads it, fine!)

* Configuration "comes from the outside". That is, an application requests services, and the *container* tells the application where those services are. For Silver Lining I've used environmental variables. I think this one point is really important -- the container *tells* the application. As a counter-example, an application that comes with a Puppet deployment recipe is essentially *telling* the server how to arrange itself to suit the application. This will never be reliable or simple!

* The application indicates what "services" it wants; for instance, it may want to have access to a MySQL database. The container then provides this to the application. In practice this means installing the actual packages, but also creating a database and setting up permissions appropriately. The alternative is never having *any* dependencies, meaning you have to use SQLite databases or ad hoc structures, etc. But in fact installing databases really isn't that hard these days.

* *All* persistence has to use a service of some kind. If you want to be able to write to files, you need to use a file service. This means the container is fully aware of everything the application is leaving behind. All the various paths an application should use are given in different environmental variables (many of which don't need to be invented anew, e.g., ``$TMPDIR``).

* It uses vendor libraries exclusively for Python libraries. That means the application bundles all the libraries it requires. Nothing ever gets installed at deploy-time. This is in contrast to using a ``requirements.txt`` list of packages at deployment time. If you want to use those tools for development that's fine, just not for deployment.

* There *is* also a way to indicate other libraries you might require; e.g., you might ``lxml``, or even something that isn't quite a library, like ``git`` (if you are making a github clone). You can't do those as vendor libraries (they include non-portable binaries). Currently in Silver Lining the application description can contain a list of Ubuntu package names to install. Of course that would have to be abstracted some.

* You can ask for scripts or a request to be invoked for an application after an installation or deployment. It's lame to try to test if is-this-app-installed on *every* request, which is the frequent alternative. Also, it gives the application the chance to signal that the installation failed.

* It has a very simple (possibly/probably too simple) sense of configuration. You don't have to use this if you make your app self-configuring (i.e., build in a web-accessible settings screen), but in practice it felt like some simple sense of configuration would be helpful.

Things that could be improved:

* There are some places where you might be encouraged to use routines from the ``silversupport`` package. There are very few! But maybe an alternative could be provided for these cases.

* A little convention-over-configuration is probably suitable for the bundled libraries; silver includes tools to manage things, but it gets a little twisty. When creating a new project I find myself creating several ``.pth`` files, special customizing modules, etc. Managing vendor libraries is also not obvious.

* `Services <http://cloudsilverlining.org/services.html>`_ are IMHO quite important and useful, but also need to be carefully specified.

* There's a bunch of runtime expectations that aren't part of the format, but in practice would be part of how the application is written. For instance, I make sure each app has its own temporary directory, and that it is cleared on update. If you keep session files in that location, and you expect the environment to clean up old sessions -- well, either all environments should do that, or none should.

* The process model is not entirely clear. I tried to simply define one process model (unthreaded, multiple processes), but I'm not sure that's suitable -- most notably, multiple processes have a significant memory impact compared to threads. An application should at least be able to indicate what process models it accepts and prefers.

* Static files are *all* convention over configuration -- you put static files under ``static/`` and then they are available. So ``static/style.css`` would be at ``/style.css``. I think this is generally *good*, but putting all static files under one URL path (e.g., ``/media/``) can be good for other reasons as well. Maybe there should be conventions for both.

* Cron jobs are important. Though maybe they could just be yet another kind of service? Many extra features could be new services.

* Logging is also important; Silver Lining attempts to handle that somewhat, but it could be specified much better.

* Silver Lining also supports PHP, which seemed to cause a bit of stress. But just ignore that. It's really easy to ignore.

There is a `description of the configuration file for apps <http://cloudsilverlining.org/appconfig.html>`_. The `environmental variables <http://cloudsilverlining.org/envvariables.html>`_ are also notably part of the application's expectations. The file layout is explained (together with a bunch of Silver Lining-specific concepts) in `Development Patterns <http://cloudsilverlining.org/devpatterns.html>`_. Besides all that there is admittedly some other stuff that is only really specified in code; but in Silver Lining's defense, specified in code is better than unspecified ;) App Engine provides another example of an application format, and would be worth using as a point of discussion or contrast (I did that myself when writing Silver Lining).

Discussing WSGI stuff with Ben Bangert at PyCon he noted that he didn't really feel like the WSGI pieces needed that much more work, or at least that's not where the interesting work was -- the interesting work is in the tooling. An application format could provide a great basis for building this tooling. And I honestly think that the tooling has been held back more by divergent patterns of development than by the difficulty of writing the tools themselves; and a good, general application format could fix that.
