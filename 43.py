#!/usr/bin/python

def factorial(n):
  s = 1
  for i in xrange(1, n+1):
    s *= i
  return s

def next_perm(perm):
  found = False
  for k in xrange(len(perm) - 2, -1, -1):
    if perm[k] < perm[k + 1]:
      found = True
      break
  if not found:
    return None

  for m in xrange(len(perm) - 1, -1, -1):
    if perm[k] < perm[m]:
      break
  tmp = perm[k]
  perm[k] = perm[m]
  perm[m] = tmp

  a = perm[(k + 1):]
  a.reverse()
  return perm[:(k+1)] + a

def petistanovki(x):
  vse = []
  for i in xrange(factorial(len(x))):
    if i % 100000 == 0:
      print i
    vse.append(x[:])
    x = next_perm(x)    
  return vse

pos = []
a = petistanovki([0,1,2,3,4,5,6,7,8,9])
for i in a:
        kk = 0
        for j in i:
            kk = kk*10 + j
        nn = str(kk)    
        if len(nn) == 10:    
          pos.append(nn)
print "121"          
no = []
for i in pos:
  if int(i[2-1]+i[3-1]+i[4-1]) % 2 == 0 and int(i[3-1]+i[4-1]+i[5-1]) % 3 == 0\
     and int(i[4-1]+i[5-1]+i[6-1]) % 5 == 0 and int(i[5-1]+i[6-1]+i[7-1]) % 7 == 0\
     and int(i[6-1]+i[7-1]+i[8-1]) % 11 == 0 and int(i[7-1]+i[8-1]+i[9-1]) % 13 == 0\
     and int(i[8-1]+i[9-1]+i[10-1]) % 17 == 0:
     no.append(int(i))
     
print sum(no)     

