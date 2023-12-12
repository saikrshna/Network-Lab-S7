#SAI KRISHNA
#20220083
#LZW (CLIENT)

import socket
import pickle

def lzw_compress(data):
    dictionary = {chr(i): i for i in range(256)}
    result = []
    current_code = 256
    current_sequence = ""

    for char in data:
        current_sequence += char
        if current_sequence not in dictionary:
            result.append(dictionary[current_sequence[:-1]])
            dictionary[current_sequence] = current_code
            current_code += 1
            current_sequence = char

    if current_sequence in dictionary:
        result.append(dictionary[current_sequence])
        
    print("Dictionary:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

	
    return result

def handle_client(client_socket):
    data = client_socket.recv(1024).decode()
    print("Received Data:", data)

    compressed_data = lzw_compress(data)
    compressed_data_pickle = pickle.dumps(compressed_data)

    client_socket.send(compressed_data_pickle)
    print("Compressed Data Sent to Client")

    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(1)
    print("Server listening on port 12345")

    while True:
        client_socket, client_address = server.accept()
        print("Accepted connection from:", client_address)
        handle_client(client_socket)

if __name__ == "__main__":
    main()

#OUTPUT
#Server listening on port 12345
#Accepted connection from: ('127.0.0.1', 45652)
#Received Data: ABBABA
#Dictionary:
#AB: 256
#BB: 257
#BA: 258
#ABA: 259
#Compressed Data Sent to Client

