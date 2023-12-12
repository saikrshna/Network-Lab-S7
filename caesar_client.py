'''
SAI KRISHNA
20220083
CAESAR_CLIENT
'''


import socket

original_text = input("Enter the original text: ")

server_host = '127.0.0.1'
server_port = 12346

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_host, server_port))

client_socket.send(original_text.encode())

result = client_socket.recv(1024).decode()
print(f"Received Result from Server:\n{result}")

client_socket.close()

'''
OUTPUT

Enter the original text: SAIKRISHNA
Received Result from Server:
Encrypted Text: VDLNULVKQD
Decrypted Text: SAIKRISHNA

'''
