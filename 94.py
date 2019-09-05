import math,time
def s(a,b,c):
    s = (a+b+c) /2.0
    if s % 1 != 0:
        return 0.5, 1
    s = int(s)    
    per = s*(s-a)*(s-b)*(s-c)
    return math.sqrt(per),per



suma = 0
per_2 = 2
e = 1000000000
while True:
    if per_2 % 500000 == 0:
        print per_2    
    if (per_2 * 2)+ per_2+1 > e:
        break    
    a, ch = s(per_2,per_2,per_2+1)
    if a % 1 == 0:
        if int(a) * int(a) == ch:
            suma += (per_2 * 2)+ per_2+1
    if (per_2 * 2)+ per_2-1 > e:
        break        
    a, ch = s(per_2,per_2,per_2-1)
    if a % 1 == 0:
        if int(a) * int(a) == ch:
            suma += (per_2 * 2)+ per_2-1
    per_2 +=1
print suma
