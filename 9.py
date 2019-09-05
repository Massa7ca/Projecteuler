def proveri(a,b,c):
    if (a**2) + (b**2) == (c**2):
        if a + b + c == 1000:
            print "Otvet",a*b*c
            return True
    else:
        return False


for i in range(500):
    for j in range(i+1,500):
        for e in range(j+1,500):
            proveri(i,j,e)
                
            
