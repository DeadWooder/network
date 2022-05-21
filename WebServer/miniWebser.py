from socket import *
import sys

serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True: 
    print('The server is ready to receive')
    connectionSocket, addr = serverSocket.accept()
    try: 
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdate = f.read()
        f.close()
        #send one HTTP header line into socket
        header = 'HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type: text/html\r\n'\
            'Content-Length: %d\r\n\r\n' % (len(outputdate))
        connectionSocket.send(header.encode())

        #send the content of the requested file to the client
        for i in range(0, len(outputdate)):
            connectionSocket.send(outputdate[i].encode())
        connectionSocket.close()
    except IOError:
        #send response message for file not found
        outputdate = 'HTTP/1.1 404 Not found\r\n\r\n'
        connectionSocket.send(outputdate.encode())
        #close client socket
        connectionSocket.close() 
#Terminate the program after sending the corresponding data
