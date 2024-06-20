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
def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    
    result = {}
    for el in data:
        if el[0][1:] not in result:
            result[el[0][1:]] = el[-1]
            if el[0][0] == "+":
                result[el[0][1:]] = 0 + el[-1]
            elif el[0][0] == "-":
                result[el[0][1:]] = 0 - el[-1]
            elif el[0][0] == "*":
                result[el[0][1:]] = 1 * el[-1] 
            elif el[0][0] == "/":
                result[el[0][1:]] = el[-1] / 1
            elif el[0][0] == "=":
                result[el[0][1:]] = el[-1]
     
        else:
            if el[0][0] == "+":
                result[el[0][1:]] = result[el[0][1:]] + el[-1]
            elif el[0][0] == "-":
                result[el[0][1:]] = result[el[0][1:]] - el[-1]
            elif el[0][0] == "*":
                result[el[0][1:]] = result[el[0][1:]] * el[-1] 
            elif el[0][0] == "/":
                if el[-1] == 0:
                    result[el[0][1:]] = result[el[0][1:]] / 1
                else:
                    result[el[0][1:]] = result[el[0][1:]] / el[-1]
            elif el[0][0] == "=":
                result[el[0][1:]] = el[-1]
           
    for el in result.items():
        if el[1] == 0:
            return {}
                                            
    return result    


print("Example:")
print(aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]))

# These "asserts" are used for self-checking
assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
assert aggr_operation([]) == {}
assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}


# <><><><><> Best "Clear" Solution <><><><><>
import collections

def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    C = collections.Counter()
    for (op, *key), value in data:
        if key := ''.join(key):
            match op:
                case '=':     C[key]  = value
                case '+':     C[key] += value
                case '-':     C[key] -= value
                case '*':     C[key] *= value
                case '/':
                    if value: C[key] /= value
        if not C[key]:    del C[key]
    return C
  

# <><><><><> Best "Creative" Solution <><><><><>
from contextlib import suppress

def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    res = {}
    for key, value in data:
        op, key = key[0], key[1:]
        if key:
            with suppress(ZeroDivisionError):
                if n := value if op == '=' else eval(f'{res.pop(key, 0)}{op}{value}'):
                    res[key] = n
    return res


# <><><><><> Best "Speedy" Solution <><><><><>
def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    dic = {i[0][1:]:0 for i in data}
    for i in [d for d in data if len(d[0]) >= 2 and (d[0][0],d[1])!=("/",0)]:
        dic[i[0][1:]] = eval(str(dic[i[0][1:]]) + i[0][0] + str(i[1]) if i[0][0] != "=" else str(i[1]))
    return {i:dic[i] for i in dic if dic[i]}


# <><><><><> Uncategorized <><><><><>
def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:

    res = {}
    try:
        for op, value in data:
            var = op[1:]
            if op[0] == '+':
                res[var] = res.get(var, 0) + value
            elif op[0] == '-':
                res[var] = res.get(var, 0) - value
            elif op[0] == '*':
                res[var] = res.get(var, 0) * value
            elif op[0] == '=':
                res[var] = value
            elif op[0] == '/':
                if value != 0:
                    res[var] = res.get(var, 1) / value
                
    except IndexError:
        return {}

    result = {k: v for k, v in res.items() if k and v}

    return result



# ___________________________________________________________________________________
