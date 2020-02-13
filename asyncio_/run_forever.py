import asyncio
import datetime

loop = asyncio.get_event_loop()


async def while_loop(caller_id: int):
    n = 0
    while True:
        print(f"{caller_id}:{n}")
        await asyncio.sleep(1)
        n += 1


async def some_func():
    await asyncio.sleep(5)
    print("Some Func")


async def countdown_timer(x):
    while x >= 0:
        x -= 1
        print("{} remaining".format(str(datetime.timedelta(seconds=x))))
        print("\n")
        await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for i in range(10):
        loop.create_task(while_loop(i))
    loop.run_until_complete(countdown_timer(10))
    print('After forever')
