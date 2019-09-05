import time
sp = []
def t(n):
    return n*(n+1)/2
def p(n):
    return n*(3*n-1)/2
def h(n):
    return n*(2*n-1)


kkk = time.time()
tt = set()
pp = set()
hh = set()
for i in xrange(300,1000):
    print i, h(i)
    ii = h(i)
    for j in xrange(i,2000):
        jj = p(j)
        for m in xrange(j,3000):
            hh = t(m)
            if ii == jj:
                if jj == hh:
                    print "gfdgdgdfgfddfgfddfgf", p(j)
                    print time.time() - kkk
                
