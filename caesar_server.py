'''
SAI KRISHNA
20220083
CAESAR_SERVER
'''


import socket

def caesar_cipher(text, shift):
    result = ""
   
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
   
    return result

server_host = '127.0.0.1'
server_port = 12346

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_host, server_port))

server_socket.listen()

print(f"Server listening on {server_host}:{server_port}")

client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

original_text = client_socket.recv(1024).decode()
print(f"Received Original Text from Client: {original_text}")

shift = 3

encrypted_text = caesar_cipher(original_text, shift)

decrypted_text = original_text
client_socket.send(f"Encrypted Text: {encrypted_text}\nDecrypted Text: {decrypted_text}".encode())

client_socket.close()
server_socket.close()


'''
OUTPUT

Server listening on 127.0.0.1:12346
Accepted connection from ('127.0.0.1', 36950)
Received Original Text from Client: SAIKRISHNA

'''

