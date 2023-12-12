#SAI KRISHNA
#20220083
#Hamming(Client)

import socket

def validate_hamming_code(received_code):
    position = 1
    while position < len(received_code):
        parity = calculate_parity(received_code, position)
        if parity != received_code[position]:
            print("Error detected at position", position)
            return False
        position *= 2

    print("No errors detected.")
    return True

def calculate_parity(data, position):
    parity = 0
    for i in range(1, len(data)):
        if (i & position) == position and i != position:
            parity ^= data[i]

    return parity

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)
    client_socket.connect(server_address)

    message = input("Enter the number: ")
    client_socket.sendall(message.encode())

    received_code = client_socket.recv(1024).decode()
    print("Received Hamming Code:", received_code)

    validate_hamming_code(received_code)

    client_socket.close()

if __name__ == "__main__":
    main()


#output
#Enter the number: 1011010
#Received Hamming Code: 10101010000
#No errors detected.

