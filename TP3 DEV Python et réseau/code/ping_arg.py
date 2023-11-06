import os
from sys import argv

def ping_arp():
    if (len(argv) < 2):
        print("Veuillez ajouter une adresse ip en argument")
        exit()
    if (len(argv) > 2):
        print("Trop d'arguments...")
        exit()
    return os.system(f"ping {argv[1]}")

ping_arp()

