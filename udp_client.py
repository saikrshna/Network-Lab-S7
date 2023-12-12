#SAI KRISHNA
#20220083
#UDP (CLIENT)

import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('127.0.0.1', 12345)

while True:
    message = input("Enter a message to send to the server (or type 'exit' to quit): ")
    
    # Send the message to the server
    client_socket.sendto(message.encode(), server_address)
    
    if message.lower() == 'exit':
        break

# Close the client socket
client_socket.close()

#OUTPUT
#Enter a message to send to the server (or type 'exit' to quit): hello

