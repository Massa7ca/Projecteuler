import time
kvad = []
for i in xrange(1,16000+1):
    kvad.append(i*i)

kv = []
for i in xrange(2000000):
    kv.append(i*i)

kvad_s = set(kv)
del kv
def daili_net(x,y,z):
    if x+y in kvad_s and x-y in kvad_s and x+z in kvad_s and \
       x-z in kvad_s and y+z in kvad_s and y-z in kvad_s:
        return True

def danet(y,z):
    if (y+z) in kvad_s and (y-z) in kvad_s:
        return True
    return False
try:
    for i in xrange(16000):
        #print i
        z = kvad[i]
        for j in xrange(i+1,16000):
            y = kvad[j]
            if danet(y,z):
                print "41"
                raise StopIteration
                for m in xrange(j+1,1600):
                    x = kvad[m]
                    if daili_net(x,y,z):
                        print x,y,z
                        raise StopIteration
    
except StopIteration:
  print "vishli iz vseh", i, j , k
