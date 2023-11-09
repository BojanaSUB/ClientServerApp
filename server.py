import socket
import random

def checkIfGuessed(userInputNumber):
  if random.randint(1, 10) == userInputNumber:
    return "SCORE!"
  else:
    return "MISS..." 
 
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind(("localhost",8080))
server_socket.listen()
client,addr = server_socket.accept()
client.send(b"Enter number from 1 to 10: ")
firstNumber = int(client.recv(32).decode("utf-8"))

res = checkIfGuessed(firstNumber)
client.send(bytes(res,"utf-8"))

    
  