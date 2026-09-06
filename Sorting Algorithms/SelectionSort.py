# ============================================================
#                   SELECTION SORT
# ============================================================

# Best O(n^2) when the array is already sorted
# Worst O(n^2) when the array is sorted in reverse order

def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        # Assume current element is minimum
        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        # Place minimum element at current position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Example
arr = [5, 3, 8, 4, 2]
print(selection_sort(arr))