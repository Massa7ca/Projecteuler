# -*- coding: utf-8 -*-
def primes(lim):
  # cas particuliers
  if lim<7:
    if lim<2: return []
    if lim<3: return [2]
    if lim<5: return [2, 3]
    return [2, 3, 5]
  #  Crible
  n = (lim-1)//30
  m = n+1
  BA = bytearray
  prime1 = BA([1])*m
  prime7 = BA([1])*m
  prime11 = BA([1])*m
  prime13 = BA([1])*m
  prime17 = BA([1])*m
  prime19 = BA([1])*m
  prime23 = BA([1])*m
  prime29 = BA([1])*m
  prime1[0] = 0
  i = 0
  try:
    while 1:
      if prime1[i]:
        p = 30*i+1
        l = i*(p+1)
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*6
        prime7[l::p] = BA(1+(n-l)//p)
        l += i*4
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*2
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*4
        prime17[l::p] = BA(1+(n-l)//p)
        l += i*2
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*4
        prime23[l::p] = BA(1+(n-l)//p)
        l += i*6
        prime29[l::p] = BA(1+(n-l)//p)
      if prime7[i]:
        p = 30*i+7
        l = i*(p+7)+1
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*4+1
        prime17[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*4
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*4+1
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*6+1
        prime23[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime7[l::p] = BA(1+(n-l)//p)
      if prime11[i]:
        p = 30*i+11
        l = i*(p+11)+4
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*2
        prime23[l::p] = BA(1+(n-l)//p)
        l += i*4+2
        prime7[l::p] = BA(1+(n-l)//p)
        l += i*2
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*4+2
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*6+2
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*6+2
        prime17[l::p] = BA(1+(n-l)//p)
      if prime13[i]:
        p = 30*i+13
        l = i*(p+13)+5
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*4+2
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime7[l::p] = BA(1+(n-l)//p)
        l += i*4+1
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*6+3
        prime17[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*6+3
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*4+1
        prime23[l::p] = BA(1+(n-l)//p)
      if prime17[i]:
        p = 30*i+17
        l = i*(p+17)+9
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime23[l::p] = BA(1+(n-l)//p)
        l += i*4+3
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*6+3
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime17[l::p] = BA(1+(n-l)//p)
        l += i*6+3
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*4+3
        prime7[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime11[l::p] = BA(1+(n-l)//p)
      if prime19[i]:
        p = 30*i+19
        l = i*(p+19)+12
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*4+2
        prime17[l::p] = BA(1+(n-l)//p)
        l += i*6+4
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*6+4
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*4+2
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*2+2
        prime7[l::p] = BA(1+(n-l)//p)
        l += i*4+2
        prime23[l::p] = BA(1+(n-l)//p)
      if prime23[i]:
        p = 30*i+23
        l = i*(p+23)+17
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*6+5
        prime7[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime23[l::p] = BA(1+(n-l)//p)
        l += i*6+5
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*4+3
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*4+4
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime17[l::p] = BA(1+(n-l)//p)
      if prime29[i]:
        p = 30*i+29
        l = i*(p+29)+28
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*6+6
        prime23[l::p] = BA(1+(n-l)//p)
        l += i*4+4
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*2+2
        prime17[l::p] = BA(1+(n-l)//p)
        l += i*4+4
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*2+2
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*4+4
        prime7[l::p] = BA(1+(n-l)//p)
      i+=1
  except:
    pass
  #  Génération
  RES = [2, 3, 5]
  A = RES.append
  ti=0
  try:
    for i in range(n):
      if prime1[i]:
        A(ti+1)
      if prime7[i]:
        A(ti+7)
      if prime11[i]:
        A(ti+11)
      if prime13[i]:
        A(ti+13)
      if prime17[i]:
        A(ti+17)
      if prime19[i]:
        A(ti+19)
      if prime23[i]:
        A(ti+23)
      if prime29[i]:
        A(ti+29)
      ti+=30
  except:
    pass
  if prime1[n] and (30*n+1)<=lim:
    A(30*n+1)
  if prime7[n] and (30*n+7)<=lim:
    A(30*n+7)
  if prime11[n] and (30*n+11)<=lim:
    A(30*n+11)
  if prime13[n] and (30*n+13)<=lim:
    A(30*n+13)
  if prime17[n] and (30*n+17)<=lim:
    A(30*n+17)
  if prime19[n] and (30*n+19)<=lim:
    A(30*n+19)
  if prime23[n] and (30*n+23)<=lim:
    A(30*n+23)
  if prime29[n] and (30*n+29)<=lim:
    A(30*n+29)
  return RES

from time import time
n = time()
print primes(10000)
print time() - n
