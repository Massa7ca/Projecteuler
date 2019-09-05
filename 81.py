# 3244 I nasaite
from time import time
matricha = []
import copy
nnnnn = time()
def razdeli(straka):
    nov = []
    n = ""
    for i in straka:
        n += i
        if i == ",":
            nov.append(int(n[:-1]))
            n = ""
    return nov

f = open("81.txt")
for liniya in f:
    matricha.append(razdeli(liniya))
def sasedi(kord, mat):
    # if kord = (9,9)
    # to (8, 9) (9, 8)  
    st, n = kord[0], kord[1]
    a = [(st-1, n), (st, n-1)]
    nov = []
    for i in a:
        try:
            if i[0] != -1:
                if i[1] != -1:
                    bb = mat[i[0]][i[1]]
                    nov.append(i)
        except IndexError:
            pass
    return nov

def sam_puti(nac,kan):
    puti = [(len(kan)-1,len(kan)-1)]
    a = 0
    while True:
        kord = puti[a] 
        zak = False
        samo_chislo = kan[kord[0]][kord[1]]
        sos = sasedi(kord, kan)
        for i in sos:
            chislo_s = nac[kord[0]][kord[1]]
            if samo_chislo - chislo_s == kan[i[0]][i[1]]:
                puti.append(i)
                if i == (0, 0):
                    zak = True
                break
        if zak:
            break        
        a +=1
    puti.reverse()
    return puti 

#print matricha
def nachni(matricha):
    ma_nov = matricha
    s = 0
    for i in xrange(len(matricha)):
        s += ma_nov[0][i]
        ma_nov[0][i] = s
    s = 0    
    for i in xrange(len(matricha)):
        s += ma_nov[i][0]
        ma_nov[i][0] = s
    return ma_nov

def vt(st,n):
    #428 = (1,1)
    return [st+1,n-1]

def prv_vn(st,n, st1, n1):
    return [st1,n]

#mam = copy.deepcopy(matricha)
def kan(matricha):
    nov = matricha
    for i in xrange(len(matricha)-1):
        for j in xrange(1,len(matricha)):
            # nov NOVAYA
            kord = vt(i,j)
            per = nov[i][j]#804
            vtor = nov[kord[0]][kord[1]]#332
            
            kord_tr = prv_vn(i,j, kord[0], kord[1])
            
            tretiy = matricha[kord_tr[0]][kord_tr[1]]
            min_sribi_p_v = [per,vtor]
            nov[kord_tr[0]][kord_tr[1]] = min(min_sribi_p_v)+tretiy
    return nov
a = nachni(matricha)
ae = kan(a)
print ae[-1][-1], time()-nnnnn

#pp = sam_puti(mam,ae)
#for i in pp:
#    print mam[i[0]][i[1]],
