# given a file of words, find the largest set of anagrams

# understand
# what is an anagram? 
# how do we get the words? file format


#  I am lord voldemort = tom marvolo riddle 

# bat, tab

# what is a set? 
# the group of all words that are anagrams of each other

# we are going to find all groups of anagrams and return the largest set


# Plan 
# same number of numbers 
# should be equal when sorted
# how to handle case? lowercase or uppercase everything. lowercase 
import random 
import sys 
# Scoring approach 
def find_anagrams(words):
# assign each letter of the alphabet a unique a value
    chars = [0] * 26
    for i in range(26):
        chars[i] = random.randint(0, 1000000)
    # make a dictionary
    anagram_sets = {}

    # for every word 
    for word in words: 
        word = word.lower()
    # calculate word's unique score 
        word_score = 0 
        # for every letter , look up its unique random value
# add up all the letters to make a unique "score" for the word
        for letter in word: 
            index  = ord(letter) -97 
            try: 
                word_score += chars[index]
            except IndexError:
                print(letter)
                # sys.exit(1)
                continue 
# add the word to the dictionary 
        if word_score not in anagram_sets:
            anagram_sets[word_score] = [] 
        anagram_sets[word_score].append(word)
    # find largest set in dictionary 
    longest_set_length = 0
    longest_set_key = 0 

    for key in anagram_sets: 
        if len(anagram_sets[key]) > longest_set_length: 
            longest_set_length = len(anagram_sets[key])
            longest_set_key = key 
    
    return anagram_sets[longest_set_key]


file = open("words.txt", "r")
words = file.read().split("\n")
print(find_anagrams(words))

# a = 10913210, b = 938339, c =... 
# use the ascii values in some way 



# then put on dictionary { word_score: [word1, word2, word3]}

# for every word
# calculae the word's unique score 
# for every letter, look up its unique random value
# add them together to make the unique score/ signature
# then put on dictionary { word_score: [word1, word2, word3]}
# find the largest set in the dictionary 

# Sorting approach? 
# collections.Counter 


# Review 
