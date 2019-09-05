import heapq,prior,time
matricha = [[131,   673,  234,  103,  18],
            [201,   96,   342,  965,  150],
            [630,   803,  746,  422,  111],
            [537,   699,  497,  121,  956],
            [805,   732,  524,  37,   331]]

matricha = []
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
  matricha.append(razdeli(liniya))


def kanec(graf, a):
    d = {}
    #p = {}
    for kluch in graf.iterkeys():
        d[kluch] = 10**9
        #p[kluch] = []
    d[a] = 0
    #p[a] = [a]
    heap = prior.priority_dict(d)
    U = set()
    while len(graf) != len(U):
        v = heap.pop_smallest()
        U.add(v)
        for u in graf[v].iterkeys():
            if not u in U:
                if d[u] > d[v] + graf[v][u]:
                    d[u] = d[v] + graf[v][u]
                    heap[u] = d[v] + graf[v][u]
                    #p_k = p[v][:]
                    #p_k.append(u)
                    #p[u] = p_k
    #return p,d
    return d

def matrica_v_graf(mat):
   n = len(mat)
   g = {} # nash graph
   for i in xrange(n):
     for j in xrange(n):
       est_u1 = True
       if j == n-1:
         est_u1 = False
       est_u2 = True
       if i == n-1:
         est_u2 = False
       est_u3 = True
       if j == 0:
         est_u3 = False
       est_u4 = True
       if i == 0:
         est_u4 = False
       
       if est_u1:
         u1 = ((i,j), (i, j+1))
         g[u1] = {}
       if est_u2:
         u2 = ((i,j), (i+1, j))
         g[u2] = {}
       if est_u3:
         u3 = ((i,j-1), (i, j))
       if est_u4:
         u4 = ((i-1, j), (i, j))

           
       # Dobavlyayem ryobra
       if est_u1 and est_u2:
         g[u1][u2] = mat[i][j]
         g[u2][u1] = mat[i][j]
       if est_u1 and est_u3:
         g[u1][u3] = mat[i][j]
         g[u3][u1] = mat[i][j]
       if est_u1 and est_u4:  
         g[u1][u4] = mat[i][j]
         g[u4][u1] = mat[i][j]
       if est_u2 and est_u3:    
         g[u2][u3] = mat[i][j]
         g[u3][u2] = mat[i][j]
       if est_u2 and est_u4:
         g[u2][u4] = mat[i][j]
         g[u4][u2] = mat[i][j]
       if est_u3 and est_u4:
         g[u3][u4] = mat[i][j]
         g[u4][u3] = mat[i][j]
   
   # Dobavim nachalnuyu
   a = ((0,0), (0,0))
   g[a] = {}
   g[a][((0,0), (0,1))] = mat[0][0]
   g[((0,0), (0,1))][a] = mat[0][0]        
   g[a][((0,0), (1,0))] = mat[0][0]
   g[((0,0), (1,0))][a] = mat[0][0]        
   
   b = ((n-1,n-1), (n-1,n-1))
   g[b] = {}
   g[b][((n-2,n-1), (n-1,n-1))] = mat[n-1][n-1]
   g[((n-2,n-1), (n-1,n-1))][b] = mat[n-1][n-1]        
   g[b][((n-1,n-2), (n-1,n-1))] = mat[n-1][n-1]
   g[((n-1,n-2), (n-1,n-1))][b] = mat[n-1][n-1]        
   
   return g
n = time.time()
graf = matrica_v_graf(matricha)
aa =  kanec(graf, ((0,0), (0,0)))
print aa[((79,79), (79,79))],time.time() - n 
