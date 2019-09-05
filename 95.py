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

def vse_deliteli(prostie_del):
    dd = {}
    for d in prostie_del:
      if d not in dd:
        dd[d] = 1
      else:
        dd[d] += 1
    #print dd

    factors = []
    for d, c in dd.iteritems():
      if c == 1:
        factors.append([d])
      else:
        factors.append([])
        for i in xrange(1, c + 1):
          factors[-1].append(pow(d, i))
    #print factors

    n = len(factors)
    all_dels = [1]
    for ind in xrange(1, pow(2,n)):
      #print "INDEX IS", ind
      count = 0
      dels = [1]
      while ind > 0:
        if ind % 2 == 1:
          orig_dels_len = len(dels)
          last = len(factors[count]) - 1
          for f in xrange(last + 1):
            if f == last:
              #print "doing last", dels
              for j in xrange(orig_dels_len):
                dels[j] *= factors[count][f]
              #print "done last", dels
            else:
              #print "doing normal", dels
              for j in xrange(orig_dels_len): 
                dels.append(dels[j] * factors[count][f])
              #print "done normal", dels
        count += 1
        ind = ind >> 1
      #print "DONE THIS INDEX", dels
      all_dels.extend(dels) 
    return all_dels
nnn = time.time()

pros, de = naiti_prostie_i_deliteli_menshe(1000001, 1000001)
ad = set(pros)
slebuyushiy = {}
for i in xrange(2,1000001):
    if i % 40000 == 0:
        print i
    a = nayti_prostie_deliteli(i, pros, ad, de)
    d = vse_deliteli(a)
    suma = sum(d)-i
    slebuyushiy[i] = suma
slebuyushiy[1] = 1
n = []
for i in xrange(2,1000000):
    if i % 5000 == 0:
        print i
    e = [i]
    per_i = i
    skoli = 0
    while True:
        if i > 1000000-1:
            break
        #try:
        per = slebuyushiy[i]
        #except KeyError:
        #    break
        if per != per_i:
            e.append(per)
        elif per == per_i:
            n.append(e)
            break
        if per > 1000000-1:
            break
        #try:
        vtor = slebuyushiy[per]
        #except KeyError:
        #    break    
        if vtor != per_i:
            e.append(vtor)
        elif vtor == per_i:
            n.append(e)
            break
        i = vtor
        skoli += 1
        if skoli == 29:
            break
    #.append(e)

maxim = []
nn = 0
for i in n:
    a = len(i)
    maxim.append([a,nn])
    nn +=1
pasled = max(maxim)
e = n[pasled[1]]
k = time.time()
print min(e),k-nnn

