A Simple CMS
############
:date: 2008-02-05 22:03
:author: Ian Bicking
:tags: Web

A while back I was reading `this post <http://m.odul.us/2007/11/01/simpler-cms>`_ about creating a simple CMS in Grok.  Similar to the author over there I often get questions from friends and family who want to build a simple website about what I'd recommend.  I still haven't figured it out.  Most of the big names (Plone, Drupal, etc) feel too big and complex and not content-oriented enough.  On the other hand, simple systems like Google Homepages are more like HTML editors and don't really help with managing *content*.

I have a vision for something much, much simpler; but I'm not sure it's a realistic vision.  There's always feature creep.  If you implement something simple, what happens when someone wants something more complicated?  Do you have to throw it out?  That sucks.  Do you have to implement the new feature?  That's not very simple.

Here's what I wish existed:

* Just edit content.  Static files.

* Probably edit content that is slightly dynamic.  Probably PHP code, but without getting too fancy with the PHP.  E.g., put ``<?php include('header.php') ?>`` at the top of each file along with a footer and some variable assignments (like ``$title``).

* Pages would have simple parent/child relationships.

* Sidebar navigation would be mostly manually managed.  It would be a single PHP file, like any other.  The parent/child relationships would help inform and automate aspects of that generation, but only on the UI side.  There would be no attempt to incorporate fancy navigation algorithms.

* The fancy things would be done with Javascript.  For instance, if you want to expand navigation depending on the context of the site.  This would be easy enough to implement in Javascript, serving everyone the same content and rendering it just slightly differently to emphasize context.

* Of course it would include the *important* stuff like versioning and staging.  With a file-oriented system you could use an existing version control system, or just simple archiving.

At my `last job <http://imagescape.com>`_ we wrote a content management system, and one of the last features I added I found really clever; a kind of `coding judo <http://www.37signals.com/svn/posts/312-lingo-judo>`_.  We wanted to add structured page types -- things like a news feature with dates summary paragraphs.  Instead of adding a fancy structured page system (akin to `Archetypes in Plone <http://plone.org/products/archetypes>`_) I just had the system look for an edit form alongside where the page would go (which itself is just a static file).  The edit form has the necessary fields, and when you save the page each field turns into a variable assignment.  Then there's a template that uses these assignments.  In PHP you'd have something like this::

    <? include('header.php'); ?>
      <h1><? echo $page_title; ?></h1>
      Posted on: <? echo $page_date ?><br>
      <blockquote><? echo $page_summary ?></blockquote>
      <div class="article"><? echo $page_article ?></div>
    <? include('footer.php'); ?>

The edit form::

    Title: <input type="text" name="title"><br>
    Date: <input type="text" name="date"> (YYYY-mm-dd)<br>
    Summary:<br>
    <textarea name="summary"></textarea> <br>
    Article:<br>
    <textarea name="article"></textarea>

You would use Javascript to make this form fancy if you were so inclined; adding client-side validation (clients were trusted to submit valid data) or marking things for a WYSIWYG editor (usually just with ``class="wysiwyg"`` and rely on `unobtrusive Javascript <http://en.wikipedia.org/wiki/Unobtrusive_JavaScript>`_ to enable it).  

For new pages you just give the form.  For editing a page you use `htmlfill <http://formencode.org/htmlfill.html>`_ to fill in the form with existing values.

The thing that is saved looks like::

    <?
    # This page is automatically generated; do not edit directly!
    $page_title = 'A Title';
    $page_date = '2008-01-11';
    $page_summary = 'A summary\netc';
    $page_article = 'The Article';
    include('article.php');
    ?>

The system would know how to parse variable assignments (to get values) and would parse the ``include`` statement to determine what editor would be used.

Extending this system required a knowledge of HTML and HTML forms, and a little knowledge of PHP (or `SSIs <http://httpd.apache.org/docs/1.3/mod/mod_include.html>`_ would also work).  It fit our company well, as there were quite a few people with that kind of knowledge who would interact with clients, and wouldn't need to come to the programmers to extend the system.  While I'd offer some advice on how to use the system, it was transparent enough that they could debug problems on their own.

This whole concept is not something I can justify spending time on, but it's a CMS that I wish existed.  It's a CMS I could recommend to my friends.

