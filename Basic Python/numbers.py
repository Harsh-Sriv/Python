# ============================================================
#                  PYTHON NUMBERS
# ============================================================

# Python mainly has these numeric types:
#
# int   -> Whole numbers
# float -> Decimal numbers
# complex -> Complex numbers
#
# Examples:

age = 22                  # int
price = 99.99             # float
complex_number = 3 + 4j   # complex

print(age)
print(price)
print(complex_number)


# ============================================================
# 1. TYPE() - Find the type of a number
# ============================================================

print("\n--- type() ---")

x = 10
y = 10.5

print(type(x))            # <class 'int'>
print(type(y))            # <class 'float'>


# ============================================================
# 2. INT() - Convert to integer
# ============================================================

print("\n--- int() ---")

print(int(10.8))          # 10
print(int("25"))          # 25

# Important:
# int() removes the decimal part.
# It does NOT round the number.

print(int(99.99))         # 99


# ============================================================
# 3. FLOAT() - Convert to decimal number
# ============================================================

print("\n--- float() ---")

print(float(10))          # 10.0
print(float("25.5"))      # 25.5


# ============================================================
# 4. ABS() - Absolute value
# ============================================================

print("\n--- abs() ---")

print(abs(10))            # 10
print(abs(-10))           # 10
print(abs(-25.5))         # 25.5

# Absolute value removes the negative sign.


# ============================================================
# 5. POW() - Power
# ============================================================

print("\n--- pow() ---")

print(pow(2, 3))          # 2³ = 8
print(pow(5, 2))          # 5² = 25

# pow(base, exponent)

# You can also use **

print(2 ** 3)
print(5 ** 2)


# ============================================================
# 6. ROUND() - Round a number
# ============================================================

print("\n--- round() ---")

print(round(10.4))        # 10
print(round(10.6))        # 11

# You can specify the number of decimal places.

print(round(10.4567, 2))  # 10.46
print(round(10.4567, 3))  # 10.457


# ============================================================
# 7. MAX() - Find the largest number
# ============================================================

print("\n--- max() ---")

print(max(10, 20, 30, 5))

numbers = [10, 50, 20, 90, 30]

print(max(numbers))


# ============================================================
# 8. MIN() - Find the smallest number
# ============================================================

print("\n--- min() ---")

print(min(10, 20, 30, 5))

numbers = [10, 50, 20, 90, 30]

print(min(numbers))


# ============================================================
# 9. SUM() - Add numbers together
# ============================================================

print("\n--- sum() ---")

numbers = [10, 20, 30, 40]

print(sum(numbers))       # 100


# ============================================================
# 10. DIVMOD() - Division + remainder together
# ============================================================

print("\n--- divmod() ---")

result = divmod(17, 5)

print(result)

# Output:
# (3, 2)
#
# 3 -> quotient
# 2 -> remainder
#
# 17 / 5 = 3 remainder 2


# ============================================================
# 11. // - FLOOR DIVISION
# ============================================================

print("\n--- Floor Division (//) ---")

