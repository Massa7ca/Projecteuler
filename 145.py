def esti(chisl):
  chislo = set(chisl)
  if not "2" in chislo and not "4" in chislo and not "6" in chislo and\
     not "8" in chislo and not "0" in chislo:
      return True
  return False

def periverni(chislo):
  a = ""
  chislo_s = str(chislo)
  for i in xrange(1,len(chislo_s)+1):
    a += chislo_s[-i]
  if a [0] == "0":
    return False
  ee = int(a)+chislo
  e_s = str(ee)
  if esti(e_s):
    return True
  return False

#print periverni(36)
s = 0
for i in xrange(10,90100000):
  if i % 100000 == 0:
    print i, s
  if periverni(i):
    s +=1
print s   
  
