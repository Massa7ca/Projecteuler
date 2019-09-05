#!/usr/bin/python
import time
import math
def znachenie(slova):
    suma = 0
    alfav = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in slova:
        n_v_alfavite = 0
        for j in alfav:
            n_v_alfavite +=1
            if i == j:
                suma +=n_v_alfavite
    return suma           
                
f = open("42.txt")
ves = f.read()
a = []
e = ""
for i in ves:
    e +=i
    if i == ",":
        ee = e[1:-2]
        a.append(ee)
        e = ""        

triu = []
for i in xrange(40):
    triu.append(i*(i+1)/2)
ss = set(triu)
sss = 0
for i in a:
    a = znachenie(i)
    if a in ss:
        sss +=1
print sss
   
