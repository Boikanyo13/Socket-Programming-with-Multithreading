from socket import*

#my IP adress 10.196.51.11

serverName = 'localhost' #'10.30.44.57' #'10.196.6.147' 

serverPort = 12520

#IP VERSION 4, 
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

while True:

    sentence = input('Input lowercase sentence: ')

    if sentence == 'close':break
       
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('Received message From Server: '+ modifiedSentence.decode() + "\n")

clientSocket.close()
        






  