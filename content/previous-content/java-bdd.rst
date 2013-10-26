Java BDD
########
:date: 2007-11-27 12:14
:author: Ian Bicking
:tags: Programming

I notice there's another `Behavior Driven Development <http://en.wikipedia.org/wiki/Behavior_driven_development>`_ framework for Java called `Instinct <http://code.google.com/p/instinct />`_ (`via <http://bright-green.com/blog/2007_11_27/behaviour_driven_design.html>`_).   I have `commented on BDD before <http://blog.ianbicking.org/behavior-driven-programming.html>`_.

Here's an `example test <http://code.google.com/p/instinct/wiki/InstinctIn2Minutes>`_::

    import static com.googlecode.instinct.expect.Expect.expect;
    import com.googlecode.instinct.marker.annotate.BeforeSpecification;
    import com.googlecode.instinct.marker.annotate.Context;
    import com.googlecode.instinct.marker.annotate.Specification;

    public final class AnEmptyStack {
        private Stack<Object> stack;

        @BeforeSpecification
        void setUp() {
            stack = new StackImpl<Object>();
        }

        @Specification
        void mustBeEmpty() {
            expect.that(stack.isEmpty()).equalTo(true);
        }
    }

Yeah, that's... great.  What would it look like in a doctest?

::

    >>> Stack<Object> stack = new StackImpl<Object>();
    >>> stack.isEmpty()
    true

Of course you have to invent a `REPL <http://en.wikipedia.org/wiki/REPL>`_ for Java, but I'm sure that's not very hard.

What does all that class infrastructure, ``setUp``, ``mustBeEmpty`` and the weird DSLish stuff give you?  Beats me.  Doctest `started in Python <http://python.org/doc/current/lib/module-doctest.html>`_ but now also exists in `Ruby <http://clintonforbes.blogspot.com/2007/08/doctest-for-ruby-and-rails.html>`_ and `Javascript <http://svn.colorstudy.com/doctestjs/trunk/docs/index.html>`_. Someone needs to port the concept to Java too.  People ported `SUnit <http://sunit.sourceforge.net />`_ all over the place, so there's no reason a good idea can't spread.  I can't help feel that BDD is a case of a bad idea spreading; the motivations for BDD are fine (a change in developer testing workflow), but the technique they use to try to reach the desired workflow is totally bizarre.
