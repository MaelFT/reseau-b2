import socket

host = ''
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))  

s.listen(1)
conn, addr = s.accept()
print(f'Un client vient de se co et son IP c\'est {addr}')

while True:

    try:
        data = conn.recv(1024)

        if not data: break

        match data:
            case 'meo':
                conn.sendall('Meo à toi confrère.')
            case 'waf':
                conn.sendall(b'ptdr t ki')
            case other:
                conn.sendall(b'Mes respects humble humain.')

    except socket.error:
        print("Error Occured.")
        break

conn.close()