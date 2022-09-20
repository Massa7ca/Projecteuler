import math
from fractions import Fraction

potolok = 1000000
const = Fraction(3, 7)
cof = 7 / 3
menihe = None
for n in range(int(potolok//cof), 1, -1):
    print("n =", n, "possible answer =", menihe)
    for b in range(int(n*cof), potolok+1):
        if math.gcd(n, b) == 1:
            drob = Fraction(n, b)
            if drob < const:
                if menihe is None or menihe < drob:
                    menihe = drob
