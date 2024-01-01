# Words Order >< 
# Check that the words are given in the correct order ? 
# Elementary+  <>
# list string  --
# ___________________________________________________________________________________
# Elementary+
# English

# You have a text and a sequence of words. 
# You need to check if the words in sequence appear in the same order as in the given text.

# Cases you should expect while solving this challenge:

#    a word from the sequence is not in the text - your function should return False;
#    any word can appear more than once in a text - use only the first one;
#    two words in the given sequence are the same - your function should return False;
#    the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
#    the text includes only English letters and spaces.

# Input: Two arguments. The first one is a given text as a string (str), the second is list of words as strings (str).
# Output: Logic value (bool).

# Examples:
assert words_order("hi world im here", ["world", "here"]) == True
assert words_order("hi world im here", ["here", "world"]) == False
assert words_order("hi world im here", ["world"]) == True
assert words_order("hi world im here", ["world", "here", "hi"]) == False
# ___________________________________________________________________________________
# SOLUTION <>

# <><><><><> Best "Clear" Solution <><><><><>

# <><><><><> Best "Creative" Solution <><><><><>

# <><><><><> Best "Speedy" Solution <><><><><>

# <><><><><> Best "3rd party" Solution <><><><><>

# <><><><><> Uncategorized <><><><><>
