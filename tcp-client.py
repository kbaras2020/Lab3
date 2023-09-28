import socket
from datetime import datetime

#HOST = '0.0.0.0'
HOST = socket.gethostbyname('tcp_server')
PORT = 6789

address = ((HOST, PORT))
max_size = 2048

print('Starting the client at', datetime.now())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(str.encode('Hey, server!'))

data = client.recv(max_size)

print(data.decode())
client.close()