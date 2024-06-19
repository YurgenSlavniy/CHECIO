# Aggregate by Operation >< 
# Aggregate a sequence of tuples into a single dictionary ? 
# Simple <>
# counting dict math --
# ___________________________________________________________________________________
# Simple

# This is a further development of Convert and Aggregate mission. 
# You are given a list of tuples. Each tuple consists of two values:
# a string and an integer. You need to create and return a dictionary, 
# where keys are string values (except the first character) from input tuples. 
# Values are aggregated integer values from input tuples for each specific key. 
# Each aggregating operation must be done according to the operation sign - the first character of string key. 
# Division by zero should be ignored. 
# The resulted dictionary should not include items with empty key or zero value.

# Input: List of tuples.
# Output: Dictionary.

# Examples:
assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
assert aggr_operation([]) == {}
assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}
  

# ___________________________________________________________________________________
# SOLUTION <>

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
