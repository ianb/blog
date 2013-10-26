Runtime vs. Test time
#####################
:date: 2008-02-06 22:39
:author: Ian Bicking
:tags: Programming

Defenders of static typing have long claimed that it helps them avoid bugs, the compiler providing a constant test of code consistency. Agile practitioners counter that tests do the same thing and much more.

I find myself inclined to something more in the middle. I don’t care for static typing, but I think `programming by contract <http://en.wikipedia.org/wiki/Design_by_contract>`_ has a lot of validity, is more powerful and helpful than static typing, and works just as well in a dynamically typed language. Programming by contract is more a principle than a particular technology. Unit testing is not `xUnit <http://en.wikipedia.org/wiki/XUnit>`_; that’s just one way to do it. You can do unit testing perfectly well without any framework or special infrastructure at all. Similarly programming by contract just means: state and check your up-front expectations in a piece of code, and state and check our expectations for what that code returns or does. This can be as simple as “assert isinstance(n, int)“ in your code.

Programming by contract is not enough to produce quality code. While the contract is checked at runtime that only means that exceptions are raised early and bad or inconsistent data does not propagate into the system. But it only works if you go through the code paths to invoke all those contracts.

Here’s where `functional tests <http://en.wikipedia.org/wiki/System_testing>`_ come in. A functional test does stuff. In a web application a functional test does a simulated HTTP request and gives you the result. Generally they are high-level and go through the entire application stack. This is in contrast to unit tests that test just one piece of code.

Proponents of unit tests say that functional tests are problematic. They often give confusing output, so that you have to work harder to debug problems when you are invoking so much code. You have combinatorial problems where it can be difficult to run tests that really get to all branches of the code. Functional tests can be slow.

Of course no one really claims you shouldn’t have a mixture of both functional and unit tests for your code, this is more a question of what the best balance is. Functional tests without runtime checks in your code *are* a problem. They can be fragile because people look for every detail of how the application responds to identify how specific features function. But every detail that is verified is a detail that might change and require updates to the tests.

With runtime tests functional tests can be much more compact. You can do things like simply verify that a page renders, or that code completes without an exception. If you have some confidence that it won’t be complete *wrong* — wrong as in without any exception but with errors — then simply exercising to code can be sufficient. In addition to getting more use out of your functional tests, you also have some assurance that production code will act in a sane way — that is, if it *is* broken, the code will *act* broken. Given a good deployment situation, the turnaround on fixing deployed bugs can be much shorter.
