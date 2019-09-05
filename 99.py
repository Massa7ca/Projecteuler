import string
import math
f = file("base_exp.txt");
num = f.readlines();
max = 0.0;
mi = 0;
ma = 0;
mb = 0;
for i in range(0,len(num)-1):
    [a , b] = (num[i]).rsplit(",");
    [a,b] = int(a),int(b);
    n = b*math.log(a,20);
    if n>max:
        mi = i;
        max = n;
        ma = a;
        mb = b;
print (mi+1),' ',max,' ',ma,' ',mb;
