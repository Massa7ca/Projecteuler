import time,itertools
def obshii(spisok1, spisok2):
    return list(set(spisok1) & set(spisok2))   

def pari(n):
    nov = []
    nnn = []
    for i in xrange(2,len(n)):
        for kom in itertools.combinations(n, i):
            a = sum(kom)
            ko = []
            ko.extend(kom)
            ko.append(a)
            ko.append(len(kom))
            nov.append(ko)
            nnn.append(a)
        if len(set(nnn)) != len(nnn):
            return 0
    for i in xrange(len(nov)):
        len_i = nov[i][-1]
        for j in xrange(i,len(nov)):
            if nov[i] != nov[j]:
                if len_i < nov[j][-1] and nov[i][-2] > nov[j][-2]:
                    a = obshii(nov[i], nov[j])
                    if a == []:
                        return 0
                elif len_i > nov[j][-1] and nov[i][-2] < nov[j][-2]:
                    a = obshii(nov[i], nov[j])
                    if a == []:
                        return 0    
    return sum(n)               

try:
    for i in xrange(1,46):
        for i1 in xrange(i+1,46):
            print i,i1
            for i2 in xrange(i1+1,46):
                for i3 in xrange(i2+1,46):
                    for i4 in xrange(i3+1,46):
                        for i5 in xrange(i4+1,46):
                            for i6 in xrange(i5+1,46):
                                a = [i,i1,i2,i3,i4,i5,i6]
                                k = pari(a)
                                if k != 0:
                                    print a
                                    raise StopIteration

except StopIteration:
  print "vishli iz vseh", i, j , k




                            
