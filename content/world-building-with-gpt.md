Title: World Building With GPT
Slug: world-building-with-gpt
Date: 2023-02-27
Category: ai
cover_image: world-building-with-gpt.jpg
header_style: color: #fff; background-color: rgba(0, 0, 0, .3); display: inline-block; padding: 0 0.5em;
header_inner_style: color: #fff;
header_cover_image_style: margin-bottom: 1em; background-color: #000; height: 190px;

I've been doing lots of experiments with GPT, though I've only [written about one](https://ianbicking.org/blog/2023/01/infinite-ai-array.html) until now... the more serious something is the harder it is to call it finished or identify the outcomes. Here I'll describe something a bit lighter: world building, or specifically city building, with GPT.

This post is for people who are interested in building interactive tools on top of GPT and want to see some of the things I've encountered and what I've found that is successful and what is still a challenge.

**Note:** Also check out my followup post: [World Building with GPT part 2: bigger, better, more declarative](https://ianbicking.org/blog/2023/04/world-building-gpt-2-declarative.html)

# Where it started

I enjoy game worlds where the world seems alive and the details suggest a backstory. The real world both is and isn't this way: every house has stories, people invested in its details, each building is occupied and reoccupied repeatedly. But our world is also quiet, private, less eccentric than we might want, and imaginary worlds can be fun. Procedurally generated roguelike games give some of the excitement of exploration but lack story and depth. A game like Stardew Valley has stories but is necessarily pretty small and static.

With generative AI we can change these trade-offs! Is it possible to make a big world that is both eclectic and consistent? Can it include story and personality? I don't know the answer, but I'd like to share what I've got...

# The tool

<aside>(Sidebar is for concrete examples)</aside>

In a previous experiment in story building I used a step-by-step approach: generate the first passage, generate a next passage, etc. That's appealing and simple but leads to a wandering and unstructured narrative. I believe in both stories and worlds we want a kind of fractal complexity: at each scale we want most things to be "typical" but also some surprise. In a story the surprises might go from large to small scale like: an unusual character arc, a surprise plot development, an alternate perspective, an unexpected response in dialog, a perceptive detail in a description, and an unusual word in a sentence. If you always write the-most-likely-next-thing then it'll be boring. If you only write surprises then there's nothing to even be surprised about.

Similarly we want to build a world or city that expresses a broad theme and consistency, but also has diversity and surprises throughout it. To do this I've approached the building hierarchically:

1. Establish the type of city (medieval, fantasy, noir, etc). Give it a name and some story.
2. Identify distinct neighborhoods.
3. Create buildings in those neighborhoods.
4. Create people associated with the buildings.
5. Populate the buildings with rooms, furniture, and objects.

There are problems with this approach that I'll touch on later, but it's a start.

You can see it in action here:

<iframe style="width: 100%; aspect-ratio: 16/9; display: block" src="https://www.youtube.com/embed/YUEXo3wrf70" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# What works?

Some stuff I really like...

### GPT-generated lists

<aside>Examples of city theme suggestions:
<ol><li>A sci-fi city on Mars with interplanetary trade</li>
<li>A space station orbiting Earth</li>
<li>A Muslim city with a vast bazaar</li>
<li>A magical kingdom with a cursed castle</li>
<li>A pirate-infested Caribbean port city</li>
<li>An Aztec city hidden in a remote jungle</li>
</aside>

GPT is good at coming up with lists: lists of city types, names, people. As I used the tool more I started to have my own opinions on what I wanted to make, but those lists were an important part of expanding my own imagination. I've made [other experiments](https://www.youtube.com/watch?v=nsIPC_eqfwg) where I filled in all the initial information by hand without any GPT suggestions, and I miss the lists.

### Natural language context

<aside>Example backstory suggestions for a jungle city:
<ol>
<li>The economy of Xochiciahuatl revolves around agriculture, fishing, and crafts such as pottery and textiles.</li>
<li>The geography of the city boasts dense jungle, mountainous terrain, and a valley basin surrounding an expansive lake.</li>
<li>The level of technology present in the city is quite advanced, with aqueducts, terraced gardens, and even a canal network.</li>
<li>The cultural context of Xochiciahuatl is multifaceted, with influences from indigenous tribes, the Spanish, and African slaves.</li>
</ol></aside>

The cities are formed in a top-down way, and all the top layers (city, backstory, neighborhood) are purely context. The top layer descriptions are very important but have no need for structure, it's all just language. Not every aspect has to be enumerated, just the ones that seem important for this city.

### Reinforcing city character

<aside>Example neighborhood suggestions for a space station:
<ol>
<li>The Gateway: The Gateway is the official entrance to Aeterna Station. It is a grand, soaring structure that serves as a reminder of the city's ambition and capability.</li>
<li>Solaria: Located in the “sunshine zone,” Solaria is where the people of Aeterna Station can find some of the best dining and entertainment in the city. It is a great place to relax and enjoy the view of Earth below.</li>
<li>Agri-Plex: The Agri-Plex is a large, domed area devoted to growing food and other crops. It provides the citizens of Aeterna Station with the necessary sustenance.</li>
<li>Stabilization Zone: This is the area where the station's mechanical infrastructure is maintained. Regularly monitored and kept running at peak efficiency, the Stabilization Zone is vital for keeping the station operating smoothly.</li>
</ol></aside>

A general character to the city (e.g., "fantasy city") isn't enough to build something consistent. The character of the city needs to be repeated and reinforced at different levels. Details like architecture and building materials may have to be specified.

This is primarily done at the neighborhood level, though it would benefit from building-specific attributes more strongly informing person generation. For instance in a fantasy city it's common that everyone will start out powerful and loyal and wise, even when they occupy a hovel or explicitly partake in the dark arts.

### Structured output

<aside>
Structure of a building:
<blockquote><strong>name:</strong> Goblin Smithy<br/>
<strong>description:</strong> A small, smoky workshop where Goblin tradesmen craft magical weapons and armor<br/>
<strong>floors:</strong> 1<br />
<strong>widthInMeters:</strong> 4<br/>
<strong>depthInMeters:</strong> 4</blockquote></aside>

When we get to parts with specific structure it's a comfortable transition. Buildings have sizes, people have roles, etc. GPT can fill in these details. If you wanted to plug the city into a map builder or other structured game format, you can produce the metaata you need.

### Filling out content you create

<aside>In response to "a whimsical factory for magical robots. Give it a fun name and description":
<blockquote><strong>name:</strong> The Clockwork Dream factory<br />
<strong>description:</strong> This magical factory is a bustling center of activity where magical robots are assembled and activated for a variety of tasks. Powered by an array of enchantments, the whirring machines churn out a steady supply of dream-like robots that fill the city with a sense of cheerful industry. Acrid smoke rises from the chimneys as the robotic workers tirelessly toil away, overseen by a crew of diligent engineers.<br/>
<strong>floors:</strong> 4<br/>
<strong>widthInMeters:</strong> 10<br/>
<strong>depthInMeters:</strong> 10</blockquote></aside>

When you don't want to take a GPT suggestion, GPT is pretty good at filling in the details in something you produce. So if you ask for a "factory" it works well for GPT to turn that into a fuller description, size, etc.

I only implemented this for structured elements, and not freeform fields like neighborhood descriptions. I should fix that!

### Pushing GPT helps

<aside>First suggestions of furniture for an <em>Activation Chamber</em> in the Clockwork Dream factory, where robots are granted power:
<ol><li>Activation Table</li>
<li>Alchemy Cauldron</li>
<li>Arcane Anvil</li>
</ol>
Kind of boring; adding "weird steampunk-inspired machines for giving robots a soul" to the prompt:
<ol><li>Tin Man Activator: This machine is a steampunk-inspired machine for giving robots a soul. In the center is a glowing magical orb that emits strange and mysterious magical energies. <em>[Lost points for copying my language!]</em></li>
<li>Alchemical Hammer of Life: This contraption is an alchemical hammer with a large hammerhead and a magical gemstone set in the top. A switch activates the powerful device, granting a spark of life to any robotic body that is placed beneath it.</li>
</ol></aside>

Small contextual prompt additions can be helpful. For instance GPT has sometimes wanted to suggest sofas and armchairs for a factory, but a small note ("factory equipment and tools") can fix that.

**However** I've found this needed too often for character descriptions. The descriptions start out seeming OK but begin to feel boring and repetitious. The building and neighborhood need to more explicitly affect the people prompt. Right now the prompt is effectively:

> **[General city context]** <br/> A list of owners, caretakers, residents, tenants, and other inhabitants for **[Building Name]** (**[Building Description]**) Give each person an interesting and culturally appropriate name and a colorful background and personality.

If you ask a more open-ended question like:

> Make a numbered list of the kinds of people that would occupy a building called **[Building Name]** described as: **[Building Description]**

then you get a good list of professions and roles (better than my hardcoded set). If you add this:

> For each item include a 10-word note on the likely personality, limitations, and character flaws

then you also start battling the relentless positivity, with results like "Supply Chain Managers: Responsible and knowledgeable, but prone to micromanaging" and "Magical Robots: Resourceful and imaginative, but restricted by programming".

[Note: after writing this I implemented a list of jobs/roles as part of buildings; it was effective!]

### Putting people in buildings is great

For all my criticisms in the previous section, adding people is great and I only want it to be better! Buildings have some history and personality, but the people associated with them make it seem much more alive.

> **Razzaqua Sephina**: Razzaqua Sephina is the mysterious and enigmatic owner of the Warehouse of the Cankered Crypt. She is a master at thaumaturgy, specializing in curses and dark artifacts. Those who have met her say she is as cold as ice. Despite this, locals claim she is fiercely loyal and protective of her tenants.
>
> **Kana Wazri**: Kana is a charming young student from a well-known family of merchants. She has a great love of magic but isn't incredibly talented at it. Despite this, she is always seen studying and researching the magical arts, hoping to one day unlock her true potential.
>
> **Morgaine de Sombra**: Morgaine de Sombra was an aristocrat in the court of King Tragen before she found her calling in the dark arts. She runs a tight ship, instilling a sense of discipline among the students of the Academy. Morgaine has a no-nonsense attitude when it comes to teaching and is feared by many of the students.
>
> **Fayza Silverwing**: Fayza is a beautiful priestess, wearing a dress of shimmering pearlescent feathers. She is gentle and kind, and her voice is melodious and soothing. She uses her singing voice to call down the blessings of the sky goddess, and to ward off evil. She also tends to the birds of the temple, providing them with a special place to dwell.
>
> **Mathilde Velasquez**: Mathilde Velasquez was a cunning and ambitious woman in life, a talented emissary and negotiator. She was the right hand of an 18th century nobleman, and in death, she still roams the halls of the Mansion, planning out her strategies and scheming her way through the afterlife.

I had to nudge some of these into existence, but I'm still quite enamored with the variety it can produce, and believe GPT can do much better with further refinement.

# What doesn't work?

I think these things could be fixed, but they aren't yet, and if you implement something similar you are likely to encounter these same problems:

### Reverting to normal/boring

GPT is constantly normalizing things, including modernization. I want to make weird stuff, but also stylistically consistent stuff.

As a general rule asking GPT for a list will help it be more creative. But when it gets on a roll producing normal/boring things, it will fill out the list with normal/boring things.

Examples of this: "smart homes" (there is no time when I want "smart homes"), lots of references to tourism, "high-end restaurants". How many cities should have art galleries? The primary attribute of a harbor area is not its historic cobbled streets and tourist amenities. These are all examples where GPT introduces a modern perspective.

### GPT is desperately positive

<aside>
Some characters; note the pattern:
<ol>
<li>Anavel Shaz: a powerful alchemist and scholar</li>
<li>Lalania Nightshadow: A powerful sorceress and former Keeper of the Order of Magi</li>
<li>Brynja Rahman: a talented enchantress whose skill is unrivaled</li>
</ol></aside>

Every building is grand. Every character is loyal and helpful. Every character is competent, respected, and wise.

If you ask very explicitly for flaws you can get _some_. It's very hard to get a truly despicable character. It's hard to even get a realistically boring character, one who is not very competent or smart. It's a fight, but armed with prompts we can still win the battle!

Some things that have helped:

1. Asking for "exotic names": this seems to result in a wide variety of ethnic names and other interesting combinations. For any one list GPT will often choose one ethnicity, such as Arabic names or Japanese names.
2. "Colorful background/history": this adds some playfulness
3. Mentioning "culture": this seems to fight against normalizing to modern American themes
4. Asking for "personality" or "character" in something: similar to "colorful", this also tends to extend the descriptions
5. Ask for "negative attributes", "flaws", "Achilles Heal": descriptions will still be positive, but you'll get some additional negative attributes

### Fine detail is too much work

Once you generate a building and occupants you also have an opportunity to build rooms, to put furniture in those rooms, to put items in those rooms, and finally to define the room connections. This takes forever and is very boring!

Many rooms have tables! Many buildings have a storage room! Many kitchens have utensils!

To generate real maps you do need these more concrete features. A building with no interior is no fun. An interior with no objects is no fun.

If I were to approach this again I'd use this strategy:

1. Ask GPT for building "types" when creating a building. Maybe offer some initial types, but also invite GPT to make up new types.
2. For each type of building ask GPT to create an expansive list of rooms. Give the rooms types as well (hang-out, cooking, storage, etc). Ask for a range of room sizes.
3. For each type of room, or perhaps building-type/room-type combos, ask about furniture and items. Again ask for a long and expansive list.

At this point you could use a simple non-GPT algorithm to assign rooms to buildings. But you could also use abbreviated forms of these list and ask for GPT to fill out a building, like:

> The building is called "**[Building Name**]" and is described as: **[Building Description]**
> Fill out this list:
>
> 1. **[Room type]**: [description]
> 1. **[Furniture]**: [description]

... basically letting GPT customize the building in one step, given a randomly chosen set of specific elements.

### Bad spatial reasoning

GPT's spatial reasoning isn't very good (unsurprisingly). It's OK at general sizes and heights of buildings, but when it has to relate spaces to each other (like placing rooms in buildings) it doesn't understand.

This probably calls for traditional procedural generation techniques.

It's possible that GPT could help by coming up with constraints. For instance when generating rooms GPT is asked if the room is "public", "private" (impolite to enter), "secure" (locked), or "secret". These hints could provide constraints that keep the room layouts plausible.

### Every detail of a prompt is a suggestion

It's very hard to tell GPT what is important and what is just framing. Some examples:

1. In an early prompt I used an example like `{name: "John Doe"}` for generating a person. GPT started coming up with names like "Jack Doe", "John Smith" etc., _specifically_ choosing stereotypically generic names. I was able to improve it with a combination of asking for "interesting and culturally appropriate names" and replacing the example with `{name: "FirstName LastName"}`. (But now every so often GPT spits out FirstName LastName characters; you can't win them all.)
2. Even a word like "building" is a suggestion. I wanted to make a floating pirate city made up of attached boats. GPT wasn't sure whether to make things that matched my city description, or that matched what a "building" typically is, and it suggested a lot of boat-inappropriate structures. Explicit prompt additions can help, but it would be even better if some of the core language could be substituted.
3. My beaver city also featured far too few dams and dens. Which is too bad because GPT is quite good at helping fill out these weird combinations so long as the prompt doesn't fight with the premise.

I can imagine having GPT rewrite some of the prompts as the city starts to be defined.

Another option is to have a glossary of terms where the author can adjust a few terms. I've specifically allowed the word "neighborhood" to be substituted (for quarter/district/etc), though the effect is minimal and GPT is happy to use different terms for neighborhoods without any special suggestions. Maybe other words are more impactful.

### Constantly poking at the prompts is tiresome

<aside>Notes I added for <a href="https://llm.ianbicking.org/citymaker/?name=builtin_talamora">Talamora</a>:
<ol><li>include a both haunted/ghost district and a desolate magically polluted district</li>
<li>include lots of magical finance and investment, as well as dark and occult elements</li>
<li>include different schools of magic: nature, clairvoyance, battle magic, golems; give each an imaginative name</li>
<li>include a list of temples for many gods</li>
<li>include haunted buildings with dark histories</li>
<li>include a list of different fraternal orders of magicians from different magical schools</li>
<li>Include lists of ruins with specific and mind-bending dangers due to the magical pollution</li>
</ol></aside>

Sometimes GPT just doesn't come up with the right things at all. When that happens there's a few ways to get GPT to change its output: adding or changing the overall context/backstory, making suggestions for a specific list, and asking for specific items.

Getting fun, interesting, and varied entities requires lots of nudging and iteration. But there's not many ways to build up those notes. You can add the notes to the global context, and that can be a good idea, but it's not a good iteration process.

I have a hunch there's a way to experiment when creating specific buildings/etc, and then use GPT itself to percolate that up into more general prompt changes. But it's only a hunch.

### Hallucinating metadata

GPT will hallucinate metadata. This is both a problem and an opportunity.

If you want to turn the output into structured data for another program you might find it annoying when it uses `{size: "6x10"}` instead of `{widthInMeters: 6, depthInMeters: 10}`.

More often it's actually interesting metadata that you might want to use more widely. For instance:

> **name:** The Cabal Of Witches <br/> **hierarchy:** Grand Witch -> Witch -> Apprentice -> Initiate <br/> **initiates:** Keeper of the Dark Art, Spiritualists, Alchemists, Shaman

> **name:** The Circle of Mages <br/> **hierarchy:** Grand Magus -> Magus -> Apprentice -> Initiate <br/> **initiates:** Evokers, Enchanters, Abjurers, Illusionists

> **name:** Abandoned Warehouse <br/> **dangers:** magically-altered creatures, unknown chemical pollutants, trapdoors and hidden passages

It seems odd to produce this metadata when presumably nothing is ready to consume it. But these attributes elicit responses from GPT, and do so more consistently than natural language requests.

Adding this metadata gives **theme** and **variation**. The attribute is the theme, the value is the variation. This makes the set of things you've created more comprehensible, with a structure that makes it easier to appreciate the variety.

I don't know how to expose this! Should we ask GPT to brainstorm attributes ahead of time? Invite it to hallucinate more widely and then the author picks the ones they like to become part of the prompts? Then... backfill?

### Corruption and fixation

Some of the magic of GPT is how it implicitly learns from context. Often it learns the wrong thing. This is particularly noticeable in ChatGPT, where it will often fixate on something despite or even because of corrections.

This tool is much more explicit about context and doesn't have anything that is specifically a chat. Still...

1. You'll think the content of the backstory is all that matters, but the tone also informs GPT. Because GPT probably created that backstory this doubles down on its tone. (Is this feedback part of its tedious positivity?)
2. When you ask for "more" of a list it will feed the existing list into the prompt... this helps it create new and distinct items, and sometimes helpfully refers to previous items (like creating interesting relations between people), but if you didn't like the suggestions before you are unlikely to like the new ones. It copies tone, but also description length, metadata, name ethnicities, and architectural styles.

### GPT is expensive

[Talamora](https://llm.ianbicking.org/citymaker/?name=builtin_talamora) cost me about $6 in GPT API costs to generate. That's a lot!

Because I'm paying for API costs directly, and because the costs increase only when I use the tool, there's a natural balance: if I'm not having fun and enjoying the output, I won't generate more costs. By the time I made Talamora I had enough improvements that I actually enjoyed the process and my enthusiasm wasn't just built on dreams (which is the fuel for the first phase of any project).

The cost means I'm not motivated to automate any of the authoring. Perhaps because the _output_ has little intrinsic value, so reducing the author's involvement is a net loss.

It also means I can't easily make this available to other people. People are providing these services with "credit" models and subscriptions but the underlying costs are enough that it's hard to imagine that working. So for now you can [try this](https://llm.ianbicking.org/) with your own API key, paying OpenAI directly, and managing your own budget.

There are some ways that this could be made more efficient:

1. Use other models (e.g., `text-ada-001`) for some tasks. Though few of the tasks feel amenable to the cheaper models.
2. Get suggestions right the first time. For Talamora in particular I used lots of prompt adjustments to get results I was happy with. Overall prompt improvements would have avoided many of those.
3. Reduce context on some queries. The base context of most prompts includes the whole city backstory, neighborhood, etc. That's not necessary for every query. Perhaps some of the context is only needed for some types of queries.
4. Get more out of every query. If there's multiple queries then the context is repeated for each. This saves money when some queries produce dead ends, such as a building that the author doesn't like and doesn't want to expand. But adding a little metadata to each item is usually a good investment.
5. Improve the quality. The more generated stuff you keep, the less queries you need to achieve some degree of success or satisfaction. Investing more time in quality parent context, like backstory and neighborhoods, will pay off with the both larger and more expensive leaf nodes like buildings.
6. Summarize to reduce context. Right now this concatenate the context information. It might save some space by rephrasing that context, both combining the text in a more compact way, and selecting the salient details for generating specific kinds of items.
7. Estimating list size for choices. If you get a list of 7 items but then you ask for the list to be extended that is _much_ more expensive than asking for 14 items up front. Similarly if you want 1 item then it's cheaper just to make one item and not a long list. It's possible that the parent could estimate the list size for the child, or that we could just make better general estimates and hardcode those list sizes into the prompts.

# Image generation

All these words are interesting but some images would also be interesting. Right now there are too many considerations to do a detailed comparison of all of them, and things are changing fast, so I'll just give a scattering of thoughts.

### The generators

I have a hard time understanding the array of AI image generators, but I've used these three enough to have opinions:

1. [Stable Diffusion](https://replicate.com/stability-ai/stable-diffusion)
2. [Dall-E 2](https://openai.com/dall-e-2/)
3. [Midjourney](https://www.midjourney.com/)

The first two have an API. That means I can integrate them directly into the tool, which has a real and significant workflow benefit. Midjourney has absolute no affordances to integrate it into another application, but it creates great images. Generally I've found Stable Diffusion to be unusable because it won't create sensible compositions. There's probably some flavor of Stable Diffusion that would work better, but there's just too much going on! Dall-E is OK but it doesn't have a natural sense of style and the resulting images... just aren't very fun.

### Generating a prompt

The easy way is just to give the text directly to an image generator and let it imagine things as it will. There's a danger it will have insufficient context, like being unaware of the era or environment.

Let's take a building to see. The base text:

> **Jubilous Forge:** A bustling forge bustling with laughter and the smell of hot metal forges and alchemical potions, with ornate decorations on its two-story walls.

It's already a pretty visual description.

Here's a quick prompt to expand the visuals:

> Given the building: Jubilous Forge: A bustling forge bustling with laughter and the smell of hot metal forges and alchemical potions, with ornate decorations on its two-story walls.
>
> In 2-3 sentences make a detailed visual description of the exterior of the building:
>
> The Jubilous Forge looks like

And it completes with:

> a large, imposing structure, with walls of gray stone reaching two stories high. The windows are framed by intricate patterns of wrought iron and the door is adorned with a bright, golden door knocker. The outdoor walls are decorated with vibrant murals of blacksmiths and alchemists at work, lit up by the warm glow of nearby forge fires.

This seems better! Unfortunately it is not... the use of the term "pillar" makes both Dall-E and Midjourney think of banks.

Here's a generated image from the simple/unmodified building description:

<img src="https://ianbicking.org/media/world-building-with-gpt/jubilant-midjourney-simple-1.png" alt="Midjourney - Isometric rendering of single building on a white background: Jubilous Forge: A bustling forge bustling with laughter and the smell of hot metal forges and alchemical potions, with ornate decorations on its two-story walls." class="content" />

And here it is with the modified description:

<img src="https://ianbicking.org/media/world-building-with-gpt/jubilant-midjourney-prompted-1.png" alt="Midjourney - Isometric art of a single building on a white background: The Jubilous Forge looks like a large, imposing structure, with walls of gray stone reaching two stories high. The windows are framed by intricate patterns of wrought iron and the door is adorned with a bright, golden door knocker. The outdoor walls are decorated with vibrant murals of blacksmiths and alchemists at work, lit up by the warm glow of nearby forge fires." class="content" />

The first prompt, which leaves more latitude to Midjourney, works better.

Oh the other hand, in a jungle city there is a building:

> **The Zigzag Tower:** A tall and slender tower with a zigzag facade, The Zigzag Tower is a temple dedicated to the reverence of nature.

The Midjourney results are all bland modern towers:

<img src="https://ianbicking.org/media/world-building-with-gpt/zigzag-midjourney-simple-1.png" alt="Midjourney - Isometric rendering of a single building on a white background: The Zigzag Tower: A tall and slender tower with a zigzag facade, The Zigzag Tower is a temple dedicated to the reverence of nature." class="content" />

When we include the city description and ask GPT to make a visual description we get:

> The Zigzag Tower looks like a towering pillar of grandeur that sharply cuts into the sky, with its unique zigzag facade. Its yellow-brown hues blend with its natural surroundings, giving off a sense of harmony with the environment. It is adorned with intricate carvings and sculptures of animals and plants that make it seem to come alive in its own right.

The description doesn't look that different but the effect is dramatic:

<img src="https://ianbicking.org/media/world-building-with-gpt/zigzag-midjourney-prompted-1.png" alt="Midjourney - Isometric rendering of a single building on a white background: The Zigzag Tower looks like a towering pillar of grandeur that sharply cuts into the sky, with its unique zigzag facade. Its yellow-brown hues blend with its natural surroundings, giving off a sense of harmony with the environment. It is adorned with intricate carvings and sculptures of animals and plants that make it seem to come alive in its own right." class="content" />

### Describing the style

If you ask for an image of a building that can mean all kinds of things. For instance this is what Stable Diffusion gives for the Jubilant Forge:

<img src="https://ianbicking.org/media/world-building-with-gpt/jubilant-sd-no-prefix.png" alt="jumbled old style drawing of a building" class="content" />

Interesting! But not the format I intended. Here's some additions to the prompt that help:

1. "Isometric" is a very strong word and will align the perspective and set the camera angle.
2. Midjourney will happily make a stand-alone building. Dall-E often zooms too far in or gets confused, but it comes close. Stable Diffusion feels hopeless! I'd be curious if Stable Diffusion and Dall-E could be asked to infill a template photo; i.e., create a isometric-shaped-building-size-hole so it has to work in those constraints.
3. "White background" suggests the building should be rendered without an environmental context.

This prompt seems decent for both Midjourney and Dall-E: **Isometric rendering of single building on a white background**

# Conclusion

Many of the lessons from this experiment could be applied to other top-down authoring environments:

1. Establishing hierarchical context.
2. Using GPT to offer suggestions at each level with author selection.
3. Using a combination of natural language and structured output.
4. Include points of intervention to "speak to" GPT.
5. Be aware of all the language in a prompt; it all matters.
6. Use the tool a lot! The first couple things feel magical, but the magic will wear off after you've made a couple dozen things without special effort.

If you want to try this yourself check out [llm.ianbicking.org](https://llm.ianbicking.org/citymaker/), or [check out GitHub](https://github.com/ianb/llm-garden). If you are curious about the exact prompts look for `prompt =` in [citymakerdb.js](104537541227697934010/content_cache/d34/d33/637). Note that this is a personal project, it's monolithic and only organized well enough for me to understand.

Similarly: when using the site be warned I have not built it carefully for other people to use, stuff will be weird, errors will appear only in the JS Console, there are no promises. And you'll have to bring your own GPT API key!

Comments welcome on [Mastodon](https://hachyderm.io/@ianbicking/109937462683423813), [Twitter](https://twitter.com/ianbicking/status/1630231712499376130), [Hacker News](https://news.ycombinator.com/item?id=34967515).

If you've gotten this far I will also throw in here that I ([Ian](https://ianbicking.org)) am looking for a job, and maybe the best job for me is one that I don't yet know exists. I'm particularly interested in the area of large language models, [natural language interfaces](https://ianbicking.org/blog/2023/01/thoughts-on-voice-interfaces-2-llms.html), new user interactions built on LLMs (especially their abilities to understand us in new ways). I'm excited about education, aiding in executive function, and human-centered interactions. [Let me know if you have ideas](mailto:ianbicking@gmail.com), [or hit me up on LinkedIn](https://www.linkedin.com/in/ianbicking/) I would appreciate it!
