import itertools,math
import time

def kfic(n,k):
  return math.factorial(n)/ (math.factorial(k)* math.factorial(n-k))

def pari(n):
    m = []
    aa = kfic(len(n),50)
    mm = 0
    for kom in itertools.combinations(n, 3):
        m.append(sum(kom))
        mm +=1
        if mm % 1000000 == 0:
            print m ,"iz", aa
                 
    k = []
    for x in m:
        e = m.count(x)
        if e == 1:
            k.append(x)
    return sum(k)        
    

e = []
for i in xrange(1,101):
    e.append(i**2)
  
print pari(e)

