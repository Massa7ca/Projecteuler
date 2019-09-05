def f3(n): return n*(n+1)/2
def f4(n): return n**2
def f5(n): return n*(3*n-1)/2
def f6(n): return n*(2*n-1)
def f7(n): return n*(5*n-3)/2
def f8(n): return n*(3*n-2)

def proverka(lis):
    e = []
    bb = 0
    p = lis[0]
    while True:
        if bb > 3:
            e.append(p)
            return False
        aa = True
        for i in xrange(len(lis)):
            if len(set(e)) == len(lis):
                if e[-1] % 100 == e[0] / 100:
                    return True
            if p % 100 == lis[i]/100:
                e.append(p)
                p = lis[i]
                aa = False
        if aa:
            return False
        
        if len(set(e)) == len(lis):
            if e[-1] % 100 == e[0] / 100:
                return True  
        bb += 1


ff3, ff4 = [f3(i) for i in xrange(45, 141)], [f4(i) for i in xrange(32, 100)]
ff5, ff6 = [f5(i) for i in xrange(26, 81)], [f6(i) for i in xrange(23, 71)]
ff7, ff8 = [f7(i) for i in xrange(21, 64)], [f8(i) for i in xrange(19, 59)]

for i in xrange(len(ff8)):
    for i1 in xrange(len(ff7)):
        for i2 in xrange(len(ff6)):
            print i, i1, i2
            for i3 in xrange(len(ff5)):
                for i4 in xrange(len(ff4)):
                    for i5 in xrange(len(ff3)):
                        a = [ff3[i5], ff4[i4], ff5[i3], ff6[i2], ff7[i1], ff8[i]]
                        if proverka(a):
                            print a, sum(a)
                            raise KeyError
