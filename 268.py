koefs = [1, -4, 10, -20, 35, -56, 84, -120, 165, -220, 286, -364, 455, -560, 680, -816, 969, -1140, 1330, -1540, 1771, -2024]
prostie = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def f(potolok, chisla):
  return potolok/reduce(lambda x, y: x*y, chisla)

import itertools
def po_k(k, koefs):
  potolok = 10**16
  s = 0
  for komb in itertools.combinations(prostie, k):
    s += f(potolok, komb)
  return koefs[k-4]*s
        
def choose(n, k):
   # killichestvo sposobov vibrat' k chisel iz mnozhestva iz n chisel
   return reduce(lambda x, y: x*y, range(k+1, n)) / reduce(lambda x, y: x*y, range(2, n-k))

def nayti_koefficienti(n):
  # Nayti vse nashi koefficienti. n budet 25 (kollichestvo prostih chisel)
  a = [1]
  for i in range(5, n+1):
    coef = 0
    for j in range(4, i):
      coef += a[i-5]*choose(i, j)
    a.append(-coef)
  return a
  
chislo = 0  
for i in xrange(4, 26):
  print i
  chislo += po_k(i, koefs)
print chislo    
