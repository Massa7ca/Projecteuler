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


def s_46(a):
    nec = range(3,a,2)
    nechotnie = set(nec)
    pros = naiti_prostie_menshe(a)
    pr = set(pros)
    vse = []
    e = 0
    for i in nec:
        if not i in pr:
            nashli = False
            for j in xrange(1,100):
                ostatok = i - 2*j**2
                if ostatok in pr:
                    nashli = True
                    break
            if nashli == False:
                print "otvet:", i
                return 
                
                
                for m in pros:
                    if i == 2*j**2 + m:
                        print i
                        break
                    elif m > i:
                        break
                    
s_46(10000000)
