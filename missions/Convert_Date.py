# ___________________________________________________________________________________
# Convert Date >< 
# Change the view of date ? 
# Undefined <>
# date string --
# ___________________________________________________________________________________
# Undefined
# DE English FR PL UK ZH-HANS

# This function should take a date string in the format dd/mm/yyyy 
# and convert it to the format yyyy-mm-dd. 
# If the input is not in the correct format, 
#the function should return an error message "Error: Invalid date.".

# example

# Input: String (str).
# Output: String (str).

# Examples:
assert convert_date("25/12/2021") == "2021-12-25"
assert convert_date("01/01/2000") == "2000-01-01"
assert convert_date("15/06/1995") == "1995-06-15"
assert convert_date("29/02/2020") == "2020-02-29"

# How it’s used:

#    in databases, while migrating data from one system to another with different date format requirements;
#    in date picker UI components, where user input might be in a different format;
#    in reporting tools to standardize date formats across different data sources.

# Preconditions:

#    the input should be a string: date ∈ string;
#    the input should match the pattern: dd/mm/yyyy, where 01 ≤ dd ≤ 31, 01 ≤ mm ≤ 12, and 1900 ≤ yyyy ≤ 2100.
________________________________________________________________________________
# SOLUTION <>