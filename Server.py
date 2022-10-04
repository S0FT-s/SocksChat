#mudar os textos para ing!!
import socket 
from threading import *


Host = '127.0.0.1'
Port = 1234
Clients_names = []
id = 0
id_List = []


ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.bind((Host,Port))

def Client_Handler(conn, addr):
    #o client vai mandar o seu nome primeiro e depois sim pode começar o chat
    name = conn.recv(64)
    Clients_names.append(name.decode('utf-8'))
    ClientsNamesNOBracelets = str(Clients_names)[1:-1]
    #mudar nome da variavel para ing
    ClientsNamesNoAspas = ClientsNamesNOBracelets.strip("'")        
    print(f"New Client connected from {addr} chose the name {name.decode('utf-8')}")
    while True:
        #Aqui o client vai mandar as suas msg para o server que depois o mesmo vai enviar para todos.
        msg = conn.recv(1024)
        msg_Decode = msg.decode('utf-8')
        conn.send(f'<{ClientsNamesNoAspas}> {msg_Decode}'.encode('utf-8'))
        print(f'<{ClientsNamesNoAspas}> {msg_Decode}')
        
        
def ServerStart():
    ServerSocket.listen(5)
    print("Server is now listening")
    conn, addr = ServerSocket.accept()
    th1 = Thread(target=Client_Handler, args=(conn,addr))
    th1.start()
    
ServerStart()