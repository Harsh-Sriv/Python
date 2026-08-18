# ============================================================
# INTERMEDIATE PYTHON — DATACLASSES
# Standalone notes + runnable quick revision reference
# ============================================================
# A dataclass is ideal for a class whose main purpose is storing data.
# @dataclass automatically creates useful methods such as __init__,
# __repr__, and __eq__, based on the declared fields.

from dataclasses import dataclass, field


# ============================================================
# 1. Basic dataclass
# ============================================================


@dataclass
class User:
    # Type-annotated attributes become dataclass fields.
    name: str
    age: int
    email: str


user_one = User("Asha", 24, "asha@example.com")
user_two = User("Asha", 24, "asha@example.com")

print("1. Basic @dataclass")
print(user_one)                    # Auto-generated readable __repr__.
print("Equal data?", user_one == user_two)  # Auto-generated __eq__.


# ============================================================
# 2. Default values
# ============================================================
# Fields with defaults must appear AFTER fields without defaults.


@dataclass
class Course:
    title: str
    duration_weeks: int = 4
    is_published: bool = False


print("\n2. Defaults")
print(Course("Python"))
print(Course("Asyncio", duration_weeks=2, is_published=True))


# ============================================================
# 3. field(default_factory=...): safe mutable defaults
# ============================================================
# Never write tags: list[str] = [] in a dataclass. That one list would be
# shared by EVERY instance. default_factory=list creates a fresh list for
# each object. Use it for list, dict, set, or other mutable default values.


@dataclass
class Project:
    name: str
    tags: list[str] = field(default_factory=list)
    settings: dict[str, bool] = field(default_factory=dict)


project_one = Project("Agent API")
project_two = Project("Portfolio")
project_one.tags.append("python")
project_one.settings["debug"] = True

print("\n3. field(default_factory=...) ")
print("Project one:", project_one)
print("Project two:", project_two)  # Still has its own empty values.


# ============================================================
# 4. field() options: repr, compare, and init
# ============================================================


@dataclass
class Account:
    username: str
    # repr=False hides a sensitive field when the object is printed.
    password_hash: str = field(repr=False)
    # compare=False means this field is ignored by == comparison.
    last_login: str | None = field(default=None, compare=False)
    # init=False means callers cannot pass this field to __init__.
    is_active: bool = field(default=True, init=False)


account_one = Account("asha", "hashed-secret", last_login="Monday")
account_two = Account("asha", "hashed-secret", last_login="Tuesday")

print("\n4. field() options")
print(account_one)  # password_hash is deliberately hidden.
print("Equal despite different last_login?", account_one == account_two)
print("Active?", account_one.is_active)


# ============================================================
# 5. __post_init__: validation or derived values after __init__
# ============================================================
# __post_init__ runs automatically after the generated __init__ method.


@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self) -> None:
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive")
        self.area = self.width * self.height


rectangle = Rectangle(5, 4)
print("\n5. __post_init__")
print(rectangle)


# ============================================================
# 6. Frozen dataclasses: immutable-style records
# ============================================================
# frozen=True prevents attribute reassignment after creation. This is useful
# for values that should not change, such as configuration or coordinates.
# Note: frozen does not deeply freeze mutable objects stored inside it.


@dataclass(frozen=True)
class Point:
    x: int
    y: int


point = Point(10, 20)
print("\n6. Frozen dataclass")
print(point)

try:
    point.x = 99  # Raises FrozenInstanceError.
except AttributeError as error:
    print("Cannot modify frozen Point:", error)


# ============================================================
# QUICK REVIEW
# ============================================================
# @dataclass                 -> generates __init__, __repr__, __eq__, etc.
# field                      -> configure one dataclass field
# default value              -> value used when caller omits that argument
# default_factory=list       -> creates a new mutable default per instance
# field(repr=False)          -> hide field from printed representation
# field(compare=False)       -> ignore field in equality comparison
# field(init=False)          -> do not accept field in generated __init__
# __post_init__              -> run validation/derived setup after __init__
# @dataclass(frozen=True)    -> prevent reassignment of fields
