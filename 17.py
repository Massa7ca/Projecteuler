slova = {
  0: "",  
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  30: "thirty",
  40: "forty",
  50: "fifty",
  60: "sixty",
  70: "seventy",
  80: "eighty",
  90: "ninety",
  100: "hundred",
  1000: "one thousand"
}

#Vot naprimer 342 - "three hundred and forty two"
def posle_100(chislo):
    n = ""
    chislo_s = str(chislo)
    per = chislo_s[0]
    n += slova[int(per)]
    if chislo % 100 == 0:
       n += "hundred"
    else:
       n += "hundredand"
    return n
    
def posle_20(chislo):
    n = ""
    chislo_s = str(chislo)
    per = chislo_s[0] + "0"
    n += slova[int(per)] 
    vtor = chislo_s[1]
    n += slova[int(vtor)] 
    return n
    
def posle_1(chislo):
    return slova[chislo]  
    
def slovo(i):
    ss = ""
    if i < 20:
        ss += posle_1(i)
    elif i < 100:
        ss += posle_20(i)
    else:
        so = str(i)    
        sot = so[0]
        ss += posle_100(i)
        posle = so[1:]
        if int(posle) < 20:
            ss += posle_1(int(posle))
        elif int(posle) < 100:
            ss += posle_20(int(posle))
    return ss

ss = "onethousand"    
for i in xrange(1, 1000):
    if (i > 99 and i < 103) or (i > 145 and i < 151) or (i > 208 and i < 222):
        print i, slovo(i)
    ss += slovo(i)
print len(ss)    
