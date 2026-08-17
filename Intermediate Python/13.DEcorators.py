# ============================================
# INTERMEDIATE PYTHON - DECORATORS
# ============================================


# ============================================
# 1. Functions are objects
# ============================================

def greet():
    print("Hello!")


# A function can be stored in a variable

say_hello = greet

say_hello()


# A function can be passed to another function

def execute_function(function):
    function()


execute_function(greet)


# ============================================
# 2. Function returning a function
# ============================================

def create_greeting():

    def greeting():
        print("Hello from inner function!")

    return greeting


my_function = create_greeting()

my_function()


# ============================================
# 3. Basic decorator
# ============================================

def my_decorator(function):

    def wrapper():

        print("Before function")

        function()

        print("After function")

    return wrapper


def say_hello():
    print("Hello!")


say_hello = my_decorator(say_hello)

say_hello()


# ============================================
# 4. @ decorator syntax
# ============================================

def my_decorator(function):

    def wrapper():

        print("Before function")

        function()

        print("After function")

    return wrapper


@my_decorator
def greet():
    print("Hello from greet()")


greet()


# This:

# @my_decorator
# def greet():
#     ...

# is equivalent to:

# def greet():
#     ...

# greet = my_decorator(greet)


# ============================================
# 5. Decorator with function arguments
# ============================================

def log_call(function):

    def wrapper(name):

        print("Calling function...")
        function(name)
        print("Function finished.")

    return wrapper


@log_call
def greet_user(name):

    print(f"Hello {name}")


greet_user("Alice")


# ============================================
# 6. *args and **kwargs
# ============================================

def log_call(function):

    def wrapper(*args, **kwargs):

        print("Function:", function.__name__)
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)

        result = function(*args, **kwargs)

        print("Finished.")

        return result

    return wrapper


@log_call
def add(a, b):

    return a + b


result = add(10, 20)

print("Result:", result)


# ============================================
# 7. functools.wraps
# ============================================

from functools import wraps


def my_decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print("Before")

        result = function(*args, **kwargs)

        print("After")

        return result

    return wrapper


@my_decorator
def multiply(a, b):
    """Multiply two numbers."""

    return a * b


print("\nFunction name:", multiply.__name__)
print("Documentation:", multiply.__doc__)


# ============================================
# 8. Timing decorator
# ============================================

import time


def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = function(*args, **kwargs)

        end = time.perf_counter()

        print(
            f"{function.__name__} "
            f"took {end - start:.6f} seconds"
        )

        return result

    return wrapper


@timer
def calculate():

    total = 0

    for i in range(1_000_000):
        total += i

    return total


calculate()


# ============================================
# 9. Authentication-style decorator
# ============================================

def require_login(function):

    @wraps(function)
    def wrapper(user, *args, **kwargs):

        if not user.get("logged_in"):
            print("Access denied.")
            return None

        return function(user, *args, **kwargs)

    return wrapper


@require_login
def view_dashboard(user):

    print(
        f"Welcome to dashboard, "
        f"{user['name']}"
    )


user1 = {
    "name": "Alice",
    "logged_in": True
}

user2 = {
    "name": "Bob",
    "logged_in": False
}

view_dashboard(user1)
view_dashboard(user2)


# ============================================
# 10. Decorator that modifies the return value
# ============================================

def uppercase_result(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        result = function(*args, **kwargs)

        return result.upper()

    return wrapper


@uppercase_result
def get_message():

    return "hello world"


print("\n", get_message())


# ============================================
# 11. Multiple decorators
# ============================================

def decorator_a(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print("Decorator A - before")

        result = function(*args, **kwargs)

        print("Decorator A - after")

        return result

    return wrapper


def decorator_b(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print("Decorator B - before")

        result = function(*args, **kwargs)

        print("Decorator B - after")

        return result

    return wrapper


@decorator_a
@decorator_b
def test():

    print("Original function")


test()


# ============================================
# 12. Decorator with parameters
# ============================================

def repeat(times):

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            for _ in range(times):
                function(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_hi():

    print("Hi!")


say_hi()


# ============================================
# 13. Practical retry decorator
# ============================================

def retry(attempts):

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            for attempt in range(1, attempts + 1):

                try:

                    return function(
                        *args,
                        **kwargs
                    )

                except Exception as error:

                    print(
                        f"Attempt {attempt} failed: "
                        f"{error}"
                    )

                    if attempt == attempts:
                        raise

        return wrapper

    return decorator


attempts = 0


@retry(3)
def unstable_function():

    global attempts

    attempts += 1

    if attempts < 3:
        raise RuntimeError("Temporary failure")

    return "Success"


print("\n", unstable_function())