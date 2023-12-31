import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9999))

# on récup une string saisie par l'utilisateur
msg = input('Calcul à envoyer: ')

# on encode le message explicitement en UTF-8 pour récup un tableau de bytes
encoded_msg = msg.encode('utf-8')

# on calcule sa taille, en nombre d'octets
msg_len = len(encoded_msg)

# on encode ce nombre d'octets sur une taille fixe de 4 octets
header = msg_len.to_bytes(4, byteorder='big')

print(int(msg[0]).to_bytes(4, byteorder='big'))

# on peut concaténer ce header avec le message, avant d'envoyer sur le réseau
payload = header + encoded_msg

# on peut envoyer ça sur le réseau
sock.send(payload)

s_data = sock.recv(4)
print(s_data.decode())

sock.close()
