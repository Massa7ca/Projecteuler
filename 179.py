#!/usr/bin/python

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

#print "ans", vse_deliteli([2])
#print "ans", vse_deliteli([2, 2])
#print "ans", vse_deliteli([2, 2, 2])
 
#print "ans", vse_deliteli([3, 2])
#print "ans", vse_deliteli([3, 2, 2])
#print "ans", vse_deliteli([3, 2, 2, 2])
#print "ans", vse_deliteli([3, 3, 2, 2])
#test_vse_deliteli()

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

chislo_deli = {}
#3798207594720
pros, de = naiti_prostie_i_deliteli_menshe(10**7+1, 10**7+1)
ad = set(pros)
for i in xrange(2,10**7+1):
    if i % 200000 == 0:
        print i
    a = nayti_prostie_deliteli(i, pros, ad, de)
    eeee = nayti_chislo_deliteley(a)
    chislo_deli[i] = eeee

kal = 0
for i in xrange(2,10**7):
    if i % 500000 == 0:
        print i
    if chislo_deli[i] == chislo_deli[i+1]:
        kal +=1
print kal       

#pros, de = naiti_prostie_i_deliteli_menshe(64000000, 15000000)
#ad = set(pros)
#s = 0
#for i in xrange(2,64000000):
#    if i % 100000 == 0:
#        print i
#    a = nayti_prostie_deliteli(i, pros, ad, de)
#    d = summa_kvadratov_deliteley(a)
#    if math.sqrt(d) % 1 == 0:
#        if int(math.sqrt(d)) ** 2 == d:
#            s += i
#print s

#528
