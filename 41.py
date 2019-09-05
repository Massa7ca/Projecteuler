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


def nam(aa):
    nov = []
    for i in aa:
        nov.append(str(i))
    e = 0    
    for j in nov:
        for i in j: 
            if i in nov[0]:
                if i in nov[1]:
                    if i in nov[2]:
                        e +=1
    if e == 12:
        return True

n = []
a = naiti_prostie_menshe(100000)
print len(a)
aa = set(a)
for i in a:
    if i in aa and i+3330 in aa and i+6660 in aa :
        ee = nam([i, i+3330, i+6660])
        if ee:
            n.append([i, i+3330, i+6660])
print n        
    
