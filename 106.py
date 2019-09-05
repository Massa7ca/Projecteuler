import time,itertools

def obshii(spisok1, spisok2):
    a = len(set(spisok1) & set(spisok2))  
    if a == 0:
        return True
    return False

def vse_bolshe(spisok1, spisok2):
    for i, j in zip(spisok1, spisok2):
        if i < j:
            return True
    return False
            
def nada_ili_net(spisok1, spisok2):
    if vse_bolshe(spisok1, spisok2) and vse_bolshe(spisok2, spisok1):
        return True
    return False            
    
def pari(n):
    kol = 0
    for i in xrange(2,len(n)):
        nov = []
        for kom in itertools.combinations(n, i):
            sp = list(kom)
            sp.sort()
            nov.append(sp)
        for i in xrange(len(nov)):
            spisok1 = nov[i]
            for j in xrange(i+1,len(nov)):
                spisok2 = nov[j]
                if obshii(spisok1, spisok2):
                    if nada_ili_net(spisok1, spisok2):
                        kol +=1
    return kol                            
                       
print pari(range(12))        




                            
