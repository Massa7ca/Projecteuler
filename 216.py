# -*- coding: utf-8 -*-
import time
import math
from random import randrange
import multiprocessing
def is_prime(n, k=10):
    if n <= 3:
        return n == 2 or n == 3
    neg_one = n - 1

    s, d = 0, neg_one
    while not d & 1:
        s, d = s+1, d>>1
    assert 2 ** s * d == neg_one and d & 1

    for i in xrange(k):
        a = randrange(2, neg_one)
        x = pow(a, d, n)
        if x in (1, neg_one):
            continue
        for r in xrange(1, s):
            x = x ** 2 % n
            if x == 1:
                return False
            if x == neg_one:
                break
        else:
            return False
    return True

def prim(procnum, return_dict):
    if procnum == 0:
        c = 0
        for n in xrange(2, 12500000):
            e = is_prime(2*n**2-1)
            if e:
                c += 1
        return_dict[procnum] = c
        
    elif procnum == 1:
        c = 0
        for n in xrange(12500000, 25000000):
            e = is_prime(2*n**2-1)
            if e:
                c += 1
        return_dict[procnum] = c
        
    elif procnum == 2:
        c = 0
        for n in xrange(25000000, 37500000):
            e = is_prime(2*n**2-1)
            if e:
                c += 1
        return_dict[procnum] = c
        
    elif procnum == 3:
        c = 0
        for n in xrange(37500000, 50000000+1):
            e = is_prime(2*n**2-1)
            if e:
                c += 1
        return_dict[procnum] = c
        
def multi(core = 4):
    global return_dict
    jobs = []
    for i in xrange(core):
        proces = multiprocessing.Process(target=prim, args=(i, return_dict))
        jobs.append(proces)
        proces.start()
    
    for proc in jobs:
        proc.join()
        
    ob = 0
    for i in xrange(core):
       ob += return_dict.values()[i]
    return ob


if __name__ == '__main__':
    n = time.time()
    multiprocessing.freeze_support()
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    print multi(core = 4), time.time() - n

    

