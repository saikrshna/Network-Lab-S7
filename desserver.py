"""
DES SERVER
SAI KRISHNA
20220083
"""

import socket
from Crypto.Cipher import DES
import binascii

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt(plaintext, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.encrypt(plaintext)

def main():
    host = '127.0.0.1'  # Localhost
    port = 12345        # Choose any port that is free

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Listening for client at {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    key = b'8bytekey'  # DES key must be 8 bytes
    plaintext = 'Hello from DES Server!'
    padded_plaintext = pad(plaintext).encode('utf-8')

    encrypted_msg = encrypt(padded_plaintext, key)
    conn.send(binascii.hexlify(encrypted_msg))
    conn.close()

if __name__ == '__main__':
    main()

"""
Listening for client at 127.0.0.1:12345
Connection from ('127.0.0.1', 50818)
"""
