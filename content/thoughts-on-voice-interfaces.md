Title: Thoughts on Voice Interfaces
Slug: thoughts-on-voice-interfaces
Date: 2020-08-03
Nocomments: true

I've been working on the Consumer Voice Products team in Mozilla for about a year now. My primary project has been [Firefox Voice](https://github.com/mozilla-extensions/firefox-voice), but our mandate is larger.

I still feel like a beginner in the area voice, but I have developed some opinions. Many observations are the influence of other people’s ideas, work, or research, but I’ve lost the provenance. I’ve benefited a great deal from the long and regular discussions I’ve had with my team, particularly [Abraham Wallin](http://abewallin.com), [Janice Tsai](http://www.harraton.com/), [Jofish Kaye](http://jofish.com), and [Julia Cambre](https://juliacambre.com).

1. Voice interfaces are voice _interfaces_. They are a way for the user to express their desire, using patterns that might be [skeuomorphism](https://en.wikipedia.org/wiki/Skeuomorph) of regular voice interactions, or might be specific learned behaviors. It's not a conversation. You aren't talking with the computer.
    1. I suspect you can push the user into a conversational skeuomorphism if you think that's best, and the user will play along, but it's no more right than another metaphor. It's a question of quality of interaction, not ease or familiarity.
    1. That said, speaking is an improvisation. You have something you want to say, you've probably prepared a few keywords, but the rest you make up word-by-word. Words won’t come out your mouth with grammatical precision.
1. I hate how voice interfaces force us to speak without pauses because a pause is treated as the end of the statement. Firefox Voice does the same thing, so I appreciate why it works this way. I still hate it.
    1. Typically tools operate on the granularity of an [utterance](https://en.wikipedia.org/wiki/Utterance): one statement, command, query. It's the same for conversational interfaces, just a different kind of turn-taking.
    1. Many systems use a "wakeword" or "keyword spotting" to start the interaction. What if we used keyword spotting to determine the end as well? "Please" might be a good choice. It's like the Enter key.
    1. I read a science fiction story where they used voice interfaces, and used "please" as a statement terminator as well (in a [story by Phillip C. Jennings](https://archive.org/details/Asimovs_v15n12n13_1991-11/page/n227/mode/2up) [[text only]](https://archive.org/stream/Asimovs_v15n12n13_1991-11/Asimovs_v15n12n13_1991-11_djvu.txt) <a id="footnote1-source" href="#footnote1">\*\*</a>). This also made "please" insulting, using it meant you regarded someone as no more important than a computer.
    1. Another option might be speculative execution while allowing amendments. A common example would be when you want to say "set reminder for 2pm to go to the post office" but you paused just a little too long and the assistant jumped on you at "set reminder for 2pm". Now it's going to blather on about a question (“what reminder?”), and not only do you have to wait, you have to time your response. It would be nice if the moment you said "set reminder for 2pm" the assistant would indicate (visually) "setting 2pm reminder for what?" and you might answer anytime, and if you were slow it might give an audio prompt which you could also talk over.
1. Some people think it is important that we [not abuse assistants](https://www.the-vital-edge.com/digital-assistants-abuse/). They believe abuse will make us cold or abusive to each other. I do not agree.
    1. We've also learned that people feel embarrassed when they can't get their assistant to understand them. It's different than other interfaces, as the voice makes it feel more personal and judgy. So concern over emotional impact is not misplaced.
    1. When I used a GPS in the car regularly it would continually give voice instructions. I'd miss a turn and it would constantly tell me to make a U-turn or otherwise backtrack. I'd also just _choose_ another route and it would complain. I knew I didn’t make a mistake, but I still felt judged. Then I turned off the voice and it was fine, the screen just informed me, it didn't judge me.
    1. Which is to say: I don’t think the answer is compassion towards our computers. They neither need it nor even ask for it. Instead of navigating through the uncanny valley we should keep computer and human separate. You want to cut short what your assistant is saying? Please do. Our challenge as implementers is to keep your heart from going cold by making it very clear this isn't a human and has no feelings.
    1. An aside, but [this classic video](https://www.youtube.com/watch?v=rVlhMGQgDkY) of people taunting a Boston Robotics robot made people uncomfortable (including me!). They are being such jerks! I think the answer is that we should not make robots that look like humans. You and I pass on the sidewalk, and we have to navigate cooperatively to keep from hitting each other. If I bust through you paying no attention that makes me the asshole. I don't want to have to start navigating politeness with robots too: they should step aside; if I place a hand on a robot it should stop, not be offended. I'm not polite to doors either, and this does not make me a worse person.
1. Voice is not a command-line interface. Voice ends up as text, and despite caveats... really it’s just treated as text. So it seems appealing to treat it like a command line interface, but no...
    1. Accuracy is a big issue. Transcription errors are common. You can recover from a lot, but I think it puts a real upper limit on how much information you can give the computer before interaction is required. Maybe you are 95% successful saying one thing. But then you only have 90% chance of saying two concepts together. If the concept is complicated then 95% accuracy is generous.
    1. If you execute something complicated using several smaller commands then you have opportunities to fix problems part way through. You'll need those opportunities. We call this “repair”.
    1. I think "undo" would be a nice capability to build into everything. It would probably be a prefix to your reparative command. Like, "no, search for nearby tacos" meaning undo last command and then do this new one.
    1. Besides accuracy, it's also mentally harder to successfully compose complex or precise sentences when speaking. Tools can ignore uninteresting words, accept multiple phrasings, put in reasonable defaults, but we can only do that once you’ve spoken. We can't boost your brain to make it easier to speak complex phrases.
    1. GUIs are a little like a discussion. You get a menu of options – buttons and controls – and micro-feedback like hover states or a depressed state, as well as macro-feedback like actual changes in the screen to indicate what happened. Trying to compose a compound voice statement can be trying to interact with a laggy UI where you outrun the screen refresh. It's frustrating by default.
    1. It's not necessarily easy to give humans compound commands either. Try accomplishing something by looking over someone's shoulder and telling them what to click...
    1. Familiarity makes it possible to talk through a task with both computers and humans. I've definitely become familiar with my Alexa, I've learned what phrases work and which don't.
    1. Short phrases are much harder for the computer to properly transcribe. Brevity is punished. The more words you use to express less information, the better it works. “Paste” is almost never detected correctly.
    1. Assuming you don't have a custom transcription language model for your application, it will be very hard to get the computer to hear what you are saying if you are required to use odd phrases or terms. It's like having a stenographer that just doesn't know anything about your domain.
    1. I do wonder if there’s something like [procedure words](https://en.wikipedia.org/wiki/Procedure_word) for voice interfaces. You’ll know these from words like “roger” and “mayday”, where there’s clear and unambiguous words to communicate vital information.
1. Voice has constraints, but it also has advantages, mostly from using language.
    1. The biggest is that you can talk about things you can't see. A GUI has to show everything you can act on (sometimes with doorways to other things)
    1. You can't see search queries. And so search is always a top use of voice! In general search is used for things you can’t see but want to find.
    1. Things-you-can't-see is also important in multitasking. You can't see the content of other tabs, and often can't see other applications. I don't think we've figured out how to unleash this, but I think there's something there.
    1. Because of the imprecision of voice everything is a search even if you wish it wasn't. So something as simple as adding a bookmark to a folder involves searching for the folder.
    1. You also can't see things that don't exist yet. I can imagine some utility in using language to create conditionals and triggers, using language’s ability to talk about something that does not yet exist. What excites me here isn’t that voice is necessarily easier, but that it’s easy to take phrases that do something now and rephrase them to talk about the future. Learning to talk about the future is implicit when learning to act right now.
1. For all the cool things one might imagine doing with natural language interfaces, right now it's all imperative commands.
    1. This is in part a human’s relationship with the computer. You don't care what the computer thinks, you don't need to theorize on what will happen or give it reassurance, you just tell it what to do.
    1. Conveniently English imperatives are simpler than most other sentences. This is probably no coincidence, as an imperative is designed to be understood and acted on unambiguously.
    1. But there may be something useful about using voice to create descriptions in parallel with other activities. For instance some researchers have found a benefit in having the user describe their actions while a recorder sees the concrete (but noisy) clicks and movements.
    1. Maybe tagging and organization are useful voice tasks, to be done in parallel with other non-voice navigation. Voice could be a layer on top of normal interfaces.
1. Access to microphones is hard and a big deal.
    1. There's lots of very reasonable privacy concerns.
    1. Like many privacy concerns, they are solved by making things harder for everyone.
    1. Analog hardware is just difficult to handle, different hardware performs differently, things cut out or fail over time.
    1. Custom hardware, like in the Alexa, makes really useful improvements.
1. The big-bag-of-intent-handlers approach to parsing causes some problems
    1. As far as I can tell every system uses some form of categorization/classification, mapping a phrase to a handler. There’s always overlap, so you have to decide which handler is best.
    1. Given variable inputs (search query, artist name, etc), mistranscriptions, and stopwords, the complete space of inputs is hard to enumerate.
    1. As a result adding new handlers can have unexpected results, throwing the balance of the system off. I’ve been unimpressed with the extensibility of most assistants, but it’s understandable.
    1. You can imagine always preferring native handlers to extension handlers, but that’s not great either. You want the handlers to be fairly broad, and it’s likely new handlers will be a refinement on functionality that’s merely a best-effort fallback for the default handlers.
1. Apparently the vanguard of technology are now marketing agencies.
    1. Growth in these areas seems to be driven by someone saying "you know, voice is the future..."
    1. The marketplaces for voice assistant skills are pretty awful for both consumers and producers. Consumers find junk, producers can't find an audience.
    1. Media outlets are the exception, but only because they are providing content instead of an interface.
    1. Everything people do with an assistant seems stable and frozen. People do factual searches, weather, timers, reminders, and turn on and off lights.
    1. The amount of technology we're bringing to bear on a replacement for The Clapper is impressive.
    1. Voice assistants, home and otherwise, are successful, but they are not successful ecosystems.
1. It's neat that people tell you exactly what they want to do.
    1. If you try to understand a GUI from behavioral telemetry you have to figure out why maybe someone hit a button and then canceled and tried a different button, and that maybe implies they wanted to do something that isn't directly exposed, or maybe they just misclicked, or...
    1. Because voice discovery is itself exploratory (if you want to find out if something works you should just try it), people will say what they want.
    1. Of course there's nothing that demands that an intent be clear enough to _ever_ be implementable. So you may just be exposed to desires you can never fulfill.
1. Voice doesn't mean we can create smart agents that take care of everything.
    1. Voice makes smart agents seductive because you can express a desire using natural language without specifying exactly how to accomplish the thing.
    1. You want a voice agent to buy tickets or order you dinner? No, you don't want this. This isn't going to be any more successful than asking a waiter to order for you. Maybe if you are adventurous or very familiar with the waiter it’s possible. Even in our family we're constantly asking each other questions about preference, and negotiating options for small questions, and we are _very_ familiar with each other.
1. Being able to state intentions instead of specific actions offers some opportunity to support greater focus and directed action.
    1. The way you do something with a normal GUI is you come up with the goal in your mind, decompose it into actions, and then start on the first action. Maybe open a tab, click on a button, find a document, etc. It’s easy to get lost along the way – not just confused, but also distracted.
    1. I doubt we can – or even should – just “make it happen” when there’s a complex goal-oriented statement. But even if the tool can’t easily break down a task, maybe the user can construct their own top-down outline of a task.
    1. This immediately leads to the idea you could then save the outline as a repeatable task. Instead of making it an opaque repeatable task, I suspect it would be better to make it a list, and make it easy to follow along with lists. Then the assistant says “next you did: ‘open most recent email from Joe’; say “ok” or a command…” and then maybe that’s the right next task, or maybe you say something else inspired by your past command. The assistant can provide task scaffolding instead of automation.
1. I am skeptical about learning and adaptation.
    1. Reliability – even reliably making mistakes – is an important feature. It means the user can learn about the system and adapt their behavior, without the system foiling them by changing its own behavior.
    1. Discovery is hard, and having the search space change under your feet only makes it worse.
    1. In summary: humans learn faster and better than machines. If the experience is going to grow, it needs to be explicit and deterministic, not clever or implied.
1. Voice output suffers from too much or not enough information.
    1. This is where impolite interruptions might make voice output feasible.
    1. Human voice interactions can have the same problem. We improve our communication by being in dialog with someone instead of just talking at them, and by using body language to interpret the interest of the other person.
    1. Some of the equivalents – asking for confirmation before speaking more, or allowing the person to interrupt – might suffer from taking too many cues from human interaction. The questions themselves easily take more time and effort than just presenting too much information, and the interruptions turn the interaction into something that feels hostile instead of helpful.
1. There’s “intent parsing” but not much I would consider “understanding”. There’s not much U in [NLU](https://en.wikipedia.org/wiki/Natural-language_understanding).
    1. Intent parsing means: given an utterance, pick the most likely thing your program can do; and also: pull out some variable parameters from the utterance
    1. There’s no room for understanding there. “Picking an intent handler” isn’t understanding.
    1. You can only have understanding if you also have a knowledge model. Some flat JSON with some labels isn’t a model. Models in turn need to be attached to functional results: stuff the assistant can actually do.
    1. I don’t know what understanding looks like, or what those models will look like. And I’m not even sure I’ll recognize them when I see them, it’s possible even in the code they’ll be implied.
    1. As an aside, I personally believe action and meaning and understanding all go together: meaning only exists when we can attach it to effects, and abstract understanding is backfilled. So models without handlers aren’t meaningful, and models that are only handler references aren’t models.
1. We could use more orthogonality. That is: meaningful phrase modifiers and statements that can apply across a wide variety of actions or application functionality.
    1. Orthogonality allows a user to come up with creative and unpredicted combinations in a phrase, and for those to actually work.
    1. The simplest form of this I’ve thought about is a simple verb/direct-object with a simple set of modifiers.
    1. Another way to think about it might be akin to [composability](https://www.ianbicking.org/blog/2018/02/web-small-composable-tools.html).
1. Discovery is naturally hard.
    1. Natural language commands don’t need to be organized into hierarchical structures of menus or screens, which is nice but doesn’t lend itself to navigation.
    1. Periodically showing the user some examples seems to be the state of the art. Sad.
    1. I feel like something might be possible with cuing. I am reminded of a small anecdote from Logo, where when you type something that isn’t defined (e.g., SQUARE) it will reply <code>I don’t know how&nbsp; TO SQUARE</code>, hinting in the error message what you should do next (`TO PROC` defines a procedure). Doing this requires a cleverness in the language design that has not revealed itself to me.
    1. Besides errors, any output (speech or text) is an opportunity to use language that suggests what phrases can be used. It’s a chance to encourage the user to mirror the computer’s language.
    1. The big bag of intent handlers approach means there’s no natural comprehensibility to the space of phrases and abilities. By pursuing “natural language” we create a very sparse space of successful phrases amid the entirety of possible language. Is it predictable?
1. Intents tend to be dominated by verbs, but I think we might do better leading with nouns.
    1. The parsers tend to focus on the constant bits, the verbs: “**play** [artist]”, “**send message to** [recipient]”.
    1. This maps to a call like `sendMessage(“Emily”, “On my way home”)`. But maybe it should map to something like `search(“Emily”).sendMessage(“On my way home”)`
    1. The point being that you want the intersection of “entities called _Emily_” and "entities that respond to _sendMessage_”.
1. STT (speech to text) and TTS (text to speech) are terrible terms.
    1. I have to _think hard_ to get the right one. Every time.
    1. I prefer “speech/voice transcription” and “speech/voice generation”.
1. Twenty seems like a good round number for a conclusion.
    1. It feels like there’s two paths before us: structured and unstructured understanding. Both ultimately lead to structured understanding, humans construct syntactic and meaningful structured statements. Is the bridge to that a structured pidgin, or an unstructured statistical understanding?
    1. Fundamental user interface standards in voice are still mysteries to us. Will a radical change and consolidation happen like with [WIMP](<https://en.wikipedia.org/wiki/WIMP_(computing)>)?
    1. A whole new level of expressivity _might_ be revealed by voice interfaces. But I don’t think we know what that kind of relationship with a computer should look like. Current voice UIs are imperative just like graphical interfaces are imperative.
    1. The details all matter: failures in speech recognition, different listening modes, microphone access and quality, output length and intonation, and all that ignores the actual _functionality_ of the thing you are interfacing with, which also will require changes.
    1. This clearly is going to happen, but I’m not at all certain the next shift will be centered on voice, or centered on something else and happen to include voice. As an analogy, touch interfaces enabled important changes… but touch interfaces themselves aren’t important.

Comments on [Twitter](https://twitter.com/ianbicking/status/1290310037198516227) or [Hacker News](https://news.ycombinator.com/item?id=24040539).

---

<blockquote><p><a href="#footnote1-source" id="footnote1">**</a> From <i>The Fourth Intercometary</i> (a story I enjoyed and would recommend!): "Director Lester Bragolio stepped out of seclusion, clad in tunic, breeches and slippers, hairbrush in hand. He spoke while combing his tousled white hair. 'Would you bring up the navscreen, please? Ten degree radius?'</p><p>"The Tipsy Witch held faithful to Yossi’s voice. He said 'Navscreen A, grid out from Gledhill, ten degree radius.' Only then did the monitor come to life. 'False color, please,' Yossi instructed. His own 'please' meant 'end of command.' Language changed when one talked to machines. Spoken as the Director said it, the word almost signified: you are the same to me as some piece of equipment."</p></blockquote>
