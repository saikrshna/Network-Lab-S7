#SAI KRISHNA
#20220083
#Hamming(server)

import socket

def generate_hamming_code(message):
    r = 1
    while 2**r < len(message) + r + 1:
        r += 1

    hamming_code = [0] * (len(message) + r + 1)

    for i, bit in enumerate(message, 1):
        hamming_code[i] = int(bit)

    for i in range(r):
        position = 2**i
        hamming_code[position] = calculate_parity(hamming_code, position)

    return hamming_code

def calculate_parity(data, position):
    parity = 0
    for i in range(1, len(data)):Enter the number: 1011010
Received Hamming Code: 
No errors detected.

        if (i & position) == position and i != position:
            parity ^= data[i]

    return parity

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("Server listening on", server_address)

    client_socket, client_address = server_socket.accept()
    print("Connection from", client_address)

    message = client_socket.recv(1024).decode()
    hamming_result = generate_hamming_code(message)
    print("Original Message:", message)
    print("Hamming Code:", "".join(map(str, hamming_result[1:])))

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()

#output
#Server listening on ('127.0.0.1', 12345)
#Connection from ('127.0.0.1', 57816)
#Original Message: 1011010
#Hamming Code: 101010100000

