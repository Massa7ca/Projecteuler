def formula(a, n):
    return (pow(a-1, n, a**2) + pow(a+1, n, a**2)) % (a**2)

def maxT(a):
    limit = 3000
    xx = [0, 0]
    while True:
        limit += 1
        t = []
        for n in range(1, limit):
            t.append(formula(a, n))
        xx.append(max(t))
        if xx[-1] == xx[-2]:
            return xx[-1]

all = []
for a in range(3, 1001):
    all.append(maxT(a))

print(sum(all))
