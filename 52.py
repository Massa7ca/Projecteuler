
def glav(x,x2,x3,x4,x5,x6):
    a = set(str(x))&set(str(x2))&set(str(x3))&set(str(x4))&set(str(x5))&set(str(x6))
    if len(a) == len(str(x)):
        print x,x2,x3,x4,x5,x6
        return True

for j in xrange(10,5000000):
    if glav(j,j*2,j*3,j*4,j*5,j*6):
        break
