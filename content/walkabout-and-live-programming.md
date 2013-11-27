Title: Live Programming, Walkabout.js
Slug: live-programming-walkabout
Date: 2013-11-27 11:30:00
Category: mozilla

There's a number of "live programming" environments used for education.  [Khan Academy](https://www.khanacademy.org/cs) is one example.  In it, you write code on the left hand side, and you immediately see the result on the right hand side.  You don't hit "save" or "run" -- it's just always running.

<center><img style="width: 100%" src="/static/media/khan-screenshot.png"></center>

There are a lot of nice features to this.  There's the feedback cycle: everything always *happens*.  Or, if you get something wrong, it distinctly *doesn't happen*.  It's similar to the static analysis we so often use -- from the simplest case of syntax highlighting (which often finds syntax errors) to code lint tools, type checking or [Intelli-sense](http://en.wikipedia.org/wiki/Intelli-sense).  Live coding takes this further and makes execution itself somewhat static.

One of the nice parts about actually *running* the code is that you aren't relying on static analysis, which is always limited.  The only thorough analysis is to model the program's execution by executing the program.  Not to mention it allows the programmer to detect bugs that just cause the program to do the wrong thing, or to be incomplete, but not clearly incorrect, not in error.  For instance, in the Khan example I make the shapes transparent:

<center><img style="width: 100%" src="/static/media/khan-screenshot-transparent.png"></center>

No static analysis could tell me that this produces an unattractive picture of a person.  Proponents of static analysis tend to have a limited concept of "bug" that doesn't include this sort of problem.

