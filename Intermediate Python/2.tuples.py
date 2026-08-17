# ============================================
# INTERMEDIATE PYTHON - TUPLES
# ============================================

# 1. Creating tuples
# ============================================

numbers = (10, 20, 30, 40, 50)
names = ("Alice", "Bob", "Charlie")

print("Numbers:", numbers)
print("Names:", names)


# A tuple can contain different data types

person = ("Harsh", 22, 9.3, True)

print("Person:", person)


# ============================================
# 2. Single-element tuple
# ============================================

# IMPORTANT:
# The comma makes it a tuple

single = (10,)

print("\nSingle-element tuple:", single)
print("Type:", type(single))


# Without comma, this is just an integer

not_a_tuple = (10)

print("Type:", type(not_a_tuple))


# ============================================
# 3. Tuple indexing
# ============================================

print("\n--- Indexing ---")

print(numbers[0])
print(numbers[2])
print(numbers[-1])
print(numbers[-2])


# ============================================
# 4. Tuple slicing
# ============================================

print("\n--- Slicing ---")

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::2])
print(numbers[::-1])


# ============================================
# 5. Tuples are immutable
# ============================================

# This will cause an error:

# numbers[0] = 100

# TypeError:
# 'tuple' object does not support item assignment


# ============================================
# 6. Tuple methods
# ============================================

numbers = (10, 20, 30, 20, 40, 20)

print("\n--- Tuple Methods ---")

print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))


# ============================================
# 7. Checking membership
# ============================================

print("\n--- Membership ---")

print(20 in numbers)
print(100 in numbers)

if 30 in numbers:
    print("30 exists in the tuple")


# ============================================
# 8. Iterating through a tuple
# ============================================

print("\n--- Iteration ---")

for number in numbers:
    print(number)


# ============================================
# 9. enumerate()
# ============================================

print("\n--- enumerate() ---")

for index, value in enumerate(numbers):
    print(index, value)


# ============================================
# 10. Tuple unpacking
# ============================================

print("\n--- Tuple Unpacking ---")

person = ("Alice", 25, "Developer")

name, age, profession = person

print("Name:", name)
print("Age:", age)
print("Profession:", profession)


# ============================================
# 11. Extended unpacking
# ============================================

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("\nFirst:", first)
print("Middle:", middle)
print("Last:", last)


# ============================================
# 12. Swapping variables
# ============================================

a = 10
b = 20

print("\nBefore swap:", a, b)

a, b = b, a

print("After swap:", a, b)


# Python internally uses tuple unpacking here.


# ============================================
# 13. Tuple concatenation
# ============================================

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2

print("\nCombined:", combined)


# ============================================
# 14. Tuple repetition
# ============================================

repeated = (1, 2, 3) * 3

print("Repeated:", repeated)


# ============================================
# 15. Nested tuples
# ============================================

students = (
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
)

print("\n--- Nested Tuples ---")

print(students)
print(students[0])
print(students[0][0])
print(students[1][1])


# Iterate through nested tuples

for name, marks in students:
    print(name, "scored", marks)


# ============================================
# 16. Tuple containing mutable objects
# ============================================

# The tuple itself cannot be changed,
# but a mutable object INSIDE it can be changed.

data = ("Python", [1, 2, 3])

data[1].append(4)

print("\nTuple containing list:")
print(data)


# But this is NOT allowed:

# data[1] = [10, 20, 30]


# ============================================
# 17. Converting list ↔ tuple
# ============================================

numbers_list = [1, 2, 3, 4, 5]

numbers_tuple = tuple(numbers_list)

print("\nList to tuple:")
print(numbers_tuple)


numbers_list_again = list(numbers_tuple)

print("Tuple to list:")
print(numbers_list_again)


# ============================================
# 18. Tuple vs list memory/use case
# ============================================

# List → usually used for collections that change
shopping_cart = ["Milk", "Bread", "Eggs"]

shopping_cart.append("Butter")


# Tuple → usually used for fixed data

coordinates = (28.6139, 77.2090)

print("\nShopping cart:", shopping_cart)
print("Coordinates:", coordinates)


# ============================================
# 19. Returning multiple values from a function
# ============================================

def get_user():
    name = "Alice"
    age = 25
    profession = "Developer"

    return name, age, profession


result = get_user()

print("\nFunction returned:", result)
print("Type:", type(result))


name, age, profession = get_user()

print(name)
print(age)
print(profession)


# ============================================
# 20. Tuple comparison
# ============================================

print("\n--- Tuple Comparison ---")

print((1, 2, 3) == (1, 2, 3))
print((1, 2, 3) == (1, 2, 4))

print((1, 2) < (2, 1))


# ============================================
# 21. Sorting tuples
# ============================================

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

students_sorted = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("\nStudents sorted by marks:")
print(students_sorted)