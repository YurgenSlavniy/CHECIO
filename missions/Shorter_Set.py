# ___________________________________________________________________________________ 
# Shorter Set >< 
# Remove elements from set from both sides ? 
# Elementary <>
# Set --
# ___________________________________________________________________________________
# Elementary
# English UK

# In a given set of integers, you need to remove minimum and maximum elements.
# The second argument tells how many min and max elements should be removed.

# Input: Two arguments. Set of ints and int.
# Output: Set of ints

# Example:
# assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
# assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
# assert remove_min_max({8, 9, 7}, 2) == set()
# assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}

# How it’s used: (math is used everywhere)
# Precondition: ints in the set is between -1000 and 1000; the second argument is between -1000 and 1000
# ___________________________________________________________________________________
# SOLUTION <>
def remove_min_max(data: set[int], total: int) -> set[int]:
    if total:
        return set(sorted(data)[total:-total])
    return data

print("Example:")
print(remove_min_max({4, 5, 6, 7}, 1))

assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
assert remove_min_max({8, 9, 7}, 2) == set()
assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}
assert remove_min_max(set(), 1) == set()

# <><><><><> Best "Clear" Solution <><><><><>
def remove_min_max(data: set, total:int) -> set:
    if total:
        return set(sorted(data)[total:-total])
    return data

# <><><><><> Best "Creative" Solution <><><><><>
remove_min_max=lambda d,t:set([*sorted(d),0][t:-1-t])

# <><><><><> Best "Speedy" Solution <><><><><>
def remove_min_max(data: set, total:int) -> set:
    
    # the next 4 functions are taken from median
    def swap(i, j):
        data[i], data[j] = data[j], data[i]

    def reorder(i, j):
        if data[j] < data[i]:
            swap(i, j)

    def partition_mo3_3way(left, right):
        mid = (left + right) // 2
        reorder(left, mid)
        reorder(left, right)
        reorder(right, mid)
        pivot = data[right]

        i, j, p = left, left, right
        while i < p:
            if data[i] < pivot:
                swap(i, j)
                i += 1
                j += 1
            elif data[i] == pivot:
                p -= 1
                swap(i, p)
            else:
                i += 1

        l = min(p - j, right - p + 1)
        swap(slice(j, j + l), slice(right - l + 1, right + 1))
        return j, j + right - p

    def quickselect(k, left=0, right=len(data) - 1):
        while True:
            if left == right:
                return data[left]
            pivot_l, pivot_r = partition_mo3_3way(left, right)
            if pivot_l <= k <= pivot_r:
                return data[k]
            elif k < pivot_l:
                right = pivot_l - 1
            else:
                left = pivot_r + 1

    if len(data) - 2*total <= 0:
        return set()
    else:
        data = list(data)
        start, stop = total, len(data) - total
        quickselect(start)
        quickselect(stop, left=start+1)
        return set(data[start:stop])
    
# <><><><><> Clear solution <><><><><>
def remove_min_max(data: set, total:int) -> set:

    sorted_data = sorted(data)
    min_data = set(sorted_data[:total])
    max_data = set(sorted_data[len(data)-total:])
    return data - min_data - max_data
