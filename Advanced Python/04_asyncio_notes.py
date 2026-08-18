# ============================================================
# INTERMEDIATE PYTHON — async / await / asyncio
# Standalone notes + runnable quick revision reference
# ============================================================
# asyncio is for concurrent I/O-bound work: API calls, databases, files,
# timers, websockets, etc. While one task waits, the event loop can run
# another task. It does NOT make CPU-heavy Python code faster by itself.

import asyncio
import time


# ============================================================
# 1. Coroutine: an async function
# ============================================================
# Calling an async function does NOT run it immediately. It creates a
# coroutine object, which must be awaited or scheduled as a task.


async def greet(name: str) -> str:
    # await pauses only this coroutine and gives control to the event loop.
    await asyncio.sleep(0.2)  # Simulates waiting for I/O; it does not block.
    return f"Hello, {name}!"


async def coroutine_example() -> None:
    message = await greet("Asha")  # Run the coroutine and wait for its result.
    print(message)


# ============================================================
# 2. asyncio.run() and the event loop
# ============================================================
# asyncio.run(main()) creates an event loop, runs main(), and closes the
# loop afterwards. Use it once at the top level of a normal script.
# Do NOT call asyncio.run() from inside another async function.


# ============================================================
# 3. Sequential await versus concurrent work
# ============================================================


async def fetch(label: str, seconds: float) -> str:
    """Pretend to wait for an API/database response."""
    print(f"  {label}: started")
    await asyncio.sleep(seconds)
    print(f"  {label}: finished")
    return f"{label} result"


async def sequential_example() -> None:
    # Each await finishes before the next fetch begins: about 0.6 seconds.
    start = time.perf_counter()
    first = await fetch("Sequential API 1", 0.3)
    second = await fetch("Sequential API 2", 0.3)
    elapsed = time.perf_counter() - start
    print("  Results:", [first, second])
    print(f"  Sequential time: about {elapsed:.1f}s")


# ============================================================
# 4. asyncio.gather(): run awaitables concurrently
# ============================================================
# gather() schedules its coroutine arguments together and waits until all
# complete. Results are returned in the SAME order as the arguments,
# regardless of which request finishes first.


async def gather_example() -> None:
    start = time.perf_counter()
    results = await asyncio.gather(
        fetch("Gather API 1", 0.3),
        fetch("Gather API 2", 0.3),
        fetch("Gather API 3", 0.1),
    )
    elapsed = time.perf_counter() - start
    print("  Results:", results)
    print(f"  Concurrent time: about {elapsed:.1f}s")


# ============================================================
# 5. asyncio.create_task(): start work now, await it later
# ============================================================
# A Task is a scheduled coroutine. create_task() lets multiple operations
# begin before you await their results. Keep a reference to every task.


async def create_task_example() -> None:
    search_task = asyncio.create_task(fetch("Search", 0.2))
    database_task = asyncio.create_task(fetch("Database", 0.3))

    # This synchronous preparation happens while tasks may be running.
    print("  Preparing the response while requests are in progress...")

    search_result = await search_task
    database_result = await database_task
    print("  Combined:", search_result, "+", database_result)


# ============================================================
# 6. Error handling with gather()
# ============================================================
# By default, an exception from gather() is raised to the caller.
# return_exceptions=True instead returns exceptions in the results list.


async def may_fail(name: str, should_fail: bool) -> str:
    await asyncio.sleep(0.1)
    if should_fail:
        raise ConnectionError(f"{name} is unavailable")
    return f"{name} succeeded"


async def gather_error_example() -> None:
    results = await asyncio.gather(
        may_fail("Service A", False),
        may_fail("Service B", True),
        return_exceptions=True,
    )
    for result in results:
        if isinstance(result, Exception):
            print("  Handled error:", result)
        else:
            print(" ", result)


# ============================================================
# 7. Async generators: yield values over time
# ============================================================
# An async generator uses `async def` + `yield`. Consume it using
# `async for`, because getting each next value may require awaiting.


async def progress_updates(total: int):
    for current in range(1, total + 1):
        await asyncio.sleep(0.05)
        yield f"Step {current}/{total}"


async def async_generator_example() -> None:
    async for update in progress_updates(3):
        print(" ", update)


# ============================================================
# 8. Cancellation
# ============================================================
# task.cancel() requests cancellation. The task receives
# asyncio.CancelledError at its next await point. Always re-raise that
# error after any necessary cleanup, so the task is truly cancelled.


async def long_running_work() -> None:
    try:
        while True:
            print("  Working...")
            await asyncio.sleep(0.1)
    except asyncio.CancelledError:
        print("  Cleaning up before cancellation.")
        raise  # Important: preserve the cancelled state.


async def cancellation_example() -> None:
    task = asyncio.create_task(long_running_work())
    await asyncio.sleep(0.25)  # Let the task run for a short time.
    task.cancel()              # Request cancellation.

    try:
        await task             # Wait until the task finishes cleanup.
    except asyncio.CancelledError:
        print("  Task cancelled successfully.")


# ============================================================
# Main coroutine: runs every example in order
# ============================================================


async def main() -> None:
    print("1. Coroutine and await")
    await coroutine_example()

    print("\n3. Sequential awaits")
    await sequential_example()

    print("\n4. asyncio.gather()")
    await gather_example()

    print("\n5. asyncio.create_task()")
    await create_task_example()

    print("\n6. gather() error handling")
    await gather_error_example()

    print("\n7. Async generator")
    await async_generator_example()

    print("\n8. Cancellation")
    await cancellation_example()


if __name__ == "__main__":
    asyncio.run(main())


# ============================================================
# QUICK REVIEW
# ============================================================
# async def             -> defines a coroutine function
# coroutine             -> object returned by calling async function
# await                 -> pause this coroutine; let event loop run others
# event loop            -> scheduler that runs ready async tasks
# asyncio.run(main())   -> top-level entry point for an async program
# create_task(coro)     -> schedule a coroutine to run concurrently
# gather(a, b)          -> run awaitables concurrently; collect results
# async for             -> consume an async generator/iterable
# task.cancel()         -> request cancellation of a task
# CancelledError        -> catch for cleanup, then normally re-raise
#
# Use asyncio primarily for I/O concurrency. For CPU-heavy work, consider
# multiprocessing, a process pool, or moving the work to another service.
