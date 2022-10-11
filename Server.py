#mudar os textos para ing!!
import socket 
from threading import *

Host = '127.0.0.1'
Port = 1234
id = 0
id_List = []


ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.bind((Host,Port))




def Client_Handler(conn, addr):
    #o client vai mandar o seu nome primeiro e depois sim pode começar o chat
    global id
    Newid = id + 1
    id_List.append(Newid)
    id = id + 1
    print(id)
    print(f"New Client connected from {addr}, recive the id of {Newid}")
    print(id_List)
    while True:
        #Aqui o client vai mandar as suas msg para o server que depois o mesmo vai enviar para todos.
        msg = conn.recv(1024)
        conn.send(msg)
        msg_Decode = msg.decode('utf-8')
        print(f"{msg_Decode}")
        
        
def ServerStart():
    ServerSocket.listen(5)
    print("Server is now listening")
    while True:
        conn, addr = ServerSocket.accept()
        th1 = Thread(target=Client_Handler, args=(conn,addr))
        th1.start()    

ServerStart()
