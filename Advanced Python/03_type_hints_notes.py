# ============================================================
# INTERMEDIATE PYTHON — TYPE HINTS
# Standalone notes + runnable quick revision reference
# ============================================================
# Type hints describe expected types of variables, parameters, and
# return values. Python does NOT enforce them at runtime. They help
# humans, editors, linters, and type checkers such as mypy.

from collections.abc import Callable, Iterable, Sequence
from typing import Any, Literal, TypedDict, TypeAlias, TypeVar


# ============================================================
# 1. Variable and function annotations
# ============================================================

# Syntax: variable_name: expected_type = value
name: str = "Asha"
age: int = 24
height: float = 1.68
is_learning: bool = True


def add(first: int, second: int) -> int:
    """Take two integers and return their sum as an integer."""
    return first + second


print("1. Basic annotations")
print(add(10, 20))
print(f"{name=}, {age=}, {height=}, {is_learning=}")


# ============================================================
# 2. Collection types (modern Python 3.9+ syntax)
# ============================================================

# list[str] means a list whose items should be strings.
languages: list[str] = ["Python", "SQL", "JavaScript"]
# dict[str, int] means string keys and integer values.
scores: dict[str, int] = {"Asha": 95, "Rahul": 88}
# tuple[str, int] means exactly a string followed by an integer.
user_record: tuple[str, int] = ("Asha", 24)
skills: set[str] = {"Python", "Git", "Docker"}


def average(numbers: list[float]) -> float:
    """Return the average of a non-empty list of numbers."""
    return sum(numbers) / len(numbers)


print("\n2. Collection annotations")
print(languages, scores, user_record, skills)
print("Average:", average([10.5, 20.0, 30.5]))


# ============================================================
# 3. Optional values: T | None
# ============================================================
# None means "no value". `str | None` means a string OR None.
# This is the modern equivalent of Optional[str].


def find_email(user_id: int) -> str | None:
    emails = {1: "asha@example.com", 2: "rahul@example.com"}
    return emails.get(user_id)  # dict.get returns None if the key is absent.


email = find_email(3)
print("\n3. Optional values")
if email is None:
    print("Email not found")
else:
    print("Email:", email)


# ============================================================
# 4. Union types: one of several possible types
# ============================================================
# `int | str` accepts an integer OR a string.


def format_id(user_id: int | str) -> str:
    return f"user-{user_id}"


print("\n4. Union types")
print(format_id(42), format_id("admin"))


# ============================================================
# 5. Any: opt out of type checking (use sparingly)
# ============================================================
# Any can be any type and permits any operation. It is useful for
# unknown external data, but precise types are safer when possible.


def display_api_value(value: Any) -> str:
    return f"Received: {value}"


print("\n5. Any")
print(display_api_value({"status": "ok"}))


# ============================================================
# 6. Callable: a function passed as a value
# ============================================================
# Callable[[input_types], return_type]
# Callable[[int], int] means a function taking int and returning int.


def apply_twice(function: Callable[[int], int], value: int) -> int:
    return function(function(value))


def double(number: int) -> int:
    return number * 2


print("\n6. Callable")
print("Double twice:", apply_twice(double, 5))


# ============================================================
# 7. Iterable versus Sequence
# ============================================================
# Iterable[T]: can be looped over (list, set, generator, etc.).
# Sequence[T]: ordered and indexable (list, tuple, str, etc.).


def total(values: Iterable[int]) -> int:
    return sum(values)


def first_item(items: Sequence[str]) -> str:
    return items[0]


print("\n7. Iterable and Sequence")
print("Total of set:", total({1, 2, 3}))
print("First item:", first_item(["first", "second"]))


# ============================================================
# 8. TypeVar: preserve a type through a generic function
# ============================================================
# T means "some type, chosen by the caller". If list[str] goes in,
# T is str and the returned value is also known to be str.

T = TypeVar("T")


def get_first(items: Sequence[T]) -> T:
    """Return the first item while preserving its specific type."""
    return items[0]


print("\n8. TypeVar / generic function")
print(get_first(["Python", "AI"]))
print(get_first([100, 200]))


# ============================================================
# 9. TypedDict: describe expected dictionary-shaped data
# ============================================================


class UserData(TypedDict):
    name: str
    age: int
    active: bool


def welcome(user: UserData) -> str:
    return f"Welcome, {user['name']}!"


user: UserData = {"name": "Asha", "age": 24, "active": True}
print("\n9. TypedDict")
print(welcome(user))


# ============================================================
# 10. Literal and TypeAlias
# ============================================================
# Literal restricts a value to exactly the listed choices.
# TypeAlias gives a long annotation a meaningful reusable name.

Status = Literal["pending", "running", "complete", "failed"]
UserScores: TypeAlias = dict[str, list[int]]


def report_status(status: Status) -> str:
    return f"Job status: {status}"


weekly_scores: UserScores = {"Asha": [90, 95], "Rahul": [88, 91]}
print("\n10. Literal and TypeAlias")
print(report_status("complete"))
print(weekly_scores)


# ============================================================
# QUICK REVIEW
# ============================================================
# parameter: type       -> expected input
# -> return_type        -> returned value
# list[str]             -> list containing strings
# dict[str, int]        -> str keys and int values
# str | None            -> string or no value
# int | str             -> one of multiple possible types
# Any                   -> unknown/unchecked type; avoid overusing it
# Callable[[int], int]  -> function: int input -> int output
# Iterable[T]           -> anything you can loop over
# Sequence[T]           -> ordered, indexable collection
# TypeVar               -> preserve the caller's specific type
# TypedDict             -> expected dictionary keys and types
# Literal               -> only specific fixed values allowed
# TypeAlias             -> readable name for a complex type
