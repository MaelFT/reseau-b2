import asyncio
import random
import time
import sys
import getopt

global CLIENTS
CLIENTS = {}

async def handle_echo(reader, writer):
    while True:
        data = await reader.read(1024)
        message = data.decode()
        addr = writer.get_extra_info('peername')

        if data.decode() == '':
            pseudo = CLIENTS[addr]["pseudo"]
            print(f"{pseudo} from {addr!r} leave the room")
            for client in CLIENTS:
                if client != addr:
                    msg = f"\033[38;5;196m\033[1mAnnonce \033[0m: " + CLIENTS[addr]["color"] + f"{pseudo}\033[0m a quitté la chatroom"
                    CLIENTS[client]["w"].write(msg.encode())
                    await CLIENTS[client]["w"].drain()
            del CLIENTS[addr]
            break

        if addr in CLIENTS:
            print(f"Message received from {addr!r} : {message!r}")
            for client in CLIENTS:
                if client != addr:
                    if message != '':
                        pseudo = CLIENTS[addr]["pseudo"]
                        msg = time.strftime("%H:%M:%S") + " | " + CLIENTS[addr]["color"] + f"{pseudo}\033[0m\033[38;5;244m a dit : \033[0m\033[38;5;256m{message!r}\033[0m"
                        CLIENTS[client]["w"].write(msg.encode())
                        await CLIENTS[client]["w"].drain()

        if addr not in CLIENTS:
            pseudo = data.decode()[6:]
            color = '\033[38;5;' + str(random.randrange(256)) + 'm'
            CLIENTS[addr] = {}
            CLIENTS[addr]["r"] = reader
            CLIENTS[addr]["w"] = writer
            CLIENTS[addr]["pseudo"] = pseudo
            CLIENTS[addr]["color"] = color
            for client in CLIENTS:
                if client != addr:
                    if message != '':
                        msg = f"\033[38;5;196m\033[1mAnnonce \033[0m: " + CLIENTS[addr]["color"] + pseudo + "\033[0m a rejoint la chatroom"
                        CLIENTS[client]["w"].write(msg.encode())
                        await CLIENTS[client]["w"].drain()

async def serv():
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

    server = await asyncio.start_server(handle_echo, address, int(port))

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on \033[38;5;196m {addrs}\033[0m')

    async with server:
        await server.serve_forever()

async def main():
    try:
        await asyncio.gather(serv())
    except:
        print('Fermeture du serveur')

if __name__ == "__main__":
    asyncio.run(main())