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

    def __init__(self,client,address):
        global sockets
        global addresses
        global bankSoal
        global hasilJawaban
        Thread.__init__(self)
        self._client = client
        self._address = address
        sockets.append(self._client)
        addresses.append(self._address)

    def run(self):
        self._client.send('Welcome to the chatroom!\n\r')
        # time.sleep(2)
        # self._client.send('soal selanjutnya\n\r')

        while 1:
            for x in bankSoal:
                #soal =( x + '\n\r')
                self._client.send(x)
                time.sleep(4)

           


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
j = 0
while j < 10:
    ops = ['+', '-', '*', '/']
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
    print sockets
    print addresses
    client, address = server.accept()
    print('...client connected from: ',address)
    handler = ClientHandler(client,address)
    handler.start()