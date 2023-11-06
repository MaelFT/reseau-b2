import os

def ping_simple():
    return os.system("ping 8.8.8.8")

ping_simple()