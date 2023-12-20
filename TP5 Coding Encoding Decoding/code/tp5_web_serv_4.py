import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.listen()
client, client_addr = sock.accept()

while True:

    data = client.recv(1024)
    if not data:
        break

    msg = data.decode()

    if msg[0:5] == "GET /":
        nspace = msg[5:].find(" ") + 5
        file = open(msg[5:nspace])
        html_content = file.read()
        file.close()

        print("LOGS: Demande d'accès au fichier `" + msg[5:nspace] + "` de la part de " + str(client_addr))

        http_response = 'HTTP/1.0 200 OK\n\n' + html_content
        client.send(http_response.encode())

client.close()
sock.close()