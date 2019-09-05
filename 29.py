c = set()
def pros():
    for a in xrange(2,101):
        for b in xrange(2,101):
            c.add(a ** b)
pros()
#def ybiri_povtor(spisak):
#    nov = []
#    for chislo in spisak:
#        if not chislo in nov:
#           nov.append(chislo)
#    return nov


#m = ybiri_povtor(c)
print len(c)

