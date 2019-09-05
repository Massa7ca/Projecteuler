import time
import math
def naiti_prostie_menshe(n):
    vsen = bytearray([1]) * (n + 1)
    prostie = []
    koren = math.sqrt(n)
    p = 2
    while p <= koren:
        prostie.append(p)
        vsen[p::p] = bytearray(n/p)
        for i in xrange(p+1, n+1):
            if vsen[i]:
                p = i
                break
            
    for i in xrange((len(prostie)/30)*30, n+1, 30):
        try:
            if vsen[i+1]:
                prostie.append(i+1)
            if vsen[i+7]:
                prostie.append(i+7)
            if vsen[i+11]:
                prostie.append(i+11)
            if vsen[i+13]:
                prostie.append(i+13)
            if vsen[i+17]:
                prostie.append(i+17)
            if vsen[i+19]:
                prostie.append(i+19)
            if vsen[i+23]:
                prostie.append(i+23)
            if vsen[i+29]:
                prostie.append(i+29) 
        except:
            pass
    return prostie

aaa = naiti_prostie_menshe(1300000000)
maxx = aaa[-1]
a_sss = set(aaa)
print "dsf"
del aaa
def is_diagonal(x, y, n):
    if x == y:
        return True
    elif x + y == n - 1:
        return True
    return False 

def udali_nuli(a):
    nn = []
    for i in a:
        if i != 0:
            nn.append(i)
    return nn
def make_spiral(n):
   global a_sss, maxx
   # n - razmer spirali.
   
   # Inicializirovat' spisok spiskov.
   a = []
   dd = []
   for noli in xrange(n):
       a.append([0]*n)

   # Postavit' edinicu
   kol_dea = 1
   center = (n-1)/2
   a[center][center] = 1
   chisla = 0.0
   px = center
   py = center
   cifra = 1
   print "dsf"
   for krug in xrange(center):
       if cifra < maxx:
           if cifra in a_sss:
               chisla += 1
       else:
           print "mala"
           time.sleep(1000000)
       cifra  +=1
       px += 1
       a[py][px] = 1
       kol_dea += 1
       while not is_diagonal(px, py, n):
           py +=1
           cifra += 1
           a[py][px] = 1
           
       if cifra < maxx:
           if cifra in a_sss:
               chisla += 1
       else:
           print "mala"
           time.sleep(1000000)  
       px -= 1   
       cifra  +=1 
       a[py][px] = 1
       kol_dea += 1
       while not is_diagonal(px, py, n):
           px -=1
           cifra += 1
           a[py][px] = 1
           
       if cifra < maxx:
           if cifra in a_sss:
               chisla += 1
       else:
           print "mala"
           time.sleep(1000000)
       cifra  +=1
       py -= 1
       a[py][px] = 1
       kol_dea += 1
       while not is_diagonal(px, py, n):
           py -=1
           cifra += 1
           a[py][px] = 1
       if cifra < maxx:
           if cifra in a_sss:
               chisla += 1
       else:
           print "mala"
           time.sleep(1000000)
           
       px += 1   
       cifra  +=1 
       a[py][px] = 1
       kol_dea += 1
       while not is_diagonal(px, py, n):
           px +=1
           cifra += 1
           a[py][px] = 1

       print chisla /kol_dea*100
       if chisla /kol_dea*100 < 10.0:
           print "otvet = ", len(udali_nuli(a[n/2]))
           time.sleep(100000)

   return chisla 

make_spiral(28051)


#[1, 3, 17, 5, 7, 9, 43, 13, 49, 21, 25, 37, 31]





















