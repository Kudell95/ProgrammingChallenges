import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 6666
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

s.listen(1)


conn, addr = s.accept() #set connection and address to the incoming connection

print('connection address: ', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("recieved data: ", data.decode())
    conn.send(data) #echo
conn.close()