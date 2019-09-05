import math
import time
def nam(u):
    pasle = []
    for i in xrange(u):
        print "per", i 
        for ii in xrange(u):
            print "Vt", ii
            for iii in xrange(u):
                for iiii in xrange(u):
                    for iiiii in xrange(u):
                        for iiiiii in xrange(u):
                            for iiiiiii in xrange(u):
                                for iiiiiiii in xrange(0, 10, 2):
                                        a = [1,i,2,ii,3,iii,4,iiii,5,iiiii,6,iiiiii,7,iiiiiii,8,iiiiiiii,9]
                                        kk = 0
                                        for j in a:
                                            kk = kk*10 + j 
                                        #nov = ""
                                        #for j in a:
                                        #    nov += str(j)
                                        #kk = int(nov)
                                        kor = math.sqrt(kk)
                                        if kor % 1 == 0:
                                            kor = int(kor)
                                            if (kor ** 2) == kk:
                                                pasle.append(kk)
                                                print  kor, "i dobav' 0 kogda budesh proveryat' na saite"
    print pasle


nam(10)
