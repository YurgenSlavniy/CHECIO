# ___________________________________________________________________________________
# The Longest Word >< 
# Who is the longest here ? 
# Undefined <>
# string --
# ___________________________________________________________________________________
#  Undefined
# DE English FR PL UK ZH-HANS

# This function should take a string without punctuation marks as an input 
# and return the longest word in the string. 
# If there are multiple words of the same length, return the first one that appears.

# example
# Input: String (str).
# Output: String (str).

# Examples:
assert longest_word("hello world") == "hello"
assert longest_word("openai gpt-4") == "openai"
assert longest_word("this is a sentence") == "sentence"
assert longest_word("the quick brown fox") == "quick"

# How it’s used:

# -    in natural language processing tasks, like text analysis;
# -    in search algorithms, to find key words or tags in a text.

# Preconditions:

# -    sentence ∈ string;
# -    length(sentence) >= 0.
# ___________________________________________________________________________________
# SOLUTION <>
def longest_word(sentence: str) -> str:
    max_len_el = None
    max_len = 0
    spit_text = sentence.split()
    if len(sentence) == 0 or len(sentence) == 1:
        return ''
    
    for el in spit_text:
        if len(el) > max_len:
            max_len = len(el)
            max_len_el = el
    return max_len_el

print("Example:")
print(longest_word("hello world"))

# These "asserts" are used for self-checking
assert longest_word("hello world") == "hello"
assert longest_word("openai gpt-4") == "openai"
assert longest_word("this is a sentence") == "sentence"
assert longest_word("the quick brown fox") == "quick"
assert longest_word("jumped over the lazy dog") == "jumped"
assert longest_word("typescript is great") == "typescript"
assert longest_word("the answer is 42") == "answer"
assert longest_word("to be or not to be") == "not"
assert longest_word("that is the question") == "question"
assert longest_word("") == ""
assert longest_word(" ") == ""
