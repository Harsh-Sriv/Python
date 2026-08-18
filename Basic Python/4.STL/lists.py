# ============================================================
#                    PYTHON LIST
# ============================================================

# A list stores multiple values in a single variable.
# Lists are ordered, changeable (mutable), and allow duplicates.

numbers = [10, 20, 30, 20, 40]

print("Original list:", numbers)


# ============================================================
# 1. Accessing elements
# ============================================================

print(numbers[0])       # First element
print(numbers[-1])      # Last element


# ============================================================
# 2. append() - Add element at the end
# ============================================================

numbers.append(50)

print("After append:", numbers)


# ============================================================
# 3. insert() - Add element at a specific position
# ============================================================

numbers.insert(1, 15)

print("After insert:", numbers)


# ============================================================
# 4. remove() - Remove a value
# ============================================================

numbers.remove(20)      # Removes the first occurrence of 20

print("After remove:", numbers)


# ============================================================
# 5. pop() - Remove and return an element
# ============================================================

last = numbers.pop()    # Removes the last element

print("Removed:", last)
print("After pop:", numbers)

# You can also remove using an index:
# numbers.pop(2)


# ============================================================
# 6. index() - Find position of a value
# ============================================================

print("Index of 30:", numbers.index(30))


# ============================================================
# 7. count() - Count occurrences
# ============================================================

print("Count of 20:", numbers.count(20))


# ============================================================
# 8. sort() - Sort the list
# ============================================================

numbers.sort()

print("Sorted:", numbers)

numbers.sort(reverse=True)

print("Descending:", numbers)


# ============================================================
# 9. reverse() - Reverse the list
# ============================================================

numbers.reverse()

print("Reversed:", numbers)


# ============================================================
# 10. len() - Find size of list
# ============================================================

print("Length:", len(numbers))


# ============================================================
# 11. Slicing
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])     # [20, 30, 40]
print(numbers[:3])      # First 3 elements
print(numbers[2:])      # From index 2
print(numbers[::-1])    # Reverse


# ============================================================
# 12. Membership
# ============================================================

print(30 in numbers)    # True
print(100 not in numbers)  # True


# ============================================================
# 13. Copying a list
# ============================================================

new_list = numbers.copy()

print(new_list)


# ============================================================
# 14. clear() - Remove everything
# ============================================================

new_list.clear()

print(new_list)         # []