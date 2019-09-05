import math,time
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
                if i % 200000 == 0:
                    print i
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
    
    
def dilitili(a):
    suma = 1
    for i in a:
        suma *= 1 + i ** 2
    return suma  
    
def summa_kvadratov_deliteley(dels):
    dd = {}
    for d in dels:
        if d not in dd:
            dd[d] = 1
        else:
            dd[d] += 1

    r = 1
    for d, c in dd.iteritems():
        s = 0
        for i in xrange(c+1):
            s += pow(d, 2*i)
        r *= s
    return r

nnn = time.time() 
pros, de = naiti_prostie_i_deliteli_menshe(64000000, 20000000)
ad = set(pros)
s = 0
for i in xrange(2,64000000):
    if i % 100000 == 0:
        print i
    a = nayti_prostie_deliteli(i, pros, ad, de)
    d = summa_kvadratov_deliteley(a)
    if math.sqrt(d) % 1 == 0:
        if int(math.sqrt(d)) ** 2 == d:
            s += i
kkk = time.time() 
print s-1,kkk-nnn
