from email import header
from socket import *
serverName = '192.168.1.101'
serverPort = 6789
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
header = 'GET /hello.html HTTP/1.1\r\nHost: ' + serverName + '\r\n\r\n'
clientSocket.send(header.encode())
data = 1
while data:
    data = clientSocket.recv(1024)
    print(data.decode(), end='')
clientSocket.close()