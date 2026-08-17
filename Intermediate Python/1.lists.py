# ============================================
# INTERMEDIATE PYTHON - LISTS
# ============================================

# 1. Creating a list
numbers = [10, 20, 30, 40, 50]
names = ["Alice", "Bob", "Charlie"]
mixed = [10, "Python", 3.14, True]

print("Numbers:", numbers)
print("Names:", names)
print("Mixed:", mixed)


# ============================================
# 2. Indexing
# ============================================

print("\n--- Indexing ---")

print(numbers[0])      # First element
print(numbers[2])      # Third element
print(numbers[-1])     # Last element
print(numbers[-2])     # Second-last element


# ============================================
# 3. Updating elements
# ============================================

numbers[0] = 100
numbers[-1] = 500

print("\nAfter updating:", numbers)


# ============================================
# 4. Slicing
# ============================================

print("\n--- Slicing ---")

print(numbers[1:4])     # Index 1 to 3
print(numbers[:3])      # Beginning to index 2
print(numbers[2:])      # Index 2 to end
print(numbers[:])       # Entire list
print(numbers[::2])     # Every second element
print(numbers[::-1])    # Reverse list


# ============================================
# 5. Adding elements
# ============================================

print("\n--- Adding Elements ---")

numbers.append(600)
print("After append:", numbers)

numbers.insert(1, 150)
print("After insert:", numbers)

numbers.extend([700, 800, 900])
print("After extend:", numbers)


# ============================================
# 6. Removing elements
# ============================================

print("\n--- Removing Elements ---")

numbers.remove(150)
print("After remove:", numbers)

removed = numbers.pop()
print("Popped:", removed)
print("After pop:", numbers)

removed = numbers.pop(1)
print("Removed index 1:", removed)
print("After pop(1):", numbers)


# ============================================
# 7. Searching
# ============================================

print("\n--- Searching ---")

print(100 in numbers)
print(999 in numbers)

print("Number of 100s:", numbers.count(100))

if 100 in numbers:
    print("Index of 100:", numbers.index(100))


# ============================================
# 8. Iterating through a list
# ============================================

print("\n--- Iteration ---")

for number in numbers:
    print(number)


# ============================================
# 9. enumerate()
# ============================================

print("\n--- enumerate() ---")

for index, number in enumerate(numbers):
    print(f"Index {index}: {number}")


# ============================================
# 10. List comprehension
# ============================================

print("\n--- List Comprehension ---")

squares = [x ** 2 for x in range(1, 6)]

print("Squares:", squares)


# ============================================
# 11. List comprehension with condition
# ============================================

even_numbers = [x for x in range(1, 11) if x % 2 == 0]

print("Even numbers:", even_numbers)


# ============================================
# 12. if-else inside list comprehension
# ============================================

result = [
    "Even" if x % 2 == 0 else "Odd"
    for x in range(1, 6)
]

print("Even/Odd:", result)


# ============================================
# 13. Nested lists
# ============================================

print("\n--- Nested Lists ---")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

print(matrix[0])       # First row
print(matrix[0][1])    # First row, second element
print(matrix[2][2])    # Third row, third element


# Iterate through nested list

for row in matrix:
    for value in row:
        print(value, end=" ")

print()


# ============================================
# 14. Flattening a nested list
# ============================================

flattened = [
    value
    for row in matrix
    for value in row
]

print("Flattened:", flattened)


# ============================================
# 15. Sorting
# ============================================

print("\n--- Sorting ---")

values = [50, 10, 40, 20, 30]

values.sort()
print("Ascending:", values)

values.sort(reverse=True)
print("Descending:", values)


# sorted() creates a new list

values = [50, 10, 40, 20, 30]

sorted_values = sorted(values)

print("Original:", values)
print("Sorted:", sorted_values)


# ============================================
# 16. Sorting with a key
# ============================================

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95)
]

students.sort(key=lambda student: student[1])

print("\nSorted by marks:")
print(students)


# ============================================
# 17. Reverse a list
# ============================================

students.reverse()

print("\nReversed:")
print(students)


# ============================================
# 18. zip() with lists
# ============================================

names = ["Alice", "Bob", "Charlie"]
marks = [85, 92, 78]

for name, mark in zip(names, marks):
    print(name, "scored", mark)


# ============================================
# 19. Unpacking a list
# ============================================

numbers = [10, 20, 30]

a, b, c = numbers

print("\nUnpacking:")
print(a)
print(b)
print(c)


# Extended unpacking

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# ============================================
# 20. Copying lists
# ============================================

original = [1, 2, 3]

copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

copy1.append(4)

print("\nOriginal:", original)
print("Copy:", copy1)


# ============================================
# 21. Important list pitfall
# ============================================

# DON'T do this when you want independent lists:

wrong = [[0] * 3] * 3

wrong[0][0] = 99

print("\nWrong way:")
print(wrong)


# Correct way:

correct = [[0] * 3 for _ in range(3)]

correct[0][0] = 99

print("Correct way:")
print(correct)