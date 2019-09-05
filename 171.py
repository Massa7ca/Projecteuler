from math import factorial,sqrt

kvadrati = {}
for i in xrange(10):
    kvadrati[i] = (i**2)

def v_int(sp):
    a = ""
    for i in sp:
        a +=str(i)
    return a

def kvadrat_iline(spisok):
    suma = 0
    for i in spisok:
        suma += kvadrati[i]   
    e = int(sqrt(suma))
    if e * e == suma:
        return (True,suma)
    return (False,suma)

def slokikaraz(spisak,chislo):
    n = 0
    for i in spisak:
        if i == chislo:
            n +=1
    return n
def vtorie_skobki(chislo):
    chislo_s = str(chislo)
    ch = "1"
    ch = ch * len(chislo_s)
    return int(ch)

def formula(spisok,verx,chislo):
    proiz = 1
    for i in spisok:
        if int(i[0]) == chislo:
            proiz *= factorial(i[1]-1) 
        else:
            proiz *= factorial(i[1]) 
    return  verx / proiz
    
def per_skobki(chislo):
    chislo_s = str(chislo)
    chislo_set = list(set((list(chislo_s))))
    dlina = len(chislo_s) 
    cifra_i_kollichestvo = []
    for i in chislo_set:
        a = slokikaraz(chislo_s,i)
        cifra_i_kollichestvo.append([i,a])
    fakt = factorial(dlina-1)    
    k = 0
    for i in cifra_i_kollichestvo:
        k += int(i[0])*formula(cifra_i_kollichestvo, fakt,int(i[0]))    
    return k


def suma(chsilo):
    return per_skobki(chsilo) * vtorie_skobki(chsilo)

s = 0
for i in xrange(10):
    for i1 in xrange(i,10):
        for i2 in xrange(i1,10):
            print i,i1,i2
            for i3 in xrange(i2,10):
                for i4 in xrange(i3,10):
                    for i5 in xrange(i4,10):
                        for i6 in xrange(i5,10):
                            for i7 in xrange(i6,10):
                                for i8 in xrange(i7,10):
                                    for i9 in xrange(i8,10):
                                        for i10 in xrange(i9,10):
                                            for i11 in xrange(i10,10):
                                                for i12 in xrange(i11,10):
                                                    for i13 in xrange(i12,10):
                                                        for i14 in xrange(i13,10):
                                                            for i15 in xrange(i14,10):
                                                                for i16 in xrange(i15,10):
                                                                    for i17 in xrange(i16,10):
                                                                        for i18 in xrange(i17,10):
                                                                            for i19 in xrange(i18,10):
                                                                                a = [i,i1,i2,i3,i4,i5,i6,
                                                                                    i7,i8,i9,i10,i11,i12,
                                                                                    i13,i14,i15,i16,
                                                                                    i17,i18,i19]
                                                                                istina,cislo = kvadrat_iline(a)
                                                                                if istina:
                                                                                    s += suma(v_int(a))
print s
