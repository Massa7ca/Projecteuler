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
                
f = open("names.txt")
ves = f.read()
a = []
e = ""
for i in ves:
    e +=i
    if i == ",":
        ee = e[1:-2]
        a.append(ee)
        e = ""        
alfav = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a.sort()
suma = 0
kakoe_n_faile = 0
print a[936]
for slova in a:
    kakoe_n_faile +=1
    s = znachenie(slova)
    su = kakoe_n_faile * s
    suma += su
print suma    
