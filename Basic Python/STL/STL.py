# ============================================================
#              PYTHON STL / DSA TOOLKIT
# ============================================================

# Python equivalents of common C++ STL containers:
#
# C++ STL              Python
# ------------------------------------------------
# vector                list
# pair                  tuple
# set                   set
# unordered_set         set
# map                   dict
# unordered_map         dict
# stack                 list
# queue                 collections.deque
# priority_queue        heapq
# multiset              list + bisect
#
# Python also provides useful modules:
# collections, heapq, bisect


# ============================================================
# 1. LIST - Similar to C++ vector
# ============================================================

print("--- LIST ---")

numbers = [10, 20, 30]

numbers.append(40)       # Add at the end
numbers.insert(1, 15)    # Insert at index 1
numbers.pop()            # Remove last element
numbers.remove(20)       # Remove value 20

print(numbers)

print(len(numbers))      # Size
print(numbers[0])        # Access element

numbers.sort()           # Sort ascending
numbers.reverse()        # Reverse

print(numbers)


# ============================================================
# 2. LIST SLICING
# ============================================================

print("\n--- LIST SLICING ---")

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])      # [20, 30, 40]
print(numbers[:3])       # First 3 elements
print(numbers[2:])       # From index 2
print(numbers[::-1])     # Reverse


# ============================================================
# 3. SET - Unique elements
# ============================================================

print("\n--- SET ---")

numbers = {10, 20, 20, 30, 30}

print(numbers)           # Duplicates automatically removed

numbers.add(40)
numbers.remove(20)

print(numbers)

print(30 in numbers)     # Check existence


# Useful set operations

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)             # Union
print(a & b)             # Intersection
print(a - b)             # Difference


# ============================================================
# 4. DICTIONARY - Similar to C++ map/unordered_map
# ============================================================

print("\n--- DICTIONARY ---")

student = {
    "name": "Harsh",
    "age": 22
}

print(student["name"])

student["age"] = 23       # Update
student["city"] = "Lucknow"  # Add

print(student)

print("name" in student)  # Check key

# Iterate through dictionary

for key, value in student.items():
    print(key, value)


# ============================================================
# 5. STACK - LIFO
# ============================================================

print("\n--- STACK ---")

stack = []

stack.append(10)          # push
stack.append(20)
stack.append(30)

print(stack)

print(stack.pop())        # pop -> 30
print(stack[-1])          # top -> 20


# ============================================================
# 6. QUEUE - FIFO
# ============================================================

print("\n--- QUEUE ---")

from collections import deque

queue = deque()

queue.append(10)          # Push
queue.append(20)
queue.append(30)

print(queue)

print(queue.popleft())    # Remove from front -> 10
print(queue[0])           # Front


# ============================================================
# 7. DEQUE - Double Ended Queue
# ============================================================

print("\n--- DEQUE ---")

dq = deque([20, 30])

dq.append(40)             # Add right
dq.appendleft(10)         # Add left

dq.pop()                  # Remove right
dq.popleft()              # Remove left

print(dq)


# ============================================================
# 8. PRIORITY QUEUE / MIN HEAP
# ============================================================

print("\n--- MIN HEAP ---")

import heapq

heap = []

heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap)

print(heapq.heappop(heap))    # Smallest -> 10
print(heap[0])                # Smallest element


# ============================================================
# 9. MAX HEAP
# ============================================================

print("\n--- MAX HEAP ---")

heap = []

heapq.heappush(heap, -30)
heapq.heappush(heap, -10)
heapq.heappush(heap, -20)

# Python's heapq is a MIN heap.
# Store negative values to simulate a MAX heap.

print(-heapq.heappop(heap))   # 30
print(-heap[0])               # 20


# ============================================================
# 10. SORTING
# ============================================================

print("\n--- SORTING ---")

numbers = [5, 2, 8, 1, 3]

print(sorted(numbers))        # Returns a new sorted list

