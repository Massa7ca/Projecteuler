nmm = [] 
def nam(aa):
    c = str(aa)
    m = []
    for ch in c:
        m.append(int(ch))
    a = len(m)/2
    if not len(m) % 2 == 0:
        return
    elif len(m) % 2 == 0:
        n = m[:a]
        kk = m[a:]
        k = []
        for i in xrange(len(kk)):
            k.insert(0,kk[i])
    if n == k:
        nmm.append(aa)
        return True


def palindrom(chislo):
    a = bin(chislo)
    des = a[2:]
    if nam(des):
        
    
print nam(1001 0 0 1001)
