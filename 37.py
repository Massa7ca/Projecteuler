import math,time
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

a = naiti_prostie_menshe(20000)
p = []
def nam(aa):
    c = str(aa)
    k = []
    if not aa in a:
        return
    else:
        for i in xrange(1,len(c)):
            k.append(int(c[:-i]))
            k.append(int(c[i:]))

    z = 0        
    for j in k:
        if j in a:
            z += 1
        else:
            return
    if z == len(k):
       p.append(aa)

i = 11       
while True:
    if i == 20001:
        a = naiti_prostie_menshe(100100)
    elif i == 100001:
        a = naiti_prostie_menshe(300100)
    elif i == 300001:
        a = naiti_prostie_menshe(500100)
    elif i == 500001:
        a = naiti_prostie_menshe(700100)
    elif i == 700001:
        a = naiti_prostie_menshe(900100)
    elif i == 900001:
        a = naiti_prostie_menshe(1500100)
    elif i == 1500001:
        a = naiti_prostie_menshe(2000100)
    elif i == 2000001:
        a = naiti_prostie_menshe(2500100)
    elif i == 2500001:
        a = naiti_prostie_menshe(3000100)
    elif i == 3000001:
        a = naiti_prostie_menshe(4000100)
    elif i == 4000001:
        a = naiti_prostie_menshe(5000100)
    elif i >= 5000001:
        a = naiti_prostie_menshe(10000100)    
    nam(i)
    #print i
    i += 2
    if len(p) == 11:
        break
s = 0
for i in p:
    s += i
print s
time.sleep(10000)












