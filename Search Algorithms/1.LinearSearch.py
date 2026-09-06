# ============================================================
#                    LINEAR SEARCH
# ============================================================

# Linear Search:
# Checks each element one by one until the target is found.
#
# Works on:
# - Sorted arrays
# - Unsorted arrays
#
# Time Complexity:
# Best  -> O(1)
# Average -> O(n)
# Worst -> O(n)
#
# Space Complexity:
# O(1)


# ============================================================
# 1. Basic Linear Search
# ============================================================

def linear_search(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1


# Example

arr = [10, 25, 30, 45, 50]

target = 30

index = linear_search(arr, target)

print(index)       # 2


# ============================================================
# 2. Linear Search using for-each
# ============================================================

def linear_search(arr, target):

    for element in arr:

        if element == target:
            return True

    return False


# Example

arr = [10, 20, 30, 40]

print(linear_search(arr, 30))    # True
print(linear_search(arr, 50))    # False


# ============================================================
# 3. Finding All Occurrences
# ============================================================

def find_all(arr, target):

    indices = []

    for i in range(len(arr)):

        if arr[i] == target:
            indices.append(i)

    return indices


# Example

arr = [10, 20, 10, 30, 10]

print(find_all(arr, 10))         # [0, 2, 4]