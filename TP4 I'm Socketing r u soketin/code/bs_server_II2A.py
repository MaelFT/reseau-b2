import socket
import argparse
import logging
import sys

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', handlers=[logging.StreamHandler(sys.stdout)])
# logging.FileHandler("/var/log/bs_server/bs_server.log"), 
host = ''

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", action="store", help="open on a specific port")
args = parser.parse_args()

port = args.port

if (port == None):
    port = 13337
else:
    port = int(port)

if (port < 0 or port > 65535):
    raise ValueError("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")

if (port > 0 and port < 1024):
    raise ValueError("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except Exception as e:
    print("On dirait qu'il y a eu un soucis, déso.")
    print(f"L'erreur native est : {e.message}")

s.listen(1)
conn, addr = s.accept()

logging.info(f'Le serveur tourne sur {host}:{port}')
print(logging.info(f'Le serveur tourne sur {host}:{port}'))
logging.info(f'Un client {addr} s\'est connecté.')

while True:

    try:
        data = conn.recv(1024)

        if not data: break

        logging.info(f'Le client {addr} a envoyé {data}.')

        message = ''

        if (data.decode().__contains__("meo")):
            message = b'Meo a toi confrere.'
        elif (data.decode().__contains__("waf")):
            message = b'ptdr t ki'
        else:
            message = b'Mes respects humble humain.'
        
        logging.info(f'Réponse envoyée au client {addr} : {message}.')
        conn.sendall(message)

    except socket.error:
        print("Error Occured.")
        break

conn.close()