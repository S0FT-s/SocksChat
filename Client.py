import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    #For now is hardcode later will not be
    Server_IP   = '127.0.0.1'
    Server_Port =  1234
    NickName    = input("Chose your nickname")