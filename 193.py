import time
import math
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

pr = naiti_prostie_menshe(2**25)
prostie_v_kvadrate = []
for i in pr:
    prostie_v_kvadrate.append(i**2)
del pr
print "31"

def zadacha(limit, prostie_v_kvadrate, chislo_za_skobkami, index_pervogo_p, glubina):
  otvet = 0
  for index_prostogo in xrange(index_pervogo_p, len(prostie_v_kvadrate)):
    pr = prostie_v_kvadrate[index_prostogo]
    if pr * chislo_za_skobkami >= limit:
      break
    if glubina == 0:
        if index_prostogo % 500 == 0 or index_prostogo == 1 or index_prostogo == 2 or index_prostogo == 3 or index_prostogo == 4:
            print "delaem prosto nomer", index_prostogo, "iz", len(prostie_v_kvadrate)
    otvet += limit/(pr*chislo_za_skobkami) - zadacha(limit, prostie_v_kvadrate, chislo_za_skobkami * pr, index_prostogo+1, glubina+1)
  return otvet

print 2**50 - zadacha(2**50, prostie_v_kvadrate, 1, 0, 0)
