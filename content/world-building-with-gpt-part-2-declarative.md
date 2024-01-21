Title: World Building with GPT part 2: bigger, better, more declarative
Category: ai
Slug: world-building-gpt-2-declarative
cover_image: world-building-with-gpt-2.jpg
header_style: color: #fff; background-color: rgba(0, 0, 0, .4); display: inline-block; padding: 0 0.5em;
header_inner_style: color: #fff;
header_cover_image_style: margin-bottom: 1em; background-color: #000; height: 190px;
Date: 2023-04-04

In my [last post](https://ianbicking.org/blog/2023/02/world-building-with-gpt.html) I described a city builder using GPT. I was planning on putting a pin in that work with the post, but the heart wants what the heart wants and I found myself returning to that work.

In this post I'll talk about [generating images from the source material](#images), [chatting with your characters](#chatting), [creating plots](#plots), some more about the [authoring experience](#authoring), and the [move to a more declarative implementation](#declarative).

To get an idea of how this works here's a video:

<iframe style="width: 100%; aspect-ratio: 16/9; display: block" src="https://www.youtube.com/embed/4DEibveZ-n8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

As a demonstration of the tool I've created [Veilvale](https://veilvale.ianbicking.org/), a fantastical city powered by esoteric magic and a populace where everyone wears a mask as their identity. It has over 280 characters, 70 buildings and landmarks, and 450 images. I specifically mention its size because while it wasn't _easy_ to build, it also wasn't that hard and I reached a level of completion that exceeds any other worldbuilding project I've attempted.

## Table of contents

<div id="toc"></div>

1. [Generating images](#images)
    1. [Contextualizing descriptions](#contextualizing)
    2. [Character race](#character-race)
    3. [Character attractiveness](#character-attractiveness)
        1. [Lots of beautiful ladies](#beautiful)
        2. [Everyone's fancy](#fancy)
    4. [Buildings](#buildings)
2. [Chatting with your creations](#chatting)
    1. [Characters floating in space](#characters-floating)
    2. [Chatting about... anything](#extending-chat)
3. [Plots](#plots)
    1. [Building plots with: summary, selection, events](#summary-selection)
    2. [Murder Mysteries](#murder-mysteries)
4. [The authoring process](#authoring)
    1. [The Rule Of Cool](#rule-of-cool)
    2. [GPT does not roll fair dice](#gpt-dice)
    3. [People existing in and out of a context](#people-context)
    4. [GPT 3.5 vs GPT 4](#gpt-3-4)
5. [A declarative approach to building](#declarative)
    1. [Updates and dependencies](#updates-dependencies)
    2. [Getting meta in the prompt](#meta-prompting)
    3. [Planning & action](#planning)
    4. [I'm glad fine tuning is dead](#fine-tuning)
6. [Conclusion](#conclusion)

# <span id="images">Generating images</span>

I equivocated on image generation in the [last post](https://ianbicking.org/blog/2023/02/world-building-with-gpt.html). But images are great! And at least at this moment [Midjourney](https://www.midjourney.com/) is making the best generative images. What Midjourney isn't good at is automation. But there's no unattended image generation process that creates good results.

To make it more feasible I created [a bit of automation](https://gist.github.com/ianb/2a81e219ec38ea46bac1ad7156f5f711). The whole city took about 55 hours of Midjourney CPU time.

## <span id="contextualizing">Contextualizing descriptions</span>

I have GPT create prompts from character descriptions. The request looks like this:

> [all the world context]
>
> [character description]
>
> Give a description of the person in the form of a picture. Do not assume any context. Focus on the visual details. Use 3-4 sentences.

I could just pass the original character description to Midjourney. Midjourney is also happy to hallucinate details in the absence of a specific prompt, which is essentially what I'm asking GPT to do. _Except_ GPT can synthesize the world description and the character description, and then pull out just the important visual details.

This is important! As an example I created a candy city where everyone was made of candy. An example character:

> **Caramel Elise** (Council member): Caramel Elise is a shrewd and calculating candy who always has an eye on the bottom line. She is a caramel candy.

If I feed the character description directly into Midjourney I get these:

<img src="/media/world-building-with-gpt-2/Ian_Full_body_digital_art_portrait_of_a_candy_person_Caramel_El_f8374638-b80a-4eb2-902a-cede26d4053d.jpg" title="Full body digital art portrait of a candy person: Caramel Elise is a shrewd and calculating candy who always has an eye on the bottom line. She is a caramel candy. --v 5" class="content">

GPT translates her description into something more specific:

> Full body digital art portrait of a candy person: Caramel Elise has a warm, golden-brown hue with a smooth, glossy surface. She has a rectangular shape and slightly curved edges, as if she's been poured into a mold. Her expression is serious and determined, with a hint of a smirk on her lips.

And the result captures the all-important fact that she's literally made of candy:

<img src="/media/world-building-with-gpt-2/Ian_Full_body_digital_art_portrait_of_a_candy_person_Caramel_El_f212fb89-1afc-448d-90f3-d82a395e0a02.jpg" title="Full body digital art portrait of a candy person: Caramel Elise has a warm, golden-brown hue with a smooth, glossy surface. She has a rectangular shape and slightly curved edges, as if she's been poured into a mold. Her expression is serious and determined, with a hint of a smirk on her lips. --v 5 " class="content">

## <span id="character-race">Character race</span>

One as-yet-unresolved issue in character generation and image generation is a tendency to default to white characters.

<img src="/media/world-building-with-gpt-2/race-collage.jpg" title="8 portraits of characters" class="content">

This should be contrasted with gender, where by default GPT is very balanced in its gender representation. I've mostly left gender unspecified in the world descriptions and GPT will create a roughly equal number of men and women characters, and even quite a few characters who use "they" as their pronouns. I'm sure GPT would be willing to stereotype genders if I made world notes to that effect, but I appreciate a balanced default when it's unspecified.

Typically the source character descriptions don't specify any race at all, nor are there enough cues to guess at the race. What I think is happening is a series of choices that narrow the possible race:

1. I ask GPT to make characters that are interesting and distinct.
2. GPT's idea of unique character descriptions includes lots of "piercing blue eyes" and "angular features". (GPT has no interest in brown eyes!)
3. GPT's preference for hair color is also affected, with a preference for black, blonde, and red hair.
4. Ironically I think GPT has such a strong preference for black hair over brown _because that's a more striking hair color on white people_. It's choosing the kinds of features an author would mention.

Many of these features effectively create a constraint that the character is white. Even if it picks black hair it may throw in blue eyes or freckles implying the person is white. Or GPT chooses red hair then any other attributes will still result in a white character.

Here the answer is probably not too hard: tell GPT to specify race explicitly. Especially if GPT _starts_ with a race then it's going to create features that align with that race. I've tried an initial experiment where I simply ask GPT to first specify the race as part of the visual description and it helps quite a bit.

## <span id="character-attractiveness">Character attractiveness/etc</span>

In addition to race, both GPT and Midjourney default to a few body types. Women and men are often described as _slender_, though men are occasionally _muscular_. Midjourney takes both of these to an extreme; here's someone who's just "a tall man with a muscular build":

<img src="/media/world-building-with-gpt-2/Ian_Full_body_fantasy_portrait_of_a_masked_figure_Vrishabha_Ste_907039fb-cce9-4406-851f-4205607ec444.jpg" title="Full body fantasy portrait of a masked figure: Vrishabha Steadfast is a tall man with a muscular build. He has a bald head, with only a few wisps of gray hair left at the back of his head. His silver mask is intricately designed, with sharp lines and curves that resemble the constellations in the night sky. His eyes are piercing and kind, and seem to hold centuries of wisdom. He wears a tunic of deep blue, with intricate embroidery on the sleeves and hem" class="content">

Or this might be a cool character study but it does not radiate _gardener_:

<img src="/media/world-building-with-gpt-2/Ian_Full_body_fantasy_portrait_of_a_masked_figure_Orion_Stargaz_9c323756-3074-4ba0-ba7e-ca969c057bab.jpg" title="Full body fantasy portrait of a masked figure: Orion Stargazer stands tall, with a muscular build and tan skin. His short, curly black hair frames his face, which is partially obscured by a constellation mask adorned with tiny glass stars and moons. With a confident gaze and intense demeanor, Orion exudes a sense of determination and purpose" class="content">

### <span id="beautiful">Lots of beautiful ladies</span>

It can also be hard to make women who _aren't_ beautiful or sexy. For instance here's Kiera Ironclad, who was given a description that only emphasized her strength:

> Kiera is a tough and experienced guard, responsible for keeping the guests of the Masked Ballroom safe. She wears a mask made of steel, symbolizing her strength and reliability.

GPT's physical description is consistent:

> Kiera Ironclad stands tall and proud, with a muscular build and a stern expression. Her steel mask covers her face, except for her piercing blue eyes that seem to glow in the dimly lit ballroom. She wears a black uniform with silver accents, and a sword on her belt, ready to protect anyone who might need her help.

But Midjourney demands she be some kind of catwoman:

<img src="/media/world-building-with-gpt-2/Ian_Full_body_fantasy_portrait_of_a_masked_figure_Kiera_Ironcla_71be9073-8960-435a-8203-61f74f634aff.jpg" title="Full body fantasy portrait of a masked figure: Kiera Ironclad stands tall and proud, with a muscular build and a stern expression. Her steel mask covers her face, except for her piercing blue eyes that seem to glow in the dimly lit ballroom. She wears a black uniform with silver accents, and a sword on her belt, ready to protect anyone who might need her help" class="content">

I tried to use "stocky build" to encourage an entirely different body type, and while Midjourney did tone itself down a little it definitely didn't hear me:

<img src="/media/world-building-with-gpt-2/Ian_Full_body_fantasy_portrait_of_a_masked_figure_Kiera_Ironcla_3671f845-8748-4beb-921c-9dec950f2b12.jpg" title="Full body fantasy portrait of a masked figure: Kiera Ironclad stands tall and proud, with a muscular and stocky build and a stern expression. Her steel mask covers her face. She wears a loose black uniform with silver accents, and a sword on her belt" class="content">

In part it's probably picking up on video game aesthetics. Stable Diffusion (v2.1) is only worse:

<img src="/media/world-building-with-gpt-2/getimg_ai_kiera1.jpg" title="Stable Diffusion v2.1: Full body fantasy portrait of a masked figure: Kiera Ironclad stands tall and proud, with a muscular and stocky build and a stern expression. Her steel mask covers her face. She wears a loose black uniform with silver accents, and a sword on her belt" class="content">

<img src="/media/world-building-with-gpt-2/getimg_ai_kiera2.jpg" title="Stable Diffusion v2.1: Full body fantasy portrait of a masked figure: Kiera Ironclad stands tall and proud, with a muscular build and a stern expression. Her steel mask covers her face, except for her piercing blue eyes that seem to glow in the dimly lit ballroom. She wears a black uniform with silver accents, and a sword on her belt, ready to protect anyone who might need her help" class="content">

I thought I had discovered a better generation when another woman guard was giving a more appropriate portrait, only to find that GPT had changed this character's pronouns from "she" to "they" when creating the portrait prompt. Unexpected, but effective:

<img src="/media/world-building-with-gpt-2/Ian_Sable_Nightshade.jpg" title="Full body fantasy portrait of a masked figure: The person known as Sable Nightshade stands tall and with a confident stance. They have sharp features, including a strong jawline and piercing eyes that seem to glow in the darkness. Adorned with a mask made of dark leather and sharp spikes, they wear clothing that is practical and allows for ease of movement. The person's hair is dark and wild, adding to their fierce appearance." class="content">

In another example:

This person's description:

> Long, silver hair that falls in gentle waves down her back_ and _she wears a flowing, white gown that glimmers in the soft light_.

GPT went overboard with this description but didn't actually give her any body type or age in the description. She comes out like this:

<img src="/media/world-building-with-gpt-2/Ian_Full_body_fantasy_portrait_of_a_masked_figure_The_person_kn_ca219878-5716-4ed4-aeff-686b302e309e.jpg" title="Full body fantasy portrait of a masked figure: The person known as Luna Dreamweaver is a young woman with long, silver hair that falls in gentle waves down her back. Her mask is intricately designed, with delicate curves and moonstones that catch the light. She wears a flowing, white gown that glimmers in the soft light of the mushroom under which she performs, and her eyes hold a mysterious and captivating gaze" class="content">

Like race it might be possible to tone this down by asking GPT to make specific statements.

Another possible cause is that Midjourney reads some fairly innocuous-sounding terms in a very specific way. For instance "glowing eyes" will make anything evil.

Here's a character _Iron Giant_ with glowing eyes:

<img src="/media/world-building-with-gpt-2/Ian_Full_body_fantasy_portrait_of_a_robot_The_Iron_Giant_is_a_m_2117b9a5-9609-4957-8bbc-d23011c4863e.jpg" title="Full body fantasy portrait of a robot: The Iron Giant is a massive automaton made of gleaming silver metal plates with rivets and gears visible all over his bulky frame. He has elongated arms and massive legs, making him look like a giant among giants. The most striking feature of the Iron Giant is his glowing red eyes, which seem to pierce through anything in its path" class="content">

And without:

<img src="/media/world-building-with-gpt-2/Ian_Full_body_fantasy_portrait_of_a_robot_The_Iron_Giant_is_a_t_dd99e1b2-7c52-4bab-b8ce-723abc9d7acc.jpg" title="Full body fantasy portrait of a robot: The Iron Giant is a towering automaton that acts as a backup power source for the Steamworks. He has a massive steam engine built into his chest that can generate enough power to run the entire city if necessary. The Iron Giant is slow and ponderous, but nearly indestructible" class="content">

So GPT may be producing terms that seem neutral but infer more than we want.

Another way to think about this: Midjourney, more than the other image generators, has a strong feedback loop of human preference. I suspect that's why it has such a good default style, it's not just learning to be accurate to the prompt but it's also learning to make something compelling _with_ the prompt. And what do people like? Beautiful people! That's basically what "beautiful" means! In a single image I, of course, am not immune to the same appeal. But it gets old, incongruous, and lacks authenticity to an imagined world.

### <span id="fancy">Everyone's fancy</span>

I have to accept some blame for this, I did imagine a fancy city where people wear fancy stuff, but Midjourney takes it too far. Midjourney likes fancy, everyone likes fancy pictures, they are very impressive. But not every person is impressive!

For instance, here's Lorelei Moondrop. She's a box office clerk; not a sorceress or etherial being, just a box office clerk:

<img src="/media/world-building-with-gpt-2/Ian_Full_body_fantasy_portrait_of_a_masked_woman_The_person_in__2b4aac41-e647-4bd1-9ea6-6ba811a0cbfd.jpg" title="Full body fantasy portrait of a masked woman: The person in the picture is a young woman wearing a mask made of smooth wood. She has long, dark hair that cascades down her shoulders. She wears a simple, yet elegant dress that flows to her feet, with intricate patterns of stars and moons adorning it" class="content">

The description doesn't call for this:

> The person in the picture is a young woman wearing a mask made of smooth wood. She has long, dark hair that cascades down her shoulders. She wears a simple, yet elegant dress that flows to her feet, with intricate patterns of stars and moons adorning it.

What I did wrong here is to ask GPT to only focus on the characters appearance, given the character description. And it does suffer from a bit of [purple prose](https://en.wikipedia.org/wiki/Purple_prose) (purple prompting?), which Midjourney in turn picks up on (e.g., "simple, yet elegant dress that flows to her feet").

I think I might do better to ask GPT to fill out a kind of template, like:

```text
Race: [black/white/Asian/South Asian/etc]
Social class: [homeless/noble/working class/bourgeois/etc]
Job: $jobType
Job location: [where $jobType typically is held]
Visual description: [A description of the person in the form of a picture, set somewhere typical for $jobType. Focus on visual details and keywords. Use 2-3 sentences]
```

Then I give Midjourney only the visual description but having prepped it with a wider awareness of the character. In some early testing this seems to help quite a bit with male characters, but female characters are much more resistant to de-prettification.

## <span id="buildings">Buildings</span>

Buildings are a lot easier: no demographics or biases here!

In my [last post](https://ianbicking.org/blog/2023/02/world-building-with-gpt.html) I focused on isometric images of buildings. This time I went for street views:

<img src="/media/world-building-with-gpt-2/Ian_Moon_Jelly_Sanctuary.jpg" title="Digital fantasy art street view of a building from the front: The Moon Jelly Sanctuary is a small, circular building with a thatched roof made of woven seaweed. The walls are made of a translucent material that allows visitors to see the inside of the sanctuary and the moon jellyfish swimming in the aquarium. The entrance is marked by a simple wooden door with a moon jellyfish emblem carved into it. The building is surrounded by a small garden of bioluminescent flowers and plants." class="content">

There's a lot left to explore in how buildings are presented. There's a couple things we want to do:

1. Instantiate the _idea_ or _description_ of a building in a concrete form
2. Give a vibe to the characters and events in that building
3. Create an anchor, a sense of place, something to remember
4. Make the location feel alive
5. Support navigating among these buildings

Street view gives some sense of entering the building. Isometric is great for navigation, and by normalizing buildings to an isometric format I think it can make them more approachable.

For _being_ in a building you probably want an interior. But what makes that interior come alive? Not _real_, but present, concrete. I sense a problem where the eye just floats over these images, places, and characters. They are fancy, even dramatic, but not engaging.

I think there may be other, more structured ways to present these buildings. To make things comprehensible in terms of theme and variation. This is one benefit of character classes: you get a category to put someone in, then you can define them in terms of how they defy that category.

[Kris Kashtanova](https://twitter.com/icreatelife) shared a [prompt](https://twitter.com/icreatelife/status/1638053494010662912) that created level designs and it added another interesting lens on these buildings. Here's the street view of [Moonbeam Manor](https://veilvale.ianbicking.org/#/neighborhood/Moon%20Garden%20Heights/building/Moonbeam%20Manor):

<img src="/media/world-building-with-gpt-2/Ian_Moonbeam_Manor.jpg" title="Digital fantasy art street view of a building from the front: Moonbeam Manor is a three-story building made of dark wood with a thatched roof that seems to glow in the moonlight. The walls are covered in silver and purple vines that seem to climb up to the roof, and the windows are adorned with intricate silver frames. The entrance is marked by a silver doorknob in the shape of a crescent moon, and a small garden of moonflowers blooms at the foot of the steps." class="content">

And here is its level design:

<img src="/media/world-building-with-gpt-2/Ian_Moonbeam_Manor_level.jpg" title="Platform game level design cross section with multiple rooms, simple, naive, silhouette: The interior of Moonbeam Manor is a mix of old-world charm and mystical enchantment. The ground floor has a grand entrance hall with marble floors and a sweeping staircase leading up to the upper floors. The first floor has a parlor with plush velvet chairs, a library filled with leather-bound books, and a laboratory with bubbling potions and arcane instruments. The second floor has a bedroom with a four-poster bed draped in silk, a dressing room with a vanity table and a full-length mirror, and a balcony with a view of the moonlit gardens. The overall feel is one of ethereal beauty and otherworldly knowledge." class="content">

The second image is much less realistic but feels embodied in a much more concrete way. Even if you can't walk around it, that interior image tells a story that an image from a realistic perspective cannot.

But you can use entirely different styles, exploring with only changes to the prompt text:

<img src="/media/world-building-with-gpt-2/Ian_isometric_digital_illustration_50_cross-section_of_The_inte_c09c1a22-bd51-455b-b545-610524d90655.jpg" title="isometric digital illustration 50% cross-section of The interior of Moonbeam Manor is a mix of old-world charm and mystical enchantment. The ground floor has a grand entrance hall with marble floors and a sweeping staircase leading up to the upper floors. The first floor has a parlor with plush velvet chairs, a library filled with leather-bound books, and a laboratory with bubbling potions and arcane instruments. The second floor has a bedroom with a four-poster bed draped in silk, a dressing room with a vanity table and a full-length mirror, and a balcony with a view of the moonlit gardens :: highly detailed, hyper realistic, cinematic lighting, professional color grading --s 500 --ar 16:9" class="content">

There's many ways to tell a visual story, and a lot to explore here.

# <span id="chatting">Chatting with your creations</span>

One of the great things about doing stuff with GPT is that it's a sort of everything engine. So once it's set up to invent characters it's also easy to add a chatbot or whatever else.

I added another step to turn a character description (with all the rest of the context) into a chat prompt, and then a simple chat interface. Here's an example of the prompt built from a character:

<img src="/media/world-building-with-gpt-2/Ian_thorne_nightshade.jpg" title="Full body fantasy portrait of a masked figure: Thorne Nightshade is a middle-aged person with sharp, angular features. Their mask is made of black leather with two holes for the eyes and a slim, pointed beak that resembles that of a crow. Their eyes are sharp and piercing, and their expression is inscrutable." style="float: right; width: 30%; border-radius: 5px; margin-right: 4px;">

> **Character description:** Thorne Nightshade is a mysterious and enigmatic representative of the Shadow District in the Senate. He rarely speaks in public and prefers to work behind the scenes, using his network of spies and informants to gather intelligence on his rivals. His mask is made of black leather and has a slim, pointed beak that resembles that of a crow.

> **Chat prompt:** Thorne Nightshade is a representative of the Shadow District in the Labyrinthine Senate. He is known to be a mysterious and enigmatic figure who prefers to work behind the scenes rather than speak in public. He wears a mask made of black leather with a slim, pointed beak that resembles that of a crow. If you were to speak with Thorne, he may speak in a hushed tone and ask pointed questions to gather information. He is highly observant and analytical which can make him appear unapproachable at times, but if he deems you trustworthy, he can be a valuable ally in navigating the political landscape of Veilvale.

Combine that with some context and instructions and you get a surprisingly good chat! By creating a chat prompt you are asking GPT to infer more conversation-related details; perhaps it could infer these directly from the character description, but those inferences may not be stable. By generating and storing a prompt the personality becomes stable.

One important addition is that after every user message I append the user's actual message with "Respond as the character [name]". This is effectively a high-powered reminder to stay in character. Note that GPT has no real history, and so I only append this to the user's latest message, leaving it off of earlier messages.

Here's an example chat with one of the city's automatons, an abrasive character that is still dedicated to keeping the city in good repair:

<img src="/media/world-building-with-gpt-2/Ian_rusty.jpg" title="Full body fantasy portrait of a masked figure: Rusty is a tall, metallic figure made of silver and brass with intricate, interlocking gears visible through their chest cavity. Their face is stern and angular, with a crooked nose and piercing, glowing eyes that seem to peer right through you. Despite their age, Rusty's joints are still smooth and well-oiled, and their hands are calloused from years of precise tinkering." style="float: right; width: 30%; border-radius: 5px; margin-left: 4px;">

> **Player:** hello there <br />
> **Rusty:** Hmph, what do you want? Can't you see I'm busy here? <br />
> **Player:** I want to know the way through the maze <br />
> **Rusty:** Bah, the maze? That's child's play. If you can't figure it out yourself, then you're not worth my time. Besides, I'm not here to hold your hand and guide you through every little obstacle in this city. I have more important things to do, like fixing broken machines and keeping Veilvale's technology up and running. So if you'll excuse me, I have work to do. <br />
> **Player:** I have to get through the maze to fix an important machine <br />
> **Rusty:** Oh, I see. Well, that changes things. If you need to fix an important machine in the maze, then I suppose I can offer some assistance. But don't expect it to be easy. The maze is designed to be tricky and not everyone comes out unscathed. However, since you seem to have a sense of purpose, I'm willing to help you out. But first, I need to know what kind of machine you're fixing and what tools you'll need. Give me the details and we can start planning our strategy to get through the maze.

## <span id="characters-floating">Characters floating in space</span>

While it's cool to chat with the characters, it suffers from the same problem of most GPT chatbots created for entertainment: nothing matters.

I picture it like the character is sitting in a featureless room, expression blank, no desires or plans, simply waiting. You sit down across from this character, it looks at you but says nothing, just waits.

<img src="/media/world-building-with-gpt-2/Ian_Sci-fi_inspired_blank_and_featureless_white_room_harsh_ligh_9d2778b8-8f3a-4883-a1b8-abd6dd7f41e6.jpg" title="Sci-fi inspired blank and featureless white room, harsh light, Benjamin Franklin sitting in a folding chair, staring placidly at the wall" class="content">

"Hello," you say. The character lights up, engages you in discussion. But the character will not leave the room, will not leave the chair. They will act as though they are real, as though everything you say matters. Until you ask them to leave the chair. Maybe if you try hard enough they'll even agree to leave the chair. But they will never leave the chair.

When you are done you stand up. The character still sits, eager anticipation on their face. As you leave the room you look back and they are still there, making eye contact with the void that you have left, poised and always ready.

At first it still seems fun, but the not-mattering will drain you.

This is not fatal, [GPT can simulate arbitrary actions](https://www.youtube.com/watch?v=nsIPC_eqfwg) or perhaps judge [specific criteria in the conversation](https://www.youtube.com/watch?v=X0x_W8YWAg8). But while it's easy to build an isolated experience, these meaningful experiences are more difficult. But they'll be worth it!

## <span id="extending-chat">Chatting about... anything</span>

Something my daughter came upon while playing around with the city: she happened into the [Academy](https://veilvale.ianbicking.org/#/faction/The%20Labyrinthine%20Academy/person/Evangeline%20Nightshade) and wanted to learn about her astrological sign. And because GPT is an everything machine it actually knows all about that (though it's cagey on making real predictions). I realized it could also teach math or anything else right in that same interface. It's not _free_ to do this, but the latent ability is there with some effort. And so you could have an in-game school where the player could learn and demonstrate real skills.

# <span id="plots">Plots</span>

Things _happen_ in an embodied world. This world definitely isn't embodied yet, but it feels like there's opportunities to move in that direction.

With this in mind I have tried a couple plot generation approaches...

## <span id="summary-selection">Building plots with: summary, selection, events</span>

In this model GPT makes suggestions at different levels. First it offers rough outlines of a story:

> **The Missing Heir**: The heir to the Labyrinthine Senate has disappeared within the maze, and now the Senate is offering a reward for their safe return. However, rumors say that the Razormaws are behind the kidnapping, and the Cult of the Moon Goddess is secretly aiding them.

Once you've selected a plot GPT will take the summary and a list of all the characters, producing a suggestion of some characters and their roles in the story. Everyone gets a plot-specific role, but it can also create entirely new characters to serve plot roles, for instance:

> **Eliana Silvermist**: Eliana is a young artist who is enamored with the legend of the Night King. She is unwittingly drawn into the cult's plan when they mistake her for the missing heir.

Then less interestingly it picks out some relevant locations. This gives GPT a smaller set of things to work with as it develops the actual events.

The event list is where a plot really develops. Right now it's listed as a kind of straight list of events for you to pick and choose from. That's questionable, and assumes freestanding events that tie into an arc but don't tie into each other. But that still works okay... the character descriptions create a framework that GPT fills in.

> **The Night King's Lair**: The investigators discover the Night King's lair within the maze, filled with strange artifacts and esoteric books. <br />
> Characters: Thorne Nightshade, Aurora Sky <br />
> Locations: The Lost Grove <br />
> Time: 10 days

I can imagine applying these events to the world on a kind of schedule. If the world just ticks through the events then we're saying the player has no real agency, events will transpire inevitably. But if this event generation is automated at a high enough quality then we can synthesize new events based on player action and ask GPT to again complete a new set of events. I think by looking ahead, even if it means creating events that will never come to pass, we can make GPT create both a satisfying arc and conclusion, and _remake_ that arc and conclusion in response to the player.

## <span id="murder-mysteries">Murder Mysteries</span>

My daughter suggested this after doing some chats with the characters, imagining that she could grill people and then accuse someone of being the murderer.

Murder mysteries are appealing because they have a very clear setup (a murder!) and a moment of obvious player participation: soon after the murder is discovered, with only intermittent action outside of the investigation.

In my first attempt I asked GPT to write a muder mystery, but (as is typical with GPT) it didn't know where to stop. It invented detectives and red herrings and an action packed conclusion. No need for a player! But that's not what I want.

So instead I kept it to the facts, with GPT as the omniscent narrator. Identify exactly who did it, why, when, how; identify other people with a motive; identify events leading up to the murder. I give it a template to fill out, avoiding a narrative voice.

> **Victim**: Marina Rossi <br />
> **Murderer**: Hector Stone <br />
> **Means of murder**: Poisoned wine <br />
> **Location of murder**: Marina's Crafts <br />
> **Time of murder**: 9pm <br />
> **Motive**: Marina discovered that Hector had been sabotaging The Stonemason's Workshop, which had resulted in several accidents and injuries. In order to silence Marina, Hector murdered her. <br />
> **Description**: Marina was having a glass of wine after closing up her shop when Hector entered. They were talking for a while, and Marina suddenly appeared to be feeling ill and collapsed. Hector quickly left the scene.

This goes on at some length, fleshing out a wide variety of facts in one go. The intention here isn't to have the author/user do much, but instead create a hands-free automatic murder mystery.

The factual source material then gets parsed in a second pass, pulling out specific information that needs to be used to construct later prompts, such as the victim's exact name.

The last (still poorly implemented) step is to indicate what each character knows. That is, all the subjective knowledge that the player will piece together to discover the truth. Maybe this alone is enough for a playable game?

> **Eira Trefor**: knows that Marina confided in her about her suspicions of Hector and sought her advice at The Seafarer's House at 6pm on the day of the murder. Eira advised her to speak to the authorities and not to confront Hector alone. <br />
> **Vladimir Kuznetsov**: witnessed Marina receiving a gift from an anonymous sender (a bottle of wine) at her shop an hour before the murder, but did not see who the sender was. Vladimir may also know about Marauder Jones's thieving tendencies.

I've only used GPT-4 sparingly on this project, but there are steps in this plot generation where it might perform significantly better, especially when given a large task.

# <span id="authoring">The authoring process</span>

While much of the authoring experience is the same as [I wrote about before](https://ianbicking.org/blog/2023/02/world-building-with-gpt.html), there are things I noticed because I generated _so much more_ world.

## <span id="rule-of-cool">The Rule Of Cool</span>

The [Rule Of Cool](https://tvtropes.org/pmwiki/pmwiki.php/Main/RuleOfCool):

> all but the most pedantic of viewers will forgive liberties with reality as long as the result is wicked sweet or awesome

The authoring process is one where GPT throws out a bunch of ideas and you pick the ones you like, over and over. If you don't like the ideas you can add suggestions, even simple suggestions like "make it weird." I did this a lot!

As a result GPT is constantly tempting the author with awesome stuff. I happily went along...

<img src="/media/world-building-with-gpt-2/soul-music-echo-soundwave.jpg" title="Full body fantasy portrait of a robot: Echo Soundwave has a silver metalic body and plays a variety of instruments | Cover of the book Soul Music: Death playing an electric guitar with a piece of his shattered scythe as the pick" class="content">

Some of the things GPT tempted me into:

1. A desert neighborhood called Shifting Sands where shape-shifters practice their arts. I don't know where these shape-shifters came from, but that sounds awesome! Later I would realize that you can't fit a desert _inside_ a city.
2. Bioluminescent Bay, that's cool right? Again, physically unclear, but how can I say no to glowing marine life...
3. It all started with this prompt: _A city in the center of a maze 🌀, where travelers often lose their way and the locals always wear masks to hide their true identities_. That sounds awesome! But integrating a maze structure is very hard and got lost in the generation. (I went long on masks though.)
4. Silver Haven: _for those who seek refuge and peace, a sanctuary where automatons are created to aid those in need._ Robotic therapists seemed pretty on point for this moment so I couldn't pass it up. But it ended up as a kind of bland retreat.

## <span id="gpt-dice">GPT does not roll fair dice</span>

This authoring process relies on GPT coming up with unique and creative ideas. It's pretty good at this, but what it does well for one attribute can feel repetitive when it happens over and over.

For instance in Veilvale there are 29 people (out of 370) with the last name "Nightshade". It's a cool name I suppose, but not that cool. In another experiment [Colin Fraser asked GPT for a random noun](https://twitter.com/colin_fraser/status/1641191388502163457) and it returned "Pineapple" 11% of the time.

The cool thing with something like name generation is that it can create punny combinations, like _Sage Pepper_ for a cook, and other less obvious names that still rhyme with the spirit of the character.

But sometimes we don't want randomness so much as _distribution_. It's not to say that we only ever want one distribution, but just a conscious explicit distribution.

Also there should only be one, or at least no more than a couple "best cooks". GPT isn't the only one who is drawn to hyperbole, so it's fine if some things are overstated, but you can't make every character exceptional. You can still make every character unique! But you need to make them unique on a variety of spectrums.

I'm not quite sure how to resolve this. Maybe pre-roll some core things and then seed the prompts with the results. But I don't have any clear answer for the hyperbole.

## <span id="people-context">People existing in and out of a context</span>

Because of the hierarchical composition process all people "belong" somewhere:

1. Factions have faction members. Faction members are created specifically in the context of their one faction.
2. Buildings have occupants. The person is built to occupy a building.
3. Plots can add new characters that serve a purpose in the plot.

An alternative might be to create a pool of people and then assign them, adjusting descriptions to fit their new home. Maybe that would be better, but I think giving GPT the freedom to create characters for a specific purpose is the right choice.

But it's not the right choice that it ends there. A few problems:

1. People don't relate to each other. When GPT creates a single list of characters it can and does relate them sometimes, for instance introducing a leader and an assistant. But that's just an accidental feature. _Density of narrative_ is a feature that's missing from this process, there aren't enough loops, enough serendipitous relationships. Even in a large city you should keep bumping into the same people for different reasons. That might not be realistic but it's _enjoyable_.
2. There's no one schema for people. People in buildings have a property that relates them to the building (like a job). People in factions have a role. "Protagonists" (narrative free agents) have a heroic archetype. I don't think we want to overspecify people and demand that all attributes be filled in, but it makes the coding harder when each character is only half-filled-out.

[Dustin Freeman](https://twitter.com/dustinfreeman) gave me the idea of doing this as a kind of fix-up: generate a cast of fully situated characters, but then start to add new properties and relationships. I'm imagining something like:

1. Create a list of characters. If there's too many for GPT to process then just sample a few randomly.
2. Ask GPT to suggest the basic outline of some relationships. E.g., "Tom and Eileen are brother and sister". Let GPT pick and choose who to match. Maybe the author selects which relationships to keep, or maybe they just scan and mass accept.
3. Represent the relationship formally somewhere.
4. Go back to each person and rewrite their description to include the relationship.

This could also be done with characters and factions (so building occupants can belong to factions, factions can own buildings, or people can belong to two factions).

I've done something like this experimenting with "faction relationships" (like, inter-faction squabbles) but it falls flat, usually explaining obvious tensions between factions. Maybe I'm doing it wrong, or maybe there's not enough material in that particular combination. (Maybe I need to focus on inter-factional _histories_ instead of _relationships_?)

## <span id="gpt-3-4">GPT 3.5 vs GPT 4</span>

The tool is built to default to use GPT-3.5 (the gpt-3.5-turbo API) for all requests. Lots of people are jumping on GPT-4, and I've now done some work with both, including places where 3.5 definitely wasn't sufficient for the task. But here I'm quite happy with GPT-3.5.

My general intuition is that GPT-4 is able to connect information across greater distances and to simultaneously follow a larger number of directions. This does come up, instructions can get lost as they accumulate. I think there's ways to solve that with 3.5, such as refining generic/universal instructions to just those applicable to certain domains. For instance some instructions only apply to buildings (like building material), others only to character generation (like demographics) and so on.

The overall development pattern for GPT-4 might also be different than 3.5. There's a lot of architecture that is there implicitly to keep down the size of any one prompt and response. With GPT-4 it may be possible to accomplish much more in one prompt, both because of a greater confidence in the output and because it's able to handle more complexity in the request.

That said, GPT-3.5 is pretty great and I'm reluctant to just switch to something that's bigger/better/slower/more-expensive.

# <span id="declarative">A declarative approach to building</span>

Inside the spaghetti code of City Maker was a much simpler idea waiting to come out, and this version is a complete rewrite of the previous code. I gave it the name [LayerCraft](https://llm.ianbicking.org/layercraft/) with [City Maker as a schema](https://github.com/ianb/llm-garden/blob/main/src/layercraft/citymakerschema.js). I don't know yet how widely applicable this approach is, but it feels like it's touching on patterns will be relevant for LLMs.

I'll try to explain it concretely using a city:

1. There's many properties: name, factions, people, neighborhoods, buildings
2. Some properties belong to others in a parent/child relationship, like buildings that belong to neighborhoods
3. For any property GPT can generate _options_
4. Generating these options requires a prompt; these prompts usually require context which creates _dependencies_. The prompts themselves are templates, dependencies are the substitution variables
5. Once a prompt can be fulfilled GPT is immediately asked about it, the author can make choices, commit choices, and thus produce new properties ready to be filled out

In practice for the City Maker this means you choose a theme for your city, then backstory, then you pick out some neighborhood types that are created based on that background, and so on.

The prompts themselves are constructed to elicit the best result from GPT. Good prompts:

1. Give the necessary context without giving too much distracting context
2. Show concrete examples that neither over-specify nor under-specify the desired results
3. Give GPT broad guidance ("exciting", "simple", etc)
4. Identify the schema for the results

For instance, the schema for building occupants:

```text
The city $cityName that is $cityType, $cityPeriod. $cityBackstory

A list of $building.jobTypes and other inhabitants for $building ($building.description). Give each person an interesting and culturally appropriate name and a colorful background and personality. Include negative attributes.

Respond with a JSON list like:

[
  {
    type: $building.jobTypes|first|repr|json, // Or $building.jobTypes|rest
    name: "FirstName LastName",
    description: "[a description of the person, their profession or role, their personality, their history]",
    age: 30, // age in years, 5-100
    arrives: "8am",
    leaves: "6pm",
  }
]
```

The building schema includes `jobTypes` which informs the example. The prompt _could_ just offer some generic advice, but I've found there's often an advantage in establishing options as part of the context.

The particular implementation of this in LayerCraft isn't half as general as this needs to be, but I'm very optimistic about the approach.

## <span id="updates-dependencies">Updates and dependencies</span>

Building up incrementally gives steering power to the author, but not correction. This is a common problem in the authoring process because it's hard to know the results of some of those early choices until you've seen what they've produced. And if you are creating dozens of characters based on these prompts you might not see the problems until you are halfway in.

If we treated this process as a pure question of dependencies, and treated the schema-defined graph like a Makefile, then changing early choices would simply regenerate later choices. But the author probably liked many of those choices!

As an example: I created a candy city. Part way through I realized it would be more fun if the characters were each made of candy. I didn't really want to change everyone's role, but only to make sure each description said what kind of candy the person was. I added an instruction to the backstory: "the people of Gummytown are made out of candy, with some being gummies, others being chocolates, and a few being marshmallows or candy canes. For each person specify what kind of candy they are in their description."

How do you tell which properties this applies to? How do you apply this change to those properties? GPT is capable of both of these things, but not in a deterministic or entirely reliable way. Fixing this is significant work and definitely needs to be present in the UI itself.

## <span id="meta-prompting">Getting meta in the prompt</span>

The use of context (such as backstory) lets the author broadly control what's being created, but it's often underpowered. It also can't change the _shape_ of what's returned, such as adding a new property to a JSON example.

You can do a lot with GPT prompts and concatenation. That is, you can "edit" a prompt by just adding more instructions. If those instructions conflict then GPT will try its best. This is usually enough, and why this entire approach works.

As an example where this worked: I added the request "describe each person's mask" to Veilvale person creation. It listened and consistently did so. But when I tried to give the instruction: "make it a list of automatons" it balked, confused by a previous instruction which clearly asked for _people_ and _automatons are not people_.

A next level is to put more of the core prompt material into properties. Yet the text of those prompt templates quickly turns into programming itself, a mode switch that's hard even for a programmer if you aren't in the driving seat.

If we turn back to GPT again to solve this we'll need meta-prompts: descriptions of what the prompt needs to accomplish, and its constraints, so that GPT can apply natural-language edits to the prompts while maintaining the required structure.

## <span id="planning">Planning & action</span>

While this is author-focused, I think the choices that GPT produces should be thought of as _proposed plans_. In City Maker it's offering plans for how to build out a world. The author chooses options (and edits and makes notes on options) to guide, correct, and expand on what GPT produces on its own.

If GPT was producing code instead of options that's also a plan. Sometimes you can build plans on plans, i.e., build more code just by looking at existing code. But often you need the output of that code to keep going. Or you need feedback, refinement, etc. I think there could be a pattern:

1. The author _specifies_ the goal
2. GPT _proposes_ up to the limits of that specification
3. The author _previews the results_
4. The author _adjusts, selects, refines_ the results, perhaps through choice, through dialog (chat), refined specification, etc
5. The choices are _committed_, expanding the specification
6. Any unresolved actions can be taken, code run, output collected, etc
7. Repeat at 2

Unfortunately this doesn't cover revision, as mentioned in the previous section, and I don't know exactly what adding that to the loop would look like.

## <span id="fine-tuning">I'm glad fine tuning is dead (for like a month)</span>

It's tempting with these problems to think about "fine tuning" a model. That's how AI has worked for a long time, and it feels like a good way to approach issues with reliability or ever-growing prompts that keep adding little instructions and caveats.

For now the fine-tuning option is off the table if you are using the gpt-3.5-turbo (what this uses) or gpt-4 APIs, which are chat-based and offer no finetuning. This probably won't last for long, but _right now_ you'll almost always get better (cheaper, faster, more flexible) results by using these new models and forgoing fine tuning.

This is the future I want to see! Everything I've described here _is not compatible with fine tuning_. You can't edit prompts and make sophisticated adjustments when the instructions are in the tuned model weights!

**Prompting is artisanal AI**. If you know something about a subject, and want to use that knowledge and your own sweat to iterate on a prompt, there is tremendous potential in prompt design. Prompt design isn't enough right now because tooling is still limited, but prompt-focused tools can give people new agency on a very individual level. I'm developing both sides of LayerCraft (the tool and the prompts) and I still feel empowered by this abstraction.

When proposing prompt-focused functionality lots of people are all like *blah blah blah, what about a moat, how do you differentiate yourself?* It's so self centered... there's a kind of thought that is addicted to consuming people rather than empowering them. Empowered people don't lay down and play the part of being your moat.

# <span id="conclusion">Conclusion</span>

It's hard to conclude this because this is just one step along the way. (To where?) Some things that stand out to me:

* GPT prompts matter. It's not just a matter of getting the prompt "right," it's iteration and exploration over a specific domain.
* When a user can enter text to affect a prompt they are also prompt engineering, and that's the magic of this technology.
* These same things are true for image prompts, but without the complexity of recursively applying output to future inputs.
* Natural language is now a data structure. We're probably all going to struggle to internalize this for a while.
* Steerability makes GPT a lot more fun than just gazing at its wise output.
* Chat is not the only way to interact with GPT.

If you want to try this yourself check out [llm.ianbicking.org](https://llm.ianbicking.org/layercraft/), or [check out GitHub](https://github.com/ianb/llm-garden). If you are curious about the exact prompts look in [citymakerschema.js](https://github.com/ianb/llm-garden/blob/main/src/layercraft/citymakerschema.js). Note that this is a personal project, it's built for personal exploration.

Similarly: when using the site be warned I have not built it carefully for other people to use, stuff will be weird, errors will appear only in the JS Console, there are no promises. And you'll have to bring your own GPT API key!

Comments welcome on [Mastodon](https://hachyderm.io/@ianbicking/110141107480811400) or [Twitter](https://twitter.com/ianbicking/status/1643265359967924226).

<script>

    let els = Array.from(document.querySelectorAll("img.content"));
    console.log("found images", els);
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
        img.src = el.src;
        img.style.maxHeight = "95%";
        img.style.maxWidth = "95%";
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
        caption.style.padding = "1px 10px";
        caption.style.bottom = "5px";
        caption.style.backgroundColor = "rgba(0, 0, 0, 0.6)";
        overlay.appendChild(caption);
        document.body.appendChild(overlay);
    }
    for (const el of els) {
        el.addEventListener("click", (event) => {
            activateEl(el);
        });
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
            const next = (els.length + cur + (event.key === "ArrowLeft" ? -1 : 1)) % els.length;
            console.log({cur, next, els, el: els[next]});
            activateEl(els[next]);
            event.preventDefault();
        }
    });

</script>

<style>
  img.content {
    border-radius: 5px;
  }
  #toc + ol, #toc + ol li ol {
    margin: 0 0 0 1.5em;
  }
  #toc + ol li, #toc + ol li ol li {
    margin: 0;
  }
</style>

<meta property="og:image" content="https://veilvale.ianbicking.org/assets/images/icon-128.png" />
<meta property="og:image:width" content="128" />
<meta property="og:image:height" content="128" />
