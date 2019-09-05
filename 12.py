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


# Nam nado funkciyu nayti_deliteli(chislo, spisok_prostih) kotoraya ispol'zuya
# spisok prostih budet nahodit' vse prostie deliteli chila bistro

def nayti_deliteli(n, prostie):
    m = n
    deliteli = []
    while True:
        nashli = False
        for p in prostie:
            if m % p == 0:
                m = m / p
                deliteli.append(p)
                nashli = True
                break
        if m == 1:
            break
        if not nashli:
            print "Nuzhno bol'she prostih chisel, etih ne hvatilo"
            return []
    return deliteli

def nayti_chislo_deliteley(prostie_deliteli):
    per = prostie_deliteli[0]
    p = 0
    vt = -1
    nov = []
    suma = 1
    for i in prostie_deliteli:
        vt+=1
        if not per == i:
            per = prostie_deliteli[vt]
            nov.append(prostie_deliteli[p:vt]) 
            p = vt
    nov.append(prostie_deliteli[p:])
    for ch in nov:
        suma *= (len(ch)+1)
    return suma
    

prostie = naiti_prostie_menshe(10000000)
nn = time.time()
n = 2
a = 1
for i in xrange(1000000):
   a += n
   n += 1
   deliteli = nayti_deliteli(a, prostie)
   k = nayti_chislo_deliteley(deliteli)
   #print k
   if k > 500:
       kk = time.time()
       print a , kk - nn
       break
