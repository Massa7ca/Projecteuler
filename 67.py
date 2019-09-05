import time
triugulinik = []
def v_int(straka):
    nov = []
    for i in straka:
        nov.append(int(i))
    return nov    
f = open("67.txt")
for liniya in f:
  chisla_s = liniya.split() # eto razdelyayet po probelam
  # teper' chisla_s eto spisok tipa ["1", "3"] ego mozhno perevesti v chisla i ih ispol'zovat'.
  triugulinik.append(v_int(chisla_s))

def bl(n):
    return [n-1, n] 

def slubuiushiia_s(per, vtor):
    nov = [0]
    nov *= len(vtor)
    nov[0] = per[0]+vtor[0]
    nov[-1] = per[-1]+vtor[-1]
    gde = 0
    for i in nov:
        if i == 0:
            g = bl(gde)
            chislo = vtor[gde]
            perv = per[g[0]]
            vt = per[g[1]]
            a = [chislo+perv,chislo+vt]
            nov[gde] = max(a)
        gde  +=1
    return nov    

k = []
ee = triugulinik[0][0]
per_s = [ee]
for i in triugulinik[1:]:
    s = slubuiushiia_s(per_s, i)
    k.append(s)
    per_s = s
print max(k[-1])
