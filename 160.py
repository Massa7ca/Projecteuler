import time
nnn = time.time()
def sleduiushie_500(na):
    s = 1
    i = na
    e = 1
    while i < na+10:
        e *= i
        i += 1
    return e


def ubiri_nuli(chislo):
    chislo_s = str(chislo)
    j = 0
    for i in xrange(1,len(chislo_s)+1):
        if chislo_s[-i] != "0":
            try:
                return int(chislo_s[0:-j])
            except ValueError:
                return int(chislo_s)
        j +=1

#a[-5:]
#print ubiri_nuli(1)
#16576
s = 1
i = 1
while i != 2560000+1:#1000000000000:
    if i % 500000-1 == 0:
        print i  
    s *= sleduiushie_500(i)
    pa = ubiri_nuli(s)
    pas = pa %100000
    s = pas
    i += 10
print pas,time.time()-nnn

