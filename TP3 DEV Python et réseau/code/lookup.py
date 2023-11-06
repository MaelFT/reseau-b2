import socket
from sys import argv

def lookup():
    if (len(argv) < 2):
        print("Veuillez ajouter un nom de domaine")
        exit()
    if (len(argv) > 2):
        print("Trop d'arguments...")
        exit()
    print(socket.gethostbyname(argv[1]))

lookup()