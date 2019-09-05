chisla = []        
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

f = open("59.txt")
for liniya in f:
  chisla.extend(razdeli(liniya))
#chisla = [97^97, 98^97, 99^97, 100^97]

def dukvi_ili_net(spisak):
    ea = [ord(" "), ord(","), ord("."), ord("!"), ord("?"), ord("-"), ord("("), ord(")"), ord("'"), 
          ord(":"), ord(";"), ord('"')]
    a = set(ea)
    for i in xrange(48,58):
        a.add(i)
    for i in xrange(97,123):
        a.add(i)
    for i in xrange(65,91):
        a.add(i)
    for i in spisak:
        if not i in a:
            return False
    return True
        

def razprinpui(spisak):
    n = ""
    for i in spisak:
        n += chr(i)
    print n

def kofit():
    sp = []
    ad = 0
    while True:
        for i in xrange(3):
            sp.append((i,ad+i))
        if (ad+3) >= len(chisla):
            break
        ad = ad+3
    return sp         
kof = kofit()
#print kof
def rashifrui(a,chisla):
    nov = []
    for i in kof[:len(chisla)]:
        nov.append(a[i[0]] ^ chisla[i[1]])
    return nov
    

for i in xrange(97,123):
    for i_1 in xrange(97,123):
        for i_2 in xrange(97,123):
            a = [i, i_1, i_2]
            text = rashifrui(a,chisla)
            bukvi = dukvi_ili_net(text)
            if bukvi:
                # Text resshifrovalsya v bukvi:
                print "Kluch:", a
                print sum(text)
                razprinpui(text)
