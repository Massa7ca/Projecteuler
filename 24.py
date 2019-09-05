sp = []
def k():
    a = "0123456789"
    n = set("0123456789")
    j = 0
    while 1 :
        j += 1
        if j % 100000 == 0:
            print len(sp)
        print sp
        e = 0
        for i in n:
            if i in a:
                e +=1
            else:
                break
        if e == 10:
            m = int(a)    
            sp.append(m)
        m = m + 1    
        if not len(str(m)) == 10:
            a = "0" + str(m)
        else:
            a = str(m)
        if len(sp) == 1000005:
            break
k()
print sp[999999]
