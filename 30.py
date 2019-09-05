chisla = []
def nam(aa):
    c = str(aa)
    f = []
    suma = 0
    for ch in c:
        a = int(ch)
        f.append(a)
        suma += (a**5)
    if suma == aa:
        chisla.append(aa)

for i in range(1,2000001):
    nam(i)
print chisla
