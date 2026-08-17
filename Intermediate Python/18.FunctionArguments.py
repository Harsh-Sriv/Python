# ============================================
# INTERMEDIATE PYTHON - FUNCTION ARGUMENTS
# ============================================


# ============================================
# 1. Positional arguments
# ============================================

def greet(name, age):

    print(
        f"Hello {name}, "
        f"you are {age} years old."
    )


greet("Alice", 25)


# Position matters.

greet("Bob", 30)


# ============================================
# 2. Keyword arguments
# ============================================

greet(
    name="Charlie",
    age=28
)


# Order doesn't matter with keywords.

greet(
    age=28,
    name="Charlie"
)


# ============================================
# 3. Mixing positional and keyword arguments
# ============================================

def introduce(name, age, city):

    print(
        f"{name}, {age}, from {city}"
    )


introduce(
    "Alice",
    age=25,
    city="Lucknow"
)


# Positional arguments must come before
# keyword arguments.


# ============================================
# 4. Default arguments
# ============================================

def greet_user(
    name,
    message="Hello"
):

    print(f"{message}, {name}")


greet_user("Alice")

greet_user(
    "Bob",
    "Good morning"
)


# ============================================
# 5. Multiple default arguments
# ============================================

def create_user(
    name,
    age=18,
    country="India"
):

    return {
        "name": name,
        "age": age,
        "country": country
    }


print("\n", create_user("Alice"))

print(
    create_user(
        "Bob",
        25
    )
)

print(
    create_user(
        "Charlie",
        30,
        "USA"
    )
)


# ============================================
# 6. *args
# ============================================

def add_numbers(*args):

    print("Arguments:", args)
    print("Type:", type(args))

    total = 0

    for number in args:
        total += number

    return total


print("\nSum:", add_numbers(1, 2, 3))

print(
    "Sum:",
    add_numbers(
        10,
        20,
        30,
        40
    )
)


# *args becomes a tuple.


# ============================================
# 7. Normal parameter + *args
# ============================================

def introduce_group(
    leader,
    *members
):

    print("\nLeader:", leader)

    print("Members:")

    for member in members:
        print(member)


introduce_group(
    "Alice",
    "Bob",
    "Charlie",
    "David"
)


# ============================================
# 8. **kwargs
# ============================================

def show_user(**kwargs):

    print("\nKeyword arguments:")
    print(kwargs)

    print(
        "Type:",
        type(kwargs)
    )


show_user(
    name="Alice",
    age=25,
    city="Lucknow"
)


# **kwargs becomes a dictionary.


# ============================================
# 9. Iterating over **kwargs
# ============================================

def print_user(**kwargs):

    for key, value in kwargs.items():

        print(
            f"{key}: {value}"
        )


print_user(
    name="Alice",
    age=25,
    skill="Python"
)


# ============================================
# 10. *args and **kwargs together
# ============================================

def example(
    *args,
    **kwargs
):

    print("\nPositional:", args)
    print("Keyword:", kwargs)


example(
    1,
    2,
    3,
    name="Alice",
    age=25
)


# ============================================
# 11. Combining normal arguments,
#     *args and **kwargs
# ============================================

def function(
    required,
    *args,
    **kwargs
):

    print("\nRequired:", required)
    print("Extra positional:", args)
    print("Extra keyword:", kwargs)


function(
    "Hello",
    10,
    20,
    30,
    name="Alice",
    age=25
)


# ============================================
# 12. Unpacking a list/tuple with *
# ============================================

def add(a, b, c):

    return a + b + c


numbers = [10, 20, 30]

result = add(*numbers)

print("\nUnpacked list:", result)


# Equivalent to:
# add(10, 20, 30)


# ============================================
# 13. Unpacking a tuple
# ============================================

values = (1, 2, 3)

print(
    "Unpacked tuple:",
    add(*values)
)


# ============================================
# 14. Unpacking dictionary with **
# ============================================

def create_profile(
    name,
    age,
    city
):

    return (
        f"{name}, "
        f"{age}, "
        f"{city}"
    )


data = {
    "name": "Alice",
    "age": 25,
    "city": "Lucknow"
}


profile = create_profile(**data)

print("\nUnpacked dictionary:")
print(profile)


# ============================================
# 15. Positional-only arguments
# ============================================

def divide(
    a,
    b,
    /
):

    return a / b


print("\nDivide:", divide(10, 2))


# This would NOT work:
#
# divide(a=10, b=2)


# Because a and b are positional-only.


# ============================================
# 16. Keyword-only arguments
# ============================================

def create_account(
    name,
    *,
    age,
    country
):

    return {
        "name": name,
        "age": age,
        "country": country
    }


account = create_account(
    "Alice",
    age=25,
    country="India"
)

print("\nAccount:")
print(account)


# These would NOT work:
#
# create_account("Alice", 25, "India")


# ============================================
# 17. Positional-only + keyword-only
# ============================================

def process(
    name,
    /,
    age,
    *,
    country,
    active=True
):

    print(
        name,
        age,
        country,
        active
    )


process(
    "Alice",
    25,
    country="India"
)


# name → positional only
# age → positional OR keyword
# country → keyword only
# active → keyword only


# ============================================
# 18. Keyword arguments with defaults
# ============================================

def connect(
    host,
    port=8080,
    *,
    secure=False
):

    print(
        f"Host: {host}"
    )

    print(
        f"Port: {port}"
    )

    print(
        f"Secure: {secure}"
    )


connect(
    "localhost"
)

connect(
    "example.com",
    443,
    secure=True
)


# ============================================
# 19. Mutable default argument problem
# ============================================

# DON'T normally do this:

def add_item(
    item,
    items=[]
):

    items.append(item)

    return items


print("\nMutable default example:")

print(add_item("A"))
print(add_item("B"))


# The same list is reused!


# ============================================
# 20. Correct approach
# ============================================

def add_item_safe(
    item,
    items=None
):

    if items is None:
        items = []

    items.append(item)

    return items


print("\nSafe version:")

print(add_item_safe("A"))
print(add_item_safe("B"))


# ============================================
# 21. Function argument validation
# ============================================

def calculate_average(*numbers):

    if not numbers:
        raise ValueError(
            "At least one number is required."
        )

    return sum(numbers) / len(numbers)


print(
    "\nAverage:",
    calculate_average(
        10,
        20,
        30
    )
)


# ============================================
# 22. Forwarding arguments
# ============================================

def log_function(
    function,
    *args,
    **kwargs
):

    print(
        f"Calling {function.__name__}"
    )

    return function(
        *args,
        **kwargs
    )


def multiply(a, b):

    return a * b


result = log_function(
    multiply,
    10,
    20
)

print("\nForwarded result:", result)