import time
import math
def naiti_prostie_menshe(n):
    vsen = [True] * (n+1)
    # esli vsen[k] == True znachit mi eshyo ne vikinuli k.
    # esli vsen[k] == False, znachit mi uzhe vikinuli k.
    prostie = []
    koren = math.sqrt(n)
    p = 2
    while p <= koren:
        # Zapominaem nashe prostoe chislo
        prostie.append(p)
        
        # Teper' vikidivayem iz spiska vsen, chisla kotorie delyatsya
        # na p.
        for i in xrange(p, n+1, p):
            vsen[i] = False
        
        # Teper' nahodim pervoy chislo v spiske vsen, kotoroe mi eshyo
        # ne vikinuli, i zapominaem ego v p.
        for i in xrange(p, n+1):
            if vsen[i] == True:
                p = i
                break
        
    # Kogda mi viydem iz cikla, vse ostavshiesya chisla v spiske
    # vsen budut prostimi. Ih nado prosto dobavit' v spisok prostie
    for i in xrange(p, n+1):
        if vsen[i] == True:
            prostie.append(i)
        
    return prostie
  
ppp = naiti_prostie_menshe(100000000)
prostie_s = set(ppp)
del ppp
print "41"
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

def v_int(sp):
    kk = 0
    for j in sp:
        kk = kk*10 + j    
    return kk

def kusochki(chislo, deleniye):
  nov = []
  chislo_s = str(chislo)
  per = deleniye[0]
  vtor = deleniye[-1]
  nov.append(int(chislo_s[:per]))
  n = 0
  for i in deleniye:
      n += 1
      if i == vtor:
          break
      posle_i = deleniye[n]
      nov.append(int(chislo_s[i:posle_i]))
  nov.append(int(chislo_s[vtor:]))
  return nov
  
def vse_deleniya():
  deleniya = []
  
  for i in xrange(1,9):
    for i1 in xrange(i+1, 9):
      for i2 in xrange(i1+1, 9):
        for i3 in xrange(i2+1, 9):
          for i4 in xrange(i3+1, 9):
            for i5 in xrange(i4+1, 9):
              for i6 in xrange(i5+1, 9):
                  deleniya.append([i, i1, i2, i3, i4, i5, i6])

  for i in xrange(1,9):
    for i1 in xrange(i+1, 9):
      for i2 in xrange(i1+1, 9):
        for i3 in xrange(i2+1, 9):
          for i4 in xrange(i3+1, 9):
            for i5 in xrange(i4+1, 9):
                deleniya.append([i, i1, i2, i3, i4, i5])

  for i in xrange(1,9):
    for i1 in xrange(i+1, 9):
      for i2 in xrange(i1+1, 9):
        for i3 in xrange(i2+1, 9):
          for i4 in xrange(i3+1, 9):
              deleniya.append([i, i1, i2, i3, i4])

  for i in xrange(1,9):
    for i1 in xrange(i+1, 9):
      for i2 in xrange(i1+1, 9):
        for i3 in xrange(i2+1, 9):
            deleniya.append([i, i1, i2, i3])

  for i in xrange(1,9):
    for i1 in xrange(i+1, 9):
      for i2 in xrange(i1+1, 9):
            deleniya.append([i, i1, i2])

  for i in xrange(1,9):
    for i1 in xrange(i+1, 9):
        deleniya.append([i, i1])
 
  return deleniya

def petistanovki(x):
  vse = []
  for i in xrange(factorial(len(x))):
    if i % 100000 == 0:
      print i
    vse.append(x[:])
    x = next_perm(x)    
  return vse

#ppp
def skolika_pros(spisok):
    k = 0  
    for i in spisok:
        if i in prostie_s:
            k +=1
    if k == len(spisok):
        return True
    return False
    
perist = []
pe = petistanovki([1,2,3,4,5,6,7,8,9])
for i in pe:
    perist.append(v_int(i))
del pe    
kk = 0
aee = vse_deleniya()
nnn = 0
for chislo in perist:
    if nnn % 1000 == 0:
        print kk,chislo
    nnn +=1
    for i in aee:
        a = kusochki(chislo, i)
        if skolika_pros(a):
            kk +=1
print kk
            





  
