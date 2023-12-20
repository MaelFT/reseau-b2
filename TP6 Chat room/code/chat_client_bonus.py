import asyncio
import sys
import time
import getopt
import aioconsole

async def conn():
    argv = sys.argv[1:]
    port = 8888
    address = '127.0.0.1'
    options, args = getopt.getopt(argv, 
                                  "p:a:",
                               ["port=",
                                "address="])
    for name, value in options:
        if name in ['-p', '--port']:
            port = value
        elif name in ['-a', '--address']:
            address = value
    return await asyncio.open_connection(host=address, port=port)

async def read_serv(reader):
    while True:
        data = await reader.read(255)
        if data.decode() == '':
            print('Annonce : Le serveur est fermer')
            sys.exit()
        if data:
            print(data.decode())
        

async def write_serv(writer):
    msg = 'Hello|' + input("Choisissez votre pseudo : ")
    writer.write(str(msg).encode())
    await writer.drain()
    while True:
        msg = await aioconsole.ainput()
        if msg == "exit":
            sys.exit()
            break
        print(time.strftime("%H:%M:%S") + f" | Vous avez dit : {msg}")
        writer.write(str(msg).encode())
        await writer.drain()

async def main():
    reader, writer = await conn()
    tasks = [ read_serv(reader), write_serv(writer) ]
    try:
        await asyncio.gather(*tasks)
    except:
        pass

if __name__ == "__main__":
    asyncio.run(main())