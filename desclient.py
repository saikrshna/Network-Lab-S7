"""
DES CLIENT
SAI KRISHNA
20220083
"""

import socket
from Crypto.Cipher import DES
import binascii

def decrypt(ciphertext, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.decrypt(ciphertext)

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    encrypted_msg = client_socket.recv(1024)
    print(f"Encrypted message from server: {encrypted_msg}")

    key = b'8bytekey'
    decrypted_msg = decrypt(binascii.unhexlify(encrypted_msg), key)
    print(f"Decrypted message: {decrypted_msg.decode().strip()}")

    client_socket.close()

if __name__ == '__main__':
    main()

"""
Encrypted message from server: b'5a85421d2c655612ae4b429d6f901f96bae8b1458bf312b3'
Decrypted message: Hello from DES Server!
"""
