import asyncio

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
                    msg = f"Annonce : {pseudo} a quitté la chatroom"
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
                        msg = f"{pseudo} a dit : {message!r}"
                        CLIENTS[client]["w"].write(msg.encode())
                        await CLIENTS[client]["w"].drain()

        if addr not in CLIENTS:
            pseudo = data.decode()[6:]
            CLIENTS[addr] = {}
            CLIENTS[addr]["r"] = reader
            CLIENTS[addr]["w"] = writer
            CLIENTS[addr]["pseudo"] = pseudo
            for client in CLIENTS:
                if client != addr:
                    if message != '':
                        msg = f"Annonce : {pseudo} a rejoint la chatroom"
                        CLIENTS[client]["w"].write(msg.encode())
                        await CLIENTS[client]["w"].drain()

async def serv():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

async def main():
    try:
        await asyncio.gather(serv())
    except:
        print('Fermeture du serveur')

if __name__ == "__main__":
    asyncio.run(main())