numbers.sort()                # Sorts original list

print(numbers)

# Descending order

print(sorted(numbers, reverse=True))


# ============================================================
# 11. CUSTOM SORTING
# ============================================================

print("\n--- CUSTOM SORTING ---")

students = [
    ("Harsh", 90),
    ("Rahul", 75),
    ("Aman", 85)
]

# Sort according to marks

students.sort(key=lambda x: x[1])

print(students)


# ============================================================
# 12. BINARY SEARCH - bisect
# ============================================================

print("\n--- BINARY SEARCH ---")

from bisect import bisect_left, bisect_right

numbers = [10, 20, 30, 30, 40, 50]

# Find first position where 30 can be inserted

print(bisect_left(numbers, 30))

# Find position after all 30s

print(bisect_right(numbers, 30))


# ============================================================
# 13. COUNTER - Frequency Counting
# ============================================================

print("\n--- COUNTER ---")

from collections import Counter

numbers = [1, 2, 2, 3, 3, 3]

frequency = Counter(numbers)

print(frequency)

print(frequency[3])       # Frequency of 3


# ============================================================
# 14. DEFAULTDICT
# ============================================================

print("\n--- DEFAULTDICT ---")

from collections import defaultdict

graph = defaultdict(list)

graph[1].append(2)
graph[1].append(3)
graph[2].append(4)

print(graph)


# This is very useful for graphs.

# graph[1] -> [2, 3]
# graph[2] -> [4]


# ============================================================
# 15. ENUMERATE - Index + Value
# ============================================================

print("\n--- ENUMERATE ---")

numbers = [10, 20, 30]

for index, value in enumerate(numbers):
    print(index, value)


# ============================================================
# 16. ZIP - Combine multiple sequences
# ============================================================

print("\n--- ZIP ---")

names = ["Harsh", "Aman", "Rahul"]
marks = [90, 80, 85]

for name, mark in zip(names, marks):
    print(name, mark)


# ============================================================
# 17. ANY() AND ALL()
# ============================================================

print("\n--- any() / all() ---")

numbers = [2, 4, 6, 8]

print(all(x % 2 == 0 for x in numbers))
# True -> all numbers are even

print(any(x > 5 for x in numbers))
# True -> at least one number is greater than 5


# ============================================================
# 18. REVERSE ITERATION
# ============================================================

print("\n--- reversed() ---")

numbers = [1, 2, 3, 4]

for x in reversed(numbers):
    print(x)


# ============================================================
#                 QUICK REFERENCE
# ============================================================

"""
C++ STL              PYTHON
------------------------------------------

vector                list

pair                  tuple

set                   set

map                   dict

unordered_map         dict

stack                 list

queue                 deque

deque                 deque

priority_queue        heapq

sort()                list.sort()
                      sorted()

lower_bound()         bisect_left()

upper_bound()         bisect_right()

frequency map         Counter

graph                 defaultdict(list)


IMPORTANT LIST FUNCTIONS:

append(x)             -> Add at end
insert(i, x)          -> Insert at index
pop()                 -> Remove last
pop(i)                -> Remove index
remove(x)             -> Remove value
sort()                -> Sort
reverse()             -> Reverse
len(list)             -> Size
x in list             -> Search


IMPORTANT SET:

add(x)                -> Insert
remove(x)             -> Delete
x in set              -> Search
|                     -> Union
&                     -> Intersection
-                     -> Difference


IMPORTANT DICT:

dict[key]             -> Access
dict[key] = value     -> Insert/update
del dict[key]         -> Delete
key in dict           -> Search
keys()                -> All keys
values()              -> All values
items()                -> Key + value


IMPORTANT HEAP:

heapq.heappush()      -> Push
heapq.heappop()       -> Pop minimum
heap[0]               -> Minimum


IMPORTANT COLLECTIONS:

deque                 -> Queue / Deque
Counter               -> Frequency counting
defaultdict           -> Convenient dictionaries
"""