import itertools

def test(A, B, C, D, E, F, G, H, I, J, suma):
    comb = [(A, B, C), (D, C, E), (F, E, G), (H, G, I), (J, I, B)]
    for i in comb:
        if sum(i) != suma:
            return ()
    return comb

def exist(slays, all):
    for i in all:
        if slays in i:
            return True
    return False

all = []
chifri = list(range(1, 10+1))
for summma in range(6, 27+1):
    for i in itertools.permutations(chifri):
        A, B, C, D, E, F, G, H, I, J = i
        result = test(A, B, C, D, E, F, G, H, I, J, summma)
        if result != () and not exist(result[0], all) and not exist(result[1], all) \
                        and not exist(result[2], all) and not exist(result[3], all) \
                        and not exist(result[4], all):
            all.append(result)

print(all)
m = []
for i in all:
    s = ""
    for j in i:
        s += "".join([str(x) for x in j])
    if len(s) == 16:
        m.append(int(s))

print("Otvet =", max(m))
print(m)
