# ============================================================
#                 TRY-EXCEPT IN PYTHON
# ============================================================

# try-except is used to handle errors (exceptions)
# without crashing the entire program.

# Basic structure:
#
# try:
#     code that may cause an error
# except:
#     code to handle the error


# ============================================================
# 1. Basic try-except
# ============================================================

try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except:
    print("Please enter a valid number.")


# ============================================================
# 2. Handling a specific exception
# ============================================================

try:
    a = 10
    b = 0

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ============================================================
# 3. Multiple except blocks
# ============================================================

try:
    a = int(input("Enter a number: "))
    print(10 / a)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")


# ============================================================
# 4. else
# ============================================================

# else runs ONLY when no exception occurs.

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)


# ============================================================
# 5. finally
# ============================================================

# finally ALWAYS executes, whether an exception occurs or not.

try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program finished.")


# ============================================================
# 6. Getting the error message
# ============================================================

try:
    number = int("hello")

except ValueError as e:
    print("Error:", e)


# ============================================================
# 7. Raising an exception
# ============================================================

def check_age(age):

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    return "Eligible"


try:
    print(check_age(15))

except ValueError as e:
    print(e)


# ============================================================
#                 QUICK REFERENCE
# ============================================================

"""
try:
    # Code that may cause an error

except:
    # Handle the error

except SomeError:
    # Handle a specific error

else:
    # Runs if NO error occurs

finally:
    # ALWAYS runs


Common exceptions:

ValueError
-> Invalid value, e.g. int("hello")

ZeroDivisionError
-> Division by zero

IndexError
-> Invalid list index

KeyError
-> Missing dictionary key

TypeError
-> Invalid operation between types

FileNotFoundError
-> File does not exist


Get error message:

except ValueError as e:
    print(e)


Manually raise an error:

raise ValueError("Invalid value")
"""