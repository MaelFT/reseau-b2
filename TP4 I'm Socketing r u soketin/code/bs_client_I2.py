import socket

host = '10.33.76.214'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
except Exception as e:
    print("On dirait qu'il y a eu un soucis, déso.")
    print(f"L'erreur native est : {e.message}")

print(f"Connecté avec succès au serveur {host} sur le port {port}")

data = input("Que veux-tu envoyer au serveur : ")

s.sendall(data.encode())

data = s.recv(1024)

s.close()

print(f"Le serveur a répondu {repr(data)}")

exit(0)