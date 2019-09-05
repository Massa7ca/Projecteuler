def suma(a):
    aa = str(a)
    nov = []
    for i in aa:
        nov.append(int(i))
    return sum(nov)

vse = []
for i in xrange(100):
    for j in xrange(100):
        vse.append(suma(i**j))
print max(vse)       
