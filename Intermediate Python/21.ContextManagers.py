# ============================================
# INTERMEDIATE PYTHON - CONTEXT MANAGERS
# ============================================

import time
from contextlib import contextmanager


# ============================================
# 1. Basic file context manager
# ============================================

print("--- File context manager ---")

with open("example.txt", "w") as file:

    file.write("Hello Python!")


# File is automatically closed here.


# ============================================
# 2. Checking closed state
# ============================================

file = open("example.txt", "r")

print(
    "Before close:",
    file.closed
)

file.close()

print(
    "After close:",
    file.closed
)


# ============================================
# 3. Custom context manager using a class
# ============================================

class MyContext:

    def __enter__(self):

        print("\nEntering context")

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        print("Exiting context")

        print(
            "Exception type:",
            exc_type
        )

        print(
            "Exception value:",
            exc_value
        )

        return False


with MyContext() as context:

    print("Inside context")


# ============================================
# 4. Context manager with exception
# ============================================

with MyContext():

    print("\nInside context")

    raise ValueError(
        "Something went wrong"
    )


# The exception still propagates because
# __exit__ returned False.


# ============================================
# 5. Suppressing an exception
# ============================================

class IgnoreErrors:

    def __enter__(self):

        print("\nEntering IgnoreErrors")

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        print("Leaving IgnoreErrors")

        # True means:
        # suppress the exception

        return True


with IgnoreErrors():

    print("This will run")

    raise ValueError(
        "This error is suppressed"
    )

print("Program continues.")


# ============================================
# 6. Returning an object from __enter__
# ============================================

class DatabaseConnection:

    def __enter__(self):

        print("\nOpening database")

        self.connection = "DB Connection"

        return self.connection

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        print("Closing database")


with DatabaseConnection() as connection:

    print(
        "Using:",
        connection
    )


# ============================================
# 7. Context manager for timing
# ============================================

class Timer:

    def __enter__(self):

        self.start = time.perf_counter()

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        self.end = time.perf_counter()

        self.elapsed = (
            self.end - self.start
        )

        print(
            f"Elapsed: "
            f"{self.elapsed:.4f} seconds"
        )


with Timer():

    time.sleep(1)


# ============================================
# 8. Context manager with @contextmanager
# ============================================

@contextmanager
def my_context():

    print("\nEntering context")

    try:

        yield

    finally:

        print("Exiting context")


with my_context():

    print("Doing work")


# ============================================
# 9. Context manager returning a value
# ============================================

@contextmanager
def database():

    print("\nConnecting...")

    connection = "Database connection"

    try:

        yield connection

    finally:

        print("Closing connection")


with database() as connection:

    print(
        "Using:",
        connection
    )


# ============================================
# 10. Exception handling with
#     @contextmanager
# ============================================

@contextmanager
def resource():

    print("\nResource acquired")

    try:

        yield "Resource"

    except Exception as error:

        print(
            "Error:",
            error
        )

        raise

    finally:

        print("Resource released")


try:

    with resource() as value:

        print(
            "Using:",
            value
        )

        raise ValueError(
            "Something failed"
        )

except ValueError:

    print("Exception handled outside.")


# ============================================
# 11. Multiple context managers
# ============================================

with open("file1.txt", "w") as file1, \
     open("file2.txt", "w") as file2:

    file1.write("File 1")
    file2.write("File 2")


# Both files are automatically closed.


# ============================================
# 12. Nested context managers
# ============================================

with open("outer.txt", "w") as outer:

    with open("inner.txt", "w") as inner:

        outer.write("Outer")
        inner.write("Inner")


# ============================================
# 13. Lock as a context manager
# ============================================

import threading

lock = threading.Lock()

with lock:

    print(
        "\nInside critical section"
    )

# Lock automatically released.


# ============================================
# 14. Practical transaction example
# ============================================

class Transaction:

    def __enter__(self):

        print("\nTransaction started")

        return self

    def commit(self):

        print("Transaction committed")

    def rollback(self):

        print("Transaction rolled back")

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        if exc_type is None:

            self.commit()

        else:

            self.rollback()

        # Don't suppress exception

        return False


with Transaction():

    print("Performing database operations")


try:

    with Transaction():

        print(
            "Performing operations..."
        )

        raise ValueError(
            "Database error"
        )

except ValueError:

    print(
        "Error handled by caller."
    )