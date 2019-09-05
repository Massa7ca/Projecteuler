import time
vsee = []
asa= set("123456789")
def d(p,v):
   global vse
   p_s = str(p)
   v_s = str(v)
   ot = p * v
   o_s = str(ot)
   vse = o_s + v_s + p_s
   ybir = ybiri_povtor(vse)
   if not len(vse)== 9:
     return
   if len(ybir) == len(vse):
      a = 0
      for i in vse:
          if i in asa:
              a +=1
          else:
              return       
      if a == 9:
            print vse
            vsee.append(ot)
   

def ybiri_povtor(spisak):
    nov = []
    for chislo in spisak:
        if not chislo in nov:
           nov.append(chislo)
    return nov

n = time.time()
for i in xrange(1,31624):
    print i,len(vsee)  
    for j in xrange(1,31624):
        aa = d(i,j)
a = ybiri_povtor(vsee)       
suma = 0
for i in a:
    suma += i
k = time.time()    
print suma ,k-n

