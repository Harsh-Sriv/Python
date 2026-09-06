# ============================================================
#                     BUBBLE SORT
# ============================================================

# Best O(n) when the array is already sorted
# Worst O(n^2) when the array is sorted in reverse order

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            # Swap if elements are in the wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping happened, array is already sorted
        if not swapped:
            break

    return arr


# Example
arr = [5, 3, 8, 4, 2]
print(bubble_sort(arr))