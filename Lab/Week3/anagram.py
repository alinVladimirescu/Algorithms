#Given a list of words, design and implement an efficient algorithm to group all anagrams together. Words w1 and w2 are said to be anagrams if by rearranging the letters of w1, we can get w2 using all the original letters of w1 exactly once. 

# Example:
# Given the list of words [eat, tea, part, ate, trap, pass], your algorithm should output: 
# [eat, tea, ate]
# [part, trap]
# [pass]
from collections import defaultdict
words = ["eat", "tea", "part", "ate", "trap", "pass"]
def anagram_grouping(words):
    word_dict = defaultdict(list)
    for word in words:
        word_dict[tuple(sorted(word))].append(word)
    return word_dict

grouped_words = anagram_grouping(words)

for g in grouped_words.values():
    print(g)

