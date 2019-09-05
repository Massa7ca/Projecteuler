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

prostie = naiti_prostie_menshe(5000000)
pro = set(prostie)
nov = [[0,0]]
print len(prostie)
eee = len(prostie)
ee = len(str(eee))-1
aa = 0
for j in xrange(eee/(math.sqrt(eee)*ee),-1,-1):
    #if j % 2 == 0:
    print j , max(nov)   
    suma = 0
    dlina = 0
    for i in prostie[j:]:
        suma +=i
        dlina +=1
        if dlina > aa:
            if suma in pro:
                nov.append([dlina,suma])
                aa = dlina
                suma = 0
                dlina = 0
print max(nov) 
