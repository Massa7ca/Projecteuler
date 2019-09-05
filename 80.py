def posle(chislo):
    chislo_s = str(chislo)
    n = ""
    bila = False
    for i in chislo_s:
        if i != '.':
            n+=i
        if len(n) == 100:
            break  
    #if len(n) == 1:
    #    return 0
    suma = 0
    for i in n:
        if i != ".": 
            suma += int(i)
    return suma

import decimal
import math

kk = []
for i in xrange(100):
    kk.append(i**2)

s = 0
for i in xrange(101):
    with decimal.localcontext() as ctx:
        ctx.prec = 202   # Perform a high precision calculation
        if not i in kk: 
            d = decimal.Decimal(i)
            korini = d.sqrt()
            #if not posle(korini) == :
            s += posle(korini)
print s

