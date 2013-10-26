Doctest.js & Callbacks
######################
:date: 2010-09-12 17:08
:author: Ian Bicking
:tags: Javascript, Programming, Testing, Web

Many years ago I wrote a fairly straight-forward port of Python's `doctest <http://docs.python.org/library/doctest.html>`_ to Javascript.  I thought it was cool, but I didn't really talk about it that much.  Especially because I knew it had one fatal flaw: it was very unfriendly towards programming with callbacks, and Javascript uses a lot of callbacks.

On a recent flight I decided to look at it again, and realized fixing that one flaw wasn't actually a big deal.  So now doctest.js really works.  And I think it works well: `doctest.js <http://doctestjs.org>`_.

I have yet to really use doctest.js on more than a couple real cases, and as I do (or you do?) I expect to tweak it more to make it flow well. But having tried a couple of examples I am particularly liking how it can be used with callbacks.

Testing with callbacks is generally a tricky thing.  You want to make assertions, but they happen entirely separately from the test runner's own loop, and your callbacks may not run at all if there's a failure.

I came upon some tests recently that used `Jasmine <http://pivotal.github.com/jasmine />`_, a `BDD-style <http://en.wikipedia.org/wiki/Behavior_Driven_Development>`_ test framework.  I'm `not a big fan of BDD <http://blog.ianbicking.org/behavior-driven-programming.html>`_ but I'm fairly new to serious Javascript development so I'm trying to withhold judgement.  The flow of the tests is a bit peculiar until you realize that it's for async reasons.  I'll try to show something that roughly approximates a real test of an XMLHttpRequest API call::

    it("should give us no results", function() {
      runs(function () {
        var callback = createSpy('callback for results');
        $.ajax({
          url: '/search',
          data: {q: "query unlikely to match anything"},
          dataType: "json",
          success: callback
        });
      });
      waits(someTimeout);
      runs(function () {
        expect(callback).toHaveBeenCalled();
        expect(callback.mostRecentCall.args[0].length).toEqual(0);
      });
    });

So, the basic pattern is ``it()`` creates a group of tests, and each call to ``run()`` is a set of items to call sequentially.  Then between these run blocks you can have signals to the runner to wait for some result, either a timeout (which is fragile), or you can setup specific conditions.

Another popular test runner is `QUnit <http://docs.jquery.com/Qunit>`_; it's popular particularly because it's what jQuery uses, and my own impression is that QUnit is just very simple and so least likely to piss you off.

QUnit has its own style for async::

    test("should give us no results", function () {
      stop();
      expect(1);
      $.ajax({
        url: '/search',
        data: {q: "query unlikely to match anything"},
        dataType: "json",
        success: function (result) {
          ok(result.length == 0, 'No results');
          start();
        }
      });
    });

``stop()`` confused me for a bit until I realized what they were really referring to stopping the *test runner*; of course the function continues on regardless.  What will happen is that the function will return, but nothing will have really been tested -- the ``success`` callback will not have been run, and *cannot* run until all Javascript execution stops and control is given back to the browser.  So the test runner will use ``setTimeout`` to let time pass before the test continues.  In this case it will continue once ``start()`` is called. And ``expect()`` also makes it fail if it didn't get at least one assertion during that interval -- it would otherwise be easy to simply miss an assertion (though in this example it would be okay because if the success callback isn't invoked then ``start()`` will never be called, and the runner will timeout and signal that as a failure).

So... now for doctest.js.  Note that doctest.js isn't "plain" Javascript, it looks like what an interactive Javascript session might look like (I've used shell-style prompts instead of typical console prompts, because the consoles didn't exist when first I wrote this, and because ``>>>/...`` kind of annoy me anyway).

::

    $ success = Spy('success', {writes: true});
    $ $.ajax({
    >   url: '/search',
    >   data: {q: "query unlikely to match anything"},
    >   dataType: "json",
    >   success: success.func
    > });
    $ success.wait();
    success([])

With doctest.js you still get a fairly linear feel -- it's similar to how Jasmine works, except every ``$`` prompt is potentially a place where the loop can be released so something async can happen.  Each prompt is equivalent to ``run()`` (though unless you call wait, directly or indirectly, everything will run in sequence).

There's also an implicit assertion for each stanza, which is anything that is written must be matched (``{writes: true}`` makes the spy/mock object write out any invocations).  This makes it much harder to miss something in your tests.

**Update**: just for the record, doctest has changed some, and while that example still works, this would be the "right" way to do it now:

::

    $.ajax({
      url: '/search',
      data: {q: "query unlikely to match anything"},
      dataType: "json",
      success: Spy("search.success", {wait: true, ignoreThis: true})
    });
    // => search.success([])

There is a new format that I now prefer with plain Javascript and "expected output" in comments.  `Spy("search.success", {wait: true, ignoreThis: true})` causes the test to wait on the Spy immediately (though the same pattern as before is also possible and sometimes preferable), and in all likelihood jQuery will set `this` to something we don't care about, so `ignoreThis: true` keeps it from being printed.  (Or maybe you are interested in it, in which case you'd leave that out)

Anyway, back to the original conclusion (update over)...

I've never actually found Python's doctest to be a particularly good way to write docs, and I don't expect any different from doctest.js, but I find it a very nice way to *write* and *run* tests... and while Python's doctest is essentially abandoned and lacks many features to make it a more humane testing environment, maybe doctest.js can do better.
