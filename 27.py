#!/usr/bin/python
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
kv = []
for i in xrange(10000):
    kv.append(i*i)

prostie = naiti_prostie_menshe(10000000)
pro = set(prostie)
nov = [[0,0]]
a = 0
b = 0
kall = 0
for b in xrange(1000,-1000,-1):
    print max(nov),b
    for a in xrange(1000,-1000,-1):
        kall = 0
        for n in xrange(10000):
            pros = kv[n] + a*n + b
            if pros in pro:
                kall +=1
            else:
                break
        if kall > 2:
            nov.append([kall,a*b])


            
