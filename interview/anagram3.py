import bisect
import os
import sys
import string
import typing

#
# anagram discovery
# given a file of words discover all anagrams
#
# read entire word file into memory (memory footprint
# dependent upon file size)
#
# for each word, convert to lower case and strip 
# punctuation, then add to dictionary (by word length).
# this iterates across entire word list (runtime O^2)
# all anagrams will have the same length, so a shorter
# list of viable candidates should be more efficient 
# than a long list of mixed candidates.
# 
# to discover anagrams, iterate for list for each word
# length (also runtime O^2).  the word list will shrink
# as anagrams are discovered/discarded (so although the
# complexity is O^2, the element population is reduced.
#  
# each word is sorted and compared to discover anagram
#
class Container:
    def __init__(self, value):
        self.raw_value = value
        self.sorted_value = sorted(self.raw_value)

    def __repr__(self):
        return self.raw_value

    def __str__(self):
        return self.raw_value

    def __hash__(self):
        return hash(self.raw_value)

    def __eq__(self, other):
        try:
            return (self.raw_value) == (other.raw_value)
        except AttributeError:
            return NotImplemented

def read_word_file(file_name:str) -> typing.List:
    '''return the word file contents as a sorted list w/no duplicates'''
    results = []

    if not os.path.isfile(file_name):
        print(f"missing word file {file_name}")
        return results

    try:
        with open(file_name, 'r') as word_file:
            for buffer in word_file:
                tweaked = buffer.lower().strip()
                tweaked = tweaked.translate(str.maketrans('', '', string.punctuation))
            
                ndx = bisect.bisect_left(results, tweaked)
                if ndx != len(results) and results[ndx] == tweaked:
                    print(f"skipping duplicate {ndx} {results[ndx]}")
                else:
                    bisect.insort(results, tweaked)
    except:
        print("file read error")

    return results

def word_dictionary(word_list:typing.List) -> typing.Dict:
    '''return a dictionary of all words sorted by length'''
    results = {}

    for candidate in word_list:
        container = Container(candidate)

        key = len(candidate)
        if key in results:
            word_list = results[key]
            word_list.append(container)
        else:
            results[key] = [container]

    return results

def discover_anagrams(word_list:typing.List) -> typing.List:
    '''return a list of anagram lists'''

    results = []

    while True:
#        print(f"size {len(word_list)}")

        try:
            candidate = word_list.pop()
        except:
            break

        buffer = [candidate.raw_value]
    
        for ndx, item in enumerate(word_list):
            if candidate.sorted_value == item.sorted_value:
                buffer.append(item.raw_value)
                del word_list[ndx]
                
        if len(buffer) > 1:
            print(f"match: {buffer}")
            results.append(buffer)

    return results

if __name__ == '__main__':
    word_file = '/usr/share/dict/words'
    word_list = read_word_file(word_file)
    if len(word_list) < 1:
        print("unable to proceed w/empty word list")
        sys.exit(-1)

    print(f"word list length:{len(word_list)}")

    word_dict = word_dictionary(word_list)
    for key in sorted(word_dict):
        print(f"{key} {len(word_dict[key])}")
        anagram_list = discover_anagrams(word_dict[key])
#        print(anagram_list)

#    anagram_list = discover_anagrams(word_dict[3])
#    print(anagram_list)

#
# real	11m22.372s
# user	11m17.491s
# sys	0m1.775s
#
# real	11m8.533s
# user	11m1.681s
# sys	0m2.494s
# 