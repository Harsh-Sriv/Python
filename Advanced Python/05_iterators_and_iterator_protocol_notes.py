# ============================================================
# INTERMEDIATE PYTHON — ITERATORS & ITERATOR PROTOCOL
# Standalone notes + runnable quick revision reference
# ============================================================
# Important spellings:
# __iter__()  -> double underscores on both sides
# __next__()  -> double underscores on both sides
#
# ITERABLE: an object you can loop over (list, tuple, string, dict, set).
# ITERATOR: an object that produces one item at a time using next().
#
# for item in iterable is conceptually similar to:
# iterator = iter(iterable)
# while True:
#     try:
#         item = next(iterator)
#     except StopIteration:
#         break


# ============================================================
# 1. Built-in iter() and next()
# ============================================================

numbers = [10, 20, 30]

# A list is iterable, but it is not itself an iterator.
number_iterator = iter(numbers)  # iter() asks numbers for an iterator.

print("1. iter() and next()")
print(next(number_iterator))  # Gets 10, then advances its internal position.
print(next(number_iterator))  # Gets 20.
print(next(number_iterator))  # Gets 30.

# Calling next() again would raise StopIteration because no values remain.
# print(next(number_iterator))


# ============================================================
# 2. A for-loop uses iter() and next() internally
# ============================================================

print("\n2. Manual version of a for-loop")
words = ["Python", "AI", "API"]
word_iterator = iter(words)

while True:
    try:
        word = next(word_iterator)
        print(word)
    except StopIteration:
        # StopIteration is the signal that iteration is complete.
        break


# ============================================================
# 3. Iterable versus iterator
# ============================================================

print("\n3. Iterable versus iterator")
names = ["Asha", "Rahul"]
names_iterator = iter(names)

print("list is its own iterator?", iter(names) is names)  # False
print("iterator is its own iterator?", iter(names_iterator) is names_iterator)  # True

# A list can be looped over repeatedly because iter(list) creates a new
# iterator each time. An iterator is consumed as you call next() on it.
print("First loop:", list(names))
print("Second loop:", list(names))


# ============================================================
# 4. Custom iterator: __iter__() and __next__()
# ============================================================
# To make an object an ITERATOR, it must implement BOTH methods:
# __iter__() returns the iterator object.
# __next__() returns the next value or raises StopIteration.


class Countdown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        # Because Countdown is itself the iterator, return self.
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration

        value = self.current
        self.current -= 1  # Update state so the next call produces a new value.
        return value


print("\n4. Custom iterator")
countdown = Countdown(3)
print(next(countdown))  # 3
print(next(countdown))  # 2
print("Remaining values:", list(countdown))  # 1; list() consumes the iterator.


# ============================================================
# 5. Custom iterable that creates fresh iterators
# ============================================================
# A reusable iterable should usually return a NEW iterator each time.
# This prevents one loop from consuming the state needed by another loop.


class NumberRange:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop  # stop is excluded, just like range(start, stop).

    def __iter__(self):
        # A generator function is an easy way to create a fresh iterator.
        current = self.start
        while current < self.stop:
            yield current
            current += 1


print("\n5. Reusable custom iterable")
range_like = NumberRange(1, 4)
print("First loop:", list(range_like))
print("Second loop:", list(range_like))  # Still works: new iterator each time.


# ============================================================
# 6. Iterator exhaustion
# ============================================================

print("\n6. Iterators are consumed")
colors_iterator = iter(["red", "green", "blue"])
print("First two:", next(colors_iterator), next(colors_iterator))
print("What remains:", list(colors_iterator))
print("After exhaustion:", list(colors_iterator))  # Empty: nothing remains.


# ============================================================
# 7. Iterating over dictionaries
# ============================================================
# A dictionary is iterable. By default, it yields KEYS.

scores = {"Asha": 95, "Rahul": 88}
print("\n7. Dictionary iteration")
print("Keys:", list(scores))
print("Values:", list(scores.values()))
print("Key-value pairs:", list(scores.items()))


# ============================================================
# QUICK REVIEW
# ============================================================
# iterable              -> can create an iterator with iter(obj)
# iterator              -> produces values one-by-one with next(obj)
# iter(obj)             -> gets an iterator from an iterable
# next(iterator)        -> gets next item and advances state
# StopIteration         -> signals there are no more values
# __iter__()            -> defines how iter(obj) works
# __next__()            -> defines how next(obj) works
# list/tuple/string     -> iterables (normally reusable)
# iter(list)            -> iterator (consumed as values are read)
# for item in obj       -> repeatedly calls iter() and next() internally