To imagine what live execution might look like when applied more dramatically, you might want to check out [Learnable Programming](http://worrydream.com/LearnableProgramming/) by Bret Victor.  Underlying all his mockups is the expectation that the code is being run and analyzed at all times.

<center><img style="width: 100%" src="/static/media/learnable-screenshot.png"></center>

That's all cool... except you can't just *run* code all the time.  It works for code that produces basically the same output every time it is run, that requires no input, that isn't reactive or interactive. This is all true for [Processing.js](http://processingjs.org/) programs which Khan Academy and the other live programming environments I've seen use (and Khan Academy even disables random numbers to ensure consistency). Processing.js is focused on drawing pictures, and drawing via code is okay, but... it doesn't excite me. What excites me about code is its emergent properties, how the execution of the program evolves. When you write interesting code you can enable things you didn't realize, things that you won't realize until you explore that same code.  What happens when you interact with it in a new order?  What happens when you give it new input?  When a program always produces the same output it makes me feel like the program could be substituted by its output. Who needs to program a drawing when you can just use a drawing program?

I was thinking about these things when I was looking at [Waterbear](http://waterbearlang.com/), which is a graphical/pluggable-tile programming language (very similar to [Scratch](http://scratch.mit.edu/)).

<center><img style="width: 100%" src="/static/media/waterbear-screenshot.png"></center>

A nice aspect of that sort of language is that you are forced to think in terms of the [AST](http://en.wikipedia.org/wiki/Abstract_syntax_tree) instead of text, because all those tiles *are* the AST.  You also get a menu of everything the language can do, including its primitive functions.

<center><img src="/static/media/waterbear-screenshot-list.png"></center>

With the language laid out like that, I saw that most of it was nice and static and deterministic.  Control structures are deterministic: `if COND then IFTRUE else IFFALSE` always executes the same code given the same input.  Most everything is: appending to a list always produces the same result, adding numbers always produces the same result.  The list of the non-deterministic building blocks of a program is *really small*.

And this is exciting!  If you can find all the non-deterministic parts of a program and come up with a range of viable results to plug in (i.e., mock) then you can run more-or-less the entire program.  And the more I think about it, the more I realize that the list of non-deterministic parts can be quite small for many programs.

For instance, consider this program:

```python
import random

def guesser():
    number = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10")
    while True:
        i = input()
        try:
            i = int(i)
        except ValueError:
            print("Please enter a number")
            continue
        if i == number:
            print("You win!")
            break
        elif i < number:
            print("Too small!")
        else:
            print("Too large!")
```

This is a simple program, but it can execute in lots of ways.  There's two non-deterministic parts: `random.randint()` and `input()`. The first can be made deterministic by seeding the random number generator with a known value (and the program can be exercised with multiple runs with multiple seeds).  The second is trickier.  We know `input()` returns a string that the user inputs, one line long. But if you throw random strings at the program you won't get something very interesting.  So we need just a little more help, a suggestion of what the person might return.  E.g., `input.suggest_returns = lambda: str(random.randint(-1, 11))` -- it's still valid that it can return anything, but we'll be able to best exercise the program with those inputs.  We still don't have a smart player for our game, but it's something.

This approach to exercising code is exciting because it's basically automatic: you write your program, and if you are using primitives that have been setup for mocking, then it's testable.  You can build tools around it, the tools can find cases where things go wrong and replay those specific cases for the programmer until they are fixed.

It's still a challenge to actually get deep into the program: the primitives often don't express the expectation.  For instance in this guessing program it's valid to enter "one", but it's not not very *interesting*.  If you are testing something interactive you might have a Cancel button that undoes a bunch of inputs; while it's worth hitting Cancel every so often, generally it's not interesting, even anti-interesting.

But with these thoughts in mind I was naturally drawn to the browser. A browser Javascript program is handy because it has very specific and a fairly limited set of primitives.  Nearly everything that's not deterministic would be considered part of the [DOM](http://en.wikipedia.org/wiki/Document_Object_Model), which includes not just the HTML page but also (at least in the terminology used by browser insiders) includes all the browser-specific functions exposed to content.

In the case of a browser program, the program tends to be fairly reactive: much of what happens is the program listening for events. This means much of the logic of the program is invoked from the outside.  This is helpful because (with some effort) we can detect those listeners, and figure out what events the program is actually interested in (since something like a click can happen *anywhere*, but usually to no effect).  Then you must also filter out handlers that apply to something that is not at the moment possible, for instance a click handler on an element that is not visible.

Trying to exercise a program is not the same as actually confirming the program did the right thing.  This testing practice will reward the program that is littered with asserts.  Asserts can't be statically examined, and in that way they are worse than static types, but they can address things that can't be statically described.

I believe there is a term for this concept: *generative testing* (for example, [some slides from a presentation](https://github.com/strangeloop/strangeloop2012/blob/master/slides/sessions/SpiewakBedra-PontificatingQuantification.pdf). Most of what I've seen under that name involves relatively small examples, with explicitly defined domains of input and output. I'm proposing to do this at the scale of an application, not a routine; to define inputs as any non-deterministic query or listener; and to define failure as some inline assertion error or warning.

## Let's Do It...?

With this in mind I created a library: [Walkabout.js](https://github.com/ianb/walkabout.js).  This either uses the evidence jQuery leaves about bound event handlers, or it can use source code rewriting to track event handlers (tracking event handlers is harder than I would like).  From this list it can create a list of plausible actions that can take place, seeing what elements might be clicked, hovered over, selected, etc., filtering out elements that aren't visible, and so on.  Then it uses a pseudo-random number generator to select an action, while checking for uncaught exceptions or warnings written to the console.

The library isn't complete in what it mocks out, but that's just a matter of doing more work.  It's a little harder to mock out server interaction, because there's easy no way to know what exactly to expect back from the server -- though if the server is deterministic (and the server's state can be reset each run) then it's okay to use it without mocking.  **Nothing deterministic need be mocked** including external components.

There's a lot I'd like to change about Walkabout.js's code itself (my opinions on Javascript have changed since I first wrote it), but I worry I get ahead of myself by doing another round of development on it right now.  There's non-trivial tooling required to use this tool, and I need to find a larger environment where it can make sense.  Or at least I *want* to find that environment, because I think the result will be more compelling.

Another big task to consider is how to actually explore the program in depth.  It's easy to come up with really boring, long, useless sequences of actions.  Open dialog, close dialog x 100.  Enter text, clear text x 10.  Hitting some control that terminates the application is only interesting once.  And though computers are *fast* they aren't so fast they can spend most of their time doing completely useless things.  I want my failures now!

To explore an application in depth we need to effectively *search* the application, using the range of possible inputs.  The first idea for scoring a result that I thought of is code coverage: if you are reaching new code, then you are doing something interesting.  Then the tooling becomes even more heavy-weight, you have to do code coverage and constantly track it to find productive avenues.  Then a second, simpler idea: look for new sets of available inputs.  If there's a new button to click or new fields to interact with, then we've probably accomplished something.  Continue to explore from that point forward. This option requires only the tooling we already have!

## Why Are We Doing This Again?

In addition to just thinking about "live programming" I think this can be a great testing tool in general.  And generally I'm suspicious of programming tools that are only applicable to toy/educational programming environments.

A common alternative approach to what I describe is to *record* user input, and then replay it as a test.  It's like random testing, only instead of a random number generator you have a person.  This is basically a refinement of the standard practice of creating a script for a functional test that exercises your full application.

If you've used this approach you've probably found it annoying. Because it is.  When you replay a recording and it doesn't work, what is more likely: the application is broken, or you deliberately changed the application in a way that affects how the recording replays?  In my experience 9 times out of 10 it's the latter.  **We spend too much time fixing test failures that are not bugs.**

The beauty of the generative approach is that it responds to your changes.  It takes your program as it is, not as you might wish it to be.  It runs the actions that are valid with *this* code, not some past version of your code.  And the "tests" aren't expected input and output, they are assertions, and those assertions live right with the code and stay updated with that code.  If we care about testing, why don't we include testing in the code itself?  If you want to entertain various possible inputs why not suggest what you are expecting directly in the code?

Once you are exercising the code, you can also learn a lot more about the code at runtime.  What kinds of object are assigned to a particular variable?  How are pieces of code linked?  What is the *temporally* related code?  Given code coverage, you could isolate patterns that exercise a particular line of code.  Having found a bug, you also have a script to reach that bug.  Having made a change, you could identify past scripts that reach that changed area, giving you a chance to dive into the effect of that change.  Many of these kinds of tools would be valid in a general sense, but require a well-exercised program to be useful -- because most software tooling doesn't include a "do lots of stuff" option we're holding ourself back when it comes to runtime analysis.

So what do you think?

If you want to give it a really quick/rough try, go [here](http://ianb.github.io/walkabout.js/), grab the bookmarklet, and go to a single-page app and try it out.  It might do silly things, or nothing, but maybe it'll do something interesting?