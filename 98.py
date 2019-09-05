#!/usr/bin/python
import time
import math
# alfav = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nnn = time.time()                     
def naidi_gde(bukva,sp):
    j = 0
    for i in sp:
        if i[0] == bukva:
            return j
        j +=1
    return -1
    
def kvadrat_eli_net(n):
    try:
        korini = math.sqrt(n)
    except TypeError:
        return False  
    if int(korini) * int(korini) == n:
        return n
    return False

def prisvoi_znachenie_bikvam(slova, chislo):
    chislo_s = str(chislo)
    #if len(chislo_s) == len(slova):
    j = 0
    nov = []
    for i in slova:
        pp = naidi_gde(i,nov)
        if pp == -1:
            nov.append([i,chislo_s[j]])
        elif pp != -1:
            if chislo_s[pp]  ==  chislo_s[j]:
                nov.append([i,chislo_s[j]]) 
            else:
                return []             
        j +=1
    return nov
    #return []

def zdelai_iz_slova_chislo(slova, znach):
    if znach != []:
        chislo = ""
        for i in slova:
            gde = naidi_gde(i,znach)
            chislo += znach[gde][1]
        if chislo[0] != "0":        
            return int(chislo)    
    
#znach =  prisvoi_znachenie_bikvam("CARE", 1296)
#print zdelai_iz_slova_chislo("RACE", znach)

def razdeli(slova):
    nov = list(slova)  
    nov.sort()    
    return nov    

def para(slova1, slova2):
    if len(slova1) > 10 and len(slova2) > 10:
        return 0
    sl1 = razdeli(slova1)
    sl2 = razdeli(slova2)
    if sl1 == sl2:
        return [slova1, slova2]
    else:
        return 0

def dalee(znach):
    for zna in znach:
        chifra = zna[1]
        bukva = zna[0]
        for i in znach:
            if chifra == i[1]:
                if bukva != i[0]:
                    if zna != i:
                        return False
    return True

def kan(slova1, slova2):
    m = []
    for i in xrange(2,10000000):
        if len(slova1) < len(str(i*i)):
            break
        elif len(slova1) == len(str(i*i)):
            znach =  prisvoi_znachenie_bikvam(slova1, i*i)
            if znach == []:
                continue
            if dalee(znach):    
                chislo = zdelai_iz_slova_chislo(slova2, znach)
                if i*i != chislo:
                    if kvadrat_eli_net(chislo):
                        m.append(i*i)
                        m.append(chislo)
    return m            

f = open("words.txt")
ves = f.read()
a = []
e = ""
for i in ves:
    e +=i
    if i == ",":
        ee = e[1:-2]
        a.append(ee)
        e = ""        


pari = []
for i in xrange(len(a)):
    for j in xrange(len(a)):
        if a[i] != a[j]:
            pe = para(a[i] , a[j])
            if pe != 0:
                pari.append(pe)

k = []
for i in pari:
    a = kan(i[0], i[1])
    print i, a
    k.extend(a)
kkk = time.time()       
print max(k), kkk-nnn

