import copy,prior,time
'''matricha = [[131,   673,  234,  103,  18],
            [201,   96,   342,  965,  150],
            [630,   803,  746,  422,  111],
            [537,   699,  497,  121,  956],
            [805,   732,  524,  37,   331]]'''
mat = []
def v_int(straka):
    nov = []
    for i in straka:
        nov.append(int(i))
    return nov

def razdeli(straka):
    nov = []
    n = ""
    for i in straka:
        n += i
        if i == ",":
            nov.append(int(n[:-1]))
            n = ""
    return nov

f = open("83.txt")
for liniya in f:
  mat.append(razdeli(liniya))

def sasedi(kord, mat):
    # if kord = (1,1)
    # to (0, 1) (1, 0) (2, 1) (1, 2)
    st, n = kord[0], kord[1]
    a = [(st-1, n), (st, n-1), (st+1, n), (st, n+1)]
    nov = []
    for i in a:
        try:
            if i[0] != -1 and i[1] != -1:
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
    #puti.reverse()
    return puti 

def kan(nach, mat):
    nov = copy.deepcopy(mat)
    ################
    ni_zachirk = []
    heap = prior.priority_dict()
    heap[nach] = 131
    izminli = set()
    zacherknuli = set()
    kvadrat = len(mat)**2
    while True:
        nn = []
        sas = sasedi(nach, mat)
        nach_c = nov[nach[0]][nach[1]]
        per_s = sas[0]
        per_c = mat[per_s[0]][per_s[1]]
        vtor_s = sas[1]
        vtor_c = mat[vtor_s[0]][vtor_s[1]]
        if len(sas) == 3 or len(sas) == 4:
            tret_s = sas[2]
            tret_c = mat[tret_s[0]][tret_s[1]]
        if len(sas) == 4:
            chit_s = sas[3]
            chit_c = mat[chit_s[0]][chit_s[1]]

        if not per_s in zacherknuli:
            suma = nach_c + per_c
            if per_s in izminli:
                if nov[per_s[0]][per_s[1]] > suma:
                    nov[per_s[0]][per_s[1]] = suma
                    heap[per_s] = suma
            else:
                nov[per_s[0]][per_s[1]] = suma
                izminli.add(per_s)
                heap[per_s] = suma
                    
        if not vtor_s in zacherknuli:
            suma = nach_c + vtor_c
            if vtor_s in izminli:
                if nov[vtor_s[0]][vtor_s[1]] > suma:
                    nov[vtor_s[0]][vtor_s[1]] = suma
                    heap[vtor_s] = suma
            else:
                nov[vtor_s[0]][vtor_s[1]] = suma
                izminli.add(vtor_s)
                heap[vtor_s] = suma
        
        if len(sas) == 3 or len(sas) == 4:
            if not tret_s in zacherknuli:
                suma = nach_c + tret_c
                if tret_s in izminli:
                    if nov[tret_s[0]][tret_s[1]] > suma:
                        nov[tret_s[0]][tret_s[1]] = suma
                        heap[tret_s] = suma

                else:
                    nov[tret_s[0]][tret_s[1]] = suma
                    izminli.add(tret_s)
                    heap[tret_s] = suma
                    
        if len(sas) == 4:            
            if not chit_s in zacherknuli:
                suma = nach_c + chit_c
                if chit_s in izminli:
                    if nov[chit_s[0]][chit_s[1]] > suma:
                        nov[chit_s[0]][chit_s[1]] = suma
                        heap[chit_s] = suma
                        
                else:
                    nov[chit_s[0]][chit_s[1]] = suma
                    izminli.add(chit_s)
                    heap[chit_s] = suma
                    
        zacherknuli.add(nach)
        del heap[nach]
        if len(zacherknuli) ==  kvadrat:
            break
        nach = heap.smallest()
    return nov
              
#mat = matricha
n = time.time() 
a = kan((0,0), mat)
print a[-1][-1],time.time() - n
a = sam_puti(mat,a)
putii = []
for i in a:
    aea =  mat[i[0]][i[1]]
    print aea,
