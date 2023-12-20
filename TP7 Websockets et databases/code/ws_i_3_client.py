import asyncio
import sys
import time
import getopt
import aioconsole
import websockets

async def conn():
    argv = sys.argv[1:]
    port = 8765
    address = 'localhost'
    options, args = getopt.getopt(argv, 
                                  "p:a:",
                               ["port=",
                                "address="])
    for name, value in options:
        if name in ['-p', '--port']:
            port = value
        elif name in ['-a', '--address']:
            address = value
    return await websockets.connect(f"ws://{address}:{port}")

async def read_serv(ws):
    async for data in ws:
        if data == '':
            print('Annonce : Le serveur est fermer')
            sys.exit()
        if data:
            print(data)

async def write_serv(ws):
    msg = 'Hello|' + input("Choisissez votre pseudo : ")
    await ws.send(msg)
    while True:
        msg = await aioconsole.ainput()
        if msg == "exit":
            sys.exit()
        print(time.strftime("%H:%M:%S") + f" | Vous avez dit : {msg}")
        await ws.send(msg)

async def main():
    ws = await conn()
    tasks = [ read_serv(ws), write_serv(ws) ]
    try:
        await asyncio.gather(*tasks)
    except:
        pass

if __name__ == "__main__":
    asyncio.run(main())