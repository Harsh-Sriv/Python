# ============================================
# INTERMEDIATE PYTHON - COLLECTIONS
# ============================================

from collections import (
    Counter,
    defaultdict,
    deque,
    namedtuple,
    ChainMap
)


# ============================================
# 1. Counter
# ============================================

print("--- Counter ---")

words = [
    "python",
    "java",
    "python",
    "cpp",
    "java",
    "python"
]

counter = Counter(words)

print(counter)


# Most common elements

print("Most common:")
print(counter.most_common())

print(counter.most_common(2))


# Access individual count

print("Python:", counter["python"])
print("Java:", counter["java"])


# Missing values return 0

print("Go:", counter["go"])


# Update counter

counter.update(["python", "go", "go"])

print("Updated:", counter)


# Subtract

counter.subtract(["python", "java"])

print("After subtract:", counter)


# ============================================
# 2. Counter with characters
# ============================================

text = "banana"

char_count = Counter(text)

print("\nCharacter count:")
print(char_count)


# ============================================
# 3. Counter arithmetic
# ============================================

a = Counter({"Python": 3, "Java": 2})
b = Counter({"Python": 1, "Java": 4})

print("\nCounter addition:")
print(a + b)

print("\nCounter subtraction:")
print(a - b)

print("\nIntersection:")
print(a & b)

print("\nUnion:")
print(a | b)


# ============================================
# 4. defaultdict
# ============================================

print("\n--- defaultdict ---")

groups = defaultdict(list)

groups["Python"].append("Alice")
groups["Python"].append("Bob")
groups["Java"].append("Charlie")

print(groups)


# Normal dictionary would require:

# if "Python" not in groups:
#     groups["Python"] = []

# defaultdict handles this automatically.


# ============================================
# 5. defaultdict with int
# ============================================

frequency = defaultdict(int)

words = ["python", "java", "python", "cpp", "python"]

for word in words:
    frequency[word] += 1

print("\nFrequency:")
print(dict(frequency))


# ============================================
# 6. defaultdict for grouping
# ============================================

students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("David", "B"),
    ("Eve", "A")
]

groups = defaultdict(list)

for name, grade in students:
    groups[grade].append(name)

print("\nStudents by grade:")
print(dict(groups))


# ============================================
# 7. deque
# ============================================

print("\n--- deque ---")

queue = deque(["Alice", "Bob", "Charlie"])

print(queue)


# Add to right

queue.append("David")

print("After append:", queue)


# Add to left

queue.appendleft("Zack")

print("After appendleft:", queue)


# Remove from right

print("Removed:", queue.pop())

# Remove from left

print("Removed:", queue.popleft())

print("Queue:", queue)


# ============================================
# 8. deque as a queue
# ============================================

queue = deque()

queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")

print("\nQueue:", queue)

while queue:
    task = queue.popleft()
    print("Processing:", task)


# ============================================
# 9. deque as a stack
# ============================================

stack = deque()

stack.append("Page 1")
stack.append("Page 2")
stack.append("Page 3")

print("\nStack:", stack)

while stack:
    page = stack.pop()
    print("Going back to:", page)


# ============================================
# 10. maxlen
# ============================================

recent = deque(maxlen=3)

recent.append(1)
recent.append(2)
recent.append(3)

print("\nRecent:", recent)

recent.append(4)

print("After adding 4:", recent)

# 1 automatically disappears


# ============================================
# 11. rotate()
# ============================================

numbers = deque([1, 2, 3, 4, 5])

numbers.rotate(2)

print("\nRotated right:", numbers)

numbers.rotate(-2)

print("Rotated left:", numbers)


# ============================================
# 12. namedtuple
# ============================================

print("\n--- namedtuple ---")

Person = namedtuple(
    "Person",
    ["name", "age", "profession"]
)

person = Person(
    "Alice",
    25,
    "Developer"
)

print(person)

print(person.name)
print(person.age)
print(person.profession)


# Can still access using indexes

print(person[0])


# ============================================
# 13. _asdict()
# ============================================

print("\nAs dictionary:")

print(person._asdict())


# ============================================
# 14. ChainMap
# ============================================

print("\n--- ChainMap ---")

default_config = {
    "theme": "dark",
    "language": "English",
    "timeout": 30
}

user_config = {
    "theme": "light",
    "timeout": 60
}

config = ChainMap(user_config, default_config)

print("Theme:", config["theme"])
print("Language:", config["language"])
print("Timeout:", config["timeout"])


# User config takes priority.


# ============================================
# 15. Practical example
# ============================================

print("\n--- Practical Example ---")

logs = [
    ("INFO", "Server started"),
    ("ERROR", "Database failed"),
    ("INFO", "User logged in"),
    ("WARNING", "High memory"),
    ("ERROR", "Connection failed"),
    ("INFO", "User logged out"),
]

log_counts = Counter(level for level, message in logs)

print("Log counts:")
print(log_counts)


messages_by_level = defaultdict(list)

for level, message in logs:
    messages_by_level[level].append(message)

print("\nMessages by level:")
print(dict(messages_by_level))