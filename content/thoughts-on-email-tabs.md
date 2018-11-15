Title: Thoughts on the Firefox Email Tabs experiment
Slug: thoughts-on-email-tabs
Category: mozilla
Date: 2018-11-15

We recently released [Email Tabs](https://testpilot.firefox.com/experiments/email-tabs) in [Firefox Test Pilot](https://testpilot.firefox.com/). This was a project I championed, and I wanted to offer some context on it.

Email Tabs is a browser add-on that makes it easier to compose an email message from your tabs/pages. The [experiment page](https://testpilot.firefox.com/experiments/email-tabs) describes how it works, but to summarize it from a technical point of view:

* You choose some tabs
* The add-on gets the best title and URL from the tab(s), makes a screenshot, and uses [reader view](https://blog.mozilla.org/firefox/reader-view/) to get simplified content from the tab
* It opens a email compose page
* It asks you what you want your email to look like (links, entire articles, screenshots)
* It injects the HTML (somewhat brutally) into the email composition window
* When the email is sent, if offers to close the compose window or all the tabs you've sent

<a href="https://testpilot.firefox.com/experiments/email-tabs"><img style="float: right; width: 300px; height: auto" src="/media/email-tabs-1.jpg" /></a>

It's not fancy engineering. It's just-make-it-work engineering. It does not propose a new standard for composing HTML emails. It doesn't pay attention to your existing mail settings. It does not push forward the state of the art. It has no mobile component. Notably, no one in Mozilla ever asked us to make this thing. And yet I really like this add-on, and so I feel a need to explain why.

### User Research origins

A long time ago [Mozilla did research into Save/Share/Revisit](https://blog.mozilla.org/ux/2015/02/save-share-revisit/). The research was based on interviews, journals, and directly watching people do work on their computers.

The results should not be surprising, but it was important to actually have them documented and backed up by research:

* People use simple techniques
* Everyone claims to be happy with their current processes
  * Everyone used multiple tools that typically fed into each other
  * Those processes might seem complicated and inefficient to me, but didn't to them
  * People said they *might* be open to improvements in specific steps
  * People were not interested in revamping their overall processes
* Some techniques were particularly popular:
  * Screenshots
  * URLs
  * Email
  * Texting
  * Bookmarks

<a href="https://testpilot.firefox.com/experiments/email-tabs"><img style="float: right; width: 300px; height: auto" src="/media/email-tabs-2.jpg" /></a>

Not everyone used all of these, but they were all popular.

The research made me change a page-freezing/saving tool (Page Shot) into what is now [Firefox Screenshots](https://screenshots.firefox.com/) (I didn't intend to lose the freezing functionality along the way, but things happen when you ship).

Even if the research was fairly clear, it wasn't prescriptive, and life moved on. But it sat in the back of my head, both email and the [general question of workflows](http://www.ianbicking.org/blog/2018/02/web-small-composable-tools.html). And once I was doing less work on Screenshots I felt compelled to come back to it. Email stuck out, both because of how ubiquitous it was, and how little anyone cared about it. It seemed easy to improve on.

Email is also multipurpose. People will apologetically talk about emailing themselves something in order to save it, even though everyone does it. It can be a note for the future, something to archive for later, a message, a question, an FYI. One of the features of Email Tabs that I'm fond of is the ability to send a set of tabs, and then close those same tabs. Have a set of tabs that represent something you don't want to forget, but don't want to use right now? Send it to yourself. And unlike structured storage (like a bookmark folder), you can describe as much as you want about your next steps in the email itself.

### Choosing to integrate with webmail

The obvious solution is to make something that emails out a page. A little web service perhaps, and you give it a URL and it fetches it, and then something that forwards the current URL to that service...

What seems simple becomes hard pretty quickly. Of course you have to fetch the page, and render it, and worry about JavaScript, and so on. But even if you skip that, then what email address will it come from? Do you integrate with a contact list? Make your own? How do you let people add a little note? A note per tab? Do you save a record?

Prepopulating an email composition answers a ton of questions:

* All the mail infrastructure
* From addresses, email verification, selecting your address, etc
* To field, CC, address book
* The editable body gives the user control and the ability to explain why they are sending something
* It's very transparent to the user what they are sending, and they confirm it by hitting Send

Since then I've come to appreciate the power of editable documents. Again it should be obvious, but there's this draw any programmer will feel towards structured data and read-only representations of that data. The open world of an email body is refreshingly unconstrained.

### Email providers & broken browsers

One downside to this integration is that we are shipping with only Gmail support. That covers [most people](https://www.statista.com/statistics/547531/e-mail-provider-ranking-consumer-usa-age/), but it feels wrong.

This is an experiment, so keep it simple, right? And that was the plan until people from marketing kept asking over and over for us to support other clients and we thought: if they care so much maybe they are right.

We didn't get support for other providers ready for launch, but we did get a good start on it. Along the way I saw that [Yahoo Mail is broken](https://bugzilla.mozilla.org/show_bug.cgi?id=1494105) and Outlook isn't supported at all in Firefox (and the [instructions](https://support.mozilla.org/en-US/kb/change-program-used-open-email-links) point to a pretty unhelpful [addons.mozilla.org search](https://addons.mozilla.org/en-US/firefox/search/?q=webmail)). That's millions of users who aren't getting a good experience.

Growing Firefox is a really hard problem. Of course Mozilla has also studied this quite a bit, and one of the strongest conclusions is that people change their browser when their browser breaks. People aren't out there looking for something better, everyone has better things to do than think about their web browser. But if things don't work people go searching.

But what does broken really mean? I suspect if we looked more closely we might be surprised. The simple answer: something is broken if it doesn't act the way it should. But what "should" something do? If you click a link and Mail.app opens up, and you don't use Mail.app, that's broken. To Mozilla developers, if Mail.app is your registered default mail provider, then it "should" open up. Who's right?

Email Tabs doesn't offer particular insight into this, but I do like that we've created something with the purpose of enabling a *successful workflow*. Nothing is built to a spec, or to a standard, it's only built to work. I think that process is itself revealing.

## Listening to the research

Research requires interpretation. We asked questions about saving, sharing, and revisiting content, and we got back answers on those topics. Were those the right questions to ask? They seem pretty good, but there's other pretty good questions that will lead to very different answers. What makes you worried when you use the web? What do you want from a browser? What do you think about Firefox? What do you use a browser for? What are you doing when you switch from a phone to a desktop browser? We've asked all these questions, and they point to different answers.

And somewhere in there you have to find an intersection between what you hear in the research and what you know how to do. There's no right answer. But there is something different when you **start from** the user research, instead of **using** the user research. There's a different sort of honesty to the conclusions, and I hope that comes through in the product.

I know what Email Tabs isn't: it's not part of any strategy. It's not part of any kind of play for anything. There's no ulterior motives. There's no income potential. This makes its future very hazy. And it won't be a blow-up success. It is merely useful. But I like it, and I hope we do more.
