# ============================================
# INTERMEDIATE PYTHON - EXCEPTIONS & ERRORS
# ============================================


# ============================================
# 1. Basic exception handling
# ============================================

print("--- Basic try/except ---")

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ============================================
# 2. Multiple exceptions
# ============================================

print("\n--- Multiple Exceptions ---")

try:
    numbers = [10, 20, 30]

    index = int(input("Enter an index: "))

    print(numbers[index])

except ValueError:
    print("Index must be an integer.")

except IndexError:
    print("That index does not exist.")


# ============================================
# 3. Catching multiple exception types
# ============================================

try:
    value = int("abc")

except (ValueError, TypeError):
    print("\nValue or type error occurred.")


# ============================================
# 4. Exception object
# ============================================

try:
    result = 10 / 0

except ZeroDivisionError as error:
    print("\nError message:", error)
    print("Error type:", type(error).__name__)


# ============================================
# 5. else
# ============================================

print("\n--- else ---")

try:
    number = int("100")
    result = 100 / number

except (ValueError, ZeroDivisionError):
    print("Something went wrong.")

else:
    print("Everything worked.")
    print("Result:", result)


# ============================================
# 6. finally
# ============================================

print("\n--- finally ---")

try:
    file = open("example.txt", "r")

except FileNotFoundError:
    print("File doesn't exist.")

finally:
    print("This always executes.")


# ============================================
# 7. Raising an exception
# ============================================

def withdraw(balance, amount):

    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    if amount > balance:
        raise ValueError("Insufficient balance.")

    return balance - amount


try:
    balance = withdraw(1000, 1500)

except ValueError as error:
    print("\nWithdrawal failed:", error)


# ============================================
# 8. Custom exceptions
# ============================================

class InsufficientBalanceError(Exception):
    """Raised when account balance is insufficient."""
    pass


def withdraw_money(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient balance."
        )

    return balance - amount


try:
    balance = withdraw_money(1000, 1500)

except InsufficientBalanceError as error:
    print("\nCustom exception:", error)


# ============================================
# 9. Custom exception with extra information
# ============================================

class InvalidAgeError(Exception):

    def __init__(self, age):
        self.age = age

        super().__init__(
            f"Invalid age: {age}. "
            f"Age must be between 0 and 120."
        )


def validate_age(age):

    if age < 0 or age > 120:
        raise InvalidAgeError(age)

    return True


try:
    validate_age(150)

except InvalidAgeError as error:
    print("\n", error)


# ============================================
# 10. Exception chaining
# ============================================

def convert_number(value):

    try:
        return int(value)

    except ValueError as error:
        raise RuntimeError(
            "Could not convert input to integer."
        ) from error


try:
    convert_number("abc")

except RuntimeError as error:
    print("\nRuntime error:", error)


# ============================================
# 11. Catching the base Exception
# ============================================

try:
    result = 10 / 0

except Exception as error:
    print("\nCaught:", type(error).__name__)


# Avoid doing this blindly:

# except:
#     pass

# It hides errors and makes debugging difficult.


# ============================================
# 12. Practical validation example
# ============================================

def create_user(username, age):

    if not username:
        raise ValueError("Username cannot be empty.")

    if age < 18:
        raise ValueError(
            "User must be at least 18 years old."
        )

    return {
        "username": username,
        "age": age
    }


try:

    user = create_user("Alice", 16)

except ValueError as error:
    print("\nCould not create user:")
    print(error)

else:
    print("\nUser created:")
    print(user)


# ============================================
# 13. File handling with exceptions
# ============================================

print("\n--- File Handling ---")

try:

    with open("data.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("data.txt was not found.")

except PermissionError:
    print("You don't have permission to read the file.")

else:
    print("File contents:")
    print(data)


# ============================================
# 14. Nested exception handling
# ============================================

try:

    try:
        number = int("abc")

    except ValueError:
        print("\nInner exception handled.")

except Exception:
    print("Outer exception handled.")


# ============================================
# 15. Assertions
# ============================================

def calculate_percentage(marks):

    assert 0 <= marks <= 100, \
        "Marks must be between 0 and 100."

    return marks


try:
    print("\nPercentage:", calculate_percentage(85))

except AssertionError as error:
    print("Assertion failed:", error)


#ValueError
#     Correct type, invalid value

# TypeError
#     Wrong type

# IndexError
#     Invalid list index

# KeyError
#     Dictionary key doesn't exist

# FileNotFoundError
#     File doesn't exist

# ZeroDivisionError
#     Division by zero

# AttributeError
#     Object doesn't have that attribute

# ImportError / ModuleNotFoundError
#     Import problem

# PermissionError
#     Operation isn't permitted