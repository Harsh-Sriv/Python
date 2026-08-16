# ============================================================
#                  PYTHON STRINGS
# ============================================================

# A string is a sequence of characters enclosed in:
# 'single quotes', "double quotes", or '''triple quotes'''

name = "Harsh"
message = "Hello, Welcome to Python!"

print("Original String:", message)


# ============================================================
# 1. LEN() - Find the length of a string
# ============================================================

print("\n--- len() ---")

# len() returns the number of characters in a string.
# Spaces are also counted.

print(len(message))


# ============================================================
# 2. INDEXING - Access individual characters
# ============================================================

print("\n--- Indexing ---")

# Python uses zero-based indexing.
# H -> index 0
# e -> index 1
# l -> index 2
# l -> index 3
# o -> index 4

print(message[0])      # First character
print(message[1])      # Second character
print(message[-1])     # Last character
print(message[-2])     # Second-last character


# ============================================================
# 3. SLICING - Extract part of a string
# ============================================================

print("\n--- Slicing ---")

text = "Python Programming"

print(text[0:6])       # Characters from index 0 to 5
print(text[7:18])      # Characters from index 7 to 17
print(text[:6])        # Beginning to index 5
print(text[7:])        # Index 7 to the end
print(text[:])         # Entire string
print(text[::2])       # Every second character
print(text[::-1])      # Reverse the string


# ============================================================
# 4. LOWER() - Convert to lowercase
# ============================================================

print("\n--- lower() ---")

text = "HELLO PYTHON"

print(text.lower())


# ============================================================
# 5. UPPER() - Convert to uppercase
# ============================================================

print("\n--- upper() ---")

text = "hello python"

print(text.upper())


# ============================================================
# 6. TITLE() - Capitalize Every Word
# ============================================================

print("\n--- title() ---")

text = "python programming language"

print(text.title())


# ============================================================
# 7. CAPITALIZE() - Capitalize First Character
# ============================================================

print("\n--- capitalize() ---")

text = "python is easy"

print(text.capitalize())


# ============================================================
# 8. SWAPCASE() - Swap uppercase and lowercase
# ============================================================

print("\n--- swapcase() ---")

text = "Hello Python"

print(text.swapcase())


# ============================================================
# 9. STRIP() - Remove spaces from beginning and end
# ============================================================

print("\n--- strip() ---")

text = "    Hello Python    "

print(text.strip())


# ============================================================
# 10. LSTRIP() - Remove spaces from left side
# ============================================================

print("\n--- lstrip() ---")

text = "    Hello Python    "

print(text.lstrip())


# ============================================================
# 11. RSTRIP() - Remove spaces from right side
# ============================================================

print("\n--- rstrip() ---")

text = "    Hello Python    "

print(text.rstrip())


# ============================================================
# 12. REPLACE() - Replace part of a string
# ============================================================

print("\n--- replace() ---")

text = "I love Java"

# Replace "Java" with "Python"

print(text.replace("Java", "Python"))


# ============================================================
# 13. FIND() - Find position of a substring
# ============================================================

print("\n--- find() ---")

text = "I love Python"

# find() returns the index where the substring starts.
# If it cannot find the substring, it returns -1.

print(text.find("Python"))
print(text.find("Java"))


# ============================================================
# 14. INDEX() - Find position of a substring
# ============================================================

print("\n--- index() ---")

text = "I love Python"

print(text.index("Python"))

# Difference:
# find()  -> returns -1 if not found
# index() -> raises an error if not found


# ============================================================
# 15. COUNT() - Count occurrences
# ============================================================

print("\n--- count() ---")

text = "banana"

print(text.count("a"))      # Number of 'a'
print(text.count("an"))     # Number of "an"


# ============================================================
# 16. STARTSWITH() - Check beginning
# ============================================================

print("\n--- startswith() ---")

text = "Python Programming"

print(text.startswith("Python"))
print(text.startswith("Java"))


# ============================================================
# 17. ENDSWITH() - Check ending
# ============================================================

print("\n--- endswith() ---")

text = "Python.py"

print(text.endswith(".py"))
print(text.endswith(".cpp"))


# ============================================================
# 18. SPLIT() - Convert string into a list
# ============================================================

print("\n--- split() ---")

text = "Python is very easy"

words = text.split()

print(words)

# You can also specify the separator

data = "apple,banana,mango"

print(data.split(","))


# ============================================================
# 19. JOIN() - Join list elements into a string
# ============================================================

print("\n--- join() ---")

words = ["Python", "is", "awesome"]

# " ".join() means join using a space

sentence = " ".join(words)

print(sentence)

# Join using comma

print(",".join(words))


# ============================================================
# 20. ISALPHA() - Check if all characters are alphabets
# ============================================================

