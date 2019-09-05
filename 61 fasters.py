import copy, time

def f3(n): return n*(n+1)/2
def f4(n): return n**2
def f5(n): return n*(3*n-1)/2
def f6(n): return n*(2*n-1)
def f7(n): return n*(5*n-3)/2
def f8(n): return n*(3*n-2)
   
def listi(fun):
    per = {}
    for i in xrange(1,1000):
        chislo = fun(i)
        if chislo > 10000:
            break
        elif chislo >= 1000:
            per_2_chisla = chislo / 100
            try:
                aa = per[per_2_chisla]
                aa.append(chislo)
                per[per_2_chisla] = aa
            except KeyError:
                per[per_2_chisla] = [chislo]
    return per

def esri_li(list_lisov, chislo):
    pos_2_chisla = chislo % 100
    esti = []
    for lis in list_lisov:
        try:
            e = lis[pos_2_chisla]
            esti.extend(e)
        except KeyError:
            pass
    return esti

def v_kavom(chislo, list_lisov):
    for i in xrange(len(list_lisov)):
        if chislo in list_lisov[i]:
            return i
    return -1

def uderi(chisla, list_lisov_c):
    ee = []
    for chislo in chisla:
        index = v_kavom(chislo, list_lisov_c)
        if index == -1:
            return False
        else:
            del list_lisov_c[index]
    return True

n = time.time()

fff3, fff4 = set(f3(i) for i in xrange(45, 141)), set(f4(i) for i in xrange(32, 100))
fff5, fff6 = set(f5(i) for i in xrange(26, 81)), set(f6(i) for i in xrange(23, 71))
fff7, fff8 = set(f7(i) for i in xrange(21, 64)), set(f8(i) for i in xrange(19, 59))

vse = listi(f3), listi(f4), listi(f5), listi(f6), listi(f7), listi(f8)
for chis in fff3:
    a = esri_li(vse, chis)
    for i1 in a:
        a1 = esri_li(vse, i1)
        for i2 in a1:
            a2 = esri_li(vse, i2)
            for i3 in a2:
                a3 = esri_li(vse, i3)
                for i4 in a3:
                    a4 = esri_li(vse, i4)
                    for i5 in a4:
                        aa = [chis, i1, i2, i3, i4, i5]
                        if aa[-1] % 100 == aa[0] / 100:
                            if uderi(aa, [fff3, fff4, fff5, fff6, fff7, fff8]):
                                print aa, sum(aa), time.time() - n

































