from sys import stdin
from collections import defaultdict

INF = float('inf')

def makeSet(v, p, rango):
    p[v] = v
    rango[v] = 0

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
    
    # Agrupar aristas por peso
    weight_groups = defaultdict(list)
    for neg_w, u, v in aristas:
        weight_groups[-neg_w].append((u, v))
    
    for w in sorted(weight_groups.keys(), reverse=True):
        edges_at_w = weight_groups[w]
        
        # PASO 1: actualizar minInterno para aristas ya internas a un componente
        for u, v in edges_at_w:
            pu = findSet(u, p)
            pv = findSet(v, p)
            if pu == pv:
                if minInterno[pu] > w:
                    minInterno[pu] = w
        
        # PASO 2: fusionar componentes distintos y contar candidatos
        for u, v in edges_at_w:
            pu = findSet(u, p)
            pv = findSet(v, p)
            if pu != pv:
                aux = sz[pu] + sz[pv]
                if minInterno[pu] > w and sz[pu] >= 2:
                    resultado += sz[pu]
                if minInterno[pv] > w and sz[pv] >= 2:
                    resultado += sz[pv]
                unionSet(pu, pv, p, rango)
                pnew = findSet(u, p)
                minInterno[pnew] = w
                sz[pnew] = aux
    
    resultado += n  # V completo siempre es candidato (sin border edges)
    return resultado

def main():
    numCases = int(stdin.readline())
    for _ in range(numCases):
        aristas = []
        numNodes, numAristas = map(int, stdin.readline().split())
        for _ in range(numAristas):
            u, v, w = map(int, stdin.readline().split())
            u -= 1; v -= 1
            aristas.append((-w, u, v))
        print(kruskal(numNodes, aristas))

main()