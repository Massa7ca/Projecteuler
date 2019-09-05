#!/usr/bin/python
import time
import math
s = 1
for po_100 in xrange(2+1):
  suma = po_100*100
  if 200 < suma:    
      break
  for po_50 in xrange(5+1):
    suma = po_100*100+po_50*50
    if 200 < suma:
      break
    for po_20 in xrange(10+1):
        suma = po_100*100+po_50*50+po_20*20
        if 200 < suma:
          break
        for po_10 in xrange(20+1):
            suma = po_100*100+po_50*50+po_20*20+po_10*10
            if 200 < suma:
              break
            for po_5 in xrange(40+1):
              suma = po_100*100+po_50*50+po_20*20+po_10*10+po_5*5
              if 200 < suma:
                break
              for po_2 in xrange(100+1):
                    suma = po_100*100+po_50*50+po_20*20+po_10*10+po_5*5+po_2*2 
                    if 200 >= suma:    
                        s +=1
                    else:
                      break
print s
