n = 0
for i in xrange(2,1001):
    print n
    for j in xrange(2,1001):
        aa = i**j
        aa_s = str(aa)
        if len(aa_s) == j:
            n +=1
