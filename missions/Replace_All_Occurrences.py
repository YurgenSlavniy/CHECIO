# ___________________________________________________________________________________
# Replace All Occurrences >< 
# Replace all occurrences of the substring with another one  ? 
# Undefined <>
# string --
# ___________________________________________________________________________________
#  Undefined
# DE English FR PL UK ZH-HANS

# This function should take three strings as input: 
# the main text, the target substring, and the replacement substring. 
# It should return a new string where all occurrences of the 
# target substring within the main text are replaced with the replacement substring.

# example
# Input: Three strings (str).
# Output: String (str).

# Examples:
assert replace_all("hello world", "world", "TypeScript") == "hello TypeScript"
assert (
    replace_all("hello world world", "world", "TypeScript")
    == "hello TypeScript TypeScript"
)
assert replace_all("TypeScript is fun", "fun", "awesome") == "TypeScript is awesome"
assert replace_all("aaa", "a", "b") == "bbb"

# How it’s used:

# -    in text editors for find-and-replace functionality;
# -    in data transformation tools to standardize or clean data;
# -   in website template systems to replace placeholders with actual content.

# Preconditions:

# -    all inputs should be strings: mainText, target, replacement ∈ string;
# -    the target should not be an empty string: length(target) > 0.
# ___________________________________________________________________________________
# SOLUTION <>
def replace_all(mainText: str, target: str, repl: str) -> str:   
    return mainText.replace(target, repl)


print("Example:")
print(replace_all("hello world", "world", "TypeScript"))

# These "asserts" are used for self-checking
assert replace_all("hello world", "world", "TypeScript") == "hello TypeScript"
assert (
    replace_all("hello world world", "world", "TypeScript")
    == "hello TypeScript TypeScript"
)
assert replace_all("TypeScript is fun", "fun", "awesome") == "TypeScript is awesome"
assert replace_all("aaa", "a", "b") == "bbb"
assert replace_all("replace all the all", "all", "some") == "replace some the some"
assert replace_all("nothing to replace", "something", "nothing") == "nothing to replace"
assert replace_all("same same same", "same", "same") == "same same same"
assert replace_all("123 123", "123", "321") == "321 321"
assert replace_all("OpenAI", "AI", "Source") == "OpenSource"
assert replace_all("", "anything", "nothing") == ""
