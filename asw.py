import asyncio
import time
import random


def task_sync(s=0):
    print("sync task:{0} begin".format(s))
    time.sleep(1)
    print("sync task:{0} complete".format(s))


task_sync(1)
task_sync(2)


async def task_async(s=0):
    print("async task:{0} begin".format(s))
    await asyncio.sleep(random.randint(1, 3))
    print("async task:{0} complete".format(s))


async def task1():
    task = [task_async(x) for x in range(0, 10)]
    await asyncio.gather(*task)


async def task2():
    for t in [asyncio.create_task(task_async(x)) for x in range(10, 20)]:
        await t


if __name__ == "__main__":
    asyncio.run(task1())
    asyncio.run(task2())
