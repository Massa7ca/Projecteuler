import math
n = []
def nam(aa):
    for i in aa:
        kor = math.sqrt(i)
        if kor % 1 == 0:
            n.append(i)
    print n                             
nam([1,2,3,4,5,6,7,8,9,10])



