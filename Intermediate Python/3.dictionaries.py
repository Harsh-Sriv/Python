# ============================================
# INTERMEDIATE PYTHON - DICTIONARIES
# ============================================


# ============================================
# 1. Creating a dictionary
# ============================================

student = {
    "name": "Alice",
    "age": 22,
    "course": "Computer Science",
    "marks": 91
}

print("Student:", student)


# Empty dictionary

empty_dict = {}

print("Empty dictionary:", empty_dict)


# Using dict()

person = dict(
    name="Bob",
    age=25,
    profession="Developer"
)

print("Person:", person)


# ============================================
# 2. Accessing values
# ============================================

print("\n--- Accessing Values ---")

print(student["name"])
print(student["age"])
print(student["marks"])


# ============================================
# 3. get()
# ============================================

print("\n--- get() ---")

print(student.get("name"))

# If key doesn't exist:
print(student.get("salary"))

# Provide a default value
print(student.get("salary", 0))


# Difference:

# student["salary"]
# -> KeyError

# student.get("salary")
# -> None


# ============================================
# 4. Adding new key-value pairs
# ============================================

print("\n--- Adding Data ---")

student["city"] = "Delhi"
student["email"] = "alice@example.com"

print(student)


# ============================================
# 5. Updating existing values
# ============================================

student["marks"] = 95

print("\nUpdated marks:", student["marks"])


# ============================================
# 6. update()
# ============================================

student.update({
    "age": 23,
    "city": "Bangalore",
    "phone": "9876543210"
})

print("\nAfter update():")
print(student)


# ============================================
# 7. Removing elements
# ============================================

print("\n--- Removing Data ---")

removed_value = student.pop("phone")

print("Removed:", removed_value)
print("Dictionary:", student)


# pop with default value

salary = student.pop("salary", 0)

print("Salary:", salary)


# popitem()

last_item = student.popitem()

print("Removed last item:", last_item)
print("Dictionary:", student)


# del

del student["email"]

print("After del:", student)


# clear()

temp = {"a": 1, "b": 2}
temp.clear()

print("After clear:", temp)


# ============================================
# 8. Checking whether a key exists
# ============================================

print("\n--- Checking Keys ---")

if "name" in student:
    print("Name exists")

if "salary" not in student:
    print("Salary does not exist")


# IMPORTANT:
# "name" in student checks KEYS, not values.


# ============================================
# 9. Dictionary length
# ============================================

print("\nNumber of entries:", len(student))


# ============================================
# 10. keys(), values(), items()
# ============================================

print("\n--- keys(), values(), items() ---")

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# ============================================
# 11. Iterating through dictionary keys
# ============================================

print("\n--- Keys ---")

for key in student:
    print(key)


# Same as:

for key in student.keys():
    print(key)


# ============================================
# 12. Iterating through values
# ============================================

print("\n--- Values ---")

for value in student.values():
    print(value)


# ============================================
# 13. Iterating through key-value pairs
# ============================================

print("\n--- Key-Value Pairs ---")

for key, value in student.items():
    print(key, "=>", value)


# ============================================
# 14. Nested dictionaries
# ============================================

print("\n--- Nested Dictionary ---")

users = {
    "user1": {
        "name": "Alice",
        "age": 22,
        "skills": ["Python", "SQL"]
    },

    "user2": {
        "name": "Bob",
        "age": 25,
        "skills": ["Java", "Docker"]
    }
}

print(users)


# Access nested data

print(users["user1"]["name"])

print(users["user1"]["skills"])

print(users["user1"]["skills"][0])


# Iterate

for user_id, user_data in users.items():

    print("\nUser ID:", user_id)
    print("Name:", user_data["name"])
    print("Age:", user_data["age"])

    print("Skills:")

    for skill in user_data["skills"]:
        print("-", skill)


# ============================================
# 15. Dictionary with lists
# ============================================

student = {
    "name": "Alice",
    "skills": ["Python", "C++"],
    "marks": [85, 90, 95]
}

student["skills"].append("Docker")
student["marks"].append(98)

print("\nUpdated student:")
print(student)


# ============================================
# 16. Dictionary comprehension
# ============================================

print("\n--- Dictionary Comprehension ---")

squares = {
    x: x ** 2
    for x in range(1, 6)
}

print(squares)


# Output:
# {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16,
#     5: 25
# }


# ============================================
# 17. Dictionary comprehension with condition
# ============================================

even_squares = {
    x: x ** 2
    for x in range(1, 11)
    if x % 2 == 0
}

print("Even squares:", even_squares)


# ============================================
# 18. Creating dictionary from two lists
# ============================================

names = ["Alice", "Bob", "Charlie"]
marks = [85, 92, 78]

student_marks = dict(zip(names, marks))

print("\nStudent marks:")
print(student_marks)


# ============================================
# 19. setdefault()
# ============================================

print("\n--- setdefault() ---")

data = {}

data.setdefault("name", "Alice")

print(data)


# If key already exists,
# setdefault() does NOT overwrite it.

data.setdefault("name", "Bob")

print(data)


# ============================================
# 20. Default values with dictionaries
# ============================================

print("\n--- Default Values ---")

user = {
    "name": "Alice",
    "age": 22
}

country = user.get("country", "India")

print("Country:", country)


# ============================================
# 21. Counting occurrences
# ============================================

print("\n--- Counting ---")

words = ["python", "java", "python", "cpp", "java", "python"]

frequency = {}

for word in words:

    frequency[word] = frequency.get(word, 0) + 1

print(frequency)


# ============================================
# 22. Grouping data
# ============================================

print("\n--- Grouping ---")

students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("David", "B"),
    ("Eve", "A")
]

groups = {}

for name, grade in students:

    if grade not in groups:
        groups[grade] = []

    groups[grade].append(name)

print(groups)


# ============================================
# 23. Dictionary keys must be hashable
# ============================================

valid = {
    "name": "Alice",
    1: "One",
    (1, 2): "Tuple key"
}

print("\nValid keys:")
print(valid)


# This would NOT work:

# invalid = {
#     [1, 2]: "List key"
# }

# Lists cannot be dictionary keys.


# ============================================
# 24. Dictionary copying
# ============================================

original = {
    "name": "Alice",
    "skills": ["Python", "SQL"]
}

copy1 = original.copy()

copy1["name"] = "Bob"
copy1["skills"].append("Docker")

print("\nOriginal:", original)
print("Copy:", copy1)


# ============================================
# 25. Merging dictionaries
# ============================================

dict1 = {
    "name": "Alice",
    "age": 22
}

dict2 = {
    "city": "Delhi",
    "country": "India"
}

merged = dict1 | dict2

print("\nMerged dictionary:")
print(merged)


# Another method

merged2 = {**dict1, **dict2}

print("Merged using **:")
print(merged2)


# ============================================
# 26. Handling duplicate keys
# ============================================

data = {
    "name": "Alice",
    "name": "Bob"
}

print("\nDuplicate key:")
print(data)


# The last value wins.


# ============================================
# 27. Sorting dictionary data
# ============================================

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

sorted_students = dict(
    sorted(
        students.items(),
        key=lambda item: item[1],
        reverse=True
    )
)

print("\nSorted by marks:")
print(sorted_students)