import socket
from threading import *

#For now is hardcode later will not be
Server_IP   = '127.0.0.1'
Server_Port =  1234
NickName    = input("Chose your nickname\n -->")


def MsgReciver(client):
    while True:
        recive_msg = client.recv(1024).decode('utf-8')
        print(recive_msg)
    

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect((Server_IP, Server_Port))
    client.send(NickName.encode('utf-8'))
    id = client.recv(64).decode('utf-8')
    th1 = Thread(target=MsgReciver, args=(client, ))
    th1.start()
    while True:
        MSG = str(input())
        client.send(f"<{NickName} {id}> {MSG}".encode("utf-8"))
            
