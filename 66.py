import decimal
from decimal import localcontext
#mn = [61, 109, 139, 149, 151, 157, 166, 181, 193, 199, 211, 214, 233, 241, 244, 253, 261, 262, 265, 268, 271, 277, 281, 283, 298, 301, 307, 309, 313, 317, 331, 334, 337, 343, 349, 353, 358, 367, 379, 382, 394, 397, 409, 412, 417, 419, 421, 431, 433, 436, 446, 449, 454, 457, 461, 463, 466, 477, 478, 481, 487, 489, 491, 493, 501, 502, 508, 509, 511, 517, 521, 523, 524, 526, 533, 537, 538, 541, 547, 549, 553, 554, 556, 559, 562, 565, 566, 569, 571, 581, 586, 589, 593, 596, 597, 599, 601, 604, 607, 610, 613, 614, 617, 619, 622, 628, 629, 631, 633, 634, 637, 641, 643, 647, 649, 652, 653, 655, 661, 662, 664, 667, 669, 673, 679, 681, 683, 685, 686, 691, 694, 701, 709, 716, 718, 719, 721, 724, 733, 737, 739, 742, 746, 749, 751, 753, 754, 757, 758, 763, 764, 766, 769, 771, 772, 773, 778, 781, 787, 789, 790, 794, 796, 797, 801, 802, 805, 809, 811, 814, 821, 823, 826, 829, 834, 835, 838, 844, 845, 849, 853, 856, 857, 859, 861, 862, 863, 865, 869, 871, 877, 879, 881, 883, 886, 889, 893, 907, 911, 913, 917, 919, 921, 922, 926, 928, 929, 931, 932, 937, 941, 946, 947, 949, 951, 953, 955, 956, 958, 964, 965, 967, 970, 971, 972, 974, 976, 977, 981, 988, 989, 991, 997, 998, 999]

def find_xy(D):
    with localcontext() as ctx:
        ctx.prec = 100   # Perform a high precision calculation
        DD = decimal.Decimal(D)
        d = DD.sqrt()
        a = []
        for i in xrange(3):
            #print "a", i
            chelaia = int(d)
            drob = d - chelaia
            try:
                d = 1/drob
            except:
                return None
            a.append(chelaia)
        #print a
        h = [a[0]] 
        k = [1]
        h.append(a[0]*a[1]+1)       
        k.append(a[1])
        for i in xrange(2,10000**2):
            chelaia = int(d)
            drob = d - chelaia
            d = 1/drob
            a.append(chelaia)
            h.append(a[i]*h[i-1] + h[i-2])
            k.append(a[i]*k[i-1] + k[i-2])   
            x = h[i]
            y = k[i]
            #print "tyring", i
            if x**2 - D*y**2 == 1:
                 return [x,D,y]

n = []
for i in xrange(1,1000):
    print i
    a = find_xy(i)
    n.append(a)
print max(n)    
