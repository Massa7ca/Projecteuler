import time
nn = time.time()
kvadrati = {}
for i in xrange(10):
    a = str(i)
    kvadrati[a] = (i**2)

def sleduyushiy(chislo):
    chislo_s = str(chislo)
    suma = 0
    for i in chislo_s:
        suma += kvadrati[i]
    return suma

sss = {}
for i in xrange(10000000):
    if i % 500000 == 0:
        print i
    sss[i] = sleduyushiy(i)

    
s = 0
for i in xrange(1,10000000):
    if i % 500000 == 0:
        print i
    #e = 0
    while True:
        per = sss[i]
        if per == 1:
            break
        elif per == 89:
            s+=1
            break
        vtor = sss[per]
        if vtor == 1:
            break
        elif vtor == 89:
            s+=1
            break
        #e +=1
        #if e == 100:
        #    break
        i = vtor
kk = time.time()
print s,kk-nn
