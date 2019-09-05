import math,time

def ybiri_povtor(spisak):
    nov = []
    for chislo in spisak:
        if not chislo in nov:
           nov.append(chislo)
    return nov

kva = []
for nnn in xrange(500001):
    kva.append(nnn*nnn)
def triug(p):
    global kva
    vse = []
    ee = 0
    for i in xrange(2,p/2):
        for j in xrange(i+1,p/2):
            m = p - (i + j)
            if p == i+j+m:
                if kva[i] + kva[j] == kva[m]:
                    vse.append([i,j,m])
                    ee +=1
    
    #print vse
    return [ee,p]

#print triug(120)
for i in xrange(10,100):
    a = triug(i)
    if a[0] == 1:
        print i
#[8, 840] 999
'''nn = time.time()
n = []
for i in xrange(1,1000):
    #print i
    a = triug(i)
    n.append(a)   
print max(n),time.time() - nn '''
