def v_int(sp):
    kk = 0
    for j in sp:
        kk = kk*10 + j    
    return kk

def pas(chis):
    chis_ss = str(chis)
    for j in xrange(100):
        chis_s = chis_ss[j:]
    for i in xrange(1,977):
            if chis_s[0:i]==chis_s[i:i*2]:
                return False
    else:
        return True

e = [1]
for i in xrange(2600):
    e.append(0)
oo = v_int(e) 
a = []
for i in xrange(1,1001):
    if i % 20==0:
        print i
    aa = oo/i
    if pas(aa):
        a.append([aa,i])
print a
