import socket   
from Configuration import *     

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       
clientSocket.connect((ServerIp, Serverport))
letter = input("Enter Character :") 
clientSocket.sendall(letter.encode()) 
if(letter == '0'):
    clientSocket.close()
else:
    print (clientSocket.recv(1024).decode(),"\n") 

         