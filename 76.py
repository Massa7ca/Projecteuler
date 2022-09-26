def _76_(n):
    history = [1]+[0]*n
    for t in range(1, n+1):
        for i, x in enumerate(range(t, n+1)):
            history[x] += history[i]
    return history[-1]


print(_76_(100)-1)
