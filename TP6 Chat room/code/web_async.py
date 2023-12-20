import aiohttp
import sys
import asyncio
import time
import aiofiles

url = 'https://www.ynov.com'

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
        r = await get_content(sys.argv[1])
        await write_content(r, 'title.txt')

if __name__ == "__main__":
    start = time.perf_counter()
    loop = asyncio.get_event_loop()

    tasks = [loop.create_task(main())]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    stop = time.perf_counter()
    print(f'Done in {stop - start} seconds')