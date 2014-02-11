Title: Introducing TowTruck
slug: introducing-towtruck
Date: 2013-04-05
Status: draft

Today we are introducing a project I've been working on for the past few months at Mozilla: [TowTruck](https://towtruck.mozillalabs.com). There's a [blog post announcing it](), but I wanted to take some time to give my own take and why I'm excited about the project.

TowTruck is a service to add real-time collaboration to any website. You put `<script src="https://towtruck.mozillalabs.com/towtruck.js"></script>` on your page, and a button to start TowTruck (`<button onclick="TowTruck(this); return false">Start TowTruck</button>`), and that's all you have to do, or at least all you have to do to get started.

Once you've done that people on your site will be able to start the TowTruck service, get a link to share with a friend, and then they'll be able to "collaborate".  I am annoyed with that word, *collaborate*: it's the catch-all word for everything on the web.  But I can't think of a better term that covers everything I want to imply.

What specifically can you do?  There's editor and form syncing, you can see each other's mouse cursors, you can chat with text and if you both have very new browsers you might be able to chat with audio using [WebRTC]().  You can collaborate on more than just that one page as well - while you aren't locked into the same page, you will be able to see where the other person is and follow along easily.

We have a lot of other features we want to include as well:

- The ability to "follow" someone, basically tracking whatever they do.

- More functionality to let applications hook into this synchronization and the communication channel we've set up.  Form fields are pretty well-understood so we can apply synchronization pretty generically, but more complicated interactions are difficult.

- We want to try to show where each person's *attention* is.  This will be somewhat subtle, but I'm excited about the challenge.  How do we show when a person is actively edit?  Or skimming a page or site looking for something?  Or waiting on the other person?  There's a body language to how someone interacts with a page and a site, and I hope we can transmit that language.

- Recording and playback.  In a mentoring or support situation, it would be great to be able to review and replay a past interaction.  I have a few things waiting in my toolchest for this one.

- Since we're working with relatively high-level events I'm hopeful that we'll be able to adjust how we display events to make them more comprehensible.  An example: you move your mouse to a link and click it.  In your head you think "there's the button, I'll just move over there and... click!" - but to the other person it's like "the mouse is moving, I think they are... wait, where we now?"  Lacking the anticipation (and perhaps attention) of the person performing the action, it can be hard to parse exactly what happened.  But we don't have to play it back exactly as it happened, with delays and highlighting I think we can make actions more transparent.

- With pair programming you often want the person who is less experienced with the task to be "driving" - if they watch over the other person's shoulder they will lose track of what's going on.  Kind of like the previous issue, except I think we could also enable a "you drive" mode.  The other person could interact with the page, but primarily pointing.  A click would mean "look here".

Because TowTruck is a service you add to your site (and that runs in the browser alongside your application code), and it's not a completely packaged program, there's a lot of opportunities for customization.  Letting someone else drive makes sense in an educational/mentorship role, but seems superfluous in other situations; but site owners and integrators have a chance to decide what pieces they'll want to enable.

Another thing that excites me about TowTruck is that we're making a lot of use of how well we can introspect the DOM.  HTML is peculiar with its
