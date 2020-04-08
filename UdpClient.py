from socket import *

server_name  = '127.0.0.1'
server_port = 3933
client_socket = socket(AF_INET,SOCK_DGRAM)
message = input('Input:')
data = message.encode()
address = (server_name,server_port)
client_socket.sendto(data,address)
modified_message, server_address = client_socket.recvfrom(2048)
print(modified_message.decode())
client_socket.close()

