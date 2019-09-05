def d(n):
    chisla = range(1,n)
    dili = []
    for i in chisla:
        if n % i == 0:
            dili.append(i)
    suma = 0        
    for di in dili:
        suma += di
    return suma

def ybiri_povtor(spisak):
    nov = []
    for chislo in spisak:
        if not chislo in nov:
           nov.append(chislo)
    return nov

#for i in xrange(1,10001):
para = []
def pa(y):
    k = d(y)    
    n = d(k)
    kk = d(n)
    if k == kk:
        if not k == n:
            para.append(k)
            para.append(n)

for i in xrange(1,10000):       
    pa(i)              
a = ybiri_povtor(para)
s = 0
for i in a:
    s += i
print s    
