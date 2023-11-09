import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("localhost",8080))
firstNum = input(client_socket.recv(256).decode("utf-8"))
client_socket.send(bytes(firstNum,"utf-8"))
print("Result is: ", client_socket.recv(256).decode("utf-8"))