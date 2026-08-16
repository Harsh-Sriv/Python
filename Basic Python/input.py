# ============================================================
#                  PYTHON input() FUNCTION
# ============================================================

# input() is used to take input from the user.
# IMPORTANT: input() always returns a STRING.


# ============================================================
# 1. Basic input
# ============================================================

print("--- Basic Input ---")

name = input("Enter your name: ")

print("Hello", name)


# ============================================================
# 2. Taking a number as input
# ============================================================

print("\n--- Integer Input ---")

# input() gives us a string, so we use int()
# to convert it into an integer.

age = int(input("Enter your age: "))

print("Your age is:", age)


# ============================================================
# 3. Taking a decimal number
# ============================================================

print("\n--- Float Input ---")

# Use float() when the user may enter a decimal number.

price = float(input("Enter the price: "))

print("Price:", price)


# ============================================================
# 4. Taking multiple inputs
# ============================================================

print("\n--- Multiple Inputs ---")

# split() separates the input into multiple values.

a, b = input("Enter two numbers: ").split()

# Convert them to integers

a = int(a)
b = int(b)

print("Sum:", a + b)


# A shorter way:

x, y = map(int, input("Enter two numbers: ").split())

print("Sum:", x + y)


# ============================================================
# 5. Taking multiple values into a list
# ============================================================

print("\n--- Input List ---")

# Example input:
# 10 20 30 40 50

numbers = list(map(int, input("Enter numbers: ").split()))

print(numbers)


# ============================================================
# 6. Taking a string with spaces
# ============================================================

print("\n--- String with Spaces ---")

# input() can directly take spaces.
# Do NOT use split() if you want the complete sentence.

sentence = input("Enter a sentence: ")

print("You entered:", sentence)


# ============================================================
# 7. Using input in a calculation
# ============================================================

print("\n--- Calculation ---")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)


# ============================================================
# 8. Checking user input
# ============================================================

print("\n--- Checking Input ---")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# ============================================================
# 9. Input with a default-looking prompt
# ============================================================

print("\n--- Prompt ---")

# The text inside input() is simply shown to the user.

name = input("Name: ")
age = int(input("Age: "))

print(f"{name} is {age} years old.")


# ============================================================
# 10. IMPORTANT: input() ALWAYS RETURNS STRING
# ============================================================

print("\n--- Important ---")

x = input("Enter a number: ")

print(type(x))

# Even if you enter 100, the type is:
# <class 'str'>

# Therefore:

x = int(input("Enter a number: "))

print(type(x))

# Now the type is:
# <class 'int'>


# ============================================================
#                 QUICK REFERENCE
# ============================================================

"""
input()                          -> Take input as string

int(input())                     -> Take integer input

float(input())                   -> Take decimal input

input().split()                  -> Take multiple inputs

map(int, input().split())        -> Convert multiple inputs to int

list(map(int, input().split()))  -> Take multiple integers as a list


Examples:

name = input("Name: ")

age = int(input("Age: "))

price = float(input("Price: "))

a, b = map(int, input().split())

numbers = list(map(int, input().split()))
"""