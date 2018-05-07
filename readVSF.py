#!/usr/bin/env python3
print ("test script read IP")
filename='31885Vl.txt'

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

from write_ufile import *
write_1Dufile('test.VSF','31885HL2A1 0 6','05/05/17','surface volts','volts',Ip[:,0]*0.001,Ip[:,1])
