

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 6666
BUFFER_SIZE = 1024
Message = "hello, world"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initialise the socket
s.connect((TCP_IP,TCP_PORT))    #connect to the socket


s.send(Message.encode())
data = s.recv(BUFFER_SIZE)
s.close()

print("recieved data - ", data.decode())