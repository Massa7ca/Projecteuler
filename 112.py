def voz(c):
  c_s = str(c)
  per = c_s[0]
  for i in c_s[1:]:
    if  int(per) > int(i):
      return False
    per = i
  return True

def ub(c):
  c_s = str(c)
  per = c_s[0]
  for i in c_s[1:]:
    if  int(per) < int(i):
      return False
    per = i
  return True

def por(chislo,k):
  pr = chislo/100.0
  return pr
    

k = 0
for j in xrange(0,2870080):
  if j % 50000 == 0:
    print j,k
  j +=1
  for i in xrange(j,j+1):
      if  ub(i) or voz(i):
        k +=1   
  if por(j,k):
      if j > 1000:
        print j
        break
    

