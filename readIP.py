#!/usr/bin/env python3
print ("test script read IP")
filename='31885 Ip.txt'

print(filename)
import numpy
Ipdata=open(filename)
commit=Ipdata.readline()
print(commit)
data=Ipdata.readlines()
print(data[0][0],data[0][1])
num=len(data)
print(data[num-1][0],data[num-1][1])
print(num)
Ip=numpy.zeros((num,2))

index=0
for line in data:
	line=line.strip()
	linelist=line.split()
	Ip[index,:]=linelist[0:2]
	index +=1
print(Ip)


fileout='X31885.CUR'
fo=open(fileout,'w')
print('31885HL2A 1 0 6 \t\t;',file=fo)
print('05/05/17 \t\t;',file=fo)
print('TIME \t SEC \t\t;',file=fo)
print('Ip \t A \t\t;',file=fo)
print('0 \t\t;',file=fo)
print(num,' \t\t;',file=fo)

ti=0
for i in range(0,num):
	print('%E'% (Ip[i,0]*0.001),file=fo,end = ' ')
	ti=ti+1
	if(ti==6):
		print('',file=fo)
		ti=0

print('',file=fo)

ti=0
for i in range(0,num):
        print('%E'% (Ip[i,1]*0.001),file=fo,end = ' ')
        ti=ti+1
        if(ti==6):
                print('',file=fo)
                ti=0
