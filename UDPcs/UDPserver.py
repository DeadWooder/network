from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

# from socket import * Include socket 
# socket class
# server port variable
# .bind init socket method 
# .recvfrom receive method
# .decode format conversion to cpu binary Method
# .encode format conversion to erb binary Method
# .sendto send message to IP_address