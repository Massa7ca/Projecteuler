import time
import math

def posled():
    n = [1,1,1]
    mm = 0 
    p = n[mm]
    v = n[mm+1]
    t = n[mm+2]
    for i in xrange(50000):
        p = n[mm]
        v = n[mm+1]
        t = n[mm+2]
        sled = p + v + t
        n.append(sled)
        mm +=1
    return n
#987
#range(1,200,2)        
a = posled()
lle = 0
ss = 0 
for i in xrange(1,10000,2):
    for j in a:
        if j % i == 0:
            s = 1
            break
    if s == 0:
        lle +=1
        print "ot",i, "pppse", lle
    s = 0
    if lle == 124:
        print "otvet",i
        break
   
        
