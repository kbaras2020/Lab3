from datetime import datetime
import socket

# HOST = 'localhost'
#HOST = '0.0.0.0'
HOST = socket.gethostbyname('tcp_server')
PORT = 6789
max_size = 2048

print('Starting the server at', datetime.now().replace(microsecond=0))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind((HOST, PORT))
except socket.error as e:
    print(str(e))

server.listen()
print('Waiting for a connection.')

while True:
    client, address = server.accept()
    print('Connected to ' + address[0] + ':' + str(address[1]))
    data = client.recv(max_size)
    print('Client said: ' + data.decode())

    reply = str(client.getsockname()) + ': Hey client!'
    client.sendall(str.encode(reply))
    client.close()


