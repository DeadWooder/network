from socket import *
serverName = '192.168.1.101'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, ServerAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
