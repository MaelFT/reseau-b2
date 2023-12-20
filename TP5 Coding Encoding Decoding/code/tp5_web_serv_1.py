import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.listen()
client, client_addr = sock.accept()

while True:

    data = client.recv(5)
    if not data:
        break

    msg = data.decode()

    if msg == "GET /":
        client.send(b'HTTP/1.0 200 OK\n\n<h1>Hello je suis un serveur HTTP</h1>')

client.close()
sock.close()