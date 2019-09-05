import time
def t(n):
    return n*(n+1)/2
def p(n):
    return n*(3*n-1)/2
def h(n):
    return n*(2*n-1)


tt = set()
pp = set()
hh = set()
for i in xrange(1,10**6):
    tt.add(t(i))
for j in xrange(1, 1000000):
    pp.add(p(j))
for m in xrange(1, 1000000):
    hh.add(h(m))
    
print "34243"
for z in hh:
    if z in pp:
        if z in tt:
            print z
#7906276

# 3976
# 2296
