import aiohttp
import sys
import asyncio
import time
import aiofiles

async def get_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp = await resp.read()
            return resp

async def write_content(content, file):
    async with aiofiles.open('tmp/' + file, "w") as out:
        await out.write(str(content))
        await out.flush()

async def main():
    if len(sys.argv) > 1:
        file = open(sys.argv[1], 'r')
        lines = file.readlines()
        tasks = [ task(lines[i]) for i in range (9) ]
        await asyncio.gather(*tasks)

async def task(line):
    r = await get_content(line)
    await write_content(r, line[8:-2])

if __name__ == '__main__':
    start = time.perf_counter()

    asyncio.run(main())

    stop = time.perf_counter()
    print(f'Done in {stop - start} seconds')
