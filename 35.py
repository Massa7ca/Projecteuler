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

prostie = naiti_prostie_menshe(1000000)
pr = set(prostie)
print "1"
def krug(a):
    a_st = str(a)
    if len(a_st) == 1:
        return [a]
    nov = []
    for j in a_st:
        nov.append(int(j))
    vse = []
    for i in xrange(len(nov)):
        #pe = nov[-1]
        pe = nov.pop(-1)
        nov.insert(0,pe)
        vse.append(nov[:])
    pos = []
    for i in vse:
        kk = 0
        for j in i:
            kk = kk*10 + j
        pos.append(kk)
    return pos

def ybiri_povtor(spisak):
    nov = []
    for chislo in spisak:
        if not chislo in nov:
           nov.append(chislo)
    return nov                   

n = time.time()
skoll = []
for iii in xrange(1000000):#prostie:
    if iii % 100000 == 0:
        print iii
    ae = krug(iii)
    aa = 0
    for i in ae:
        if i in pr:
            aa +=1
        else:
            break
    if aa == len(ae):
        skoll.append(ae)           

print "121" 
ss = ybiri_povtor(skoll)
k = time.time()
print len(ss),k-n    
