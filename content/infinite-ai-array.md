Title: Infinite AI Array
Category: ai
Date: 2023-01-02
Slug: infinite-ai-array
cover_image: infinite-ai-array-logo.png
header_style: background-color: rgba(255, 255, 255, 0.5)

<center><blockquote class="twitter-tweet"><p lang="en" dir="ltr">making new string and list classes that call gpt3 under the hood so you can access elements beyond the final one. no more index errors!</p>&mdash; shb (@himbodhisattva) <a href="https://twitter.com/himbodhisattva/status/1606712418587267072?ref_src=twsrc%5Etfw">December 24, 2022</a></blockquote></center> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Some ideas are dumb enough you just have to try them, so I introduce to you the Python library: [Infinite AI Array](https://github.com/ianb/infinite-ai-array). Let's see it in action...

```python
$ pip install git+https://github.com/ianb/infinite-ai-array.git
$ export OPENAI_API_KEY=sk-...
$ python
>>> from iaia import InfiniteAIArray, InfiniteAIDict
>>> primes = InfiniteAIArray()
>>> primes[:10]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> minnesota_cities = InfiniteAIArray()
>>> city_populations = InfiniteAIDict()
>>> for i, city in enumerate(minnesota_cities[:6]):
...     print(f"{i+1:>2}. {city:<20} {city_populations[city]}")
 1. Minneapolis          422331
 2. St. Paul             302551
 3. Duluth               87622
 4. Rochester            111264
 5. Bloomington          84863
 6. St. Cloud            68320
```

Or more contextual...

```python
>>> favorite_books = InfiniteAIArray(["Dune", "Perdido Street Station", "Red Mars"])
>>> favorite_books[:8]
['Dune', 'Perdido Street Station', 'Red Mars', "The Hitchhiker's Guide to the Galaxy", '1984', 'The Lord of the Rings', "The Handmaid's Tale", 'The Martian Chronicles']
>>> other_favorite_books = InfiniteAIArray(["Wizard Of Oz", "The Trials Of Morrigan Crow", "James and the Giant Peach"])
>>> other_favorite_books[:8]
['Wizard Of Oz', 'The Trials Of Morrigan Crow', 'James and the Giant Peach', 'The Catcher in the Rye', 'The Lion, the Witch and the Wardrobe', 'The Hobbit', 'To Kill a Mockingbird', 'The Alchemist']
```

## The Problem Statement

All great tools _solve a problem_.

-   Lists end
-   Dictionaries don't have every key
-   I don't have enough ideas
-   List operations usually happen right away and sometimes I'd like them to take a second or two so I can appreciate the effort involved in programming
-   My types and values are consistent like a program, not expressive and eclectic like natural language

## But wait, there's more!

```python
>>> from iaia import magic
>>> magic.first_wikipedia_paragraph("Minneapolis")[:80]
Missing imports: wikipedia
  To install (gessing):
     pip install wikipedia
Do it now? [y/N]
y
... installation ...
'Minneapolis ( (listen)) is the largest city in Minnesota, United States, and the'
>>> print(magic.first_wikipedia_paragraph) # see what it's doing
def first_wikipedia_paragraph(arg1: str): ...
```

Who knew there was a `wikipedia` package? (GPT knew, but I did not.)

Let's make it more like a chat, and circle in on our answer...

```python
>>> magic.primes(10)
[2, 3, 5, 7]
>>> # We wanted the first 10 primes, not the primes up to 10, let's try...
>>> magic.primes(count=10)
[2, 3, 5, 7]
>>> magic.primes(quantity=10)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> # We did it! Now let's stretch it...
>>> magic.primes(quantity="11")
Attempting to fix exception '<' not supported between instances of 'int' and 'str'...
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
```

## Extending the problem statement

-   So many functions haven't been written
-   Maybe functions should be more of a... negotiation?
-   Function signatures tell a story but the computer hasn't been listening
-   All exceptions are bad and should be eliminated
-   Old security holes don't offer us enough excitement, we need to explore new frontiers of vulnerabilities

## But really, how does it work?

To see what's happening just set `$IAIA_VERBOSE` or run `iaia.set_verbose(True)`. You'll see the GPT queries printed out. For lists they look like this:

```python
>>> books = InfiniteAIArray(["Les Misérables"])
>>> books[1]
Request 1: temperature=0.5
A list of 2 items, created with the code `books =  ...# books`:

1. Les Misérables
2.
------------------------------------------------------------ Response
 The Catcher in the Rye
Stop reason: stop
Response time: 1.23s
Tokens used: 30+6  total: 36 + cached: 0 = 36 ($0.0007 w/o cache $0.0007)
'The Catcher in the Rye'
```

In my experience GPT thinks very highly of _Catcher in the Rye_.

Dictionaries are similar:

```python
>>> authors = InfiniteAIDict()
>>> authors["Les Misérables"]
Request 2: temperature=0.5
A list of name: value pairs, created with the code `authors =  ...# authors`:


1. Les Misérables:
------------------------------------------------------------ Response
 Victor Hugo
Stop reason: stop
Response time: 1.04s
Tokens used: 30+2  total: 68 + cached: 0 = 68 ($0.0014 w/o cache $0.0014)
============================================================
'Victor Hugo'
```

Functions are based on the signature:

````python
>>> iaia.magic.arctan(1.0)
Request 1: from cache
Create a function named `arctan`:

```
def arctan(arg1: float):
------------------------------------------------------------ Response

    """
    Calculates the arctangent of a given number.

    Parameters:
    arg1 (float): The number to calculate the arctangent of.

    Returns:
    float: The arctangent of the given number.
    """
    return math.atan(arg1)
``
Stop reason: stop
Tokens used: 25+76 total: 0 + cached: 0 = 0 ($0 w/o cache $0)
============================================================
````

You'll notice in this case it uses the `math` module but doesn't import it. This causes an exception which is caught and GPT is asked to fix it:

````
The following function throws an exception NameError: name 'math' is not defined
At the line `return math.atan(arg1)`

```
(function definition)
```

The same function but with the NameError exception fixed:

```
````

It tries one time to fix an exception, though if you keep calling the function using the same signature it will try each time to get rid of the exceptions and may incrementally succeed. Though with this prompt it tends to cover up errors as often as fix them.

## Following up...

Comments welcome on [Mastodon](https://hachyderm.io/@ianbicking/109621627461377616), [Twitter](https://twitter.com/ianbicking/status/1610018555222695936), [Hacker News discussion](https://news.ycombinator.com/item?id=34224664). Contributions [kind of welcome](https://github.com/ianb/infinite-ai-array#contributing).

If you've gotten this far I will also throw in here that I ([Ian](https://ianbicking.org)) am looking for a job, and maybe the best job for me is one that I don't yet know exists. I'm particularly interested in the area of large language models (not just as a joke), new user interactions built on LLMs (especially their abilities to understand us in new ways). I'm excited about education, aiding in executive function, and human-centered interactions. [Let me know if you have ideas](mailto:ianbicking@gmail.com), I would appreciate it!
