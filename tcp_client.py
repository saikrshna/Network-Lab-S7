#SAIKRISHNA
#20220083

#CLIENT-SERVER (CLIENT)tcp

import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = "127.0.0.1" 
server_port = 12345

# Connect to the server
client_socket.connect((server_ip, server_port))

message_to_server2=input("enter data to send to server: ")
client_socket.send(message_to_server2.encode())

# Close the client socket
client_socket.close()

#OUTPUT
#enter data to send to server: hello 
