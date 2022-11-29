#mudar os textos para ing!!
import socket 
from time import sleep
from threading import *
from encryption import decrypt, encrypt

#Acabar a implementação de encriptação 

Host        = '127.0.0.1' #change if you dont want to use localHost
Port        = 1234  
id          = 0
Newid       = 0
clients     = []
id_List     = []
NicksList   = []

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.bind((Host,Port))


def Admin():
    pass



#MsgSender is going encrypt and send the msg for all the clients
def MsgSender(msg):
    nonce, ciphertext, tag = encrypt(msg) 
    print(ciphertext)           
    for conn in clients:
        conn.send(nonce)
        sleep(0.05)
        conn.send(ciphertext)
        sleep(0.05)
        conn.send(tag)
        
def NamesIds(conn):
    #This part is just to give a id to every user
    global id
    global Newid
    Newid = id + 1
    id_List.append(Newid)
    id = id + 1
    conn.send(f"{id}".encode('utf-8'))
    #this is just to recv the nickname of all users connect
    global Names
    name  = conn.recv(4024)
    NicksList.append(name.decode('utf-8'))


def Client_Handler(conn, addr):
    #the client will send his name first and then he can start the chat
    NamesIds(conn)
    print(f"New Client connected from {addr}, recive the id of {Newid}")
    while True:
        #Here the client will send his messages to the server which will then send them to everyone.
        nonce       = conn.recv(1024)
        ciphertext  = conn.recv(1024)
        tag         = conn.recv(1024)
        msg         = decrypt(nonce, ciphertext, tag)
        MsgSender(msg)        
              
def ServerStart():
    ServerSocket.listen(5)
    print("Server is now listening")
    while True:
        conn, addr = ServerSocket.accept()
        clients.append(conn)
        th1 = Thread(target=Client_Handler, args=(conn,addr))
        th1.start()    

ServerStart()
