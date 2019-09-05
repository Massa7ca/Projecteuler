import copy
matrica =  [[1,   2,  3, 4],
            [5,   6,  7, 8],
            [9,  10, 11, 12],
            [13, 14, 15, 16]]

'''matrica = [[7,    53, 183, 439, 863],
           [497, 383, 563,  79, 973],
           [287,  63, 343, 169, 583],
           [627, 343, 773, 959, 943],
           [767, 473, 103, 699, 303]]'''

def remove_stoblec_and_strociku(matrica, kor_chisla):
    strocika = kor_chisla[0]
    stoblec = kor_chisla[1]
    mat = copy.deepcopy(matrica)
    for i in xrange(len(mat)):
        del mat[i][stoblec]
    del mat[strocika]
    return mat
    
def if_matrica_2x2(matrica):
    a = matrica[0][0] + matrica[1][1]
    b = matrica[0][1] + matrica[1][0]
    a = [a, b]
    return max(a)

def kordimati(matrica):
    a = []
    for i in xrange(len(matrica)):
        d = [len(matrica)-1, i]
        a.append(d)
    return a

skolika = len(matrica)
def glav(matrica):
    if len(matrica) == 2:
        return 0
    a = kordimati(matrica)
    for i in a:
        b = remove_stoblec_and_strociku(matrica, i)
        print b


glav(matrica)

#print asasa

#for i in asasa:
#    print i


            
            
