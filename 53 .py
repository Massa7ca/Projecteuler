import math

def kfic(n,r):
  return math.factorial(n)/ (math.factorial(r)* math.factorial(n-r))


kk = 0
for n in xrange(1,101):
  for r in xrange(1,n):
    a = kfic(n,r)
    if a > 10**6:
      kk +=1
print kk
