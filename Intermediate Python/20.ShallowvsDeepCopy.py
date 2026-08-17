# ============================================
# INTERMEDIATE PYTHON - SHALLOW VS DEEP COPY
# ============================================

import copy


# ============================================
# 1. Assignment is NOT copying
# ============================================

original = [1, 2, 3]

assigned = original

assigned.append(4)

print("--- Assignment ---")
print("Original:", original)
print("Assigned:", assigned)

print(
    "Same object:",
    original is assigned
)


# Both variables refer to the same object.


# ============================================
# 2. Shallow copy using copy()
# ============================================

original = [1, 2, 3]

shallow = original.copy()

shallow.append(4)

print("\n--- Shallow copy ---")
print("Original:", original)
print("Shallow:", shallow)

print(
    "Same object:",
    original is shallow
)


# Outer lists are different.


# ============================================
# 3. Shallow copy using slicing
# ============================================

original = [1, 2, 3]

shallow = original[:]

shallow.append(4)

print("\n--- Slicing copy ---")
print("Original:", original)
print("Shallow:", shallow)


# ============================================
# 4. Shallow copy using copy.copy()
# ============================================

original = [1, 2, 3]

shallow = copy.copy(original)

shallow.append(4)

print("\n--- copy.copy() ---")
print("Original:", original)
print("Shallow:", shallow)


# ============================================
# 5. Nested list problem
# ============================================

original = [
    [1, 2],
    [3, 4]
]

shallow = copy.copy(original)

shallow[0].append(99)

print("\n--- Nested shallow copy ---")

print("Original:", original)
print("Shallow:", shallow)


# The nested list was shared.


# ============================================
# 6. Understanding nested references
# ============================================

original = [
    [1, 2],
    [3, 4]
]

shallow = copy.copy(original)

print("\n--- Object identity ---")

print(
    "Outer same:",
    original is shallow
)

print(
    "Inner same:",
    original[0] is shallow[0]
)


# Outer → different
# Inner → same


# ============================================
# 7. Deep copy
# ============================================

original = [
    [1, 2],
    [3, 4]
]

deep = copy.deepcopy(original)

deep[0].append(99)

print("\n--- Deep copy ---")

print("Original:", original)
print("Deep:", deep)


# ============================================
# 8. Identity with deep copy
# ============================================

print("\n--- Deep identity ---")

print(
    "Outer same:",
    original is deep
)

print(
    "Inner same:",
    original[0] is deep[0]
)


# Both are False.


# ============================================
# 9. Nested dictionaries
# ============================================

original = {
    "user": {
        "name": "Alice",
        "age": 25
    },
    "skills": [
        "Python",
        "Docker"
    ]
}

shallow = copy.copy(original)

shallow["user"]["age"] = 30

print("\n--- Nested dictionary ---")

print("Original:", original)
print("Shallow:", shallow)


# ============================================
# 10. Deep copy nested dictionary
# ============================================

original = {
    "user": {
        "name": "Alice",
        "age": 25
    },
    "skills": [
        "Python",
        "Docker"
    ]
}

deep = copy.deepcopy(original)

deep["user"]["age"] = 30
deep["skills"].append("MongoDB")

print("\n--- Deep dictionary copy ---")

print("Original:", original)
print("Deep:", deep)


# ============================================
# 11. Mixed nested objects
# ============================================

original = {
    "users": [
        {
            "name": "Alice",
            "skills": ["Python"]
        }
    ]
}

shallow = copy.copy(original)

shallow["users"][0]["skills"].append("AI")

print("\n--- Mixed nested structure ---")

print("Original:", original)
print("Shallow:", shallow)


# ============================================
# 12. Deep copy mixed structure
# ============================================

original = {
    "users": [
        {
            "name": "Alice",
            "skills": ["Python"]
        }
    ]
}

deep = copy.deepcopy(original)

deep["users"][0]["skills"].append("AI")

print("\n--- Deep mixed copy ---")

print("Original:", original)
print("Deep:", deep)


# ============================================
# 13. Immutable objects
# ============================================

original = (1, 2, 3)

shallow = copy.copy(original)
deep = copy.deepcopy(original)

print("\n--- Immutable objects ---")

print(
    "Original:",
    original
)

print(
    "Shallow:",
    shallow
)

print(
    "Deep:",
    deep
)


# ============================================
# 14. Practical example
# ============================================

default_config = {
    "database": {
        "host": "localhost",
        "port": 27017
    },
    "features": {
        "logging": True,
        "cache": True
    }
}

# We want a completely independent config.

user_config = copy.deepcopy(
    default_config
)

user_config["database"]["port"] = 27018
user_config["features"]["cache"] = False

print("\n--- Configuration ---")

print("Default:")
print(default_config)

print("User:")
print(user_config)