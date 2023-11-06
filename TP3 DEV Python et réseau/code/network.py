from sys import argv
import socket
import os
import psutil

def network():
    if(len(argv) < 2):
        print("Veuillez rajouter des arguments")
        exit()
    if(argv[1] == "lookup"):
        return lookup()
    if(argv[1] == "ping"):
        return ping()
    if(argv[1] == "ip"):
        return ip()
    else:
        return f"'{argv[1]}' is not an available command. Déso."
    
def lookup():
    if (len(argv) < 3):
        print("Veuillez ajouter un nom de domaine")
        exit()
    if (len(argv) > 3):
        print("Trop d'arguments...")
        exit()
    return socket.gethostbyname(argv[2])

def ping():
    if (len(argv) < 3):
        print("Veuillez ajouter une adresse ip en argument")
        exit()
    if (len(argv) > 3):
        print("Trop d'arguments...")
        exit()
    if (os.system(f"ping {argv[2]} > nul") == 0):
        return "UP !"
    else:
        return "DOWN !"

def ip():
    return psutil.net_if_addrs()['Wi-Fi'][1][1]

print(network())