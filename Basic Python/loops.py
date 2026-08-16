# ============================================================
#                     LOOPS IN PYTHON
# ============================================================

# Loops are used to execute a block of code repeatedly.


# ============================================================
# 1. for loop
# ============================================================

print("--- for loop ---")

for i in range(5):
    print(i)

# range(5) generates:
# 0, 1, 2, 3, 4


# ============================================================
# 2. range(start, stop)
# ============================================================

print("\n--- range(start, stop) ---")

for i in range(1, 6):
    print(i)

# Output: 1 2 3 4 5
# stop value (6) is NOT included.


# ============================================================
# 3. range(start, stop, step)
# ============================================================

print("\n--- range(start, stop, step) ---")

for i in range(0, 10, 2):
    print(i)

# Output: 0 2 4 6 8


# ============================================================
# 4. Reverse loop
# ============================================================

print("\n--- Reverse loop ---")

for i in range(5, 0, -1):
    print(i)

# Output: 5 4 3 2 1


# ============================================================
# 5. Loop through a list
# ============================================================

print("\n--- List loop ---")

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)


# ============================================================
# 6. Loop through a string
# ============================================================

print("\n--- String loop ---")

word = "Python"

for character in word:
    print(character)


# ============================================================
# 7. while loop
# ============================================================

print("\n--- while loop ---")

i = 1

while i <= 5:
    print(i)
    i += 1

# while continues as long as the condition is True.


# ============================================================
# 8. break
# ============================================================

print("\n--- break ---")

for i in range(1, 10):

    if i == 5:
        break              # Immediately stops the loop

    print(i)

# Output:
# 1
# 2
# 3
# 4


# ============================================================
# 9. continue
# ============================================================

print("\n--- continue ---")

for i in range(1, 6):

    if i == 3:
        continue           # Skip this iteration

    print(i)

# Output:
# 1
# 2
# 4
# 5


# ============================================================
# 10. Nested loops
# ============================================================

print("\n--- Nested loops ---")

for i in range(3):

    for j in range(3):
        print(i, j)

# A loop inside another loop.


# ============================================================
# 11. enumerate()
# ============================================================

print("\n--- enumerate() ---")

numbers = [10, 20, 30]

for index, value in enumerate(numbers):
    print(index, value)

# Gives both index and value.


# ============================================================
# 12. Loop with else
# ============================================================

print("\n--- loop else ---")

for i in range(5):

    if i == 10:
        break

else:
    print("Loop completed without break.")

# The else executes when the loop finishes normally.
# It does NOT execute if break is used.


# ============================================================
# 13. Practical example - Find an element
# ============================================================

print("\n--- Search ---")

numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:

    if number == target:
        print("Found!")
        break


# ============================================================
# 14. Practical example - Sum of numbers
# ============================================================

print("\n--- Sum ---")

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print("Sum:", total)


# ============================================================
#                 QUICK REFERENCE
# ============================================================

"""
FOR LOOP:

for i in range(5):
    print(i)


RANGE:

range(stop)
range(start, stop)
range(start, stop, step)


WHILE:

while condition:
    code


BREAK:

break
-> Immediately exits the loop.


CONTINUE:

continue
-> Skips current iteration.


NESTED LOOP:

for i in ...:
    for j in ...:
        ...


USEFUL:

enumerate(list)
-> Gives index + value


LOOP ELSE:

for x in numbers:
    if condition:
        break
else:
    print("Not found")
"""