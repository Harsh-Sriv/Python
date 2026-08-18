# ============================================================
#                 MODULES AND PIP IN PYTHON
# ============================================================

# A MODULE is a Python file containing functions, classes,
# and variables that we can reuse in another program.


# ============================================================
# 1. Importing a built-in module
# ============================================================

import math

print(math.sqrt(25))       # Square root
print(math.pi)             # Value of π


# ============================================================
# 2. Import specific functions
# ============================================================

from math import sqrt, factorial

print(sqrt(16))
print(factorial(5))


# ============================================================
# 3. Import with an alias
# ============================================================

import math as m

print(m.sqrt(100))


# ============================================================
# 4. Some useful built-in modules
# ============================================================

import random
import datetime

print(random.randint(1, 10))       # Random number

print(datetime.date.today())       # Today's date


# ============================================================
# 5. Creating your own module
# ============================================================

# Suppose we have a file called calculator.py:
#
# calculator.py
#
# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b
#
#
# We can import it into another Python file:

# import calculator
#
# print(calculator.add(10, 20))
# print(calculator.multiply(5, 4))


# ============================================================
# 6. __name__ == "__main__"
# ============================================================

# This is commonly used in Python modules.

def greet():
    print("Hello Python")


if __name__ == "__main__":
    greet()

# The code inside this if statement runs only when
# this file is executed directly.


# ============================================================
#                         PIP
# ============================================================

# pip is Python's package manager.
#
# It is used to install third-party Python packages.


# Install a package from the terminal:
#
# pip install requests
#
# Then use it:
#
# import requests


# ============================================================
# Useful pip commands
# ============================================================

"""
pip install package_name
    -> Install a package

pip uninstall package_name
    -> Remove a package

pip list
    -> Show installed packages

pip show package_name
    -> Show package information

pip install --upgrade package_name
    -> Upgrade a package

pip freeze
    -> Show installed packages and versions

pip install -r requirements.txt
    -> Install packages listed in requirements.txt
"""


# ============================================================
#             MODULE vs PACKAGE vs LIBRARY
# ============================================================

"""
MODULE
-> Usually a single .py file.

Example:
math.py


PACKAGE
-> Collection of Python modules.

Example:
requests


LIBRARY
-> General term for reusable code/packages.


PIP
-> Tool used to install and manage Python packages.
"""