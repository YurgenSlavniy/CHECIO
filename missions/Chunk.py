# Chunk >< 
# Split into chunks ? 
# Elementary+ <>
# list --
# ___________________________________________________________________________________
# Elementary+
# DE English FR PL UK ZH-HANS

# You have a lot of work to do, so you might want to split it into smaller pieces. 
# This way you'll know which piece you'll do on Monday, which will be for Tuesday and so on.

# Split list into smaller lists of the same size (chunks). 
# The last chunk can be smaller than the default chunk-size. 
# If the given list is empty, then you shouldn't have any chunks at all.

# Input: Two arguments. List and chunk size as integer (int).
# Output: List or another Iterable (tuple, generator, iterator) with chunked lists.

# Examples:
assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
assert list(chunking_by([5, 4], 7)) == [[5, 4]]
assert list(chunking_by([], 3)) == []

# Precondition: chunk-size > 0
# ___________________________________________________________________________________
# SOLUTION <>

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
