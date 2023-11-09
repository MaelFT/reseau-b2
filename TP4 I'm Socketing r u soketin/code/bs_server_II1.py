import socket
import argparse

host = ''
port = 13337

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", action="store", help="open on an specific port")
args = parser.parse_args()

port = args.port

if (port < 0 or port > 65535):
    raise ValueError("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")

if (port > 0 and port > 1024):
    raise ValueError("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except Exception as e:
    print("On dirait qu'il y a eu un soucis, déso.")
    print(f"L'erreur native est : {e.message}")

s.listen(1)
conn, addr = s.accept()
print(f'Un client vient de se co et son IP c\'est {addr}')

while True:

    try:
        data = conn.recv(1024)

        if not data: break

        if (data.decode().__contains__("meo")):
            conn.sendall(b'Meo a toi confrere.')
        elif (data.decode().__contains__("waf")):
            conn.sendall(b'ptdr t ki')
        else:
            conn.sendall(b'Mes respects humble humain.')

    except socket.error:
        print("Error Occured.")
        break

conn.close()