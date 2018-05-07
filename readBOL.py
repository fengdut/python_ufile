#!/usr/bin/env python3
print ("test script read IP")
filename='31885brem.txt'

print(filename)
import numpy

Ipdata=open(filename)
data=Ipdata.readlines()
print(data[0][0],data[0][1])
num=len(data)
print(data[num-1][0],data[num-1][1])
print(num)
BOL=numpy.zeros((num,2))

index=0
for line in data:
	line=line.strip()
	linelist=line.split()
	BOL[index,:]=linelist[0:2]
	index +=1

from write_ufile import *
write_1Dufile('test.BOL','31885HL2A1 0 6','05/05/17','Rad Power','W',BOL[:,0]*0.001,BOL[:,1]*1.190791608491535e+09)
