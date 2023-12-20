import time
import asyncio

async def sleep_and_print():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

if __name__ == '__main__':
    start = time.perf_counter()
    loop = asyncio.get_event_loop()

    tasks = [loop.create_task(sleep_and_print()), loop.create_task(sleep_and_print())]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    stop = time.perf_counter()
    print(f'Done in {stop - start} seconds')

# import time
# import asyncio

# async def sleep_and_print():
#     for i in range(10):
#         print(i)
#         await asyncio.sleep(0.5)

# async def main():
#     tasks = [ sleep_and_print() for i in range(2) ]
#     await asyncio.gather(*tasks)

# if __name__ == '__main__':
#     start = time.perf_counter()
#     asyncio.run(main())
#     stop = time.perf_counter()
#     print(f'Done in {stop - start} seconds')