print("\n--- isalpha() ---")

print("Python".isalpha())      # True
print("Python123".isalpha())   # False


# ============================================================
# 21. ISDIGIT() - Check if all characters are digits
# ============================================================

print("\n--- isdigit() ---")

print("12345".isdigit())       # True
print("123abc".isdigit())      # False


# ============================================================
# 22. ISALNUM() - Check alphabets + numbers
# ============================================================

print("\n--- isalnum() ---")

print("Python123".isalnum())   # True
print("Python 123".isalnum())  # False because of space


# ============================================================
# 23. ISSPACE() - Check if string contains only spaces
# ============================================================

print("\n--- isspace() ---")

print("   ".isspace())         # True
print("Hello".isspace())       # False


# ============================================================
# 24. ISLOWER() - Check whether string is lowercase
# ============================================================

print("\n--- islower() ---")

print("hello".islower())       # True
print("Hello".islower())       # False


# ============================================================
# 25. ISUPPER() - Check whether string is uppercase
# ============================================================

print("\n--- isupper() ---")

print("HELLO".isupper())       # True
print("Hello".isupper())       # False


# ============================================================
# 26. F-STRING - Insert variables inside strings
# ============================================================

print("\n--- f-string ---")

name = "Harsh"
age = 22

# f before the string allows us to directly insert variables.

print(f"My name is {name} and I am {age} years old.")


# ============================================================
# 27. STRING CONCATENATION
# ============================================================

print("\n--- Concatenation ---")

first_name = "Harsh"
last_name = "Srivastava"

# + is used to combine strings

full_name = first_name + " " + last_name

print(full_name)


# ============================================================
# 28. STRING REPETITION
# ============================================================

print("\n--- Repetition ---")

# * repeats a string multiple times

print("Python " * 3)


# ============================================================
# 29. MEMBERSHIP - in / not in
# ============================================================

print("\n--- Membership ---")

text = "Python Programming"

print("Python" in text)        # True
print("Java" in text)          # False

print("Java" not in text)      # True


# ============================================================
# 30. ESCAPE CHARACTERS
# ============================================================

print("\n--- Escape Characters ---")

# \n -> New line
# \t -> Tab
# \" -> Double quote
# \' -> Single quote
# \\ -> Backslash

print("Hello\nWorld")

print("Hello\tWorld")

print("He said \"Hello\"")

print('It\'s Python')


# ============================================================
# 31. RAW STRING
# ============================================================

print("\n--- Raw String ---")

# Normally \n means a new line.
# With r before the string, backslashes are treated literally.

path = r"C:\Users\Harsh\Documents"

print(path)


# ============================================================
# 32. FORMAT() - Another way to format strings
# ============================================================

print("\n--- format() ---")

name = "Harsh"
age = 22

print("My name is {} and I am {} years old.".format(name, age))


# ============================================================
# 33. PARTITION() - Split into three parts
# ============================================================

print("\n--- partition() ---")

text = "Python is awesome"

print(text.partition("is"))

# Result:
# ('Python ', 'is', ' awesome')


# ============================================================
# 34. REMOVEPREFIX() - Remove beginning
# ============================================================

print("\n--- removeprefix() ---")

text = "Mr. Harsh"

print(text.removeprefix("Mr. "))


# ============================================================
# 35. REMOVESUFFIX() - Remove ending
# ============================================================

print("\n--- removesuffix() ---")

filename = "program.py"

print(filename.removesuffix(".py"))


# ============================================================
#                 QUICK REFERENCE
# ============================================================

"""
Important Python String Methods:

len()          -> Length of string
lower()        -> Convert to lowercase
upper()        -> Convert to uppercase
title()        -> Capitalize every word
capitalize()   -> Capitalize first character
swapcase()     -> Swap upper/lower case

strip()        -> Remove spaces from both sides
lstrip()       -> Remove spaces from left
rstrip()       -> Remove spaces from right

replace()      -> Replace text
find()         -> Find position
index()        -> Find position (error if not found)
count()        -> Count occurrences

startswith()   -> Check beginning
endswith()     -> Check ending

split()        -> String -> List
join()         -> List -> String

isalpha()      -> Check alphabets
isdigit()      -> Check digits
isalnum()      -> Check alphabets/numbers
isspace()      -> Check spaces
islower()      -> Check lowercase
isupper()      -> Check uppercase

partition()    -> Split into 3 parts
removeprefix() -> Remove prefix
removesuffix() -> Remove suffix

Also remember:

Indexing       -> string[index]
Slicing        -> string[start:end:step]
Concatenation -> string1 + string2
Repetition     -> string * number
Membership     -> value in string
Formatting     -> f"Hello {name}"
"""