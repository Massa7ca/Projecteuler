import time
import math
def naiti_prostie_menshe(upperLimit):
    isPrime = [True] * ((upperLimit >> 1))
    prostie = [2]
    end = int(math.sqrt(upperLimit))
    for i in xrange(3, end, 2):
        if isPrime[i >> 1]:
            composite = 3 
            while composite*i <= upperLimit:
                isPrime[(i*composite) >> 1] = False
                composite += 2
    i = 1      
    for j in xrange(1, (upperLimit >> 1)):
        if isPrime[j]:
            prostie.append((j << 1) +1)
            i += 1
    return prostie
        
            

n = time.time()
a = naiti_prostie_menshe(7200)
print a
#print time.time() - n
