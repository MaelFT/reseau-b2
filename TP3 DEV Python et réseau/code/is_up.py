from sys import argv
import os

def is_up():
    if (len(argv) < 2):
        print("Veuillez ajouter une adresse ip en argument")
        exit()
    if (len(argv) > 2):
        print("Trop d'arguments...")
        exit()
    if (os.system(f"ping {argv[1]} > nul") == 0):
        print("UP !")
    else:
        print("DOWN !")

is_up()