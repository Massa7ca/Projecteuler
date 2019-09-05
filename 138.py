import time
import math
#math.sqrt(n)
import decimal,math
from decimal import localcontext
def find_xy(D):
    n = []
    with localcontext() as ctx:
        ctx.prec = 100   # Perform a high precision calculation
        DD = decimal.Decimal(D)
        d = DD.sqrt()
        a = []
        for i in xrange(3):
            #print "a", i
            chelaia = int(d)
            drob = d - chelaia
            try:
                d = 1/drob
            except:
                return None
            a.append(chelaia)
        #print a
        h = [a[0]] 
        k = [1]
        h.append(a[0]*a[1]+1)       
        k.append(a[1])
        for i in xrange(2,10000**2):
            chelaia = int(d)
            drob = d - chelaia
            d = 1/drob
            a.append(chelaia)
            h.append(a[i]*h[i-1] + h[i-2])
            k.append(a[i]*k[i-1] + k[i-2])   
            x = h[i]
            y = k[i]
            #print "tyring", i
            if x**2 - D*y**2 == -1:
                 n.append([x,y])
            if len(n) == 12:
                return n

a = find_xy(5)
s = 0
for i in a:
    s += i[1]
print s

