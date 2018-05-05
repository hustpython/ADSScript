#encoding:utf-8
import struct

fd = open('data/cell_1.ds', 'rb')
nWav = struct.unpack(
    '2s2sii', fd.read(12))
print(nWav)

'''f=open('data/cell_1.ds','rb')
sn=f.read(20)

tu=struct.unpack('5l',sn)
print(tu)'''
