def fak(m):
    if m == 0:
        return 1
    return fak(m-1)*m


fakt = {}
for i in xrange(10):
    fakt[i] = fak(i)

vse = []
def nam(aa,fak):
    c = str(aa)
    faktor = []
    for ch in c:
        t = int(ch)
        kaz = fak[t]
        faktor.append(kaz)
    a = 0    
    for j in  faktor:
        a += j
    return a
    

slebuiushiy_f = {}
for i in xrange(3650000):
    if i % 50000 == 0:
        print i
    a = nam(i,fakt)
    slebuiushiy_f[i] = a

def g(ee):
    suma = 0
    for i in xrange(1,1000000):
        if i % 10000 == 0:
            print i
        vse = []
        p = i
        vse.append(p)
        ea = 0
        for j in xrange(ee):
                nach = slebuiushiy_f[p]
                vse.append(nach)
                ea += 1
                p = slebuiushiy_f[nach]
                vse.append(p)
                ea += 1
                if ea >= 60:
                    if len(set(vse)) == 60:
                        suma +=1
                        break
                if not len(set(vse)) == len(vse):
                    break
    return suma
print g(40)
