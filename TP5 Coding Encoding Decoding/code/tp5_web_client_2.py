import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8080))

msg = "GET /"

sock.send(msg.encode())

s_data = sock.recv(1024)
print(s_data.decode())

sock.close()