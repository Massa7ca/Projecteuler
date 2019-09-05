t = 0
c, d0, d1, s = 5, 8, 28, 1
while 3*c + s <= 10**9:
    t += 3*c + s
    d0, d1, s = d1, d1*4-d0, -s
    c = (2*s + d1)/6
print t
