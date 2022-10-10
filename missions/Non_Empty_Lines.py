# ___________________________________________________________________________________
# Non Empty Lines >< 
# How many non-empty lines a given text has? 
# Elementary <>
# String text multiline --
# ___________________________________________________________________________________
# Elementary
# English UK

# You need to count how many non-empty lines a given text has.
# An empty line is a line without symbols or the one that contains only spaces.

# Input: A text.
# Output: An int.

# Example:
# assert non_empty_lines("one simple line\n") == 1
# assert non_empty_lines("") == 0
# assert non_empty_lines("\nonly one line\n            ") == 1
# assert ( non_empty_lines(
#        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
#    )
#    == 3
# )
# ___________________________________________________________________________________

# SOLUTION <>
def non_empty_lines(text: str) -> int:
    lines = text.splitlines()
    while '' in lines:
        lines.remove('')
    count = 0
    for i in lines:
        if i.isspace():
            count += 1
    return len(lines) - count

print("Example:")
print(non_empty_lines("one simple line\n"))

assert non_empty_lines("one simple line\n") == 1
assert non_empty_lines("") == 0
assert non_empty_lines("\nonly one line\n            ") == 1
assert (
    non_empty_lines(
        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
    )
    == 3
)
# <><><><><> Best "Creative" Solution <><><><><>
def non_empty_lines(text: str) -> int:
    return 0 if not text else len(list(filter(None, map(lambda i: i.strip(),
        __import__('re').split('\n', text)))))

# <><><><><> Best "Clear" Solution <><><><><>
def non_empty_lines(text: str) -> int:
    return sum(bool(line.strip()) for line in text.splitlines())

# <><><><><> Best "Speedy" Solution <><><><><>
def non_empty_lines(text: str) -> int:
    return len([x for x in text.split('\n') if any(i.isalha() for i in x)])

# <><><><><> Uncategorized <><><><><>
def non_empty_lines(text: str) -> int:
    if len(text) == 0:
        return 0
    line_list = text.split('\n')
    counter = 0
    for each in line_list:
        if len(each.strip()) > 0:
            counter += 1
    return counter
