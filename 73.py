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

def ia(a,iii):
    prostie = list(set(a)) 
    aa = iii
    nosloliko = 1
    def umnozh(spisak):
      s = 1
      for i in spisak:
        s *= i
      return aa / s

    import itertools,math

    def kfic(n,k):
      return math.factorial(n)/ (math.factorial(k)* math.factorial(n-k)) 
    def kof(n,nachalinoe):
      a = [1]
      e = 0
      for i in xrange(nachalinoe,n):
        if e % 2 != 0:
          a.append(abs(kfic(i,nachalinoe) - kfic(i+1,nachalinoe)))
        else:
          a.append(kfic(i,nachalinoe) - kfic(i+1,nachalinoe))
        e +=1  
      return a

    kofit = kof(len(prostie),nosloliko)
    def razdeli(dlina):
      suma = 0
      for komb in itertools.combinations(prostie, dlina):
        um = umnozh(komb)
        suma += um 
      return suma

    otvet = 0
    pred_otvet = 0
    for i in xrange(nosloliko,len(prostie)+1):
      pred_otvet = otvet
      otvet += razdeli(i)*kofit[i-nosloliko]
      if otvet == pred_otvet:
        break
    otvet = iii - otvet 
    return otvet


pros, de = naiti_prostie_i_deliteli_menshe(12000+1, 10)
ad = set(pros)
k = 0
for iii in xrange(2,12000+1):
    #if iii % 10000 == 0:
    #    print iii
    #iii = 4    
    a = nayti_prostie_deliteli(iii, pros, ad, de)
###############################################################
    k+= ia(a,int(iii/2.0))

s = 0
for iii in xrange(2,12000+1):
    #if iii % 10000 == 0:
    #    print iii
    #iii = 4    
    a = nayti_prostie_deliteli(iii, pros, ad, de)
###############################################################
    s+= ia(a,int(iii/3.0))
print k-s-1  
