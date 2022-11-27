import socket
from time import sleep
from threading import *
from encryption import decrypt, encrypt

#For now is hardcode later will not be
Server_IP   = '127.0.0.1'
Server_Port =  1234
NickName    = input("Chose your nickname\n -->")


def MsgReciver(client):
    while True:
        #send everthing need to decrypt the message 
        nonce = client.recv(1024)
        ciphertext = client.recv(1024)
        tag = client.recv(1024)
        message = decrypt(nonce,ciphertext,tag)
        print(message)

        
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect((Server_IP, Server_Port))
    #send the id and the nickname
    client.send(NickName.encode('utf-8'))
    id = client.recv(64).decode('utf-8')
    #start a new thread to use recive msg
    th1 = Thread(target=MsgReciver, args=(client, ))
    th1.start()
    while True:
        MSG = str(input())
        #Format message
        FMessage = f"<{NickName} {id}> {MSG}"
        nonce, ciphertext, tag =encrypt(FMessage)
        #the sleep is need to dont bug the program in the server side 
        client.send(nonce)
        sleep(0.05)
        client.send(ciphertext)
        sleep(0.05)
        client.send(tag)
