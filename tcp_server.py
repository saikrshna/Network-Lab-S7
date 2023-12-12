#SAI KRISHNA
#20220083
#CLIENT-SERVER (SERVER) tcp

import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's IP address and port
server_ip = "127.0.0.1"  # Use "127.0.0.1" for localhost
server_port = 12345

# Bind the socket to the address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections (max queue size is 5)
server_socket.listen(5)

print(f"Server listening on {server_ip}:{server_port}")

# Accept a client connection
client_socket, client_address = server_socket.accept()

print(f"Accepted connection from {client_address}")

data_from_client2 = client_socket.recv(1024).decode()
print(f"Received from client: {data_from_client2}")


# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()

#OUTPUT
#Server listening on 127.0.0.1:12345
#Accepted connection from ('127.0.0.1', 38562)
#Received from client: hello


