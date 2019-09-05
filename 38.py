def ybiri_povtor(spisak):
    nov = []
    for chislo in spisak:
        if not chislo in nov:
           nov.append(chislo)
    return nov

def v_int(sp):
    kk = 0
    for j in sp:
        kk = kk*10 + j    
    return str(kk)

def raz(sp):
    nov = []
    for i in sp:
        nov.append(int(i))
    return nov

def nam(aa):
    no = ""
    for i in aa:
        no += str(i)
    if not len(no) == 9:
        return False
    novv = ybiri_povtor(no)
    novvv = raz(novv)
    nov = v_int(novvv)
    v = "123456789"
    vse = set(v)
    a = 0
    for i in nov:
        if i in vse:
            a +=1       
    if a == 9:
        return int(nov)

no = [0]
for n in xrange(2,6):
    print max(no)
    for i in xrange(10001):
        f = ""
        for j in xrange(1,n):
            f += str(i * j)  
        a = nam(f)
        no.append(a)
print max(no)
