#SAI KRISHNA
#20220083
#UDP (SERVER)

import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('127.0.0.1', 12345)

# Bind the socket to the server address and port
server_socket.bind(server_address)

print("UDP server is listening on {}:{}".format(*server_address))

while True:
    # Receive data and the client's address
    data, client_address = server_socket.recvfrom(1024)
    print("Received message from {}:{}".format(*client_address))
    
    # Display the received message
    print("Message from client:", data.decode())

#OUTPUT
#UDP server is listening on 127.0.0.1:12345
#Received message from 127.0.0.1:50666
#Message from client: hello


