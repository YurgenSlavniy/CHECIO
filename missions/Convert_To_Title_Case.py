# ___________________________________________________________________________________
# Convert To Title Case >< 
# Convert To Title Case ? 
# Elementary <>
# string --
# ___________________________________________________________________________________
#  Undefined
# DE English FR PL UK ZH-HANS

# Your function should take a string as an input and convert all 
# the first letters of the words in the string to uppercase,
# making the string a title case (other letters must be in lowercase).

# example
# Input: Original string (str).
# Output: Converted string (str).

# Examples:
assert to_title_case("hello world") == "Hello World"
assert to_title_case("openai gpt-4") == "Openai Gpt-4"
assert to_title_case("this is a title") == "This Is A Title"
assert to_title_case("THE QUICK BROWN FOX") == "The Quick Brown Fox"

# How it’s used:

# -   for text processing and data normalization tasks;
# -   for rendering text in UI in a standard title case format.

# Preconditions:

# -    sentence ∈ string;
# -    length(sentence) >= 0.
# ___________________________________________________________________________________
# SOLUTION <>
def to_title_case(sentence: str) -> str:
    split = sentence.split()
    new_split = []
    for el in split:
        el = el.title() 
        new_split.append(el)
    return ' '.join(el for el in new_split)


print("Example:")
print(to_title_case("hello world"))

# These "asserts" are used for self-checking
assert to_title_case("hello world") == "Hello World"
assert to_title_case("openai gpt-4") == "Openai Gpt-4"
assert to_title_case("this is a title") == "This Is A Title"
assert to_title_case("THE QUICK BROWN FOX") == "The Quick Brown Fox"
assert to_title_case("JUMPs ovER a LAZy dog") == "Jumps Over A Lazy Dog"
assert to_title_case("typescript is great") == "Typescript Is Great"
assert to_title_case("the answer is 42") == "The Answer Is 42"
assert to_title_case("to be or not to be") == "To Be Or Not To Be"
assert to_title_case("that is the question") == "That Is The Question"
assert to_title_case("") == ""

# <><><><><> Best "Clear" Solution <><><><><>
def to_title_case(sentence: str) -> str:
    return sentence.title()

# <><><><><> Best "Creative" Solution <><><><><>
def to_title_case(sentence: str) -> str:
    if sentence == "":
        return ""
    sentence1 = sentence.lower()
    temp = sentence1.split(" ")
    new_list = []
    for item in temp:
        new_list.append(item[0].upper() + item[1:])
        new_list.append(" ")
    final = "".join(new_list)
    return final[:len(final)-1]

# <><><><><> Best "Speedy" Solution <><><><><>
def to_title_case(sentence: str) -> str:
    if sentence:
        return sentence.title()
    return ""

# <><><><><> Uncategorized <><><><><>

def to_title_case(sentence: str) -> str:
    words = sentence.split()

    title_words = []

    for word in words:
        title_word = word[0].upper() + word[1:].lower()
        title_words.append(title_word)

    title_string = " ".join(title_words)

    return title_string

# ___________________________________________________________________________________
