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

def petistanovki(x):
  vse = []
  for i in xrange(factorial(len(x))):
    if i % 100000 == 0:
      print i
    vse.append(x[:])
    x = next_perm(x)    
  return vse

a = petistanovki([0,1,2,3,4,5,6,7,8,9])
posle_a = []
for i in a:
    chislo = v_int(i)
    if len(str(chislo)) == 10:
        posle_a.append(chislo)
del a
posle_set = set(posle_a)
9873402516

def vse_deleniya():
  deleniya = []
  for a in xrange(1,3):
    for b in xrange(a + 1, 10):
      deleniya.append([a,b])    
  return deleniya      
  
def kusochki(chislo, deleniye):
  # chislo eto 10 znachnoe chislo predstavlennoe kak stroka
  # delenie eto odin iz spiskov vozvrashyonnih funkciyey vse_deleniya()
  # Eta funkciya dolzhna vozvratit kusochki chisla "chislo" kak [n[:a], n[a:b], n[b:c], n[c:]]
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
      if chislo_s[i] == "0":
          return False
      nov.append(int(chislo_s[i:posle_i]))
  if chislo_s[vtor] == "0":
      return False
  nov.append(int(chislo_s[vtor:]))
  return nov


def kusochki_dayut_vse_cifri(kusochki,posle_set):
  # Eta funkciya budet proveryat' dayut' li kusochki palindrom.
  # To est' perviy kusochek umnozhit' na vtotory, potom na tret'iy, itd.
  n = ""
  per = kusochki[0]    
  for i in kusochki[1:]:
      n += str(per*i)
  if int(n) in posle_set:
      return int(n)
  return 0    
  
a = vse_deleniya()  
ee = 0 
n = [1]
for i in posle_a:
    if ee % 1000 == 0:
      print i ,"Dlina",len(n),"Max", max(n)
    for j in a:
        kus = kusochki(i, j)
        if kus == False:
           continue
        e = kusochki_dayut_vse_cifri(kus,posle_set)    
        if e != 0:
            n.append(e)        
    ee +=1        
print max(n)  
