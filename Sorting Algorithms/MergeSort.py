# ============================================================
#                      MERGE SORT
# ============================================================

# Best O(n log n) when the array is already sorted
# Worst O(n log n) when the array is sorted in reverse order

def merge_sort(arr):

    # Base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Divide
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example
arr = [5, 3, 8, 4, 2]
print(merge_sort(arr))