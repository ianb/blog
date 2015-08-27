Title: Conway's Corollary
Slug: conways-corollary
Date: 2015-08-27
Category: mozilla

[Conway's Law](http://www.melconway.com/Home/Conways_Law.html) states:

> organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations

I've always read this as an accusation: we are doomed to recreate the structure of our organizations in the structure of software projects.  And further: projects cannot become their True Selves, cannot realize the most superior design, unless the organization is itself practically structureless.  That only without the constraints of structure can the engineer make the truly correct choices.  Michelangelo sculpted from marble, a smooth and uniform stone, not from an aggregate, where any hit with the chisel might reveal only the chaotic structure and fault lines of the rock and not his vision.

But most software is built, not revealed.  I'm starting to believe that Conway's observation is a corollary, not so clearly cause-and-effect.  Maybe we should work with it, not struggle against it.  (With age I've lost the passion for pointless struggle.)  It's not that developers can't imagine a design that goes contrary to the organizational structure, it's that they can't *ship* those designs.  What we're seeing is natural selection.  And when through force of will such a design is shipped, that it survives and is maintained depends on whether that the organization changed in the process, whether a structure was created to support that design.  

A second skepticism: must a particular construction and modularity of code be paramount?  Code is malleable, and its modularity is for the purpose of humans.  Most of what we do disappears anyway when the machine takes over – functions are inlined, types erased, the pieces become linked, and the machine doesn't care one whit about everything we've done to make the software comprehensible.  Modularity is to serve our purposes.  And sometimes organization structure serves a purpose; we change it to meet goals, and we shouldn't assume the people who change it are just busybodies.  But those changes are often aspirational, and so those changes are setting ourselves up for conflict as the new structure probably does not mirror the software design.

> If the parts of an organization (e.g. teams, departments, or subdivisions) do not closely reflect the essential parts of the product, or if the relationship between organizations do not reflect the relationships between product parts, then the project will be in trouble... Therefore: Make sure the organization is compatible with the product architecture
> – [Coplien and Harrison](https://en.wikipedia.org/wiki/Conway%27s_law#cite_note-5)

So change the architecture!  There's more than one way to resolve these tensions.

A last speculation: as described in the [Second System Effect](http://c2.com/cgi/wiki?SecondSystemEffect) we see teams rearchitect systems with excessive modularity and abstraction.  Maybe because they remember all these conflicts, they remember all the times organizational structure and product motivations didn't match architecture.  The team makes an incorrect response by creating an architecture that can simultaneously embody all imagined organizational structures, a granularity that embodies not just current organizational tensions but also organizational boundaries that have come and gone.  But the value is only in predicting future changes in structure, and only then if you are lucky.

Maybe we should look at Conway's Law as a prescription: projects *should only* have hard boundaries where there are organizational boundaries.  Soft boundaries and definitions still exist everywhere: just like we give local variables meaningful names (even though outside the function no one can tell the difference), we might also create abstractions and modularity that serve immediate and concrete purposes.  But they should only be built for the moment and the task at hand.  Extra effort should be applied to being *ready* to refactor in the future, not predicting and embodying those predictions in present modularity.  Perhaps this is another rephrasing of Agile and [YAGNI](http://martinfowler.com/bliki/Yagni.html).  Code is a liability, agency over that code is an asset.
