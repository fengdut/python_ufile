#!/usr/bin/env python3
import numpy
import scipy.io as sio

def write_array(f,data):
	ti=0
	datalen=len(data)
	for i in range(0,datalen):
		if(ti==0):
			print('',file=f,end='  ')
		print('%E'% (data[i]),file=f,end = ' ')
		ti=ti+1
		if(ti==6):
			print('',file=f)
			ti=0
	if(ti!=0):
		print('',file=f)

def write_label_unit(f,dataname,dataunit,commts):
	print(' %s\t\t %s\t\t;%s'%(dataname,dataunit,commts),file=f)
	

def write_1Dufile(filename,shootID,shootdate,dataname,dataunit,timearray,dataarray):
	f=open(filename,'w')
	datalen=len(timearray)
	print(' %s               ;-SHOT #- F(X) DATA -UF1DWR- 12Oct2005'%shootID,file=f)
	print(' %s                      ;-SHOT DATE-  UFILES ASCII FILE SYSTEM'%shootdate,file=f)
	print(' 0                           ;-NUMBER OF ASSOCIATED SCALAR QUANTITIES-',file=f)
	print(' TIME                SEC       ;-INDEPENDENT VARIABLE LABEL-',file=f)
	print(' %s                  %s         ;-DEPENDENT VARIABLE LABEL-'%(dataname,dataunit),file=f)
	print(' 0                             ;-PROC CODE- 0:RAW 1:AVG 2:SM. 3:AVG+SM',file=f)
	print(' %d                    ;-# OF PTS-  X, F(X) DATA FOLLOW:'%datalen,file=f)
	write_array(f,timearray)
	write_array(f,dataarray)
	print(' ;----END-OF-DATA-----------------COMMENTS:-----------',file=f)		
	f.close()

def write_2Dufile(filename,shootID,shootdate,xname,xunit,dataname,dataunit,xarray,timearray,dataarray):
	f=open(filename,'w')
	print(' %s               ;-SHOT #- F(X) DATA -UF1DWR- 12Oct2005'%shootID,file=f)
	print(' %s                      ;-SHOT DATE-  UFILES ASCII FILE SYSTEM'%shootdate,file=f)
	print(' 0                           ;-NUMBER OF ASSOCIATED SCALAR QUANTITIES-',file=f)
	write_label_unit(f,xname,xunit,'-INDEPENDENT VARIABLE LABEL: X-')
	write_label_unit(f,'TIME','SEC','-INDEPENDENT VARIABLE LABEL: Y-')
	write_label_unit(f,dataname,dataunit,'-DEPENDENT VARIABLE LABEL-')
	print(' 0                             ;-PROC CODE- 0:RAW 1:AVG 2:SM. 3:AVG+SM',file=f)
	Xlen=len(xarray)
	Ylen=len(timearray)
	print(' %d                    ;-# OF X PTS-'%Xlen,file=f)
	print(' %d                    ;-# OF Y PTS- X,Y,F(X,Y) DATA FOLLOW:'%Ylen,file=f)
	write_array(f,xarray)	
	write_array(f,timearray)	
	write_array(f,dataarray.reshape(-1))	
	print(' ;----END-OF-DATA-----------------COMMENTS:-----------',file=f)		
	
	f.close()

	
def readCUR(filename):
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
	writestr=filename[:-7]
	writefile=writestr+'.CUR'
	commstr=writestr+'HL2A 1 0 6'
	write_1Dufile(writefile,commstr,'05/05/17','Ip','A',Ip[:,0]*0.001,Ip[:,1])

def readRBZ(filename):
	print(filename)
	Ipdata=open(filename)
	data=Ipdata.readlines()
	num=len(data)
	Ip=numpy.zeros((num,2))

	index=0
	for line in data:
		line=line.strip()
		linelist=line.split()
		Ip[index,:]=linelist[0:2]
		index +=1


	writestr=filename[:-7]
	writefile=writestr+'.RBZ'
	commstr=writestr+'HL2A 1 0 6'
	write_1Dufile(writefile,commstr,'05/05/17',' Rp*Bt','T*cm',Ip[:,0]*0.001,Ip[:,1])
def readTER(filename):
	data=sio.loadmat(filename) 
	Te=data['Te']
	R=data['R']
	t=data['t']
	writestr=filename[:-7]
	writefile=writestr+'.TER'
	commstr=writestr+'HL2A 1 0 6'
	write_2Dufile(writefile,commstr,'05/05/17','R','cm','Te','EV',R[0,:],t[0,:],Te)

def readVSF(filename):

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
	writestr=filename[:-7]
	writefile=writestr+'.VSF'
	commstr=writestr+'HL2A 1 0 6'
	write_1Dufile(writefile,commstr,'05/05/17','surface volts','volts',Ip[:,0]*0.001,Ip[:,1])

print ("test script read IP")
def readNER(filename):
	print(filename)
	data=sio.loadmat(filename) 
	d=data['Ne']
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

	writestr=filename[:-7]
	writefile=writestr+'.NER'
	commstr=writestr+'HL2A 1 0 6'
	write_2Dufile(writefile,commstr,'05/05/17','x','(r/a)','Electron Density','N/CM**3',r,t,NE_new)

def readBOL(filename):
	Ipdata=open(filename)
	commit=Ipdata.readline()
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
	writestr=filename[:-7]
	writefile=writestr+'.BOL'
	commstr=writestr+'HL2A 1 0 6'
	write_1Dufile(writefile,commstr,'05/05/17','Rad Power','W',BOL[:,0]*0.001,BOL[:,1]*1.190791608491535e+09)
