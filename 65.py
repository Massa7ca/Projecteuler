from fractions import Fraction

def gen_pos(n):
    a = [2, 1, 2]
    nub = 4
    for i in range(1, n+1):
        if i % 3 == 0:
            a.append(nub)
            nub += 2
        else:
            a.append(1)
    return a[:n]

all = list(reversed(gen_pos(100)))
otvet = Fraction(1, all[0])
for i in all[1:-1]:
    otvet += i
    otvet = Fraction(1, otvet)

otvet += 2
print(f"{otvet}")
print(sum([int(i) for i in str(otvet.numerator)]))

f = Fraction
# print(2)
# print(2 + f(1, 1))
# print(2 + f(1, 1 + f(1, 2)))
# print(2 + f(1, 1 + f(1, 2 + f(1, 1))))
# print(2 + f(1, 1 + f(1, 2 + f(1, 1 + f(1, 1)))))
# print(2 + f(1, 1 + f(1, 2 + f(1, 1 + f(1, 1 + f(1, 4))))))
# print(2 + f(1, 1 + f(1, 2 + f(1, 1 + f(1, 1 + f(1, 4 + f(1, 1)))))))
# print(2 + f(1, 1 + f(1, 2 + f(1, 1 + f(1, 1 + f(1, 4 + f(1, 1 + f(1, 1))))))))

