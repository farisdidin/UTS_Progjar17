from socket import *
from threading import Thread
from time import ctime
import time
import random
import math
import sys
import operator
import logging
logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s)%(message)s',)

class ClientHandler(Thread):

    def __init__(self,client,number):
        global bankSoal
        global hasilJawaban
        global finalScore
        Thread.__init__(self)
        self._jawaban = []
        self._client = client
        self._number = number
        
    def run(self):
        logging.debug('running')
        nomorId = ('Selamat Datang di Quiz\nKamu mendapatkan ID '+str(self._number)+'\n\r')
        #deskself._client.send('QUIZ akan dimulai beberapa saat lagi \n\r')
        self._client.send(nomorId)

        
        time.sleep(5)
        for x in bankSoal:
            self._client.send(x)
            time.sleep(5)
            jawabanClient = self._client.recv(BUFSIZE).strip('\n')
            self._jawaban.append(int (jawabanClient))

        
        print self._jawaban
        print hasilJawaban
        # print self._nilaiClient 
        x = 0
        nilai = 0
        while x < len(bankSoal):
            if self._jawaban[x] == hasilJawaban[x]:
                nilai += 5
            else:
                nilai += 0
            x+=1
        print nilai
        finalScore[self._number] = nilai
        #self._client.close()
        logging.debug('Over')


           


HOST = 'localhost'
PORT = 1235
ADDRESS = (HOST,PORT)
BUFSIZE = 1024
server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDRESS)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.listen(5)
sockets=[]
idPort = []
bankSoal = []
hasilJawaban = []
finalScore = {
    
}


j = 0
while j < 1:
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
    bankSoal.append(soaljoinfix)
    hasil = eval(soaljoin)
    hasilJawaban.append(hasil)
    print bankSoal
    print hasilJawaban
    j+=1


while True:
    print "Waiting for connection..."
    client, address = server.accept()
    sockets.append(client)
    idPort.append(address[1])
    print('...client connected from: ',address,'with id : ', address[1])
    peserta = len(sockets)
    if peserta >= 3:
        handlers = []
        for client,number in zip(sockets,idPort):
            handler = ClientHandler(client,number)
            handlers.append(handler)
            handler.daemon = True
            handler.start()
            #handler.join()
            #time.sleep(0.5)
            print 'OPO'

        for x in handlers:
            x.join()

    
    print finalScore
    sortedScore = sorted(finalScore.values())
    print sortedScore