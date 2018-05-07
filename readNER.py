#!/usr/bin/env python3
print ("test script read IP")
filename='31885Ne.mat'
print(filename)
import numpy
import scipy.io as sio
data=sio.loadmat(filename) 
#print(data)
d=data['HCOOH']
rarray=d[0,1:]
lr=len(rarray)
print(lr)
r=rarray[lr//2:lr]

timearray=d[1:,0]
lt=len(timearray)
t=timearray[0:lt-1]
NE=d[1:,1:]
print('lr=%d',lr)
print('lr=%d',lr//2)

NE_new=numpy.zeros((lr//2,lt-1))
print(NE_new.shape)
for i in range(0,lr//2):
	for j in range(0,lt-1):
		NE_new[i,j]=NE[j,i]
print(r.shape)
print(t.shape)
print(NE_new.shape)
from write_ufile import *

write_2Dufile('test.NER','31885HL2A1 0 6','05/05/17','x','(r/a)','Electron Density','N/CM**3',r,t,NE_new)

