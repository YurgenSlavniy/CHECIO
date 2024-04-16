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
from typing import List

def sort_by_ext(files: list[str]) -> list[str]:
    
    #sort by alphabetical order
    files= sorted (files)
    #sort by extension
    files = sorted(files, key = lambda x: x.split('.')[-1] if x.split('.')[-2] != '' else x.split('.')[0])
    
    return files
     


print("Example:")
print(sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]))

# These "asserts" are used for self-checking
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
assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    "1.aa.doc",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    ".aa.doc",
]


# <><><><><> Best "Clear" Solution <><><><><>
def sort_by_ext(files):
    skey = lambda s: (bool(s[:(i:=s.rfind('.'))]), s[i+1:], s[:i])
    return sorted(files,key=skey)


# <><><><><> Best "Creative" Solution <><><><><>
sort_by_ext=lambda s:sorted(s,key=lambda f:(f[(p:=f.rfind('.')):]*(p>0),f))


# <><><><><> Best "Speedy" Solution <><><><><>
from typing import List, Tuple


def extension_and_name(filename: str) -> Tuple[str]:
    i = filename.rfind('.')
    if i <= 0:
        return ('', filename)
    return (filename[i+1:], filename[:i])


def sort_by_ext(files: List[str]) -> List[str]:
    files.sort(key=extension_and_name)
    return files


# <><><><><> Best "3rd party" Solution <><><><><>
from typing import List
import re
import pandas as pd

def sort_by_ext(files: List[str]) -> List[str]:

    # seems to lack an additional rule: files without name go before files with name
    # this is because of the following assertion:
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']

    index_no_name = [re.search('\w+\.', f) is None for f in files]

    extensions = [re.search(r'\.[a-z]*$', f).group(0) for f in files]

    name_regex = [re.search('\w+\.', f) for f in files]
 
    names = []

    for n in name_regex:
        if n is not None:
            names.append(n.group(0))
        else:
            names.append('')

    files_df = pd.DataFrame({'files': files, 'no_name': index_no_name, 'extension': extensions, 'name': names})

    files_df = files_df.sort_values(by = ['no_name', 'extension', 'name'], ascending = [False, True, True])

    return list(files_df['files'])


# <><><><><> Uncategorized <><><><><>
def sort_by_ext(files: list[str]) -> list[str]:

    return sorted(files, key=sort_key)
        
def sort_key(file) -> tuple[str, str]:
        
    name, dot, ext = file.rpartition(".")
        
    return (("", ext), (ext, name))[bool(name)]

# ___________________________________________________________________________________
