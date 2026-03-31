
"""
Tarea  : ADA  Tarea 3
Fecha  : 29 Marzo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem E - Racing
"""

from sys import stdin

# Operaciones Disjoint set
def makeSet(v,p,rango):
    p[v] = v
    rango[v] = 0
    
# def findSet(v,p,rango):
#     if(v == p[v]):
#         ans = v
#     else:
#         p[v] = findSet(p[v],p,rango)
#         ans = p[v]
#     return ans

# intento opt iterativo
def findSet(v, p):
    while v != p[v]:
        p[v] = p[p[v]]  
        v = p[v]
    return v

# def unionSet(u,v,p,rango):
#     u = findSet(u,p,rango)
#     v = findSet(v,p,rango)
    
#     if u != v:
#         if rango[u] < rango[v]:
#             u, v = v, u
        
#         p[v] = u

#         if rango[u] == rango[v]:
#             rango[u] += 1


def unionSet(u, v, p, rango):
    if rango[u] < rango[v]:
        u, v = v, u
    p[v] = u
    if rango[u] == rango[v]:
        rango[u] += 1
        
# Kruskal modificado que calcula directamente el costo de las camaras
def kruskal(n, aristas, total):
    p = [0] * n
    rango = [0] * n
    
    for i in range(n):
        makeSet(i, p, rango)
    
    aristas.sort()
    
    costoSinCamaras = 0
    
    for peso, u, v in aristas:
        pu = findSet(u, p)
        pv = findSet(v, p)
        
        if pu != pv:
            costoSinCamaras += -peso   # peso viene negativo
            unionSet(pu, pv, p, rango)
    costoCamaras = total - costoSinCamaras
    return costoCamaras
    
    
def main():
    
    numCases = int(stdin.readline())
    while (numCases != 0):
        for _ in range(numCases):
            aristas = []
            numNodes, numAristas = map(int,stdin.readline().split())
            total = 0
            for _ in range(numAristas):
                u , v, w = map(int, stdin.readline().split())
                u -= 1
                v -= 1
                aristas.append((-w,u,v))
                # Asumo que todas inicialmente que ninguan aritas pertence al MST 
                total += w
            resultado = kruskal(numNodes, aristas, total)
            print(resultado)
        
        numCases = int(stdin.readline())
                
main()


"""
Sample Input
1
6 7
1 2 5
2 3 3
1 4 5
4 5 4
5 6 4
6 3 3
5 2 3
0
Sample Output
6
"""