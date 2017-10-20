from socket import *
from codecs import decode
#from chatrecord import ChatRecord
from threading import Thread
from time import ctime
import time
import random
import math
import sys

class ClientHandler(Thread):

    def __init__(self,client):
        global sockets
        global addresses
        global bankSoal
        global hasilJawaban
        global jawabanDariClient
        Thread.__init__(self)
        self._client = client
        #self._address = address
        # sockets.append(self._client)
        # addresses.append(self._address)

    def run(self):
        self._client.send('QUIZ akan dimulai beberapa saat lagi \n\r')
        # time.sleep(2)
        # self._client.send('soal selanjutnya\n\r')

        
        time.sleep(5)
        for x in bankSoal:
            #soal =( x + '\n\r')
            self._client.send(x)
            jawabanClient = self._client.recv(BUFSIZE).strip('\n')
            jawabanDariClient.append(jawabanClient)
            print jawabanDariClient
            time.sleep(10)


           


HOST = 'localhost'
PORT = 1235
ADDRESS = (HOST,PORT)
BUFSIZE = 1024
server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)
sockets=[]
addresses=[]
bankSoal = []
hasilJawaban = []
jawabanDariClient = []
j = 0
while j < 10:
    jml = random.randint(3,8)
    i =0
    soal = []

    while i < jml:
        num = random.randint(1, 10)
        numstr = str(num)
        opr = ['+', '-', '*', '/']
        operand = random.choice(opr)
        operandstr = str(operand)
        soal.append(numstr)
        soal.append(operandstr)
        i+=1
    num1 = random.randint(1, 10)
    num1str = str(num1)
    soal.append(num1str)
    soaljoin = ' '.join(soal)
    soaljoinfix = soaljoin+'\n'
    print soaljoinfix
    bankSoal.append(soaljoinfix)
    hasil = eval(soaljoin)
    hasilJawaban.append(hasil)
    
#     print hasil
#     print 'halo'
    j+=1
# for x in bankSoal:
#     print x
#     time.sleep(4)
# sys.exit()


while True:
    print "Waiting for connection..."
    client, address = server.accept()
    sockets.append(client)
    print('...client connected from: ',address)
    peserta = len(sockets)
    if peserta >= 3:
        for client in sockets:
            handler = ClientHandler(client)
            handler.start()
    print sockets
    print addresses
    print jawabanDariClient