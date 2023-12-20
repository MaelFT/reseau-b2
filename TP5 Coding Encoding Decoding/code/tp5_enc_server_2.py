import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9999))
sock.listen()
client, client_addr = sock.accept()

res = 0

while True:

    header = client.recv(1)
    if not header:
        break

    msg_len = int.from_bytes(header, byteorder='big')

    fnumb = client.recv(msg_len)

    operation = client.recv(1)
    if operation == b'\x01':
        operation = "+"
    elif operation == b'\x02':
        operation = "-"
    elif operation == b'\x03':
        operation = "*"

    header = client.recv(1)

    msg_len = int.from_bytes(header[0:1], byteorder='big')

    snumb = client.recv(msg_len)

    res = eval(str(int.from_bytes(fnumb, byteorder='big')) + str(operation) + str(int.from_bytes(snumb, byteorder='big')))

    print(res)
    client.send(str(res).encode())
    break

client.close()
sock.close()