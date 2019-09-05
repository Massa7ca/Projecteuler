rim = [ ("M" , 1000),
	("CM",  900),
	("D" ,  500),
	("CD",  400),
	("C" ,  100),
	("XC",   90),
	("L" ,   50),
	("XL",   40),
	("X" ,   10),
	("IX",    9),
	("V" ,    5),
	("IV",    4),
	("I" ,    1)]

def iz_rim_v_arab(s, rim): 
    result = 0
    while len(s) > 0:
        for rims, arab in rim:
            if s.startswith(rims):
                result += arab
                s = s[len(rims):]
                break
    return result

def arab_to_rim(chislo, rim):
    ret = ''
    for rims, arab in rim:
        while chislo >= arab:
            ret += rims
            chislo -= arab
    return ret

ee = 0
for line in open("89.txt"):
    if line[-1] == "\n":
        line = line[:-1]
    ar = iz_rim_v_arab(line, rim)
    ri = arab_to_rim(ar, rim)
    ee += len(line) - len(ri)

print ee
