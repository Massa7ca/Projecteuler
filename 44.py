import time
def p(n):
    return n*(3*n-1)/2

ppp = []
for j in xrange(1,10000):
    ppp.append(p(j))
 
ppp_set = set(ppp)

def ggg():
    global ppp, ppp_set
    for vt in ppp:
        for per in ppp:
            if (per + vt) in ppp_set and (per - vt) in ppp_set:
                print per,vt
                return 0

n = time.time()
ggg()
print time.time() - n
