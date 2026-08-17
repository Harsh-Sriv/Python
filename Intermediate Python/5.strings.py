# ============================================
# INTERMEDIATE PYTHON - STRINGS
# ============================================


# ============================================
# 1. Creating strings
# ============================================

name = "Python"
language = 'Python'
message = """This is
a multi-line
string."""

print(name)
print(language)
print(message)


# ============================================
# 2. Indexing
# ============================================

text = "Python"

print("\n--- Indexing ---")

print(text[0])
print(text[1])
print(text[-1])
print(text[-2])


# ============================================
# 3. Slicing
# ============================================

print("\n--- Slicing ---")

print(text[0:3])
print(text[:3])
print(text[3:])
print(text[:])
print(text[::2])
print(text[::-1])


# ============================================
# 4. Strings are immutable
# ============================================

# This is NOT allowed:

# text[0] = "J"

# Instead create a new string:

text = "J" + text[1:]

print("\nNew string:", text)


# ============================================
# 5. String length
# ============================================

text = "Python"

print("\nLength:", len(text))


# ============================================
# 6. Searching
# ============================================

text = "Python is a powerful language"

print("\n--- Searching ---")

print("Python" in text)
print("Java" in text)

print(text.find("powerful"))
print(text.find("Java"))

print(text.index("Python"))

# index() raises ValueError if not found
# find() returns -1 if not found


# ============================================
# 7. startswith() / endswith()
# ============================================

url = "https://example.com"

print("\n--- Prefix/Suffix ---")

print(url.startswith("https"))
print(url.endswith(".com"))


# ============================================
# 8. Changing case
# ============================================

text = "Python Programming"

print("\n--- Case ---")

print(text.lower())
print(text.upper())
print(text.title())
print(text.capitalize())
print(text.swapcase())


# ============================================
# 9. Removing whitespace
# ============================================

text = "   Python Programming   "

print("\n--- Whitespace ---")

print(text.strip())
print(text.lstrip())
print(text.rstrip())


# ============================================
# 10. Replacing text
# ============================================

text = "I like Java"

new_text = text.replace("Java", "Python")

print("\nReplaced:", new_text)


# ============================================
# 11. Splitting
# ============================================

text = "Python,Java,C++,Go"

languages = text.split(",")

print("\nSplit:")
print(languages)


# ============================================
# 12. Joining
# ============================================

languages = ["Python", "Java", "C++"]

result = ", ".join(languages)

print("\nJoined:")
print(result)


# ============================================
# 13. splitlines()
# ============================================

text = """Python
Java
C++
Go"""

print("\nLines:")
print(text.splitlines())


# ============================================
# 14. String checks
# ============================================

print("\n--- String Checks ---")

print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())
print("hello".islower())
print("HELLO".isupper())
print("   ".isspace())


# ============================================
# 15. Counting occurrences
# ============================================

text = "banana"

print("\nCount of a:", text.count("a"))
print("Count of an:", text.count("an"))


# ============================================
# 16. String formatting
# ============================================

name = "Alice"
age = 25

# f-string

message = f"My name is {name} and I am {age} years old."

print("\n" + message)


# Expressions inside f-strings

x = 10
y = 20

print(f"{x} + {y} = {x + y}")


# ============================================
# 17. Formatting numbers
# ============================================

price = 1234.56789

print(f"\nPrice: {price:.2f}")

percentage = 0.8567

print(f"Percentage: {percentage:.2%}")


# ============================================
# 18. Alignment
# ============================================

name = "Python"

print(f"\n|{name:<10}|")
print(f"|{name:>10}|")
print(f"|{name:^10}|")


# ============================================
# 19. Escape characters
# ============================================

print("\n--- Escape Characters ---")

print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Hello\"")


# ============================================
# 20. Raw strings
# ============================================

path = r"C:\Users\Alice\Documents"

print("\nRaw string:")
print(path)


# ============================================
# 21. String concatenation
# ============================================

first = "Hello"
second = "World"

result = first + " " + second

print("\n" + result)


# ============================================
# 22. String repetition
# ============================================

print("Python " * 3)


# ============================================
# 23. Iterating through a string
# ============================================

text = "Python"

print("\n--- Iteration ---")

for character in text:
    print(character)


# ============================================
# 24. enumerate()
# ============================================

for index, character in enumerate(text):
    print(index, character)


# ============================================
# 25. Reverse a string
# ============================================

text = "Python"

reversed_text = text[::-1]

print("\nReversed:", reversed_text)


# ============================================
# 26. Character frequency
# ============================================

text = "banana"

frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

print("\nCharacter frequency:")
print(frequency)


# ============================================
# 27. String comprehension
# ============================================

text = "Python"

uppercase = "".join(
    character.upper()
    for character in text
)

print("\nUppercase:", uppercase)


# ============================================
# 28. Removing punctuation
# ============================================

import string

text = "Hello, Python! How are you?"

cleaned = text.translate(
    str.maketrans("", "", string.punctuation)
)

print("\nWithout punctuation:")
print(cleaned)


# ============================================
# 29. Partition
# ============================================

email = "alice@example.com"

username, separator, domain = email.partition("@")

print("\nUsername:", username)
print("Separator:", separator)
print("Domain:", domain)


# ============================================
# 30. Practical example
# ============================================

sentence = "  Python is AMAZING and Python is powerful.  "

sentence = sentence.strip()

words = sentence.lower().split()

print("\nWords:")
print(words)

python_count = words.count("python")

print("Python appears:", python_count, "times")