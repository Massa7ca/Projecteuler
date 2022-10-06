def _78_(n, dil):
    history = [1] + [0] * n
    for t in range(1, n + 1):
        for i, x in enumerate(range(t, n + 1)):
            history[x] += history[i]
        if history[t] % dil == 0:
            return t
        if t % 100 == 0:
            print(t)

print(_78_(100000, 1000000))
# 11224 - 100000
# 599 - 10000

