""" #!/usr/bin/env python3 Hello world  of  Async """
import asyncio


async def count():
    print("one")
    await asyncio.sleep(2)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter() - start
    print(f"Executed in {end}s")