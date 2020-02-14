import asyncio
import time


async def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        # if i % 50000000 == 0:
        #     await asyncio.sleep(0.000001)
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


async def main():
    divs1 = loop.create_task(find_divisibles(20000, 30))
    divs2 = loop.create_task(find_divisibles(200, 30))
    divs3 = loop.create_task(find_divisibles(23809330, 30))
    await asyncio.wait([divs1, divs2, divs3])


if __name__ == '__main__':
    start = time.perf_counter()

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
    finish = time.perf_counter()
    print(f'Took {round(finish - start, 2)}')
