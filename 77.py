import math

def naiti_prostie_menshe(n):
    vsen = [True] * (n + 1)
    prostie = []
    koren = math.sqrt(n)
    p = 2
    while p <= koren:
        prostie.append(p)

        for i in range(p, n + 1, p):
            vsen[i] = False

        for i in range(p, n + 1):
            if vsen[i]:
                p = i
                break

    for i in range(p, n + 1):
        if vsen[i]:
            prostie.append(i)

    return prostie

def varianti(n, chisla):
    history = [1]+[0]*n
    for c in chisla:
        for i, x in enumerate(range(c, n+1)):
            history[x] += history[i]
    return history[n]

prime = naiti_prostie_menshe(10000)
for i in range(1, 1000000):
    if varianti(i, prime) > 5000:
        print(i)
        break
