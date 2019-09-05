import time
def is_diagonal(x, y, n):
    if x == y:
        return True
    elif x + y == n - 1:
        return True
    return False 
       
def make_spiral(n):
   # n - razmer spirali.
   
   # Inicializirovat' spisok spiskov.
   a = []
   for noli in xrange(n):
       a.append([])
       for i in xrange(n):
           a[noli].append(0)
           
   # Postavit' edinicu
   center = (n-1)/2
   a[center][center] = 1
   px = center
   py = center
   cifra = 1
   for krug in xrange(center):
       if krug % 100 == 0:
           print krug
       # Postavit' cifri iz sleduyushego kruga.
       cifra  +=1
       px += 1
       a[py][px] = cifra  
       while not is_diagonal(px, py, n):
           py +=1
           cifra += 1
           a[py][px] = cifra   
           
       px -= 1   
       cifra  +=1 
       a[py][px] = cifra  
       while not is_diagonal(px, py, n):
           px -=1
           cifra += 1
           a[py][px] = cifra
           
       cifra  +=1
       py -= 1
       a[py][px] = cifra    
       while not is_diagonal(px, py, n):
           py -=1
           cifra += 1
           a[py][px] = cifra
        
       px += 1   
       cifra  +=1 
       a[py][px] = cifra    
       while not is_diagonal(px, py, n):
           px +=1
           cifra += 1
           a[py][px] = cifra
   '''s = 0        
   for i in xrange(n):
       for j in xrange(n):
           if is_diagonal(i, j, n):
               s += a[i][j]
   print "per",s'''
   s = -1
   for i in xrange(n):
       s += a[i][i]   
   ii = 0    
   for j in xrange(n-1,-1,-1):
        s += a[ii][j]
        ii +=1
   print s
   
n = time.time()   
make_spiral(1001)
k = time.time()
print k - n
