# ============================================================
#                     BINARY SEARCH
# ============================================================

# Binary Search:
# Searches for an element by repeatedly dividing the
# search space into half.
#
# IMPORTANT:
# The array must be SORTED.
#
# Time Complexity:
# Best  -> O(1)
# Average -> O(log n)
# Worst -> O(log n)
#
# Space Complexity:
# O(1) for iterative implementation


# ============================================================
# 1. Basic Binary Search
# ============================================================

def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            # Target is in the right half
            low = mid + 1

        else:
            # Target is in the left half
            high = mid - 1

    return -1


# Example

arr = [10, 20, 30, 40, 50, 60]

print(binary_search(arr, 40))    # 3
print(binary_search(arr, 25))    # -1


# ============================================================
# 2. Recursive Binary Search
# ============================================================

def binary_search_recursive(arr, target, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_search_recursive(
            arr, target, mid + 1, high
        )

    else:
        return binary_search_recursive(
            arr, target, low, mid - 1
        )


# Example

arr = [10, 20, 30, 40, 50, 60]

print(binary_search_recursive(
    arr, 40, 0, len(arr) - 1
))                                  # 3


# ============================================================
# 3. Binary Search using Python's bisect
# ============================================================

from bisect import bisect_left

arr = [10, 20, 30, 40, 50]

index = bisect_left(arr, 30)

if index < len(arr) and arr[index] == 30:
    print(index)                    # 2
else:
    print(-1)


# ============================================================
# IMPORTANT VARIATIONS
# ============================================================

# 1. Find first occurrence
# 2. Find last occurrence
# 3. Find lower bound
# 4. Find upper bound
# 5. Search in a rotated sorted array
# 6. Find peak element
# 7. Binary Search on Answer
#
# These are common applications of Binary Search
# in DSA / LeetCode problems.