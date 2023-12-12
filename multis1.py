#SAIKRISHNA
#20220083
#MULTICHAT SERVER

import threading
import socket

host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = {}
aliases = {}

def broadcast(message):
    for client_socket in clients:
        client_socket.send(message)

def handle_client(client_socket):
    alias = aliases[client_socket]
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                if message.startswith('@'):
                    recipient_alias, message_content = message.split(' ', 1)
                    recipient_socket = None
                    
                    # Make the recipient lookup case-insensitive
                    recipient_alias = recipient_alias[1:].lower()
                    
                    for socket, username in aliases.items():
                        if username.lower() == recipient_alias:
                            recipient_socket = socket
                            break
                    
                    if recipient_socket:
                        recipient_socket.send(f'{alias} (private): {message_content}'.encode('utf-8'))
                    else:
                        client_socket.send(f"User '@{recipient_alias}' not found or offline.".encode('utf-8'))
                else:
                    broadcast(f'{alias}: {message}'.encode('utf-8'))
        except:
            alias = aliases[client_socket]
            del aliases[client_socket]
            clients.pop(client_socket)
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            break

def receive():
    while True:
        print('Server is running and listening ...')
        client_socket, address = server.accept()
        print(f'Connection is established with {str(address)}')
        client_socket.send('alias?'.encode('utf-8'))
        alias = client_socket.recv(1024).decode('utf-8')
        aliases[client_socket] = alias
        clients[client_socket] = True
        print(f'The alias of this client is {alias}')
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client_socket.send('You are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    receive()

'''
OUTPUT:

Server is running and listening ...
Connection is established with ('127.0.0.1', 57804)
The alias of this client is user1
Server is running and listening ...
Connection is established with ('127.0.0.1', 52012)
The alias of this client is user2
Server is running and listening ...
Connection is established with ('127.0.0.1', 44778)
The alias of this client is user3
Server is running and listening ...




'''

