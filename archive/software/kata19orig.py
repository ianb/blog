#!/usr/bin/env python
import sets
import sys
import time
import os

# This is how many words are in my dictionary, for progress reports
total_words = 96274
# And this is where my dictionary is kept:
default_dictionary = '/etc/dictionaries-common/words'

# The "ones" are the words missing a letter, like for "python":
#  _ython, p_thon, py_hon, pyt_on, pyth_n, pytho_.
# This is a dictionary of '_ython': ['python']
all_words_by_one = {}
# This is 'python': ['_ython', 'p_thon', ...]
all_words_to_one = {}

def load_words(file=None):
    """
    Loads words from a dictionary
    """
    words_done = 0
    start = time.time()

    if file is None:
        file = default_dictionary
    if isinstance(file, str):
        file = open(file)

    for line in file:
        word = line.strip().lower()
        if not word: continue
        if "'" in word:
            # Words sometimes have apostrophes, but we don't want that
            word = word.split("'")[0]
        to_one = sets.Set()
        for i in range(len(word)):
            shortword = word[:i] + "_" + word[i+1:]
            to_one.add(shortword)
            if not all_words_by_one.has_key(shortword):
                all_words_by_one[shortword] = sets.Set()
            all_words_by_one[shortword].add(word)
        all_words_to_one[word] = to_one
        
        words_done += 1
        if not words_done % 100:
            sys.stdout.write('\r%5i/%5i (%3i%%) done...' % \
                             (words_done, total_words,
                              100*words_done/total_words))
            sys.stdout.flush()

    sys.stdout.write('\rdone, %.1f secs.' % (time.time()-start)
                     + ' '*20 + '\n')
    file.close()

def check_spelling(word):
    return all_words_to_one.has_key(word)

def lookup(word1, word2, verbose=1):
    """
    Finds the shortest path from word1 to word2, where each word on
    the path differs from the one before by one letter.  Returns
    a list of paths, including all the paths that tie.  So it might
    be something like:
        [['tub', 'hub', 'hue', 'hoe'],
         ['tub', 'hub', 'hob', 'hoe']]
    If verbose is true, then print a status message each time it
    increases the depth of the search by one.
    """
    assert len(word1) == len(word2), "Words must be of the same length"
    # We search from both ends at once.  "found" is a set of words that
    # we can connect to the source (found1 to word1, found2 to word2).
    # If there's any interection between found1 and found2, then we
    # have a path.  "trace" is a dictionary that gives the path from
    # any word in found to the original word.  E.g.,
    #   trace1['hob'] = ['hub', 'tub']
    found1 = sets.Set()
    trace1 = {word1: []}
    found2 = sets.Set()
    trace2 = {word2: []}
    seen1 = sets.Set()
    seen2 = sets.Set()
    # Seeding our list:
    found1.add(word1)
    found2.add(word2)
    level = 1
    # We increase the depth of word1, then word2, then word1 again...
    # switching on this variable.
    next_found1 = True
    
    while 1:
        intersect = found1.intersection(found2)
        if intersect:
            print 'Got an intersection on %s' % ', '.join(intersect)
            # We got a match...
            results = []
            for word in intersect:
                trace1[word].reverse()
                results.append(trace1[word] + [word] + trace2[word])
            return results

        if next_found1:
            found = found1
            trace = trace1
            seen = seen1
        else:
            found = found2
            trace = trace2
            seen = seen2
        found, trace = add_one_off(found, trace, seen)
        if next_found1:
            trace1 = trace
            found1 = found
        else:
            trace2 = trace
            found2 = found

        next_found1 = not next_found1
        level += 1

        if verbose:
            print "Checking level: %2i, %3i words (%3i,%3i), %4i seen" \
                  % (level,
                     len(found1)+len(found2),
                     len(found1), len(found2),
                     len(seen1)+len(seen2))
            if verbose > 1:
                print "Words:"
                print "  * ", ", ".join(found1)
                print "  * ", ", ".join(found2)
        if not found1 or not found2:
            print "There is no path from %s to %s" % (word1, word2)
            return []

def add_one_off(source, trace, seen):
    """
    Returns a new trace and new `found` set, based off source (the
    previous `found` set).  Words in `seen` have already been used
    before, so we can ignore those.
    """
    new_trace = {}
    dest = sets.Set()
    for word in source:
        for subword in all_words_to_one[word]:
            for destword in all_words_by_one[subword]:
                # `destword` is all the words that are one step away
                # from `word`
                if destword not in seen:
                    dest.add(destword)
                    new_trace[destword] = [word] + trace[word]
                    seen.add(destword)
    return dest, new_trace

def wordspace(source):
    """
    Returns a set of all the words that are connected to the source
    word by any path of any length.  All the words in the set are
    interconnected.
    """
    seen = sets.Set()
    words = [source]
    while 1:
        new_words = []
        for word in words:
            for subword in all_words_to_one[word]:
                for destword in all_words_by_one[subword]:
                    if destword not in seen:
                        seen.add(destword)
                        new_words.append(destword)
        if not new_words:
            break
        words = new_words
    return seen
        
def reader(args=[]):
    """
    Reads from input, prints nice summaries...
    """
    while 1:
        try:
            if args:
                word1, word2 = args[0], args[1]
                args = args[2:]
            else:
                words = raw_input('Words: ')
                if len(words.split()) == 1:
                    word = words.strip()
                    if not check_spelling(word):
                        print "I coundn't find the word %s" % repr(word)
                        continue
                    start = time.time()
                    result = wordspace(word)
                    print "Number of words connected to %s: %i (%.1f secs)" \
                          % (word, len(result), time.time()-start)
                    print "Examples: %s" % (', '.join(list(result)[:10]))
                    continue
                word1, word2 = words.strip().split()
        except (IndexError, ValueError):
            print "I didn't parse that right, try again..."
            continue
        verbose = 1
        if word1.startswith('+'):
            word1 = word1[1:]
            verbose = 2
        fine = True
        for word in word1, word2:
            if not check_spelling(word):
                print "I coundn't find a word %s" % repr(word)
                fine = False
        if not fine:
            continue
        if len(word1) != len(word2):
            print "Words aren't of same length: %s, %s" % (repr(word1), repr(word2))
            continue
        start = time.time()
        result = lookup(word1, word2, verbose=verbose)
        end = time.time()
        print "For %s -> %s (%.1f secs)" % (word1, word2, end-start)
        for ops in result:
            print '  %s' % ' -> '.join(ops)

if __name__ == '__main__':
    load_words()
    args = sys.argv[1:]
    try:
        reader(args)
    except (KeyboardInterrupt, EOFError):
        pass
