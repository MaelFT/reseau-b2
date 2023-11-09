import socket
import re

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

regexp = re.compile(r'\b(?!meo|waf)')
print(regexp.search(data))
if (regexp.search(data)):
    raise ValueError("Votre message doit contenir 'meo' ou 'waf' !")

if type(data) is not str:
    raise TypeError("Ici on veut que des strings !")

s.sendall(data.encode())

data = s.recv(1024)

s.close()

print(f"Le serveur a répondu {repr(data)}")

exit(0)