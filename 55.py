#!/usr/bin/python
import time
import math

def raz(sp):
    nov = []
    for i in sp:
        nov.append(int(i))
    return nov

def v_int(sp):
    kk = 0
    for j in sp:
        kk = kk*10 + j    
    return str(kk)

def per_int(chi):
    chi_str = str(chi)
    r = raz(chi_str)
    r.reverse()
    return int(v_int(r))

def palindrom(chi):
    chi_s = str(chi)
    if chi_s == "0":
        return True
    elif not len(chi_s) % 2 == 0:
        na_dva = len(chi_s) / 2
        c = raz(chi_s) 
        c.insert(na_dva,int(chi_s[int(na_dva)]))
        vv = v_int(c)
        return palindrom(vv)
    else:
        per = chi_s[:len(chi_s)/2]
        v = chi_s[len(chi_s)/2:]
        vv = raz(v)
        vv.reverse()
        vto = raz(vv)
        vtor = v_int(vto)
        if per == vtor:
            return True
    return False

print palindrom(101101)
