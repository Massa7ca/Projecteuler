import math,itertools,time
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


def obedini(spikok):
    n = ""
    for j in spikok:
        for i in j:
            n += str(i)
    return int(n)


def kombin(spisok,pros):
    nov = []
    #reverse()
    for komb in itertools.combinations(spisok, 2):
        nov.append([komb])
        k = []
        k.append((komb[1],komb[0]))
        nov.append(k)   
    obed = []
    for i in nov:
        obed.append(obedini(i))
        
    for i in obed:
        if i in pros:
            pass
        else:
            return False
    return True    

def k():
    p = naiti_prostie_menshe(90000000)
    pros = set(p)
    del p
    prostie = naiti_prostie_menshe(8400)
    m = len(prostie)
    for j in xrange(m):
        print prostie[j]
        for j_1 in xrange(j+1, m):
            if kombin([prostie[j], prostie[j_1]],pros):
                for j_2 in xrange(j_1+1, m):
                    if kombin([prostie[j], prostie[j_1], prostie[j_2]],pros):
                        for j_3 in xrange(j_2+1, m):
                            if kombin([prostie[j], prostie[j_1], prostie[j_2], prostie[j_3]],pros):
                                for j_4 in xrange(j_3+1, m):
                                    if kombin([prostie[j], prostie[j_1], prostie[j_2], prostie[j_3], prostie[j_4]],pros):
                                       return prostie[j], prostie[j_1], prostie[j_2], prostie[j_3], prostie[j_4]
                                    
print k()





  
