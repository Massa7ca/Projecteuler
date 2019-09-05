ob = []
maxx = []
def suma(a):
   nov = 0
   v = a
   while a != 1:
       if a % 2 == 0:
           a /= 2
           nov += 1
       else:
           a = (3 * a) + 1
           nov += 1
   ob.append((nov,v))

for i in xrange(13,1000001):
    if i % 10000 == 0:
       print i
    suma(i)
print max(ob), max(maxx)
