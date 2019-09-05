import math
n = ""
for i in xrange(1,1000000+1):
    if i % 100000 == 0:
        print i
    n += str(i)
print len(n)
s = 1
for i in (1,10,100,1000,10000,100000,1000000):
    s *= int(n[i-1])

print s
