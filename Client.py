import socket

#For now is hardcode later will not be
Server_IP   = '127.0.0.1'
Server_Port =  1234
NickName    = input("Chose your nickname")

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect((Server_IP, Server_Port))
    while True:
        MSG = str(input())
        client.send(f"<{NickName}> {MSG}".encode("utf-8"))
        client.recv(1024)
