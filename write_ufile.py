#!/usr/bin/env python3

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
	print('  %s               ;-SHOT #- F(X) DATA -UF1DWR- 12Oct2005'%shootID,file=f)
	print(' %s                      ;-SHOT DATE-  UFILES ASCII FILE SYSTEM'%shootdate,file=f)
	print('   0                           ;-NUMBER OF ASSOCIATED SCALAR QUANTITIES-',file=f)
	print(' TIME                SEC       ;-INDEPENDENT VARIABLE LABEL-',file=f)
	print(' %s                  %s         ;-DEPENDENT VARIABLE LABEL-'%(dataname,dataunit),file=f)
	print(' 0                             ;-PROC CODE- 0:RAW 1:AVG 2:SM. 3:AVG+SM',file=f)
	print('        %d                    ;-# OF PTS-  X, F(X) DATA FOLLOW:'%datalen,file=f)
	write_array(f,timearray)
	write_array(f,dataarray)
	print(' ;----END-OF-DATA-----------------COMMENTS:-----------',file=f)		
	f.close()

def write_2Dufile(filename,shootID,shootdate,xname,xunit,dataname,dataunit,xarray,timearray,dataarray):
	f=open(filename,'w')
	print('  %s               ;-SHOT #- F(X) DATA -UF1DWR- 12Oct2005'%shootID,file=f)
	print(' %s                      ;-SHOT DATE-  UFILES ASCII FILE SYSTEM'%shootdate,file=f)
	print('   0                           ;-NUMBER OF ASSOCIATED SCALAR QUANTITIES-',file=f)
	write_label_unit(f,xname,xunit,'-INDEPENDENT VARIABLE LABEL: X-')
	write_label_unit(f,'TIME','SEC','-INDEPENDENT VARIABLE LABEL: Y-')
	write_label_unit(f,dataname,dataunit,'-DEPENDENT VARIABLE LABEL-')
	print(' 0                             ;-PROC CODE- 0:RAW 1:AVG 2:SM. 3:AVG+SM',file=f)
	Xlen=len(xarray)
	Ylen=len(timearray)
	print('        %d                    ;-# OF X PTS-'%Xlen,file=f)
	print('        %d                    ;-# OF Y PTS- X,Y,F(X,Y) DATA FOLLOW:'%Ylen,file=f)
	write_array(f,xarray)	
	write_array(f,timearray)	
	write_array(f,dataarray.reshape(-1))	
	print(' ;----END-OF-DATA-----------------COMMENTS:-----------',file=f)		
	
	f.close()

	

