#!/usr/bin/env python

# Ostatochnaya matrica - matrica poluchaemaya stiraniem neskol'kih stolbcov i
# strok iz pervonachal'noy matrici

# Kazhduyu ostatochnuyu matricu mi oboznachaem temi stolbcami kotorie mi ubrali
# iz pervonachal'noy. Stolbci vsegda pokuyutsya v uporyadochenniy kartezh. Iz
# pervonachalnoy matrici mi vsegda uberaem tol'ko nizhnih strok skol'ko i ubrali
# stolbcov.

# Naprimer esli nasha pervonachal'naya martica
# 1  2  3  4 
# 4  6  7  8
# 9  10 11 12
# 13 14 15 16
#
# To ostatochnaya matrica oboznachaemaya (2) eto
# 1  2  4 
# 4  6  8
# 9  10 12
#
# oboznachaemaya (1, 3) eto
# 1 3
# 4 7
#
# oboznachaemaya (0, 2, 3) eto
# 2

import itertools as it

# slovar' otvetov dlya ostatochnih matric.
OTVETI = {}

if 0:
    ORIG = [
        [2, 5, 7, 4],
        [10, 11, 1, 17],
        [10, 11, 1, 5],
        [8, 10, 4, 8]]
else:
    ORIG = [
        [7, 53, 183, 439, 863, 497, 383, 563,  79, 973, 287,  63, 343, 169, 583],
        [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
        [447, 283, 463,  29,  23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
        [217, 623,  3, 399, 853, 407, 103, 983,  89, 463, 290, 516, 212, 462, 350],
        [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
        [870, 456, 192, 162, 593, 473, 915,  45, 989, 873, 823, 965, 425, 329, 803],
        [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
        [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601,  95, 973],
        [445, 721,  11, 525, 473,  65, 511, 164, 138, 672,  18, 428, 154, 448, 848],
        [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
        [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
        [821, 461, 843, 513,  17, 901, 711, 993, 293, 157, 274,  94, 192, 156, 574],
        [ 34, 124,  4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
        [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
        [813, 883, 451, 509, 615,  77, 281, 613, 459, 205, 380, 274, 302,  35, 805]]


L = len(ORIG)
R = range(len(ORIG))
SR = set(range(len(ORIG)))

# Poschitay vse otveti dlya pervogo ryada.
# Mozhesh poprobovat' chto itertools.combinations vidayot sam.
for i, c in enumerate(it.combinations(R, L - 1)):
    ostavshiysya = list(SR - set(c))[0]
    OTVETI[c] = ORIG[0][ostavshiysya]

# Poschitay otveti dlya vseh ryadov ot vtorogo do poslednego.
for rows in range(2, L):
    for i, c in enumerate(it.combinations(R, L - rows)):
        ostavshiysya = list(SR - set(c))
        kandidati = []
        for o in ostavshiysya:
            cc = list(c)
            cc.append(o)
            cc.sort()
            cc = tuple(cc)
            kandidati.append(OTVETI[cc] + ORIG[rows - 1][o])
        OTVETI[c] = max(kandidati)

# Poschitay okonchatel'niy otvet.
k = []
for o in R:
    t = (o,)
    k.append(OTVETI[t] + ORIG[L-1][o])
print "OTVET:", max(k)



