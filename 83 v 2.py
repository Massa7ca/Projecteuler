import time
orig_arr = []
def v_int(straka):
    nov = []
    for i in straka:
        nov.append(int(i))
    return nov

def razdeli(straka):
    nov = []
    n = ""
    for i in straka:
        n += i
        if i == ",":
            nov.append(int(n[:-1]))
            n = ""
    return nov

f = open("83.txt")
for liniya in f:
  orig_arr.append(razdeli(liniya))
nn = time.time()
xsize = len(orig_arr)
ysize = len(orig_arr)

calc_arr = []    
for y in xrange(len(orig_arr)):
    calc_arr.append([99999999999999] * xsize)
 
def array_insert(val, x, y) :
    l = 0
    r = len(walk_array)
    while l < r :
        m = (l+r) / 2
        if walk_array[m][0] > val :
            r = m
        else :
            l = m + 1
    walk_array.insert(l, (val, x, y))
 
def check_cell(x, y, val) :
    if x < 0 or x >= xsize or y < 0 or y >= ysize :
        return
 
    val += orig_arr[y][x]
    if  calc_arr[y][x] > val :
        calc_arr[y][x] = val
        array_insert(val, x, y)
 
calc_arr[0][0] = orig_arr[0][0]
walk_array = [(0, 0, 0)]
 
while len(walk_array) :
    (dummy, x, y) = walk_array[0]
    walk_array = walk_array[1:]
 
    val = calc_arr[y][x]
    check_cell(x+1, y, val)
    check_cell(x-1, y, val)
    check_cell(x, y+1, val)
    check_cell(x, y-1, val)
 
print calc_arr[xsize-1][ysize-1],time.time()-nn 
