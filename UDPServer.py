from socket import *

server_port = 3933
server_socket = socket(AF_INET,SOCK_DGRAM)
server_socket.bind(('',server_port))
print("Server is ready to receive")
while True:
    buf_size = 2048
    message, clientAddress = server_socket.recvfrom(buf_size)
    modified_message = message.decode().upper()
    data = modified_message.encode()
    server_socket.sendto(data,clientAddress)