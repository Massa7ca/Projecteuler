import time
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

def fabinachi(n):
    fn = fn1 = fn2 = 1
    i = 3
    while i <= n:
        fn = fn1 + fn2
        fn2 = fn1
        fn1 = fn
        #print fn
        i += 1
    return fn

#print cifri(1215464655566454654656423)
#print n-k
#len(a[-9:])
#len(a[:9])
v = "123456789"
vse = set(v)
def nam(aa):
    #global vse,v
    novv = set(aa)
    if len(novv) == len(aa):
        return True
    return False

from decimal import localcontext
import decimal
with localcontext() as ctx:
    ctx.prec = 50   # Perform a high precision calculation
    DD = decimal.Decimal(5)
    d = DD.sqrt()
koreni = d
#562.891000032
#551.625
#481.661000013
# 127000
n = time.time()
i = 3
fn = fn1 = fn2 = 1#fabinachi(50)
while True:
    #if i % 500 == 0:
    #    print i
    fn = fn1%1000000000 + fn2%1000000000
    fn2 = fn1
    fn1 = fn
    f = fn%1000000000
    a = str(f%1000000000)
    aa = a       
    if "1" in aa and "2" in aa and "3" in aa and "4" in aa and "5" in aa\
       and "6" in aa and "7" in aa and "8" in aa and "9" in aa:
        #print i,a
        if nam(a):
            nnn = i
            ver = ((1+koreni)/2)**nnn - ((1-koreni)/2)**nnn
            k = int(ver / koreni)
            f_s = str(k)
            ppp = f_s[:9]
            print i,a
            if nam(ppp):
                k = time.time()
                print i,k-n
                break
    i += 1
