#!/usr/bin/env python3
print ("test script read IP")
filename='31885 Ip.txt'

print(filename)
import numpy

Ipdata=open(filename)
commit=Ipdata.readline()
print(commit)
data=Ipdata.readlines()
num=len(data)
Ip=numpy.zeros((num,2))

index=0
for line in data:
	line=line.strip()
	linelist=line.split()
	Ip[index,:]=linelist[0:2]
	index +=1

from write_ufile import *
write_1Dufile('test.CUR','31885HL2A1 0 6','05/05/17','Ip','A',Ip[:,0]*0.001,Ip[:,1])

