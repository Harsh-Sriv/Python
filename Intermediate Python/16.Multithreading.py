# ============================================
# INTERMEDIATE PYTHON - MULTITHREADING
# ============================================

import threading
import time


# ============================================
# 1. Basic thread
# ============================================

def print_numbers():

    for i in range(5):

        print("Number:", i)

        time.sleep(0.5)


thread = threading.Thread(
    target=print_numbers
)

thread.start()

thread.join()

print("Main thread finished.")


# ============================================
# 2. Running multiple threads
# ============================================

def task(name):

    for i in range(3):

        print(f"{name}: {i}")

        time.sleep(0.5)


thread1 = threading.Thread(
    target=task,
    args=("Thread 1",)
)

thread2 = threading.Thread(
    target=task,
    args=("Thread 2",)
)


thread1.start()
thread2.start()


thread1.join()
thread2.join()

print("\nBoth threads finished.")


# ============================================
# 3. Passing multiple arguments
# ============================================

def calculate(name, start, end):

    print(
        f"{name}: calculating "
        f"{start} to {end}"
    )

    total = sum(range(start, end))

    print(f"{name}: result = {total}")


thread = threading.Thread(
    target=calculate,
    args=("Worker", 1, 100)
)

thread.start()
thread.join()


# ============================================
# 4. Thread names
# ============================================

def worker():

    current = threading.current_thread()

    print(
        "\nCurrent thread:",
        current.name
    )


thread = threading.Thread(
    target=worker,
    name="MyWorker"
)

thread.start()
thread.join()


# ============================================
# 5. Checking whether thread is alive
# ============================================

def long_task():

    time.sleep(2)


thread = threading.Thread(
    target=long_task
)

thread.start()

print("\nThread alive:", thread.is_alive())

thread.join()

print("Thread alive:", thread.is_alive())


# ============================================
# 6. Daemon thread
# ============================================

def background_task():

    while True:

        print("Background task running...")

        time.sleep(1)


thread = threading.Thread(
    target=background_task,
    daemon=True
)

thread.start()

time.sleep(2)

print("\nMain program ending.")

# Daemon thread automatically stops when
# the main program exits.


# ============================================
# 7. Race condition
# ============================================

counter = 0


def increment():

    global counter

    for _ in range(100000):

        counter += 1


thread1 = threading.Thread(
    target=increment
)

thread2 = threading.Thread(
    target=increment
)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("\nCounter:", counter)


# ============================================
# 8. Lock
# ============================================

counter = 0

lock = threading.Lock()


def safe_increment():

    global counter

    for _ in range(100000):

        with lock:

            counter += 1


thread1 = threading.Thread(
    target=safe_increment
)

thread2 = threading.Thread(
    target=safe_increment
)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Safe counter:", counter)


# ============================================
# 9. Lock manually
# ============================================

lock = threading.Lock()

lock.acquire()

try:

    print("\nCritical section")

finally:

    lock.release()


# Prefer:

with lock:

    print("Critical section")


# ============================================
# 10. RLock
# ============================================

rlock = threading.RLock()


def outer():

    with rlock:

        print("Outer lock acquired")

        inner()


def inner():

    with rlock:

        print("Inner lock acquired")


outer()


# ============================================
# 11. Event
# ============================================

event = threading.Event()


def worker():

    print("\nWorker waiting...")

    event.wait()

    print("Worker received signal.")


thread = threading.Thread(
    target=worker
)

thread.start()

time.sleep(2)

print("Sending signal...")

event.set()

thread.join()


# ============================================
# 12. Semaphore
# ============================================

semaphore = threading.Semaphore(2)


def limited_task(name):

    with semaphore:

        print(
            f"{name} entered resource"
        )

        time.sleep(2)

        print(
            f"{name} leaving resource"
        )


threads = []

for i in range(5):

    thread = threading.Thread(
        target=limited_task,
        args=(f"Thread-{i}",)
    )

    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


# ============================================
# 13. Thread-safe queue
# ============================================

from queue import Queue


queue = Queue()


def producer():

    for i in range(5):

        print("Producing:", i)

        queue.put(i)

        time.sleep(0.5)


def consumer():

    while True:

        item = queue.get()

        if item is None:
            break

        print("Consuming:", item)

        queue.task_done()


producer_thread = threading.Thread(
    target=producer
)

consumer_thread = threading.Thread(
    target=consumer
)

producer_thread.start()
consumer_thread.start()

producer_thread.join()

queue.put(None)

consumer_thread.join()


# ============================================
# 14. ThreadPoolExecutor
# ============================================

from concurrent.futures import ThreadPoolExecutor


def download_file(file_number):

    print(
        f"Downloading file {file_number}"
    )

    time.sleep(1)

    return f"File {file_number} downloaded"


print("\n--- ThreadPoolExecutor ---")

with ThreadPoolExecutor(
    max_workers=3
) as executor:

    results = executor.map(
        download_file,
        range(1, 6)
    )

    for result in results:

        print(result)


# ============================================
# 15. submit() and Future
# ============================================

def calculate_square(number):

    time.sleep(1)

    return number ** 2


with ThreadPoolExecutor(
    max_workers=3
) as executor:

    future1 = executor.submit(
        calculate_square,
        5
    )

    future2 = executor.submit(
        calculate_square,
        10
    )

    print("\nFuture 1 result:", future1.result())
    print("Future 2 result:", future2.result())


# ============================================
# 16. as_completed()
# ============================================

from concurrent.futures import as_completed


def task(number):

    time.sleep(number)

    return number * 10


with ThreadPoolExecutor(
    max_workers=3
) as executor:

    futures = [
        executor.submit(task, number)
        for number in [3, 1, 2]
    ]

    print("\nCompleted results:")

    for future in as_completed(futures):

        print(future.result())