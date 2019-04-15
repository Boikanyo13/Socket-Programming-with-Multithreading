from socket import*
from _thread import*
import threading

class myThread (threading.Thread):
    def __init__(self,clientAdress):
        threading.Thread.__init__(self)
        #self.threadID = threadID
        self.clientAdress = clientAdress   
    def run(self):
        print("Starting connection..... " + "ID")
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAdress)
        print("Closing connection ....." + "ID" + "\n")

serverPort = 12050

serverSocket = socket(AF_INET, SOCK_DGRAM)

#Assigns port number to the server socket
serverSocket.bind(('', serverPort))

threads = []

print("The server is ready to receive")

while True:
	
    (message, clientAdress) = serverSocket.recvfrom(2048)	
	
    newthread =  myThread(clientAdress) 
    newthread.start() 
    threads.append(newthread)

