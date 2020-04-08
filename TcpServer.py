from socket import *

server_port = 3933
server_socket = socket(AF_INET,SOCK_STREAM)

server_socket.bind(('',server_port))
server_socket.listen(1)
print("Server is ready to receive")
while True:
    buf_size = 1024
    connection_socket,addres=  server_socket.accept()
    message= server_socket.recv(buf_size)
    modified_message = message.decode().upper()
    data = modified_message.encode()
    server_socket.sendto(data)
    connection_socket.close()