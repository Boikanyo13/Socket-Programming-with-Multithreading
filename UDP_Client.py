from socket import*

serverName = 'localhost'  #IP Adress
serverPort = 12050

# MY IP ADRESS 10.30.40.117
#10.196.51.24
#Create the client socket


clientSocket = socket(AF_INET, SOCK_DGRAM)  #SOCK_DGRAM---> UPD

while True:

    message = input('Input a lowercase sentence: ')

    if message == 'close':break

    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("Modified message from Server: " + modifiedMessage.decode()+"\n")

clientSocket.close()
