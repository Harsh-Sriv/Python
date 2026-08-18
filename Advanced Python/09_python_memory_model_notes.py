# ============================================================
# INTERMEDIATE PYTHON — MEMORY / OBJECT MODEL
# Standalone notes + runnable quick revision reference
# ============================================================
# Variables are NAMES that refer to OBJECTS. They do not normally store
# values directly. Multiple names can refer to the same object in memory.

import gc
import sys


# ============================================================
# 1. References and identity
# ============================================================

first = [1, 2, 3]
second = first  # No copy: both names refer to the SAME list object.

print("1. References and identity")
print("first is second:", first is second)
print("Same id:", id(first) == id(second))
second.append(4)
print("first changed too:", first)


# ============================================================
# 2. Identity (`is`) versus equality (`==`)
# ============================================================
# == asks: "Do these objects have equal values?"
# is asks: "Are these names pointing to the exact same object?"

third = [1, 2, 3, 4]  # Equal content, but a separate list object.

print("\n2. is versus ==")
print("first == third:", first == third)
print("first is third:", first is third)

# Use `is None`, not `== None`, when checking for no value.
result = None
print("result is None:", result is None)


# ============================================================
# 3. Mutability: object can change after creation
# ============================================================
# Mutable built-in types include list, dict, and set.
# Immutable built-in types include int, float, bool, str, tuple, and frozenset.

print("\n3. Mutable object")
items = ["pen", "book"]
same_items = items
items.append("laptop")  # Changes the existing list object in place.
print("Both names see mutation:", same_items)

print("\n3. Immutable object")
score = 10
same_score = score
score += 5  # Integers cannot change; this binds score to a NEW int object.
print("score:", score)
print("same_score:", same_score)


# ============================================================
# 4. Function arguments are object references
# ============================================================
# Python uses "call by object reference" (also called call by sharing).
# A function can mutate a mutable argument, but rebinding its local parameter
# does not change which object the caller's variable refers to.


def add_item(values: list[str]) -> None:
    values.append("added inside function")  # Mutates caller's list.


def reassign_values(values: list[str]) -> None:
    values = ["new local list"]  # Only rebinds this local parameter.
    print("Inside function:", values)


shopping_list = ["milk"]
add_item(shopping_list)
print("\n4. Function arguments")
print("After mutation:", shopping_list)
reassign_values(shopping_list)
print("After local reassignment:", shopping_list)


# ============================================================
# 5. Copying: shallow versus deep
# ============================================================
# A shallow copy makes a new OUTER container but still shares nested objects.
# A deep copy recursively copies nested objects too.

original = [["a"], ["b"]]
shallow_copy = original.copy()

shallow_copy[0].append("changed")
print("\n5. Shallow copy")
print("Original changed through shared inner list:", original)

import copy

deep_copy = copy.deepcopy(original)
deep_copy[1].append("only in deep copy")
print("\n5. Deep copy")
print("Original:", original)
print("Deep copy:", deep_copy)


# ============================================================
# 6. Garbage collection and reference counting
# ============================================================
# CPython mainly frees an object when no references point to it. It also has
# a garbage collector that can clean up reference cycles.
# sys.getrefcount() is CPython-specific and includes a temporary reference
# created by the function call, so its exact number is not important.

temporary = {"status": "active"}
print("\n6. Garbage collection")
print("Approximate reference count:", sys.getrefcount(temporary))

# A reference cycle: each object refers to the other. Modern Python's cycle
# collector can detect and reclaim such unreachable cycles.
cycle_a = []
cycle_b = []
cycle_a.append(cycle_b)
cycle_b.append(cycle_a)
del cycle_a
del cycle_b  # Neither name remains; the collector can clean the cycle.
print("Unreachable objects collected:", gc.collect())


# ============================================================
# QUICK REVIEW
# ============================================================
# variable/name          -> reference to an object
# id(obj)                -> identity of an object during its lifetime
# a is b                 -> same exact object?
# a == b                 -> equal values?
# mutable                -> object can change in place (list, dict, set)
# immutable              -> change creates/binds a new object (int, str, tuple)
# assignment b = a       -> another reference, NOT a copy
# shallow copy           -> copies outer object, shares nested objects
# deep copy              -> recursively copies nested objects
# reference counting     -> CPython frees when references reach zero
# garbage collector      -> also finds unreachable reference cycles
