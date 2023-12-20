import asyncio
import random
import time
import sys
import getopt
import websockets
import redis.asyncio as redis

global CLIENTS
CLIENTS = {}
global redisDB
redisDB = redis.Redis(host="10.33.76.214", port=6379)

async def handle_echo(websocket):
    while True:
        message = await websocket.recv()
        addr = str(websocket.remote_address)

        if message == '':
            pseudo = await redisDB.get(client + "pseudo") 
            print(f"{pseudo} from {addr!r} leave the room")
            for client in CLIENTS:
                if client != addr:
                    msg = f"\033[38;5;196m\033[1mAnnonce \033[0m: \033" + str(await redisDB.get(client + "color"))[6:-1] + f"{pseudo.decode()}\033[0m a quitté la chatroom"
                    await CLIENTS[client]["w"].send(msg)
            del CLIENTS[addr]
            await redisDB.delete(addr + "pseudo")
            await redisDB.delete(addr + "color") 
            break

        if addr in CLIENTS:
            print(f"Message received from {addr!r} : {message!r}")
            for client in CLIENTS:
                if client != addr:
                    if message != '':
                        pseudo = await redisDB.get(addr + "pseudo")
                        msg = time.strftime("%H:%M:%S") + " | \033" + str(await redisDB.get(client + "color"))[6:-1] + f"{pseudo.decode()}\033[0m\033[38;5;244m a dit : \033[0m\033[38;5;256m{message!r}\033[0m"
                        await CLIENTS[client]["w"].send(msg)

        if addr not in CLIENTS:
            pseudo = message[6:]
            color = '\033[38;5;' + str(random.randrange(256)) + 'm'
            CLIENTS[addr] = {}
            CLIENTS[addr]["w"] = websocket
            await redisDB.set(addr + "pseudo", pseudo)
            await redisDB.set(addr + "color", color)
            for client in CLIENTS:
                if client != addr:
                    if message != '':
                        msg = f"\033[38;5;196m\033[1mAnnonce \033[0m: \033" + str(await redisDB.get(client + "color"))[6:-1] + f"{str(pseudo)}\033[0m a rejoint la chatroom"
                        await CLIENTS[client]["w"].send(msg)

async def main():
    await redisDB.flushall()
    argv = sys.argv[1:]
    port = 8765
    address = "localhost"
    options, args = getopt.getopt(argv, 
                                  "p:a:",
                               ["port=",
                                "address="])
    for name, value in options:
        if name in ['-p', '--port']:
            port = value
        elif name in ['-a', '--address']:
            address = value
    addrs = address + ':' + str(port)
    try:
        async with websockets.serve(handle_echo, address, port):
            print(f'Serving on \033[38;5;196m{addrs}\033[0m')
            await asyncio.Future()
    except:
        await redisDB.aclose()
        print('Fermeture du serveur')

if __name__ == "__main__":
    asyncio.run(main())