print(17 // 5)            # 3
print(20 // 4)            # 5

# // gives the quotient without the decimal part.


# ============================================================
# 12. % - MODULUS / REMAINDER
# ============================================================

print("\n--- Modulus (%) ---")

print(17 % 5)             # 2
print(20 % 4)             # 0

# % gives the remainder.

# Very useful for checking even/odd numbers.

number = 10

print(number % 2)         # 0 -> Even


# ============================================================
# 13. BASIC ARITHMETIC OPERATORS
# ============================================================

print("\n--- Arithmetic Operators ---")

a = 20
b = 6

print(a + b)              # Addition
print(a - b)              # Subtraction
print(a * b)              # Multiplication
print(a / b)              # Division
print(a // b)             # Floor division
print(a % b)              # Remainder
print(a ** b)             # Power


# ============================================================
# 14. COMPARISON OPERATORS
# ============================================================

print("\n--- Comparison Operators ---")

a = 10
b = 20

print(a == b)             # Equal to
print(a != b)             # Not equal to
print(a > b)              # Greater than
print(a < b)              # Less than
print(a >= b)             # Greater than or equal
print(a <= b)             # Less than or equal

# These return True or False.


# ============================================================
# 15. AUGMENTED ASSIGNMENT OPERATORS
# ============================================================

print("\n--- Assignment Operators ---")

x = 10

x += 5                    # x = x + 5
print(x)                  # 15

x -= 3                    # x = x - 3
print(x)                  # 12

x *= 2                    # x = x * 2
print(x)                  # 24

x /= 4                    # x = x / 4
print(x)                  # 6.0


# ============================================================
# 16. MATH MODULE
# ============================================================

# Python's math module provides many additional
# mathematical functions.

import math


# ============================================================
# 17. math.sqrt() - Square root
# ============================================================

print("\n--- math.sqrt() ---")

print(math.sqrt(25))      # 5.0
print(math.sqrt(100))     # 10.0


# ============================================================
# 18. math.ceil() - Round UP
# ============================================================

print("\n--- math.ceil() ---")

print(math.ceil(10.1))    # 11
print(math.ceil(10.9))    # 11


# ============================================================
# 19. math.floor() - Round DOWN
# ============================================================

print("\n--- math.floor() ---")

print(math.floor(10.1))   # 10
print(math.floor(10.9))   # 10


# ============================================================
# 20. math.factorial() - Factorial
# ============================================================

print("\n--- math.factorial() ---")

print(math.factorial(5))

# 5! = 5 × 4 × 3 × 2 × 1
# Result = 120


# ============================================================
# 21. math.gcd() - Greatest Common Divisor
# ============================================================

print("\n--- math.gcd() ---")

print(math.gcd(12, 18))

# Factors:
# 12 -> 1, 2, 3, 4, 6, 12
# 18 -> 1, 2, 3, 6, 9, 18
#
# GCD = 6


# ============================================================
# 22. math.lcm() - Least Common Multiple
# ============================================================

print("\n--- math.lcm() ---")

print(math.lcm(4, 6))

# Multiples:
# 4 -> 4, 8, 12, 16...
# 6 -> 6, 12, 18...
#
# LCM = 12


# ============================================================
# 23. math.pow() - Power as a float
# ============================================================

print("\n--- math.pow() ---")

print(math.pow(2, 3))     # 8.0

# Difference:
#
# pow(2, 3)      -> 8
# math.pow(2, 3) -> 8.0


# ============================================================
# 24. math.pi - PI
# ============================================================

print("\n--- math.pi ---")

print(math.pi)

# Useful for mathematical calculations involving circles.


# ============================================================
# 25. math.e - Euler's Number
# ============================================================

print("\n--- math.e ---")

print(math.e)


# ============================================================
# 26. CHECK EVEN / ODD
# ============================================================

print("\n--- Even / Odd ---")

number = 17

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ============================================================
# 27. CHECK POSITIVE / NEGATIVE / ZERO
# ============================================================

print("\n--- Positive / Negative / Zero ---")

number = -10

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# ============================================================
# 28. SWAP TWO NUMBERS
# ============================================================

print("\n--- Swapping Numbers ---")

a = 10
b = 20

# Python allows swapping without a temporary variable.

a, b = b, a

print("a =", a)
print("b =", b)


# ============================================================
# 29. CONVERT NUMBER TO DIFFERENT BASES
# ============================================================

print("\n--- Number Bases ---")

number = 10

print(bin(number))        # Binary
print(oct(number))        # Octal
print(hex(number))        # Hexadecimal

# Output:
# 0b1010
# 0o12
# 0xa


# ============================================================
# 30. CHECK INTEGER / FLOAT
# ============================================================

print("\n--- Integer / Float ---")

x = 10
y = 10.5

print(isinstance(x, int))     # True
print(isinstance(y, int))     # False

print(isinstance(y, float))   # True


# ============================================================
# 31. INTEGER BITWISE OPERATIONS
# ============================================================

print("\n--- Bitwise Operators ---")

a = 5
b = 3

print(a & b)              # Bitwise AND
print(a | b)              # Bitwise OR
print(a ^ b)              # Bitwise XOR
print(~a)                 # Bitwise NOT

print(a << 1)             # Left shift
print(a >> 1)             # Right shift


# ============================================================
#                 QUICK REFERENCE
# ============================================================

"""
IMPORTANT NUMBER FUNCTIONS:

type()          -> Find the data type
int()           -> Convert to integer
float()         -> Convert to float

abs()           -> Absolute value
pow()           -> Power
round()         -> Round a number

max()           -> Largest number
min()           -> Smallest number
sum()           -> Add numbers
divmod()        -> Quotient + remainder

IMPORTANT OPERATORS:

+               -> Addition
-               -> Subtraction
*               -> Multiplication
/               -> Division
//              -> Floor division
%               -> Remainder
**              -> Power

COMPARISON:

==              -> Equal
!=              -> Not equal
>               -> Greater than
<               -> Less than
>=              -> Greater/equal
<=              -> Less/equal

MATH MODULE:

math.sqrt()     -> Square root
math.ceil()     -> Round up
math.floor()    -> Round down
math.factorial() -> Factorial
math.gcd()      -> GCD
math.lcm()      -> LCM
math.pow()      -> Power
math.pi         -> π
math.e          -> Euler's number

NUMBER BASES:

bin()           -> Binary
oct()           -> Octal
hex()           -> Hexadecimal

CHECKING:

isinstance()    -> Check data type
% 2             -> Check even/odd

BITWISE:

&               -> AND
|               -> OR
^               -> XOR
~               -> NOT
<<              -> Left shift
>>              -> Right shift
"""