# ============================================
# INTERMEDIATE PYTHON - ITERTOOLS
# ============================================

import itertools


# ============================================
# 1. count()
# ============================================

print("--- count() ---")

# Creates an infinite sequence:
# 10, 12, 14, 16, ...

counter = itertools.count(10, 2)

for number in itertools.islice(counter, 5):
    print(number)


# ============================================
# 2. cycle()
# ============================================

print("\n--- cycle() ---")

colors = ["Red", "Green", "Blue"]

cycled = itertools.cycle(colors)

for _ in range(7):
    print(next(cycled))


# ============================================
# 3. repeat()
# ============================================

print("\n--- repeat() ---")

for value in itertools.repeat("Python", 3):
    print(value)


# ============================================
# 4. chain()
# ============================================

print("\n--- chain() ---")

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7]

combined = itertools.chain(list1, list2, list3)

for number in combined:
    print(number)


# ============================================
# 5. chain.from_iterable()
# ============================================

print("\n--- chain.from_iterable() ---")

lists = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flattened = itertools.chain.from_iterable(lists)

print(list(flattened))


# ============================================
# 6. zip_longest()
# ============================================

print("\n--- zip_longest() ---")

names = ["Alice", "Bob", "Charlie"]
marks = [90, 85]

result = itertools.zip_longest(
    names,
    marks,
    fillvalue=0
)

for name, mark in result:
    print(name, mark)


# ============================================
# 7. product()
# ============================================

print("\n--- product() ---")

colors = ["Red", "Blue"]
sizes = ["S", "M", "L"]

products = itertools.product(colors, sizes)

for product in products:
    print(product)


# ============================================
# 8. product() with repeat
# ============================================

print("\n--- product() repeat ---")

for result in itertools.product([0, 1], repeat=3):
    print(result)


# ============================================
# 9. permutations()
# ============================================

print("\n--- permutations() ---")

letters = ["A", "B", "C"]

for result in itertools.permutations(letters):
    print(result)


# Permutations of length 2

print("\nLength 2 permutations:")

for result in itertools.permutations(letters, 2):
    print(result)


# ============================================
# 10. combinations()
# ============================================

print("\n--- combinations() ---")

numbers = [1, 2, 3, 4]

for result in itertools.combinations(numbers, 2):
    print(result)


# ============================================
# 11. combinations_with_replacement()
# ============================================

print("\n--- combinations_with_replacement() ---")

for result in itertools.combinations_with_replacement(
    [1, 2, 3],
    2
):
    print(result)


# ============================================
# 12. accumulate()
# ============================================

print("\n--- accumulate() ---")

numbers = [1, 2, 3, 4, 5]

running_total = itertools.accumulate(numbers)

print(list(running_total))


# ============================================
# 13. accumulate() with multiplication
# ============================================

print("\n--- Accumulate multiplication ---")

numbers = [1, 2, 3, 4]

running_product = itertools.accumulate(
    numbers,
    lambda x, y: x * y
)

print(list(running_product))


# ============================================
# 14. accumulate() with max
# ============================================

numbers = [3, 7, 2, 9, 5]

running_max = itertools.accumulate(
    numbers,
    max
)

print("\nRunning maximum:")
print(list(running_max))


# ============================================
# 15. islice()
# ============================================

print("\n--- islice() ---")

numbers = range(100)

first_five = itertools.islice(numbers, 5)

print(list(first_five))


# Similar to slicing, but works with iterators.

numbers = range(20)

selected = itertools.islice(
    numbers,
    2,
    10,
    2
)

print(list(selected))


# ============================================
# 16. takewhile()
# ============================================

print("\n--- takewhile() ---")

numbers = [2, 4, 6, 8, 9, 10, 12]

result = itertools.takewhile(
    lambda x: x % 2 == 0,
    numbers
)

print(list(result))


# ============================================
# 17. dropwhile()
# ============================================

print("\n--- dropwhile() ---")

numbers = [2, 4, 6, 8, 9, 10, 12]

result = itertools.dropwhile(
    lambda x: x % 2 == 0,
    numbers
)

print(list(result))


# ============================================
# 18. filterfalse()
# ============================================

print("\n--- filterfalse() ---")

numbers = range(1, 11)

odd_numbers = itertools.filterfalse(
    lambda x: x % 2 == 0,
    numbers
)

print(list(odd_numbers))


# ============================================
# 19. compress()
# ============================================

print("\n--- compress() ---")

names = ["Alice", "Bob", "Charlie", "David"]

selectors = [True, False, True, False]

selected_names = itertools.compress(
    names,
    selectors
)

print(list(selected_names))


# ============================================
# 20. groupby()
# ============================================

print("\n--- groupby() ---")

students = [
    ("Alice", "A"),
    ("Bob", "A"),
    ("Charlie", "B"),
    ("David", "B"),
    ("Eve", "C")
]

# IMPORTANT:
# groupby() groups consecutive elements
# with the same key.

for grade, group in itertools.groupby(
    students,
    key=lambda student: student[1]
):
    print(grade, list(group))


# ============================================
# 21. groupby() after sorting
# ============================================

students = [
    ("Alice", "A"),
    ("Charlie", "B"),
    ("Bob", "A"),
    ("David", "B"),
    ("Eve", "A")
]

students.sort(key=lambda student: student[1])

print("\nGrouped after sorting:")

for grade, group in itertools.groupby(
    students,
    key=lambda student: student[1]
):
    print(grade, list(group))


# ============================================
# 22. Practical example
# ============================================

print("\n--- Practical Example ---")

servers = ["Server A", "Server B", "Server C"]

statuses = ["Online", "Offline", "Online"]

server_status = itertools.zip_longest(
    servers,
    statuses,
    fillvalue="Unknown"
)

for server, status in server_status:
    print(f"{server}: {status}")


# ============================================
# 23. Combining multiple itertools
# ============================================

print("\n--- Combining itertools ---")

numbers = range(1, 21)

result = itertools.islice(
    itertools.filterfalse(
        lambda x: x % 2 != 0,
        numbers
    ),
    5
)

print(list(result))