a1, a2 = 1, 1
suma = 0
for i in xrange(100):
    if a1 > 4000000:
        break
    if a1 % 2 == 0:
        suma += a1
    AS = a1+a2
    a1 = a2
    a2 = AS
print suma
