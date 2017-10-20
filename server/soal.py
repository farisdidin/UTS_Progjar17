import random
import math

ops = ['+', '-', '*', '/']
jml = random.randint(3,8)
i =0
soal = []

while i < jml:
	num = random.randint(0, 10)
	numstr = str(num)
	opr = ['+', '-', '*', '/']
	operand = random.choice(opr)
	operandstr = str(operand)
	soal.append(numstr)
	soal.append(operandstr)
	i+=1
num1 = random.randint(0, 10)
num1str = str(num1)
soal.append(num1str)
soaljoin = ' '.join(soal)
print soaljoin
hasil = eval(soaljoin)
print hasil
print 'halo'