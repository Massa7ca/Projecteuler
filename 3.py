from math import sqrt
def prostoe(n):
    for i in xrange(2,int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


for i in xrange(1,10000000):
    if 600851475143 % i == 0 and prostoe(i):
        a = i

print a
