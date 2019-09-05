#!/usr/bin/python

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
    print factors

    n = len(factors)
    dels = [1]
    for ind in xrange(pow(2,n)):
      count = 0
      if ind % 2 == 1:
        orig_dels_len = len(dels)
        last = len(factors[count]) - 1
        for f in xrange(last + 1):
          if f == last:
            for j in xrange(orig_dels_len):
              dels[j] *= factors[count][f]
          else:
            for j in xrange(orig_dels_len): 
              dels.append(dels[j] * factors[count][f])   
        count += 1
        ind >> 1  
    return dels

'''print vse_deliteli([2])
print vse_deliteli([2, 2])
print vse_deliteli([2, 2, 2])
 
print vse_deliteli([3, 2])
print vse_deliteli([3, 2, 2])'''
#a = naiti_prostie_menshe(3)
print vse_deliteli([552])

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


