ee = []
for a in xrange(1,10):
    for k in xrange(1,10):
        for n in xrange(1,100):
            per = a*(10**n - k)
            vtor = 10*k - 1
            if per % vtor == 0:
                print per, vtor
                B = per/vtor
                m = len(str(B))
                if m == n:
                    assert((a*10**n + B) % (k*(10*B + a)) == 0)
                    ee.append(10*B + a)
ee_s = set(ee)
e = list(ee_s)
print len(e)
print sum(e)
