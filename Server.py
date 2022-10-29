#mudar os textos para ing!!
import socket 
from threading import *

Host        = '127.0.0.1'
Port        = 1234
id          = 0
Newid       = 0
clients     = []
id_List     = []
NicksList   = []


ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.bind((Host,Port))

#MsgSender is going to send the msg for all the clients
def MsgSender(msg):
    for conn in clients:
        conn.send(msg)

def NamesIds(conn):
    #id Part
    global id
    global Newid
    Newid = id + 1
    id_List.append(Newid)
    id = id + 1
    conn.send(f"{id}".encode('utf-8'))
    #Name Part
    global Names
    name  = conn.recv(1024)
    NicksList.append(name.decode('utf-8'))


def Client_Handler(conn, addr):
    #o client vai mandar o seu nome primeiro e depois sim pode começar o chat
    NamesIds(conn)
    print(f"New Client connected from {addr}, recive the id of {Newid}")
    while True:
        #Aqui o client vai mandar as suas msg para o server que depois o mesmo vai enviar para todos.
        msg = conn.recv(1024)
        msg_Decode = msg.decode('utf-8')
        print(f"{msg_Decode}")
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
