import socket

host = '10.33.76.212'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.sendall(b"Meooooo !")

data = s.recv(1024)

s.close()

print(f"Le serveur a répondu {repr(data)}")

exit(0)