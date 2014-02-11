Title: Nouning the Verb of Browsing
Slug: nouning-the-verb-of-browsing-and-activity
Date: 2013-11-05 11:34:00
Category: mozilla

I was talking for a while with [Gregg Lind](https://twitter.com/gregglind) about [TogetherJS](https://togetherjs.com) and about all the ways it *could* and *should* be cool, if we keep building out this idea.  Both to build out TogetherJS, but also the general area of [cobrowsing](http://en.wikipedia.org/wiki/Cobrowsing) (cobrowsing is where two or more people can browse the web together, each from their own device).

In the course of the discussion Gregg had an idea that I'm becoming increasingly excited about.  Can we use this to give users something new to own?  Specifically: their actions.

A side-effect of any cobrowsing tool is that you send information about what you are doing to the other person.  That's how people see what each other are doing.  Those messages are the "noun" I am referring to the title: all the actions you make become a set of messages that form a record of your actions.  There's a half-baked feature in TogetherJS where you can type `/record` in the chat window and it will pop up a window where you see a record of what you do, as a sequence of JSON messages.

<center><img style="width: 100%" src="/static/media/togetherjs-record-screenshot.png"></center>

There's a lot of chatter in that log, but still it's a relatively high-level log of actions, one that you could compress (e.g., by combining adjacent edits), filter, search, replay.

What we're really talking about is a series of events.  Not quite what TogetherJS produces, but the kind of document I'm talking about looks kind of like this:

<style>
  .user-log td {border: 1px #666 solid; padding: 0.4em;}
  .user-log {margin-bottom: 1em;}
</style>
<table class="user-log">
 <tr>
  <th>Date</th>
  <th>Type</th>
  <th>Data</th>
 </tr>
 <tr>
  <td>T+0</td>
  <td><code>load</code></td>
  <td>url: http://example.com</td>
 </tr>
 <tr>
  <td>T+0.5</td>
  <td><code>mousemove<code></td>
  <td>element: #content:nth-child(2):nth-child(1); offset: 50%, 18%</td>
 </tr>
 <tr>
  <td>T+1.6</td>
  <td><code>click</code></td>
  <td>element: #content:nth-child(2):nth-child(1)</td>
 </tr>
</table>

I.e, a list of actions.  We try to anchor actions to elements instead of absolute coordinates.  We give elements names; here I am using CSS notation, using `nth-child()` to handle elements that don't have ids. It's fairly simple.

## But Anyone Can Do This!

Actually collecting that information and creating a bunch of JSON messages isn't actually that hard.  More importantly it's not *new*. And yet a whole new category of development using this description of a person's actions has not emerged.  Why would this be any different in the context of cobrowsing?

### Information needs to be used

One of the principles of [Microformats](http://microformats.org/about) that I've most appreciated is the principle that data needs to be visible in order to be accurate.  That is, if you have an address in the body of a page, and then a hidden [RDF](http://en.wikipedia.org/wiki/Resource_Description_Framework) address alongside it, everyone will be proofreading only the visible address.

*Visibility* is not exactly what you need: you need someone to be using data in order to ensure that the data is accurate.  Someone has to *care*.  You don't view the `src` attribute on images, but you can tell when it's broken (though there's lots of things you can't tell, like when you are accidentally pointing to an offsite image – those problems are much more likely to slip through).  Real visibility is nice, though, because in addition to detecting problems it also tends to make it much easier to fix problems.  But I digress...

Cobrowsing means that something is built to actually *consume* that data.  That means we're checking the data and it means we're selecting the data that actually means something to someone else.

### Free the data from the browser and page

Browsers actually have all kinds of great information, normal developers just can't *get* any of that information.

As I mentioned, I like the concept of Microformats.  But the reality of Microformats has been disappointing.  You can't *do* anything with them.  They are just stuck in a page on the browser.  The creative remixing of that data is possible with effort, but apparently never enough reward.

Cobrowsing means always exporting that data, at least to your collaborator.  That means a really big barrier is automatically overcome.

The recorder I mention above is actually just a mock collaborator, that instead of interacting just remembers everything that happens.

## But It Makes Me Afraid!

When I talk about [TogetherJS](https://togetherjs.com) people frequently comment (with a sly wink): *this would be a great tool to spy on people with, wouldn't it?*

And in a sense, yes.  But TogetherJS doesn't do anything that a website can't do already, and which many sites actually do right now. Because TogetherJS runs in content, at the behest of the site owner, it doesn't really change what's *possible*.

With more expansive cobrowsing this starts to change.  Give people a new thing to own, and you also create a new thing that can be stolen. This might also be a justification: the harm will be in proportion to the good.

One benefit to the concrete nature of cobrowsing is that it builds awareness in people about what exactly is being exported.  When you watch your collaborator while cobrowsing, you see their mouse, inputs and edits and backspaces, new URLs they go to, etc.  It becomes clear that these are the things you are sharing.

This does not keep the tool from transmitting hidden information, which is why by principle we must implement these tools exposing only what information we need to: not because of simple conservatism, but because the information we *need* to export is also the information we present to the collaborator, and so it is the information that a user understands is being exposed.  The more thoroughly we utilize information the better the user's understanding of the scope of that information.

## And Why Is This Cool?

What, do I have to spell everything out for you?  **I'm writing this so other people come up with cool ideas.**

But anyway, a few thoughts:

* cobrowsing is really cool.  And it's a whole category of interactions, not just a single tool.

* Provides a kind of high-level recording of an interaction.  Like a screencast, but you can parse it as something other than pixels. Replaying later you can add contextual navigation, like automatic detection of "interesting" events.

* Test recording.

* Sequencing user actions alongside application state, for understanding bugs or usability issues.

* Automation: turn a series of actions into a bookmarklet to repeat those actions.

* Depending on what is exported, it could be a form of data extraction.

* As we become better at understanding these logs of activity, we can start remixing or editing them before sending them to these other tools.

* Tools that *consume* these activity logs become powerable by external sources.  For instance, the automation could take the form of an external robot producing events, but what it does would use all the same permission and auditing abilities you'd have for working with other collaborators (who, like a robot, you may only half-trust to do things correctly).

Of course a bunch of these things are being done right now.  But they aren't very accessible, they don't scale to the uninitiated, they typically lack transparency, they tend to be fragile.  And the idea of a *log of actions* isn't central to existing techniques – they typically go from capturing events directly to producing whatever the final creation is.

In the short term, given a cobrowsing tool, creating an interesting robot to collaborate with is incredibly easy.  This leaves room for people to spend their intellectual effort on doing cool stuff.

This is the kind of data I'd be excited to hack on, and I hope this article gets you thinking the same way.  Now we just have to get this cobrowsing thing going...
