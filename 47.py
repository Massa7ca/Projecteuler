import math
def naiti_prostie_i_deliteli_menshe(n, m):
    vsen = [True] * (n+1)
    # esli vsen[k] == True znachit mi eshyo ne vikinuli k.
    # esli vsen[k] == False, znachit mi uzhe vikinuli k.
    prostie = []
    deliteli = []
    # deliteli chisel mi budem sohranyat' v spiske spiskov
    # naprimer deliteli[5] eto spisok prostih deliteley 5, to est' [5],
    # deliteli[10] = [2, 5]
    
    # Snachala nado inicializirovat' nash spisok deliteli 
    for i in xrange(m):
        deliteli.append([])
        
    koren = math.sqrt(n)
    p = 2
    while p <= koren:
        # Zapominaem nashe prostoe chislo
        prostie.append(p)
        
        # Teper' vikidivayem iz spiska vsen, chisla kotorie delyatsya
        # na p.
        for i in xrange(p, n+1, p):
            vsen[i] = False
            # chislo i delitsya na p, dobavlyayem p v spisok ego deliteley
            if i < m:
                deliteli[i].append(p)
                chislo = i/p
                while True:
                    if chislo % p == 0:
                        deliteli[i].append(p)
                        chislo = chislo / p
                    else:
                        break
        
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
            if i < m:
                for k in xrange(i, m, i):
                    deliteli[k].append(i)
                    chislo = k/i
                    while True:
                        if chislo % i == 0:
                            deliteli[k].append(i)
                            chislo = chislo / i
                        else:
                            break
    return prostie, deliteli

def nayti_prostie_deliteli(n, prostie, tt, de):
    max_de = len(de)
    if n in tt:
        return [n]
    if n < max_de:
        return de[n]
    if not n in tt: 
        m = n
        deliteli = []
        posledniy_index = 0
        num_prostih = len(prostie)
        while True:
            nashli = False
            for ind in xrange(posledniy_index, num_prostih):
                p = prostie[ind]
                if m % p == 0:
                    m =  m / p
                    deliteli.append(p)
                    posledniy_index = ind
                    nashli = True
                    break
            if m in tt:
                deliteli.append(m)
                return deliteli
            if m == 1:
                return deliteli
            if m < max_de:
                deliteli.extend(de[m])
                break
            if not nashli:
                print "Nuzhno bol'she prostih chisel, etih ne hvatilo"
                return []
        return deliteli

dili = []
pros, de = naiti_prostie_i_deliteli_menshe(1000000, 100000)
ad = set(pros)
s = []
for i in xrange(2,1000000):
    if i % 100000 == 0:
        print i
    a = nayti_prostie_deliteli(i, pros, ad, de)
    if len(set(a)) >= 4:
        s.append(i)

s.sort()
gde = 0
for i in s:
    gde += 1
    v = s[gde]-1
    t = s[gde+1]-2
    ch = s[gde+2]-3
    if i == v == t == ch:
        print i
        break

'''gde = 0
s = [1,2,3,4,6,5,6,7,8,9,10]
for i in s:
    gde += 1
    v = s[gde]-1
    t = s[gde+1]-2
    ch = s[gde+2]-3
    if i == v == t == ch:
        print i'''




