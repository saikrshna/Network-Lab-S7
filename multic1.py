#SAIKRISHNA
#20220083
#MULTICHAT CLIENT

import threading
import socket

alias = input('Choose a username >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)Choose a username >>> user1
user1 has connected to the chat room
You are now connected!
user2 has connected to the chat room
user3 has connected to the chat room
hai hello i am user1
user1: hai hello i am user1
user2: hai i am user2
user3: hai i am user 3
user3 (private): hai user1

        except:
            print('Error!')
            client.close()
            break

def client_send():
    while True:
        message = input("")
        if message.startswith("@"):
            recipient_alias, message_content = message.split(" ", 1)
            private_message = f'{recipient_alias} {message_content}' 
            client.send(private_message.encode('utf-8'))
        else:
            client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()



'''
OUTPUT

USER1:

Choose a username >>> user1
user1 has connected to the chat room
You are now connected!
user2 has connected to the chat room
user3 has connected to the chat room
hai hello i am user1
user1: hai hello i am user1
user2: hai i am user2
user3: hai i am user 3
user3 (private): hai user1


USER2:

Choose a username >>> user2
user2 has connected to the chat room
You are now connected!
user3 has connected to the chat room
user1: hai hello i am user1
hai i am user2
user2: hai i am user2

USER 3:

Choose a username >>> user3
user3 has connected to the chat room
You are now connected!
user1: hai hello i am user1
user2: hai i am user2
hai i am user 3
user3: hai i am user 3
@user1 hai user1
user2 (private): hai i am user2
user3: hai i am user 3
@user3 hai i am user2



'''
