from sys import argv
import socket
import os
import psutil

def network():
    if(len(argv) < 2):
        return "Veuillez rajouter des arguments"
    match argv[1]:
        case "lookup":
            return lookup()
        case "ping":
            return ping()
        case "ip":
            return ip()
    return f"'{argv[1]}' is not an available command. Déso."
    
def lookup():
    if (len(argv) < 3):
        return "Veuillez ajouter un nom de domaine"
    if (len(argv) > 3):
        return "Trop d'arguments..."
    return socket.gethostbyname(argv[2])

def ping():
    if (len(argv) < 3):
        return "Veuillez ajouter une adresse ip en argument"
    if (len(argv) > 3):
        return "Trop d'arguments..."
    if (os.system(f"ping {argv[2]} > nul") == 0):
        return "UP !"
    else:
        return "DOWN !"

def ip():
    return psutil.net_if_addrs()['Wi-Fi'][1][1]

print(network())