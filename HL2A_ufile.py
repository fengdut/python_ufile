#!/usr/bin/env python3
print('this is python script to transform HL-2A experimental data to ufiles for transp run')
print('writted by Feng Wang@DLUT')

from read_HL2A import *

DischargeNo=22493

CURfile=str(DischargeNo)+'CUR.txt'
readCUR(CURfile)
RBZfile=str(DischargeNo)+'RBZ.txt'
#readRBZ(RBZfile) 
TERfile=str(DischargeNo)+'TER.mat'
readTER(TERfile)
#readTI2.py
VSFfile=str(DischargeNo)+'VSF.txt'
readVSF(VSFfile)
NERfile=str(DischargeNo)+'NER.mat'
readNER(NERfile)

BOLfile=str(DischargeNo)+'BOL.txt'
readBOL(BOLfile)





