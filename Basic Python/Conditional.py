# ============================================================
#              CONDITIONAL STATEMENTS IN PYTHON
# ============================================================

# Conditional statements are used to make decisions
# based on whether a condition is True or False.


# ============================================================
# 1. if statement
# ============================================================

age = 20

if age >= 18:
    print("You are an adult.")


# ============================================================
# 2. if-else
# ============================================================

number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ============================================================
# 3. if-elif-else
# ============================================================

marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")


# ============================================================
# 4. Nested if
# ============================================================

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("ID required.")
else:
    print("You must be 18 or older.")


# ============================================================
# 5. Logical operators
# ============================================================

age = 22
has_ticket = True

# and -> Both conditions must be True
if age >= 18 and has_ticket:
    print("You can enter.")


# or -> At least one condition must be True
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("It's a day off.")


# not -> Reverses True/False
logged_in = False

if not logged_in:
    print("Please log in.")


# ============================================================
# 6. Comparison operators
# ============================================================

a = 10
b = 20

if a < b:
    print("a is smaller")

# Operators:
# ==    Equal
# !=    Not equal
# >     Greater than
# <     Less than
# >=    Greater than or equal
# <=    Less than or equal


# ============================================================
# 7. Checking membership
# ============================================================

numbers = [10, 20, 30]

if 20 in numbers:
    print("20 exists in the list.")

if 50 not in numbers:
    print("50 does not exist.")


# ============================================================
# 8. Checking multiple conditions
# ============================================================

number = 15

if number > 0 and number % 2 == 0:
    print("Positive even number")
elif number > 0:
    print("Positive odd number")
else:
    print("Negative or zero")


# ============================================================
# 9. Ternary / Conditional Expression
# ============================================================

number = 10

result = "Even" if number % 2 == 0 else "Odd"

print(result)

# Equivalent to:
#
# if number % 2 == 0:
#     result = "Even"
# else:
#     result = "Odd"


# ============================================================
# 10. Truthy and Falsy values
# ============================================================

# Python treats some values as False:
#
# False
# None
# 0
# 0.0
# ""
# []
# {}
# set()
#
# Most other values are True.

name = ""

if name:
    print("Name exists.")
else:
    print("Name is empty.")


# ============================================================
# 11. pass - Do nothing
# ============================================================

number = 10

if number > 0:
    pass                # Placeholder for code written later
else:
    print("Negative")


# ============================================================
#                 QUICK REFERENCE
# ============================================================

"""
if:

if condition:
    code


if-else:

if condition:
    code
else:
    code


if-elif-else:

if condition:
    code
elif condition:
    code
else:
    code


Logical operators:

and -> Both conditions True
or  -> At least one condition True
not -> Reverses condition


Comparison:

==  -> Equal
!=  -> Not equal
>   -> Greater
<   -> Less
>=  -> Greater/equal
<=  -> Less/equal


Membership:

x in collection
x not in collection


Ternary:

value_if_true if condition else value_if_false
"""