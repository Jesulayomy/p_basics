#!/usr/bin/env python3
"""  Sample function to test async operations """
import asyncio


async def sleeperFunction(times):
    """ Sleepwer dunctions """

    print("Calling the generator")
    for i in times:
        print("Awaiting")
        await asyncio.sleep(1)
        yield i

async def nightTime(times):
    print("Calling  the coroutine")
    async for item in sleeperFunction(times):
        print("Async For-ing")
        print(item)

times = ["one", "two", "three", "four", "five"]
asyncio.run(nightTime(times))
print("Hello World")
