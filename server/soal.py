import random
import math
import sys
import time
j = 0
bankSoal = []

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
	bankSoal.append(soaljoin)
	hasil = eval(soaljoin)
	print hasil
	print 'halo'
	j+=1
for x in bankSoal:
	print x
	time.sleep(4)
sys.exit()

