# ============================================
# INTERMEDIATE PYTHON - MULTIPROCESSING
# ============================================

import multiprocessing
import time
import os


# ============================================
# 1. Basic Process
# ============================================

def worker():
    print("Worker process running")
    print("Process ID:", os.getpid())


if __name__ == "__main__":

    process = multiprocessing.Process(
        target=worker
    )

    process.start()

    process.join()

    print("Main process finished.")


# ============================================
# 2. Passing arguments to Process
# ============================================

def greet(name):
    print(f"Hello {name}")
    print("Process ID:", os.getpid())


if __name__ == "__main__":

    process = multiprocessing.Process(
        target=greet,
        args=("Alice",)
    )

    process.start()
    process.join()


# ============================================
# 3. Multiple processes
# ============================================

def task(name):

    print(f"{name} started")

    time.sleep(2)

    print(f"{name} finished")


if __name__ == "__main__":

    processes = []

    for i in range(3):

        process = multiprocessing.Process(
            target=task,
            args=(f"Process-{i}",)
        )

        processes.append(process)

        process.start()

    for process in processes:
        process.join()

    print("All processes completed.")


# ============================================
# 4. Process IDs
# ============================================

def show_process_info():

    print(
        "Current PID:",
        os.getpid()
    )

    print(
        "Parent PID:",
        os.getppid()
    )


if __name__ == "__main__":

    process = multiprocessing.Process(
        target=show_process_info
    )

    process.start()
    process.join()


# ============================================
# 5. Process return values
# ============================================

# A Process does NOT directly return a value
# like a normal function.

# We need IPC/shared mechanisms.

from multiprocessing import Queue


def calculate_square(number, queue):

    result = number ** 2

    queue.put(result)


if __name__ == "__main__":

    queue = Queue()

    process = multiprocessing.Process(
        target=calculate_square,
        args=(10, queue)
    )

    process.start()

    result = queue.get()

    process.join()

    print("\nSquare:", result)


# ============================================
# 6. Queue
# ============================================

def producer(queue):

    for i in range(5):

        print("Producing:", i)

        queue.put(i)

        time.sleep(0.5)


def consumer(queue):

    for _ in range(5):

        item = queue.get()

        print("Consuming:", item)


if __name__ == "__main__":

    queue = multiprocessing.Queue()

    producer_process = multiprocessing.Process(
        target=producer,
        args=(queue,)
    )

    consumer_process = multiprocessing.Process(
        target=consumer,
        args=(queue,)
    )

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()


# ============================================
# 7. Pipe
# ============================================

def sender(connection):

    connection.send(
        "Hello from child process"
    )

    connection.close()


if __name__ == "__main__":

    parent_connection, child_connection = (
        multiprocessing.Pipe()
    )

    process = multiprocessing.Process(
        target=sender,
        args=(child_connection,)
    )

    process.start()

    message = parent_connection.recv()

    print("\nMessage:", message)

    process.join()


# ============================================
# 8. Shared Value
# ============================================

from multiprocessing import Value


def increment(counter):

    for _ in range(10000):

        with counter.get_lock():

            counter.value += 1


if __name__ == "__main__":

    counter = Value("i", 0)

    process1 = multiprocessing.Process(
        target=increment,
        args=(counter,)
    )

    process2 = multiprocessing.Process(
        target=increment,
        args=(counter,)
    )

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("\nShared counter:", counter.value)


# ============================================
# 9. Shared Array
# ============================================

from multiprocessing import Array


def modify_array(numbers):

    for i in range(len(numbers)):

        numbers[i] *= 2


if __name__ == "__main__":

    numbers = Array(
        "i",
        [1, 2, 3, 4, 5]
    )

    process = multiprocessing.Process(
        target=modify_array,
        args=(numbers,)
    )

    process.start()
    process.join()

    print("\nShared array:", list(numbers))


# ============================================
# 10. Lock
# ============================================

def safe_increment(counter, lock):

    for _ in range(10000):

        with lock:

            counter.value += 1


if __name__ == "__main__":

    counter = Value("i", 0)

    lock = multiprocessing.Lock()

    process1 = multiprocessing.Process(
        target=safe_increment,
        args=(counter, lock)
    )

    process2 = multiprocessing.Process(
        target=safe_increment,
        args=(counter, lock)
    )

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("\nSafe counter:", counter.value)


# ============================================
# 11. Pool
# ============================================

from multiprocessing import Pool


def square(number):

    return number ** 2


if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]

    with Pool(processes=3) as pool:

        results = pool.map(
            square,
            numbers
        )

    print("\nPool results:")
    print(results)


# ============================================
# 12. Pool apply
# ============================================

if __name__ == "__main__":

    with Pool(processes=3) as pool:

        result = pool.apply(
            square,
            (10,)
        )

    print("\napply result:", result)


# ============================================
# 13. Pool apply_async
# ============================================

if __name__ == "__main__":

    with Pool(processes=3) as pool:

        results = [
            pool.apply_async(
                square,
                (number,)
            )
            for number in range(1, 6)
        ]

        output = [
            result.get()
            for result in results
        ]

    print("\nAsync pool results:")
    print(output)


# ============================================
# 14. Pool starmap
# ============================================

def add(a, b):

    return a + b


if __name__ == "__main__":

    values = [
        (1, 10),
        (2, 20),
        (3, 30)
    ]

    with Pool(processes=3) as pool:

        results = pool.starmap(
            add,
            values
        )

    print("\nstarmap results:")
    print(results)


# ============================================
# 15. ProcessPoolExecutor
# ============================================

from concurrent.futures import ProcessPoolExecutor


def cube(number):

    return number ** 3


if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]

    with ProcessPoolExecutor(
        max_workers=3
    ) as executor:

        results = executor.map(
            cube,
            numbers
        )

    print("\nProcessPoolExecutor:")
    print(list(results))


# ============================================
# 16. submit() and Future
# ============================================

if __name__ == "__main__":

    with ProcessPoolExecutor(
        max_workers=3
    ) as executor:

        future = executor.submit(
            cube,
            10
        )

        print(
            "\nFuture result:",
            future.result()
        )