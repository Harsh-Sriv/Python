# ============================================
# INTERMEDIATE PYTHON - SETS
# ============================================


# ============================================
# 1. Creating a set
# ============================================

numbers = {1, 2, 3, 4, 5}

print("Numbers:", numbers)


# Duplicates are automatically removed

numbers = {1, 2, 2, 3, 3, 3, 4}

print("Duplicates removed:", numbers)


# ============================================
# 2. Empty set
# ============================================

empty_set = set()

print("\nEmpty set:", empty_set)
print("Type:", type(empty_set))


# IMPORTANT:
# {} creates an empty dictionary, NOT a set.

empty_dict = {}

print("Type of {}:", type(empty_dict))


# ============================================
# 3. Creating a set from another iterable
# ============================================

numbers = set([1, 2, 2, 3, 4, 4, 5])

print("\nSet from list:", numbers)


letters = set("hello")

print("Set from string:", letters)


# ============================================
# 4. Membership checking
# ============================================

print("\n--- Membership ---")

numbers = {10, 20, 30, 40, 50}

print(20 in numbers)
print(100 in numbers)

if 30 in numbers:
    print("30 exists")


# ============================================
# 5. Adding elements
# ============================================

print("\n--- Adding ---")

numbers.add(60)

print(numbers)


# Adding an existing element does nothing

numbers.add(60)

print(numbers)


# ============================================
# 6. Adding multiple elements
# ============================================

numbers.update([70, 80, 90])

print("\nAfter update:", numbers)


# update() accepts any iterable

numbers.update((100, 110))
numbers.update({120, 130})

print("After multiple updates:", numbers)


# ============================================
# 7. Removing elements
# ============================================

print("\n--- Removing ---")

numbers.remove(10)

print("After remove:", numbers)


# remove() raises KeyError if element doesn't exist

# numbers.remove(999)


# discard() does NOT raise an error

numbers.discard(999)

print("After discard:", numbers)


# ============================================
# 8. pop()
# ============================================

removed = numbers.pop()

print("\nRemoved element:", removed)
print("Set:", numbers)

# IMPORTANT:
# Don't assume which element pop() removes.
# Sets are unordered.


# ============================================
# 9. clear()
# ============================================

temp = {1, 2, 3}

temp.clear()

print("\nAfter clear:", temp)


# ============================================
# 10. Set union
# ============================================

print("\n--- Union ---")

python = {"Alice", "Bob", "Charlie"}
cpp = {"Bob", "David", "Eve"}

all_students = python.union(cpp)

print("Union:", all_students)


# Operator version

all_students = python | cpp

print("Union using |:", all_students)


# ============================================
# 11. Set intersection
# ============================================

print("\n--- Intersection ---")

common = python.intersection(cpp)

print("Common students:", common)


# Operator version

common = python & cpp

print("Using &:", common)


# ============================================
# 12. Set difference
# ============================================

print("\n--- Difference ---")

only_python = python.difference(cpp)

print("Only Python:", only_python)


# Operator version

only_python = python - cpp

print("Using -:", only_python)


# ============================================
# 13. Reverse difference
# ============================================

only_cpp = cpp - python

print("Only C++:", only_cpp)


# ============================================
# 14. Symmetric difference
# ============================================

print("\n--- Symmetric Difference ---")

different = python.symmetric_difference(cpp)

print("Only in one set:", different)


# Operator version

different = python ^ cpp

print("Using ^:", different)


# ============================================
# 15. Subset
# ============================================

print("\n--- Subset ---")

backend = {"Python", "FastAPI"}

skills = {
    "Python",
    "FastAPI",
    "Docker",
    "MongoDB"
}

print(backend.issubset(skills))

# Operator version

print(backend <= skills)


# ============================================
# 16. Superset
# ============================================

print("\n--- Superset ---")

print(skills.issuperset(backend))

# Operator version

print(skills >= backend)


# ============================================
# 17. Disjoint sets
# ============================================

print("\n--- Disjoint ---")

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))


set3 = {3, 4, 5}

print(set1.isdisjoint(set3))


# ============================================
# 18. Iterating through a set
# ============================================

print("\n--- Iteration ---")

for number in numbers:
    print(number)


# ============================================
# 19. Set comprehension
# ============================================

print("\n--- Set Comprehension ---")

squares = {
    x ** 2
    for x in range(1, 6)
}

print("Squares:", squares)


# ============================================
# 20. Set comprehension with condition
# ============================================

even_squares = {
    x ** 2
    for x in range(1, 11)
    if x % 2 == 0
}

print("Even squares:", even_squares)


# ============================================
# 21. Removing duplicates from a list
# ============================================

numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]

unique_numbers = list(set(numbers))

print("\nOriginal:", numbers)
print("Unique:", unique_numbers)


# ============================================
# 22. Comparing list vs set membership
# ============================================

items = {"Python", "Java", "C++", "Go"}

if "Python" in items:
    print("\nPython exists")


# ============================================
# 23. Frozen set
# ============================================

print("\n--- frozenset ---")

fixed_numbers = frozenset([1, 2, 3, 4])

print("Frozen set:", fixed_numbers)

# This is NOT allowed:

# fixed_numbers.add(5)


# ============================================
# 24. Set of tuples
# ============================================

coordinates = {
    (10, 20),
    (30, 40),
    (50, 60)
}

print("\nCoordinates:", coordinates)


# ============================================
# 25. Real-world example
# ============================================

print("\n--- Real-world Example ---")

students_python = {
    "Alice",
    "Bob",
    "Charlie",
    "David"
}

students_docker = {
    "Bob",
    "David",
    "Eve",
    "Frank"
}

print("Both Python and Docker:")
print(students_python & students_docker)

print("\nPython only:")
print(students_python - students_docker)

print("\nDocker only:")
print(students_docker - students_python)

print("\nEveryone:")
print(students_python | students_docker)

print("\nExactly one course:")
print(students_python ^ students_docker)