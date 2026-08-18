# ============================================================
#             READING AND WRITING FILES IN PYTHON
# ============================================================

# open() is used to open a file.
#
# Common modes:
#
# "r" -> Read
# "w" -> Write (overwrites existing content)
# "a" -> Append
# "x" -> Create a new file
#
# Always prefer "with open()" because it automatically
# closes the file.


# ============================================================
# 1. Writing to a file
# ============================================================

with open("data.txt", "w") as file:
    file.write("Hello Python!\n")
    file.write("Learning file handling.")


# ============================================================
# 2. Reading the entire file
# ============================================================

with open("data.txt", "r") as file:
    content = file.read()

print(content)


# ============================================================
# 3. Reading line by line
# ============================================================

with open("data.txt", "r") as file:

    for line in file:
        print(line.strip())


# ============================================================
# 4. readlines() - Read all lines into a list
# ============================================================

with open("data.txt", "r") as file:
    lines = file.readlines()

print(lines)


# ============================================================
# 5. Appending to a file
# ============================================================

with open("data.txt", "a") as file:
    file.write("\nThis line was added later.")


# ============================================================
# 6. Writing multiple lines
# ============================================================

lines = [
    "Python\n",
    "C++\n",
    "Java\n"
]

with open("languages.txt", "w") as file:
    file.writelines(lines)


# ============================================================
# 7. Checking if a file exists
# ============================================================

import os

if os.path.exists("data.txt"):
    print("File exists.")
else:
    print("File does not exist.")


# ============================================================
# 8. Reading with exception handling
# ============================================================

try:
    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")


# ============================================================
#                 QUICK REFERENCE
# ============================================================

"""
OPEN:

with open("file.txt", "r") as file:
    ...


MODES:

"r" -> Read
"w" -> Write / overwrite
"a" -> Append
"x" -> Create new file


READ:

file.read()
    -> Read entire file

file.readline()
    -> Read one line

file.readlines()
    -> Read all lines as a list


WRITE:

file.write("Hello")
    -> Write a string

file.writelines(lines)
    -> Write multiple strings


IMPORTANT:

with open(...) as file:
    ...

Automatically closes the file.
"""