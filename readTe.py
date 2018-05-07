#!/usr/bin/env python3
print ("test script read IP")
filename='31885Te.mat'
print(filename)
import numpy
import scipy.io as sio
data=sio.loadmat(filename) 
Te=data['Te']
R=data['R']
t=data['t']
#print(Te)
#print(Te.shape)
#print(R.shape)
#print(t.shape)
from write_ufile import *

write_2Dufile('test.TER','31885HL2A1 0 6','05/05/17','R','cm','Te','EV',R[0,:],t[0,:],Te)

