from math import factorial
import time
nnn = time.time()
kvadrati = {}
fac = {}
for i in xrange(10):
    #a = str(i)
    fac[i] = factorial(i)  

def sleduyushiy(chisloo):
    suma = 0
    for i in chisloo:
        suma += i*i
    return suma

def razedini(c):
    c_s = str(c)
    nn = []
    for i in c_s:
        nn.append(int(i))
    return nn    

sss = {}
for i in xrange(81*7+1):
    sss[i] = sleduyushiy(razedini(i))
#567
def shagi(chislo):
    if chislo == 0:
        return False
    i = chislo
    while True:
        sleduyush = sss[i]
        if sleduyush == 89:
            return True
        elif sleduyush == 1:
            return False
        i = sleduyush

def skolika(n):
    x = set(n)
    f = fac[len(n)]
    for i in x:
        f = f/fac[n.count(i)]
    return f    

#print skolika([1,2,3,4,5,6,7,8,9])
#10 000 000L
#77325494663740682469
kol = 0
for i in xrange(10):
    for i1 in xrange(i,10):
        for i2 in xrange(i1,10):
            for i3 in xrange(i2,10):
                for i4 in xrange(i3,10):
                    for i5 in xrange(i4,10):
                        for i6 in xrange(i5,10):
                            a = [i,i1,i2,i3,i4,i5,i6]
                            if shagi(sleduyushiy(a)):
                                kol += skolika(a)
                               
print kol, time.time()- nnn             












    
