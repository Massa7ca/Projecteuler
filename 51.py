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



import itertools
pr = naiti_prostie_menshe(60000000)
def skolika(s,el):
    n = []
    gde = 0
    for i in s:
        if i == el:
            n.append((i,gde))
        gde += 1    
    return n

def mozna(chislo,pr):
    if chislo in pr:
        return True
    return False

def zam(straka,n,nashto):
    per = straka[:n]
    vtor = straka[1+n:]
    return per + nashto + vtor
    
def zameni(indeksi,straka,nashto):
    n = straka
    for i in indeksi:
        n = zam(n,i,nashto)
    return int(n)

def zameni_komdinachyu(indeksi, pros, straka):
    n = "0123456789"
    if 0 in indeksi:
        n = "123456789"
    pr = []
    for nashto in n:
        zameniaem = zameni(indeksi,straka,nashto)
        if zameniaem in pros:
            pr.append(zameniaem)
    return pr        

#for komb in itertools.combinations(prostie, dlina):
pr_set = set(pr)
k = []
try:
    for i in pr[1000:]:
        if i % 500 == 1:
            print i
        i_s = str(i)
        for ii in xrange(2,8):
            for komb in itertools.combinations([0,1,2,3,4,5,6,7], ii):
                n = zameni_komdinachyu(komb, pr_set, i_s)
                if len(n) == 9:
                    print n
                    raise StopIteration
    
except StopIteration:
    pass
