from socket import*
from _thread import*
import threading

class myThread (threading.Thread):
    def __init__(self,ip, port):
        threading.Thread.__init__(self)
        #self.threadID = threadID
        self.ip = ip
        self.port = port
    
    def run(self):
        print("Starting connection..... " + "ID" )
        
        while True:
        
            sentence = connectionSocket.recv(1024).decode()
            if sentence == 'close': break
       
            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence.encode())

        print("Closing connection ....." + "ID" )


serverPort = 12555
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

threads = []

print('The server is ready to receive')

while True:
    serverSocket.listen(5)
    
    (connectionSocket, (ip,port)) = serverSocket.accept() 
    

    newthread =  myThread(ip, port) 
    newthread.start() 
    threads.append(newthread)
    #connectionSocket.close()

for t in threads:
    t.join()
