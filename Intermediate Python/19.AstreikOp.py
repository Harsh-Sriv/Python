# ============================================
# INTERMEDIATE PYTHON - ASTERISK (*) OPERATOR
# ============================================


# ============================================
# 1. *args
# ============================================

def add_numbers(*args):

    print("args:", args)
    print("Type:", type(args))

    return sum(args)


print("--- *args ---")

print(add_numbers(1, 2, 3))
print(add_numbers(10, 20, 30, 40))


# *args collects extra positional arguments
# into a tuple.


# ============================================
# 2. **kwargs
# ============================================

def show_info(**kwargs):

    print("\nkwargs:", kwargs)
    print("Type:", type(kwargs))


show_info(
    name="Alice",
    age=25,
    city="Lucknow"
)


# **kwargs collects extra keyword arguments
# into a dictionary.


# ============================================
# 3. *args + **kwargs
# ============================================

def function(*args, **kwargs):

    print("\nPositional:", args)
    print("Keyword:", kwargs)


function(
    10,
    20,
    30,
    name="Alice",
    age=25
)


# ============================================
# 4. Unpacking a list using *
# ============================================

def add(a, b, c):

    return a + b + c


numbers = [10, 20, 30]

result = add(*numbers)

print("\nList unpacking:", result)


# This:
#
# add(*numbers)
#
# is equivalent to:
#
# add(10, 20, 30)


# ============================================
# 5. Unpacking a tuple
# ============================================

values = (5, 10, 15)

print(
    "Tuple unpacking:",
    add(*values)
)


# ============================================
# 6. Unpacking a string
# ============================================

letters = "ABC"

print("\nString unpacking:")

print(*letters)


# Equivalent to:

print("A", "B", "C")


# ============================================
# 7. Combining lists with *
# ============================================

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = [
    *list1,
    *list2
]

print("\nCombined list:")
print(combined)


# ============================================
# 8. Combining multiple iterables
# ============================================

numbers = [1, 2]
letters = ["A", "B"]
colors = ["Red", "Blue"]

combined = [
    *numbers,
    *letters,
    *colors
]

print("\nCombined:")
print(combined)


# ============================================
# 9. Unpacking inside a list
# ============================================

numbers = [1, 2, 3]

result = [
    0,
    *numbers,
    4
]

print("\nInsert using unpacking:")
print(result)


# ============================================
# 10. Dictionary unpacking with **
# ============================================

user = {
    "name": "Alice",
    "age": 25
}

extra = {
    "city": "Lucknow",
    "country": "India"
}

combined = {
    **user,
    **extra
}

print("\nCombined dictionaries:")
print(combined)


# ============================================
# 11. Dictionary overriding
# ============================================

defaults = {
    "theme": "light",
    "language": "English",
    "notifications": True
}

user_settings = {
    "theme": "dark"
}

settings = {
    **defaults,
    **user_settings
}

print("\nMerged settings:")
print(settings)


# user_settings overrides theme.


# ============================================
# 12. Passing dictionary as keyword arguments
# ============================================

def create_user(name, age, city):

    return (
        f"{name}, {age}, {city}"
    )


data = {
    "name": "Bob",
    "age": 30,
    "city": "Delhi"
}

result = create_user(**data)

print("\nDictionary unpacking:")
print(result)


# ============================================
# 13. * in function definition
# ============================================

def create_account(
    name,
    *,
    age,
    country
):

    print(
        name,
        age,
        country
    )


create_account(
    "Alice",
    age=25,
    country="India"
)


# age and country MUST be keyword arguments.


# ============================================
# 14. / in function definition
# ============================================

def divide(a, b, /):

    return a / b


print("\nPositional-only:")
print(divide(10, 2))


# divide(a=10, b=2) would raise TypeError.


# ============================================
# 15. Extended unpacking
# ============================================

numbers = [
    1,
    2,
    3,
    4,
    5
]

first, *middle, last = numbers

print("\nExtended unpacking:")

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# ============================================
# 16. First + remaining
# ============================================

numbers = [10, 20, 30, 40, 50]

first, *remaining = numbers

print("\nFirst:", first)
print("Remaining:", remaining)


# ============================================
# 17. Remaining + last
# ============================================

numbers = [10, 20, 30, 40, 50]

*remaining, last = numbers

print("\nRemaining:", remaining)
print("Last:", last)


# ============================================
# 18. Unpacking nested data
# ============================================

data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 28)
]

for name, age in data:

    print(
        f"{name}: {age}"
    )


# ============================================
# 19. Star unpacking in loops
# ============================================

records = [
    ("Alice", 25, "Python", "AI"),
    ("Bob", 30, "Java", "Spring"),
    ("Charlie", 28, "C++", "Docker")
]

for name, age, *skills in records:

    print(
        name,
        age,
        skills
    )


# ============================================
# 20. Practical function forwarding
# ============================================

def execute(function, *args, **kwargs):

    print(
        f"Calling {function.__name__}"
    )

    return function(
        *args,
        **kwargs
    )


def multiply(a, b):

    return a * b


result = execute(
    multiply,
    10,
    20
)

print("\nForwarded result:", result)