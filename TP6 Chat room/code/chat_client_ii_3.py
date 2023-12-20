import asyncio
import aioconsole

async def conn():
    return await asyncio.open_connection(host="127.0.0.1", port=8888)

async def read_serv(reader):
    while True:
        data = await reader.read(255)
        if data:
            print(data.decode())

async def write_serv(writer):
    while True:
        msg = await aioconsole.ainput()
        writer.write(str(msg).encode())
        await writer.drain()

async def main():
    reader, writer = await conn()
    tasks = [ read_serv(reader), write_serv(writer) ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())