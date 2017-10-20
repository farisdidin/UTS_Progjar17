from socket import *
from codecs import decode
#from chatrecord import ChatRecord
from threading import Thread
from time import ctime
import time

class ClientHandler(Thread):

    def __init__(self,client,address):
        global sockets
        global addresses
        Thread.__init__(self)
        self._client = client
        self._address = address
        sockets.append(self._client)
        addresses.append(self._address)

    def run(self):
        self._client.send('Welcome to the chatroom!\n')
        time.sleep(10)
        self._client.send('soal selanjutnya')

        while 1:
            message =self._client.recv(BUFSIZE)
            print '\n\n',sockets
            if not message:
                print "Client disconnected."
                addIndex=sockets.index(self._client)
                del sockets[addIndex]
                del addresses[addIndex]
                self._client.close()
                break
            else:
                if 'ONLINE#' in message:
                    for x in sockets:
                        if (x!=self._client):
                            try:
                                x.send(message[7:])
                            except:
                                print 'disconnected'
                                continue
                    print message[7:]
                else:     
                    for x in sockets:
                        try:
                            x.send(message)
                            #/*sockets is the list of all client*/
                        except:
                            print ' '
                            continue
                    print message


HOST = 'localhost'
PORT = 1235
ADDRESS = (HOST,PORT)
BUFSIZE = 1024
server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)
sockets=[]
addresses=[]

while True:
    print "Waiting for connection..."
    client, address = server.accept()
    print('...client connected from: ',address)
    handler = ClientHandler(client,address)
    handler.start()