import math
import csv
v = []
def nam(aa):
    for i in xrange(aa):
        print "PERVOE",i 
        for ii in xrange(aa):
            print "VTOROE",ii
            for iii in xrange(aa):
                for iiii in xrange(aa):
                    for iiiii in xrange(aa):
                        for iiiiii in xrange(aa):
                            for iiiiiii in xrange(aa):
                                for iiiiiiii in xrange(aa):
                                    for iiiiiiiii in xrange(aa):
                                        a = [1,i,2,ii,3,iii,4,iiii,5,iiiii,6,iiiiii,7,iiiiiii,8,iiiiiiii,9,iiiiiiiii,0]
                                        nov = ""
                                        for j in a:
                                            nov += str(j)    
                                        v.append(int(nov))
                
                                        
nam(6)

pasle = []
def nam(aa):
    for i in aa:
        kor = math.sqrt(i)
        if kor % 1 == 0:
            pasle.append(i)   
    print pasle                            
nam(v)

    

