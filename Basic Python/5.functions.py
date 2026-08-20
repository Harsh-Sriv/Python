# ============================================================
#                    PYTHON FUNCTIONS
# ============================================================

# A function is a reusable block of code.
#
# Basic syntax:
#
# def function_name(parameters):
#     code
#
# Use the function by calling:
# function_name(arguments)


# ============================================================
# 1. Function without parameters
# ============================================================

def greet():
    print("Hello, Python!")


greet()


# ============================================================
# 2. Function with parameters
# ============================================================

def greet_user(name):
    print("Hello", name)


greet_user("Harsh")


# ============================================================
# 3. Function with multiple parameters
# ============================================================

def add(a, b):
    print(a + b)


add(10, 20)


# ============================================================
# 4. Function with return
# ============================================================

def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)

print("Result:", result)

# return sends the result back to the place
# where the function was called.


# ============================================================
# 5. Returning multiple values
# ============================================================

def calculate(a, b):
    return a + b, a - b


sum_value, difference = calculate(10, 5)

print(sum_value)
print(difference)

# Python actually returns these values as a tuple.


# ============================================================
# 6. Default parameters
# ============================================================

def greet(name="User"):
    print("Hello", name)


greet("Harsh")
greet()                  # Uses default value


# ============================================================
# 7. Keyword arguments
# ============================================================

def student(name, age):
    print("Name:", name)
    print("Age:", age)


student(age=22, name="Harsh")

# We specify the parameter name,
# so the order doesn't matter.


# ============================================================
# 8. Positional arguments
# ============================================================

def multiply(a, b):
    return a * b


print(multiply(5, 4))

# 5 goes to a
# 4 goes to b


# ============================================================
# 9. *args - Variable number of arguments
# ============================================================

def total(*numbers):
    return sum(numbers)


print(total(10, 20))
print(total(10, 20, 30, 40))

# *args stores multiple positional arguments
# inside a tuple.


# ============================================================
# 10. **kwargs - Variable keyword arguments
# ============================================================

def information(**details):
    print(details)


information(name="Harsh", age=22, city="Lucknow")

# **kwargs stores multiple keyword arguments
# inside a dictionary.


# ============================================================
# 11. Function with *args and normal parameter
# ============================================================

def calculate_sum(name, *numbers):
    print(name, ":", sum(numbers))


calculate_sum("Total", 10, 20, 30)


# ============================================================
# 12. Return without a value
# ============================================================

def check_age(age):

    if age < 18:
        return                # Stops the function

    print("You are eligible.")


check_age(15)


# ============================================================
# 13. Multiple return conditions
# ============================================================

def check_number(number):

    if number > 0:
        return "Positive"

    elif number < 0:
        return "Negative"

    return "Zero"


print(check_number(10))
print(check_number(-5))
print(check_number(0))


# ============================================================
# 14. Function calling another function
# ============================================================

def square(n):
    return n * n


def cube(n):
    return square(n) * n


print(cube(3))


# ============================================================
# 15. Lambda function
# ============================================================

# A lambda is a small anonymous function.

square = lambda x: x * x

print(square(5))

# Equivalent normal function:
#
# def square(x):
#     return x * x


# ============================================================
# 16. Function with type hints
# ============================================================

def add(a: int, b: int) -> int:# the "-> int" indicates that the function is expected to return an integer
    # if the given values are not integers like foat or string, it will still work but it is not recommended to use other types.
    return a + b


print(add(10, 20))

# Type hints tell us what type is expected.
#
# a: int       -> a should be an integer
# -> int       -> function is expected to return an integer
#
# Python does not strictly enforce these types.


# ============================================================
#                QUICK REFERENCE
# ============================================================

"""
1. Basic function

def greet():
    print("Hello")


2. Parameters

def greet(name):
    print(name)


3. Return

def add(a, b):
    return a + b


4. Default parameter

def greet(name="User"):
    print(name)


5. Keyword arguments

greet(name="Harsh")


6. *args

def total(*numbers):
    return sum(numbers)

# Multiple positional arguments -> tuple


7. **kwargs

def info(**details):
    print(details)

# Multiple keyword arguments -> dictionary


8. Lambda

square = lambda x: x * x


9. Type hints

def add(a: int, b: int) -> int:
    return a + b
"""