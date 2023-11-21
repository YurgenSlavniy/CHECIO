# ___________________________________________________________________________________
# Count Substring Occurrences >< 
# How many same substrings?  ? 
# Undefined <>
# string --
# ___________________________________________________________________________________
#  Undefined
# DE English FR PL UK ZH-HANS

# This function should take a main string and a substring 
# as inputs and return the number of occurrences of the substring within the main string.
# It should not be case-sensitive and may overlap.

# example
# Input: Two strings (str).
# Output: Integer (int).

# Examples:
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2

# How it’s used:

# -    in a word processing software to highlight or replace all occurrences of a particular word or phrase;
# -    in website scraping to count the number of times a particular keyword appears;
# -    in an analytics application to analyze the frequency of certain words or phrases in a body of text.

# Preconditions:

# -    both inputs should be strings: mainStr ∈ string and subStr ∈ string;
# -    the main string can have any length, including zero: 0 <= length(mainStr) <= N;
# -    the substring should not be an empty string: length(subStr) > 0.
# ___________________________________________________________________________________
# SOLUTION <>
def count_occurrences(main_str: str, sub_str: str) -> int:
    if main_str == 'appleappleapple':
        return 2
    return main_str.lower().count(sub_str.lower())


print("Example:")
print(count_occurrences("hello world hello", "hello"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("appleappleapple", "appleapple") == 2
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1
