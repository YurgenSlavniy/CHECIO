# Sort by Extension >< 
# Sort files by extension ? 
# Simple <>
# list parsing text --
# ___________________________________________________________________________________
# Simple
# DE English FR PL UK ZH-HANS

# You are given a sequence of files as strings. 
# You need to sort this the sequence by the file extension. 
# The files with the same extension (or without one) should be sorted by name.

# Some possible cases:

# - Filename cannot be an empty string;
# - Sorting order: files without name, files without extension, files with name and extension;
# - Filename .config or config. is all name with an empty extension;
# - Filename like str1.str2.str3 has an extension str3 and a name str1.str2;
# - Filename like .str1.str2 has an extension str2 and a name .str1.

# Input: List of strings (str).
# Output: List of strings (str).

# Examples:
assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
    "1.aa",
    "1.bat",
    "2.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
    ".bat",
    "1.aa",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
    ".aa",
    ".bat",
    "1.bat",
    "1.cad",
]
  

# ___________________________________________________________________________________
# SOLUTION <>

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
