kub = []
for i in xrange(9000):
    kub.append(i**3)

def da_net(sp):
    if len(set(sp)) != len(sp):
        return False
    n = []
    for i in sp:
        a = list(str(i))
        a.sort()
        n.append(a)
    p = n[0]
    for i in n:
        if p != i:
            return False
    return True
try:
    for j in xrange(len(kub)):
        i = kub[j]
        print j
        for j1 in xrange(j,len(kub)):
            i1 = kub[j1]
            if da_net([i,i1]):
                for j2 in xrange(j1,len(kub)):
                    i2 = kub[j2]
                    if da_net([i,i1,i2]):
                        for j3 in xrange(j2,len(kub)):
                            i3 = kub[j3]
                            if da_net([i,i1,i2,i3]):
                                for j4 in xrange(j3,len(kub)):
                                    i4 = kub[j4]
                                    if da_net([i,i1,i2,i3,i4]):
                                        print i,i1,i2,i3,i4
                                        raise StopIteration
                    
except StopIteration:
    pass
            
   
