"""
Estudio : ADA 2026_1 Parcial Practico 2 
Fecha   : 2 Mayo 2026
Nombre  : Miguel Angel Padilla Rosero
Cod     : 8988878

Problem D - Tour Belt
"""

from sys import stdin

INF = float('inf')

# Operaciones Disjoint set
def makeSet(v,p,rango):
    p[v] = v
    rango[v] = 0
    
# findSet iterativo
def findSet(v, p):
    while v != p[v]:
        p[v] = p[p[v]]  
        v = p[v]
    return v

def unionSet(u, v, p, rango):
    if rango[u] < rango[v]:
        u, v = v, u
    p[v] = u
    if rango[u] == rango[v]:
        rango[u] += 1
        
# Kruskal modificado que calcula directamente el costo de las camaras
def kruskal(n, aristas):
    p = [0] * n
    rango = [0] * n
    minInterno = {}  
    sz = {}      
    resultado = 0
    
    for i in range(n):
        makeSet(i, p, rango)
        sz[i] = 1
        minInterno[i] = INF  
    # Mayor a menor
    aristas.sort()  
    
    for peso, u, v in aristas:
        peso = -peso
        pu = findSet(u, p)
        pv = findSet(v, p)
        
        if pu != pv:
            aux = sz[pu] + sz[pv]
            if minInterno[pu] > peso:
                resultado += sz[pu]
            if minInterno[pv] > peso:
                resultado += sz[pv]
                
            unionSet(pu, pv, p, rango)
            pnew = findSet(u, p)
            minInterno[pnew] = peso
            sz[pnew] = aux
        else:
            minInterno[pu] = peso
    
    return resultado
    
    
def main():
    numCases = int(stdin.readline())
    for _ in range(numCases):
        aristas = []
        numNodes, numAristas = map(int,stdin.readline().split())
        for _ in range(numAristas):
            u , v, w = map(int, stdin.readline().split())
            u -= 1
            v -= 1
            aristas.append((-w,u,v))

        resultado = kruskal(numNodes, aristas)
        print(resultado)
    
main()
"""
Sample Input
2
4 6
1 2 3
2 3 2
4 3 4
1 4 1
2 4 2
1 3 2
8 7
1 2 2
2 3 1
3 4 4
4 5 3
5 6 4
6 7 1
7 8 2
Sample Output
8
20
"""
