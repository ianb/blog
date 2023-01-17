Title: Thoughts On Voice Interfaces Part 2: LLMs
Slug: thoughts-on-voice-interfaces-2-llms
Date: 2023-01-17
cover_image: voice-header.png
header_style: color: #fff; padding-left: 50%;
header_inner_style: color: #fff;
header_cover_image_style: margin-bottom: 1em; background-color: #000;

Over two years ago I wrote [Thoughts On Voice Interfaces](https://ianbicking.org/blog/2020/08/thoughts-on-voice-interfaces.html), a scattering of ideas about voice interactions. Time has passed, I've been working more on voice interfaces, and though products in the market have barely changed, I still have **NEW THOUGHTS**.

## Large Language Models

I've only been exploring large language models for a couple months, and limited to GPT-3, but most of this post will be about LLMs.

I've included examples of prompts and outputs in this section. Click `⊕ Example` to see the examples, all screenshots of the [GPT Playground](https://beta.openai.com/playground).

1.  With the addition of Large Language Models (LLMs), especially GPT-3, I believe everything will change. But not quickly, there's a huge amount of implementation and experimentation and finding and fixing problems.
2.  Existing systems are based on intent categorization and entity extraction:
    1.  You have a bunch of commands, the commands take certain kinds of arguments (song title, time span, search query, etc).
    2.  Any utterance is compared to examples and categorized as a command, and the arguments ("entities") are extracted.
    3.  This isn't just an implementation detail, but also forms the basic shape of voice interactions. Voice interactions work the way they do because this is the technology we have (until now). This command-based model is not begging for LLMs, though it could probably increase accuracy.
3.  If you plug voice into a GPT-3-driven interaction you'll find it's very sensitive to speech recognition inaccuracies.
    1.  In the traditional categorization model it will naturally ignore many inaccuracies because it's just trying to find the best match among a finite set of commands and examples.
    2.  That is: the traditional model tries very hard to keep the conversation on the rails, and one inaccuracy won't make you jump to another rail.
    3.  The beauty of an LLM is that we might not need rails, that we can make vastly more capable agents that can operate on a much wider set of input.
    4.  The danger of LLMs is they take things very literally, and are very credulous. You want to know _what's next on my caliper_? It will try very hard to come up with a creative answer instead of figuring out you were asking about your calendar.
    5.  I'm sure this isn't a fatal flaw, but it's a challenge right now.
4.  LLMs are stereotyped as text _generators_, but they are also great at _understanding_. Two years ago I complained there's no "understanding" in "natural language understanding". That will change.
    1.  We still have to remind ourselves that what it's doing is not "understanding" as we know it; when an LLM responds to something there isn't an entity underneath that is understanding things.
        1.  The understanding is when we fuse that a person's input with meaningful output or action. When we ground the model in some purpose.
        2.  [Prompt Engineering](https://en.wikipedia.org/wiki/Prompt_engineering) is an important part of that fusion: adding context to the input and interpreting the output. These shells we create are an embodiment of AI, what turns a mechanism (an LLM) into a meaningful entity.
    2.  Some understanding will be inference: being able to contextualize and make reasonable assumptions about what the a person means. This is what people pay a lot of attention to when talking about "understanding," though I think it's over-emphasized. [Example][1]
    3.  Much of understanding will be translation: taking our speech and translating it into an actionable form.
        1.  We see this currently in GPT's code generation. You can ask GPT for concrete answer but it's also very good at writing down the steps by which you can get an answer. [Example][2]
        2.  "The steps by which you can get an answer" is another way of saying "a program". We will be programming our agents and getting our agents to generate programs. [Example][3]
        3.  You won't see the programs of course. Mostly. GPT is also pretty good at turning code into natural language. I expect this round-tripping will be useful in debugging our agents, something we'll probably have to do individually from time to time. The same way we ask another person to repeat our instructions to make sure we're clear, we may ask our AI agents to do the same. [Example][4]
        4.  What's the programming language that our personal agents will be generating based on our commands? Probably something new, probably accidental, maybe the product of implicit negotiations between developers and the large language models, each of which is going to try to satisfy the other.
5.  The LLM "prompt" is more than just a command for the LLM. It's instruction and goal-setting and things we haven't yet discovered. But it's especially _context_.
    1.  We haven't been providing this context to intent parser or to speech recognition itself. What context we've been giving is mostly internal implementation details, not accessible to language understanding. That will have to change.
    2.  Consider a case like sending a message to a contact: this often involves the difficult vocabulary of people's names. We may solve this generally by personalizing models so they work better with individualized information like your list of contacts. But with an LLM we can include that information in the prompt or context, much more casually and contextually than most personalization. [Example][5]
    3.  This represents an alternative to how we usually think about "learning" in voice interfaces, which is about frequency and probabilities. There's a lot of ideas about how to predict what the user will do and then bias the result based on that, or change the interface to make the likely thing easier, or even to do something proactively for the user. This is not that!
    4.  Armed with many predictive capabilities I think we've been projecting prediction onto human-to-human interactions where it doesn't exist. Your favorite barista does not actually make the coffee before you arrive. And even if they ask "the regular?" they are picking up the thread of past interactions and past conversations, not just predicting what you'll have. Prediction removes the autonomy and self-direction of the user. If there's a predictive analog in human-to-human interaction it's probably in how we stereotype each other and our respective roles, not in how we communicate.
    5.  LLMs _love_ context. In your conversation you're building a transcript. It doesn't stop you from wandering, but it's always ready to build off that previous context.
    6.  We'll have to figure out when to forget and when to erase context. GPT has a fixation problem where it will sometimes persistently attend to an unimportant detail in a conversation. [Example][7]. And as we support longer conversations and relationships that happen over days and months, we will have to think about how to keep the model's focus aligned with the user's mental model and focus.
6.  Follow-up and refining commands will be much easier with LLMs. Maybe everything will feel a little like a chatbot, though for functional and not personality reasons. People will become used to refinements that we've been self-censoring because we don't believe they are possible. [Example][8]
7.  A mind-bending part of building a chat interface directly on GPT-3 is that you have to create archetypes and entities from scratch.
    1.  There is no "you" and "me". "You" is a character that has to be introduced and described to the LLM. Armed with a description the LLM will then predict what this entity might do. The LLM doesn't "pretend" to be "you" as there is no underlying personality. And "me" (the human) is again an introduced entity. Without constraints the LLM will gladly predict _both_ sides of the conversation. [Example][10]
    2.  Maybe there's something cool that could be done by making it a conversation between me and me: that is, modeling the interaction on internal dialog. [Example 1][11] [Example 2][9]
8.  It's a fun party trick to make GPT-3 say things in the style of [The Bible](https://twitter.com/tqbf/status/1598513757805858820) or [Jar Jar Binks](https://twitter.com/goodside/status/1562991379915341824), but it's more than that...
    1.  Asking GPT to write something for a kindergartener is great. Maybe that should even be a standard starting instead of "normal" output. [Example][12]
    2.  Asking it to write for speech output could work, though I haven't had much success in my brief experiments. I don't know what to ask for, and I'm not sure what "good for speech output" really means. Some people have had good success with [SSML generation](https://twitter.com/ramsri_goutham/status/1612818789858697216).
        1.  Adjustments to the output are very amenable to user override: changing the tone to be more brief, emphasize certain points, etc. These kinds of adjustments can be done without introducing combinatorial complexity. [Example][13]
    3.  Given the right chat context for an individual, and enough quantity, I'm guessing an LLM may naturally adopt the user's phrasing and language style. Though I wonder if people naturally [code switch](https://en.wikipedia.org/wiki/Code-switching) to speak in a "formal" style with voice interfaces. ("Naturally" may be learned behavior to avoid speech recognition errors, or it might also be based on the mental model we have about our relationship with the AI agent.)
9.  I'm optimistic about the novel way you can compose text in ChatGPT, by acting more as an editor than an author, and how this will be applicable to voice...
    1.  If ChatGPT writes something for you and you want to change it, the best way is usually to ask for the change. "Make it shorter," or "take out the part about Jar Jar Binks." [Example][14]
    2.  This is also a good way to edit with your voice. Referring to specific sentences or paragraphs or describing mechanical changes is very hard to do with voice. It's hard to compose those edits in your head, and it's hard to say them accurately. GPT is quite good at editing text that is human generated. [Example][16]
10. I think there are entirely new patterns of interaction possible with LLMs
    1.  Instead of commanding, maybe you speak to your AI agent freely; the emphasis is just to dump a lot of stuff into it. Then you start using that accumulated information as the basis for action. [Example][17]
    2.  Maybe it's less transactional, less modal. You could be asking it to do something and then instead of pausing and waiting for it to do the thing you could just... keep going. The AI starts to assemble a plan for complicated actions, while still immediately acting on things that are easy and low-impact, though also respecting any higher-level instructions like ordering or conditionals. [Example][18]
11. GPT and probably all LLMs are fairly expensive, more expensive than any of the current techniques.
    1.  Hopefully this stuff gets cheaper, not because compute gets much cheaper but because smart people just figure things out. But there may be a hard lower bound on the cost.
    2.  It's possible to select different models and approaches in different contexts, most of them more efficient; I expect very eclectic stacks to emerge.
12. When we start getting Large Language Models built on [predicting text AND behavior](https://twitter.com/ianbicking/status/1612944221199294464) I think we'll see another burst of capability.

## More Voice Thoughts

So obviously I'm personally pretty focused on the effect of LLMs, but there's more to be said...

1.  Endpointing remains a major issue. That is, deciding when the person is "done" speaking and then acting on that speech.
    1.  The idea of "done" itself imposes very specific ideas on how an interaction works.
    2.  This whole "done" thing is imposed. Every system that uses silence-based endpointing is also capable of listening a little longer, with no real privacy issue. It feels a bit like a "lalala I'm not listening to you" situation, where it's better just to not know that the user is continuing to speak.
    3.  TTS output _does_ make it difficult to leave the mic open. With the right physical device setup I assume it would be possible to quickly stop TTS when the original speaker continues to speak. Thoroughly designed and vertically integrated physical devices are not the norm, so this pattern doesn't become the norm.
        1.  I feel a sense of both optimism and disappointment about a well integrated physical device; that is a device where the microphone, speaker, physical controls, other input modalities (like an [IMU](https://en.wikipedia.org/wiki/Inertial_measurement_unit)), speech recognition, speech understanding, command execution, and output systems are all integrated for a more ideal experience. The potential is there at every level but hardware like this requires capital and the total experience requires vision. Will we have to wait for a big player to discover the vision, or for the hardware design to become more accessible for a new entrant? (I wish [Rayban Stories](https://www.ray-ban.com/usa/ray-ban-stories) were a more open environment!)
    4.  Humans have many forms of non-verbal or at least non-speech ways to indicate a desire to continue or interrupt. This is also a point of frequent errors, and requires reading other people in a way that many people find difficult. Still I think there's more room to mimic some of these patterns: the "uh" call to attention, the stare-at-the-sky please-wait gesture, the facial expression of pausing mid-sentence.
2.  Invocation remains a barrier to fluid voice interactions.
    1.  Wake words and other voice invocations like special hardware gestures are only accessible when you have control of the OS.
    2.  There aren't many tools to prototype wake words or keyword spotting. This also gets in the way of using [procedure words](https://en.wikipedia.org/wiki/Procedure_word) to control things like mic state or make markers in your voice transcript to correspond to other events. I still like the idea of procedure words but I've poor luck actually making them work.
    3.  I'm divided on purely wake-word-based initiation and hardware buttons or other ways to initiate. Using a wake word is more socially appropriate because it informs any bystanders what is happening. And if you are going to talk, why not start it by talking? But people – sometimes including myself – seem to like other controls. It also opens up some possibility for multitasking with voice. If you are in a call you don't want to use a wake word because the word will end up in the call... it can mute once you complete, but you've already said something weird.
3.  Speech recognition systems aren't just "better" and "worse", individual systems have different behavior.
    1. Though it's seldom used, I like the idea of using spelling to handle difficult-to-recognize words. That is, you might say "tee oh oh" if you want to force the system to write "too" instead of "to". But support for this is spotty and inconsistent. Systems don't frequently distinguish between explicit cases like this or spoken punctuation, and implied text.
    2. Punctuation is also handled differently, some systems mostly emit just words, others try to punctuate everything. And somehow even spoken punctuation (e.g., saying "period" for ".") is applied inconsistently in a single system.
4.  [Whisper](https://github.com/openai/whisper) is an impressive speech recognizer but it's not real time and not easy to apply to interactions.
    1.  Right now speech recognition systems usually have _partial_ and _final_ transcriptions. We've all seen the partial recognition change as we continue to speak and earlier words are corrected given later context. These represent two levels of recognition. Whisper uses an even wider window of analysis to identify a sensible sentence given the input. Maybe we could have three levels: very fast partial transcriptions, ~1 second transcriptions, and then a ~4+ second "this time it's really final" transcript? But seeing the transcript update even further back may be confusing or distracting for the user, and it may be hard to trust that errors in the not-quite-final transcription will get fixed with a little patience. And the programming is already hard to get right with just two versions of the transcript.
    2.  Whisper makes retraining seem more accessible. Are there alternatives to current microphones that get enough information to create a transcription, even if they don't get enough information to build an audio recording that other people could recognize? Like a microphone in earbuds, embedded in eyeglass temples, or something touching the nose bridge or neck... and instead of using tricks to make those microphones sound "normal," train directly on the raw data they produce.
5.  There's room for more voice consumption that doesn't have any output at all, or immediately do anything.
    1.  That isn't _just_ voice recorders. There are tools like Otter or Google Recorder that faithfully listen, but mostly just transcribe.
    2.  I've imagined a process for recording family photos and documents with voice and photos, so that your photos are directly connected with those stories.
    3.  Maybe a generalization: you can, without real time feedback, fuse voice with other input if you have a _record_ of that other input, so that you can fix mistakes later instead of relying on feedback to fix mistakes during the interaction.
6.  I'm excited about the possibility for asymmetric I/O: speaking into the AI, but presenting the results visually.
    1.  This would solve some of the all-or-nothing issue with intent parsing. It's much easier to live update something visual so the computer can show its best-effort interpretation at any time.
    2.  Screens represent a conversation between the human and the computer. The computer is showing what is possible (buttons and fields), what it knows (informational elements), the status of different inputs (cursors, dialog boxes). The standard GUI conversation with a computer is more like whiteboarding than a conversation.
        1.  Just doing voice control of our screens hasn't caught on. But these traditional GUI elements – buttons, etc – are specific to non-voice inputs. What would a GUI designed voice input look like? I genuinely don't know!
        2.  When phrased as an accessibility technology voice will be caught in this not-design-for-voice trap. "Accessibility" implies "small group of people," and "not your real audience," and "applicable to status quo software."

Comments welcome on [Mastodon](), [Twitter]().

If you've gotten this far I will also throw in here that I ([Ian](https://ianbicking.org)) am looking for a job, and maybe the best job for me is one that I don't yet know exists. I'm particularly interested in the area of large language models, new user interactions built on LLMs (especially their abilities to understand us in new ways). I'm excited about education, aiding in executive function, and human-centered interactions. [Let me know if you have ideas](mailto:ianbicking@gmail.com), I would appreciate it!

[1]: /media/voice-2/math-inference.png 'This is the most kind of "reasoning" referred to in GPT, being able to decompose and explain a formal multi-step problem.'
[2]: /media/voice-2/decomposing-steps.png "These queries are personalized, and can't be answered by GPT, but GPT can come up with a plan to answer the questions. That plan could also be reused or treated like a trigger, it's not a single concrete answer."
[3]: /media/voice-2/decode-intent-to-instructions.png "Here we take examples of typical intents and have GPT translate them into a made-up programming language"
[4]: /media/voice-2/describe-instructions-as-intent.png "We take the output from the previous example and have GPT turn those programmatic instructions back into an English description. (Note there's no shared context between these examples, these descriptions are created only from the code.)"
[5]: /media/voice-2/messaging-example.png "The beginning is context from a messaging app. Using this, as well as examples to show GPT how to format the response, it can interpret the destination for a message as well as separating those instructions from the body of the message."

[7]: /media/voice-2/question-fixation.png 'Here you can see that GPT has decided to ask the same question over and over. While GPT is good at reacting to responses that don't follow the question, in cases like these it can "learn" from its own examples to do the wrong thing.'
[8]: /media/voice-2/followups.png "Here we see how GPT will interpret following follow-ups contextually, making easy use of implied references to those earlier statements."
[9]: /media/voice-2/long-term-short-term.png "This example imagines an assistant that you talk to fairly continuously as an ongoing record of your day, thoughts, and tasks; while it also tries to ask you questions to make sure it gets all the details it will need for later."
[10]: /media/voice-2/both-sides-conversation.png "Here GPT interprets what is intended to be a chat as something closer to a transcript, and predicts both sides of the conversation in the transcript proceed"
[11]: /media/voice-2/two-self-personalities.png 'This is more attempt than example, presenting two personas (the human and AI) as two aspects of the same person. GPT is somewhat stubborn about actually using words like "I" for both sides of the conversation to refer to the same person.'
[12]: /media/voice-2/kindergartener.png "In this example we took a fairly technical description of a model, pasted it in and asked it to be summarized for a kindergartener. It loses a lot of information, but keep a general gist. Results vary considerably based on the source of the information."
[13]: /media/voice-2/summary-lengths.png "The source material for this example was a long day-by-day forecast. This shows several levels of detail and summary that can be created from that one source."
[14]: /media/voice-2/edit-make-list.png "This uses the GPT Edit API which is constrained just to these kinds of editing commands. Here it's able to understand what part of the first sentence is a list and then turn that into a formatted list and two paragraphs"
[16]: /media/voice-2/edit-pronouns.png "When we ask to make a substitution with GPT it doesn't just make a string substitution, but also all the changes that keep the text grammatically correct."
[17]: /media/voice-2/turn-voice-into-todo-list.png "Here we take a long and unstructured transcript, brainstorming tasks for the day, and use GPT to turn it into a structured to-do list"
[18]: /media/voice-2/decompose-actions.png "This is a rough example of trying to take a number of actions and turn them into a plan. A more complete example would find dependencies between actions, determine actions are timed, and which actions require confirmation, and then producing a plan based on that. GPT doesn't have to compose the entire plan if it can categorize the actions so that a more formal algorithm can produce a complete plan."

<script>
    let els = Array.from(document.getElementsByTagName("a"));
    els = els.filter((e) => e.textContent.includes("Example"));
    let activeEl;
    let overlay;
    function closeOverlay() {
        activeEl = null;
        if (overlay) {
            overlay.remove();
        }
        overlay = null;

    }
    function activateEl(el) {
        if (overlay) {
            closeOverlay();
        }
        activeEl = el;
        event.preventDefault();
        overlay = document.createElement("div");
        overlay.style.position = "fixed";
        overlay.style.height = "100%";
        overlay.style.width = "100%";
        overlay.style.top = 0;
        overlay.style.left = 0;
        overlay.style.zIndex = 9999;
        overlay.style.backgroundColor = "rgba(0, 0, 0, 0.8)";
        overlay.addEventListener("click", closeOverlay);
        const inner = document.createElement("div");
        inner.style.display = "flex";
        inner.style.alignItems = "center";
        inner.style.justifyContent = "center";
        inner.style.height = "100%";
        overlay.appendChild(inner);
        const img = document.createElement("img");
        img.src = el.href;
        img.style.maxHeight = "80%";
        img.style.maxWidth = "80%";
        img.style.marginBottom = "1em";
        inner.appendChild(img);
        const x = document.createElement("div");
        x.textContent = "✖";
        x.style.position = "absolute";
        x.style.right = "20px";
        x.style.top = "10px";
        x.style.fontSize = "200%";
        x.style.color = "#fff";
        overlay.appendChild(x);
        const caption = document.createElement("caption");
        caption.textContent = el.getAttribute("title");
        const pos = els.indexOf(el);
        caption.textContent += " " + (pos+1) + "/" + els.length;
        caption.style.color = "#fff";
        caption.style.textAlign = "center";
        caption.style.position = "absolute";
        caption.style.width = "100%";
        caption.style.padding = "1em 6em";
        caption.style.bottom = "10px";
        caption.style.backgroundColor = "rgba(0, 0, 0, 0.6)";
        overlay.appendChild(caption);
        document.body.appendChild(overlay);
    }
    for (const el of els) {
        el.addEventListener("click", (event) => {
            activateEl(el);
        });
        var symbol = document.createTextNode("⊕\u00A0");
        el.insertBefore(symbol, el.firstChild);
        el.style.textDecoration = "none";
    }
    document.addEventListener("keydown", function(event) {
        if (!overlay) {
            return;
        }
        if (event.key === "Escape") {
            closeOverlay();
            event.preventDefault();
            return;
        }
        if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
            const cur = els.indexOf(activeEl);
            const next = (els.length + cur + (event.key === "ArrowLeft" ? -1 : -1)) % els.length;
            console.log({cur, next, els, el: els[next]});
            activateEl(els[next]);
            event.preventDefault();
        }
    });

</script>
