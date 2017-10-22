from socket import *
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
        self._score = []
        self._jawaban = []
        self._client = client
        
    def run(self):
        self._client.send('QUIZ akan dimulai beberapa saat lagi \n\r')
        

        
        time.sleep(5)
        for x in bankSoal:
            self._client.send(x)
            jawabanClient = self._client.recv(BUFSIZE).strip('\n')
            self._jawaban.append(int (jawabanClient))

            time.sleep(5)
        
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
while j < 2:
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
    
    j+=1


while True:
    print "Waiting for connection..."
    client, address = server.accept()
    sockets.append(client)
    print('...client connected from: ',address,'with id : ', address[1])
    peserta = len(sockets)
    if peserta >= 1:
        for client in sockets:
            handler = ClientHandler(client)
            handler.start()
    