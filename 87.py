import math
import time
def naiti_prostie_menshe(n):
    vsen = [True] * (n+1)
    prostie = []
    koren = math.sqrt(n)
    p = 2
    while p <= koren:
        prostie.append(p)
        for i in xrange(p, n+1, p):
            vsen[i] = False
            
        for i in xrange(p, n+1):
            if vsen[i] == True:
                p = i
                break

    for i in xrange(p, n+1):
        if vsen[i] == True:
            prostie.append(i)
        
    return prostie

potolok = 50000000
ee = []
a = naiti_prostie_menshe(int(math.sqrt(potolok)))
kv, ku, ch = {}, {}, {} 
for i in xrange(len(a)):
    kv[a[i]] = a[i] ** 2
    ku[a[i]] = a[i] ** 3
    ch[a[i]] = a[i] ** 4

for i in xrange(len(a)):
    kva = kv[a[i]]
    for j in xrange(len(a)):
        kub = ku[a[j]]
        if kva + kub > potolok:
            break
        for z in xrange(len(a)):
            chet = ch[a[z]]
            chislo = kva + kub + chet
            if chislo > potolok:
                break
            elif chislo < potolok:
                ee.append(chislo)
                
print len(list(set(ee)))
