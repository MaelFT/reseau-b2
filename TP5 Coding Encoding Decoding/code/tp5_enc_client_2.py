import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9999))

msg = input('Calcul à envoyer: ')

msg_split = msg.split(" ")

operation = msg_split[1]

if operation == "+":
    operation = 1
elif operation == "-":
    operation = 2
elif operation == "*":
    operation = 3

operation_bytes = operation.to_bytes(1, byteorder='big')

f_numb = int(msg_split[0])

f_numb_bytes = f_numb.to_bytes(1, byteorder='big')

s_numb = int(msg_split[2])

s_numb_bytes = s_numb.to_bytes(1, byteorder='big')

encoded_msg = msg.encode('utf-8')

msg_len = 1

header = msg_len.to_bytes(1, byteorder='big')

payload = header + f_numb_bytes + operation_bytes + header + s_numb_bytes

sock.send(payload)

s_data = sock.recv(4)
print(s_data.decode())

sock.close()