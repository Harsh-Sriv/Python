# ============================================================
# INTERMEDIATE PYTHON — SCOPE & CLOSURES
# Standalone notes + runnable quick revision reference
# ============================================================
# SCOPE means the region of code where a name can be found.
# Python searches names using the LEGB rule, in this order:
# L = Local      -> inside the current function
# E = Enclosing  -> inside an outer function (for nested functions)
# G = Global     -> at the top level of this file/module
# B = Built-in   -> names Python provides, such as len, print, and range


# ============================================================
# 1. Local scope (L)
# ============================================================


def local_scope_example() -> None:
    message = "I exist only inside this function"  # Local variable
    print(message)


print("1. Local scope")
local_scope_example()

# This would fail because message is local to the function above:
# print(message)  # NameError


# ============================================================
# 2. Global scope (G)
# ============================================================

app_name = "Study Tracker"  # Defined at module/file level: global scope.


def show_app_name() -> None:
    # Reading a global variable is allowed without the global keyword.
    print(app_name)


print("\n2. Global scope")
show_app_name()


# ============================================================
# 3. LEGB lookup order
# ============================================================

label = "global label"


def outer() -> None:
    label = "enclosing label"

    def inner() -> None:
        label = "local label"
        # Python finds local label first, so it stops searching here.
        print(label)

    inner()


print("\n3. LEGB: Local wins")
outer()


def enclosing_example() -> None:
    label = "enclosing label"

    def inner() -> None:
        # No local `label`, so Python searches enclosing scope next.
        print(label)

    inner()


print("\n3. LEGB: Enclosing is used when no local exists")
enclosing_example()


def global_example() -> None:
    # No local or enclosing `label`, so Python uses the global variable.
    print(label)


print("\n3. LEGB: Global is used when no local/enclosing name exists")
global_example()

# Built-ins are the final lookup level. Here len is a built-in function.
print("\n3. LEGB: Built-in example")
print("Length:", len([10, 20, 30]))


# ============================================================
# 4. global: reassign a global variable inside a function
# ============================================================
# Use `global name` ONLY when you intend to REASSIGN the global name.
# Reading it does not require global. Excessive global state makes code
# harder to test and reason about, so prefer passing/returning values.

visits = 0


def record_visit() -> None:
    global visits
    visits += 1


print("\n4. global")
record_visit()
record_visit()
print("Visits:", visits)


# ============================================================
# 5. Why assignment changes scope
# ============================================================
# If Python sees `name = value` anywhere in a function, it treats name as
# local throughout that function unless you explicitly declare global or
# nonlocal. The commented code below would raise UnboundLocalError.

points = 10


def safe_points_example() -> None:
    # This reads the global value because there is no assignment to points.
    print("Read global points:", points)


safe_points_example()

# def broken_points_example():
#     print(points)       # Python considers points local due to next line.
#     points += 1         # UnboundLocalError


# ============================================================
# 6. nonlocal: reassign an enclosing variable
# ============================================================
# nonlocal is used inside a nested function. It targets a variable in the
# nearest enclosing FUNCTION scope (not a global/module scope).


def make_counter():
    count = 0  # Enclosing variable for increment().

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


print("\n6. nonlocal")
counter = make_counter()
print(counter())  # 1
print(counter())  # 2; count was preserved and updated.
print(counter())  # 3


# ============================================================
# 7. Closures
# ============================================================
# A CLOSURE is a function that remembers values from its enclosing scope,
# even after the outer function has finished. `nonlocal` is only needed
# when the closure must REASSIGN an enclosing variable.


def make_multiplier(factor: int):
    # factor is remembered by the returned inner function.
    def multiply(value: int) -> int:
        return value * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print("\n7. Closure")
print("Double 10:", double(10))
print("Triple 10:", triple(10))


# ============================================================
# 8. Practical closure: configure a reusable logger function
# ============================================================


def make_logger(prefix: str):
    """Return a logger that permanently remembers its prefix."""
    def log(message: str) -> None:
        print(f"[{prefix}] {message}")

    return log


api_log = make_logger("API")
database_log = make_logger("DATABASE")

print("\n8. Practical closure")
api_log("Request started")
database_log("Connection opened")


# ============================================================
# 9. Common closure pitfall: late binding in a loop
# ============================================================
# Closures look up a variable when called, not when created. Therefore all
# three functions below would see the final loop value (2):
#
# functions = []
# for number in range(3):
#     functions.append(lambda: number)
# print([function() for function in functions])  # [2, 2, 2]
#
# Fix it by storing the current value as a default parameter:

functions = []
for number in range(3):
    functions.append(lambda saved_number=number: saved_number)

print("\n9. Closure loop pitfall - fixed")
print([function() for function in functions])  # [0, 1, 2]


# ============================================================
# QUICK REVIEW
# ============================================================
# LEGB                 -> Local, Enclosing, Global, Built-in lookup order
# local variable       -> defined inside current function
# enclosing variable   -> defined in an outer function
# global variable      -> defined at module/file level
# global name          -> reassign a global variable from a function
# nonlocal name        -> reassign an enclosing function variable
# closure              -> inner function remembering enclosing values
# global/nonlocal      -> only required for reassignment, not simple reading
