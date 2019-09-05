#73162890
def esti(slovari, zna):
    for k, z in slovari.items():
        if k == zna:
            return True
    return False

lines = [list(line)[:-1] for line in open("79.txt")]

slovari = {}
for i in lines:
    for j in i:
        if esti(slovari, j):
            e = slovari[j]
            e.append(float(i.index(j)+1))
        else:
            slovari[j] = [float(i.index(j)+1)]


slo = []    
for k, z in slovari.items():
    slo.append([sum(z)/len(z), k])
slo.sort()
otvet = ""
for i in slo:
    otvet += i[1]
print otvet

