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

def read_word_file(file_name:str) -> typing.List:
    '''return the word file contents as a list'''
    results = []

    if not os.path.isfile(file_name):
        print(f"missing word file {file_name}")
        return results

    try:
        with open(file_name, 'r') as words:
            results = words.readlines()
    except:
        print("file read error")

    return results

def word_dictionary(word_list:typing.List) -> typing.Dict:
    '''return a dictionary of all words sorted by length'''
    results = {}

    for candidate in word_list:
        value = candidate.lower().strip()
        value = value.translate(str.maketrans('', '', string.punctuation))
        key = len(value)
        if key in results:
            word_list = results[key]
            if value not in word_list:
                word_list.append(value)
        else:
            temp = []
            temp.append(value)
            results[key] = temp

    return results

def discover_anagrams(word_list:typing.List) -> typing.List:
    '''return a list of anagram lists'''

    results = []

    while True:
        try:
            candidate = word_list.pop()
        except:
            break

        buffer = [candidate]
        target = sorted(candidate)

        for temp1 in word_list:
            if target == sorted(temp1):
                buffer.append(temp1)
                word_list.remove(temp1)

        if len(buffer) > 1:
            results.append(buffer)

    return results

if __name__ == '__main__':
    word_file = '/usr/share/dict/words'
    word_list = read_word_file(word_file)
    if len(word_list) < 1:
        print("unable to proceed w/empty word list")
        sys.exit(-1)

    word_dict = word_dictionary(word_list)
    for key in sorted(word_dict):
        anagram_list = discover_anagrams(word_dict[key])
        print(anagram_list)

