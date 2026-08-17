# ============================================
# INTERMEDIATE PYTHON - GENERATORS
# ============================================


# ============================================
# 1. Basic generator
# ============================================

def generate_numbers():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


numbers = generate_numbers()

print("--- Generator ---")

print(numbers)

print(next(numbers))
print(next(numbers))
print(next(numbers))


# ============================================
# 2. Continue iteration
# ============================================

print("\nRemaining values:")

for number in numbers:
    print(number)


# ============================================
# 3. Generator function with loop
# ============================================

def count_up_to(limit):

    number = 1

    while number <= limit:

        yield number

        number += 1


print("\n--- count_up_to ---")

for number in count_up_to(5):
    print(number)


# ============================================
# 4. Generator expression
# ============================================

squares = (
    x ** 2
    for x in range(1, 6)
)

print("\n--- Generator Expression ---")

print(squares)

for square in squares:
    print(square)


# ============================================
# 5. List vs generator
# ============================================

numbers_list = [
    x ** 2
    for x in range(1, 6)
]

numbers_generator = (
    x ** 2
    for x in range(1, 6)
)

print("\nList:")
print(numbers_list)

print("\nGenerator:")
print(numbers_generator)


# ============================================
# 6. Generator with condition
# ============================================

even_numbers = (
    x
    for x in range(1, 11)
    if x % 2 == 0
)

print("\nEven numbers:")

for number in even_numbers:
    print(number)


# ============================================
# 7. Generator using next()
# ============================================

def letters():

    yield "A"
    yield "B"
    yield "C"


generator = letters()

print("\n--- next() ---")

print(next(generator))
print(next(generator))
print(next(generator))

# Calling next() again would raise StopIteration.


# ============================================
# 8. Handling StopIteration
# ============================================

generator = letters()

while True:

    try:
        value = next(generator)
        print(value)

    except StopIteration:
        print("Generator finished.")
        break


# ============================================
# 9. Generator state
# ============================================

def counter():

    number = 0

    while True:

        yield number

        number += 1


generator = counter()

print("\n--- Generator State ---")

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


# ============================================
# 10. Infinite generator
# ============================================

def infinite_numbers():

    number = 1

    while True:

        yield number

        number += 1


generator = infinite_numbers()

print("\n--- Infinite Generator ---")

for _ in range(5):
    print(next(generator))


# ============================================
# 11. Generator for large data
# ============================================

def read_large_data():

    for number in range(1, 1_000_001):

        yield number


print("\n--- Large Generator ---")

generator = read_large_data()

print(next(generator))
print(next(generator))
print(next(generator))


# We don't need to store one million
# numbers in a list.


# ============================================
# 12. Generator pipeline
# ============================================

def numbers(limit):

    for number in range(limit):

        yield number


def squares(generator):

    for number in generator:

        yield number ** 2


def even_only(generator):

    for number in generator:

        if number % 2 == 0:
            yield number


pipeline = even_only(
    squares(
        numbers(10)
    )
)

print("\n--- Generator Pipeline ---")

for value in pipeline:
    print(value)


# ============================================
# 13. Generator with send()
# ============================================

def calculator():

    total = 0

    while True:

        value = yield total

        if value is None:
            return

        total += value


calc = calculator()

print("\n--- send() ---")

print(next(calc))

print(calc.send(10))
print(calc.send(20))
print(calc.send(30))


# ============================================
# 14. yield from
# ============================================

def generate_numbers():

    yield from [1, 2, 3]


def generate_letters():

    yield from ["A", "B", "C"]


def combined():

    yield from generate_numbers()
    yield from generate_letters()


print("\n--- yield from ---")

for value in combined():
    print(value)


# ============================================
# 15. Generator returning a value
# ============================================

def example():

    yield 1
    yield 2

    return "Finished"


generator = example()

print("\n--- Generator return ---")

print(next(generator))
print(next(generator))

try:
    next(generator)

except StopIteration as error:
    print("Return value:", error.value)


# ============================================
# 16. Generator expression with sum()
# ============================================

total = sum(
    x ** 2
    for x in range(1, 1000000)
)

print("\nSum:", total)


# ============================================
# 17. Practical file-processing generator
# ============================================

def read_lines(filename):

    with open(filename, "r") as file:

        for line in file:

            yield line.strip()


# Example usage:
#
# for line in read_lines("large_file.txt"):
#     print(line)


# ============================================
# 18. Practical filtering generator
# ============================================

def positive_numbers(numbers):

    for number in numbers:

        if number > 0:
            yield number


values = [-5, 10, -2, 7, 0, 3]

print("\nPositive numbers:")

for number in positive_numbers(values):
    print(number)