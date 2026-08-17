# ============================================
# INTERMEDIATE PYTHON - LAMBDA   UNCTIONS
# ============================================


# ============================================
# 1. Basic lambda
# ============================================

square = lambda x: x ** 2

print(square(5))


# ============================================
# 2. Multiple arguments
# ============================================

add = lambda a, b: a + b

print("\nAdd:", add(10, 20))


# ============================================
# 3. Multiple operations
# ============================================

calculate = lambda a, b: (a + b) * 2

print("Calculate:", calculate(5, 10))


# ============================================
# 4. Lambda with condition
# ============================================

check_even = lambda x: "Even" if x % 2 == 0 else "Odd"

print("\n10:", check_even(10))
print("7:", check_even(7))


# ============================================
# 5. Lambda with sorted()
# ============================================

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95)
]

students_sorted = sorted(
    students,
    key=lambda student: student[1]
)

print("\nSorted by marks:")
print(students_sorted)


# Descending

students_sorted = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("Descending:")
print(students_sorted)


# ============================================
# 6. Sorting strings by length
# ============================================

words = [
    "Python",
    "AI",
    "Programming",
    "API",
    "Docker"
]

sorted_words = sorted(
    words,
    key=lambda word: len(word)
)

print("\nSorted by length:")
print(sorted_words)


# ============================================
# 7. max() and min() with lambda
# ============================================

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

best_student = max(
    students,
    key=lambda student: student[1]
)

worst_student = min(
    students,
    key=lambda student: student[1]
)

print("\nBest:", best_student)
print("Worst:", worst_student)


# ============================================
# 8. map()
# ============================================

numbers = [1, 2, 3, 4, 5]

squares = map(
    lambda x: x ** 2,
    numbers
)

print("\nSquares:")
print(list(squares))


# ============================================
# 9. filter()
# ============================================

numbers = range(1, 11)

even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers
)

print("\nEven numbers:")
print(list(even_numbers))


# ============================================
# 10. map() + lambda
# ============================================

names = ["alice", "bob", "charlie"]

uppercase = map(
    lambda name: name.upper(),
    names
)

print("\nUppercase:")
print(list(uppercase))


# ============================================
# 11. filter() + lambda
# ============================================

words = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "Go"
]

long_words = filter(
    lambda word: len(word) > 3,
    words
)

print("\nLong words:")
print(list(long_words))


# ============================================
# 12. map() with multiple iterables
# ============================================

numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

sums = map(
    lambda x, y: x + y,
    numbers1,
    numbers2
)

print("\nSums:")
print(list(sums))


# ============================================
# 13. reduce()
# ============================================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda x, y: x + y,
    numbers
)

print("\nTotal:", total)


# Multiplication

product = reduce(
    lambda x, y: x * y,
    numbers
)

print("Product:", product)


# ============================================
# 14. Lambda returning a lambda
# ============================================

multiply_by = lambda x: lambda y: x * y

double = multiply_by(2)
triple = multiply_by(3)

print("\nDouble:", double(10))
print("Triple:", triple(10))


# ============================================
# 15. Lambda with dictionary
# ============================================

products = [
    {"name": "Laptop", "price": 80000},
    {"name": "Mouse", "price": 2000},
    {"name": "Keyboard", "price": 5000}
]

products.sort(
    key=lambda product: product["price"]
)

print("\nProducts sorted by price:")

for product in products:
    print(product)


# ============================================
# 16. Practical example
# ============================================

employees = [
    {"name": "Alice", "salary": 70000},
    {"name": "Bob", "salary": 90000},
    {"name": "Charlie", "salary": 60000}
]

highest_paid = max(
    employees,
    key=lambda employee: employee["salary"]
)

print("\nHighest paid:")
print(highest_paid)