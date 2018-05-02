# -*- coding: utf-8 -*-
import sys

class bdffont():
    ch = -1
    bbx = ()
    bitmap = []


f = open(sys.argv[1])
lines = f.readlines()
f.close()
fontlist = []

#STARTCHAR 0000
#ENCODING 0
#SWIDTH 540 0
#DWIDTH 6 0
#BBX 0 0 0 0
#BITMAP
#ENDCHAR
STARTCHAR = 'STARTCHAR'
ENDCHAR = 'ENDCHAR'

i = 0
numlines = len(lines)
numchars = -1
while i < numlines:
    l = lines[i]
    if l.split()[0] == 'CHARS':
        tmp = l.strip().split(' ')
        numchars = int(tmp[1])
        #print numchars
        i+=1
    elif l[0:len(STARTCHAR)] == STARTCHAR :
        c = lines[i].strip().split(' ')[1]
        #print c
        i+=1
        enc =lines[i]
        i+=1
        swidth =lines[i]
        i+=1
        dwidth =lines[i]
        i+=1
        bbx = [ int(x) for x in  lines[i].strip().split()[1:]]
        #print bbx

        i+=2
        bitmap = []
        if bbx[0] > 0:
            y =0
            while y <bbx[1]:
                bitmap.append( lines[i].strip())
                i+=1
                y+=1
            #print bitmap
        else:
            i+=1
 
        bf = bdffont()
        bf.ch = c
        bf.bbx = bbx
        bf.bitmap =  bitmap
        fontlist.append(bf)

    else:
        i+=1

def printbit(ch):
    #print hex(ch)
    print fontlist[ch].ch
    print fontlist[ch].bitmap
    px = ['.','*']
    for bit in fontlist[ch].bitmap:
        s = ''
        #print bit
        for i in range(8,0,-1):
            tmp = int(bit,16) & 0xff
            p = (tmp & (1 << i)) > 0
            s += px[p]
        print s

def toCarray():
    for x in range(numchars):
        if fontlist[x].bbx[1] == 0:
            print "{},"
            continue
        arrstr = "{"
        for bit in fontlist[x].bitmap:
            arrstr += "0x"+bit + ","
        tmp = arrstr[0:len(arrstr)-1]
        tmp += "},"
        print tmp 
#print i
c = raw_input().strip()
printbit(ord(c))
#toCarray()
