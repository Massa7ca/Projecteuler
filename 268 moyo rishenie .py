prostie = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
           97]

aa = 10 ** 16
nosloliko = 4
def umnozh(spisak):
  s = 1
  for i in spisak:
    s *= i
  return aa / s

import itertools,math

def kfic(n,k):
  return math.factorial(n)/ (math.factorial(k)* math.factorial(n-k))

def kof(n,nachalinoe):
  a = [1]
  e = 0
  for i in xrange(nachalinoe,n):
    if e % 2 != 0:
      a.append(abs(kfic(i,nachalinoe) - kfic(i+1,nachalinoe)))
    else:
      a.append(kfic(i,nachalinoe) - kfic(i+1,nachalinoe))
    e +=1  
  return a

kofit = kof(len(prostie),nosloliko)
#print kofit
def razdeli(dlina):
  suma = 0
  for komb in itertools.combinations(prostie, dlina):
    um = umnozh(komb)
    suma += um 
  return suma

otvet = 0
pred_otvet = 0
for i in xrange(nosloliko,len(prostie)+1):
  pred_otvet = otvet
  otvet += razdeli(i)*kofit[i-nosloliko]
  print i,otvet
  if otvet == pred_otvet:
    print "545"
    break
    
print otvet
