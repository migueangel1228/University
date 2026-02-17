from sys import stdin
from collections import deque
from heapq import heappush, heappop

"""
K VAMOS A HACER:
1.  Encontrar componentes conexos(puntes y bfs ignorantes puentes, y encuntro el max de cada componente)
2.  Dijkstra desde kenny a todas las estaciones principales estacion mas cercana,  
"""
INF = float('inf')

# Implementación algoritmo de Dijkstra para la versión uno a todos 
def dijkstra(G, s):
    dist = [INF for _ in range(len(G))] 
    print(s)
    dist[s] = 0
    pqueue = list()
    heappush(pqueue,(0, s))# (distancia, node) 
    while len(pqueue) != 0:
        du, u, = heappop(pqueue)
        if dist[u] == du:
            for v, duv in G[u]:
                if duv + du < dist[v]:
                    dist[v] = duv + du 
                    heappush(pqueue, (duv + du, v))
                    print(*pqueue)          
    return dist

# Implementación algoritmo Bridges de Tarjan 
def bridgesAux(G,vis,low,p,bridgesSet,t,v):
    vis[v] = low[v] = t[0]
    t[0] += 1
    for w, dw in G[v]:
        if vis[w] == -1:
            p[w] = v
            bridgesAux(G,vis,low,p,bridgesSet,t,w)
            low[v] = min(low[v], low[w])

            #verificar si es un puente
            if low[w] > vis[v]:
                bridgesSet.add((v, w))
                bridgesSet.add((w, v))   
        elif w != p[v]:
            low[v] = min(low[v], vis[w])

def bridgesTarjan(G,vis,low,p,bridgesSet):
    n = len(G)
    t = [0]
    for i in range(n):
        low[i] = vis[i] = p[i] = -1

    for i in range(n):
        if vis[i] == -1:
            bridgesAux(G,vis,low,p,bridgesSet,t,i)

#  BFS ignorando puentes para encontrar componentes conexos"
def bfsAux(G, vis, i, bridgesSet):
    vis[i] = True
    q = deque()
    q.append(i)
    estacionPrincipal = i

    while len(q) > 0:
        u = q.popleft()
        for v, p in G[u]:
            # Verificar si la arista es un puente
            if not vis[v] and (u, v) not in bridgesSet:
                vis[v] = True
                q.append(v)
                if estacionPrincipal < v:
                    estacionPrincipal = v

    return estacionPrincipal

def bfs(G, bridgesSet):
    #Encuentra Estaciones principales de cada componente conexo, ignorando puentes
    vis = [False for _ in range(len(G))]
    estacionesPrincipales = [] # lista de enteros
    estacionPrincipal = 0
    for i in range(len(G)):
        if not vis[i] and len(G[i]) > 0:  # Si no ha sido visitado y tiene vecinos
            estacionPrincipal = bfsAux(G, vis, i, bridgesSet)
            estacionesPrincipales.append(estacionPrincipal)
    return estacionesPrincipales

def main():
    n, m = map(int, stdin.readline().split())
    n = n + 1
    G = [[] for _ in range(n)]
    vis = [-1 for _ in range(n)]
    low = [-1 for _ in range(n)]
    p = [-1 for _ in range(n)]
    bridgesSet = set()

    # Recibo Entrada
    for i in range(m):
        u, v, w = map(int, stdin.readline().split())
        G[u].append((v,w))
        G[v].append((u,w))
    kenny = int(stdin.readline())

    # Encontrar puentes
    bridgesTarjan(G, vis, low, p, bridgesSet)
    print("PUENTES")
    if len(bridgesSet) == 0:
        print("El grafo no tiene puentes")
    else:
        print(f"Total puentes {len(bridgesSet)}")
        for puente in bridgesSet:
            print(f"{puente[0]} - {puente[1]}")

    # Encontrar componentes conexos ignorando puentes
    componentes = bfs(G, bridgesSet)
    print("ESTACIONES PRINCIPALES")
    print(f"Total E.P {len(componentes)}")
    print(*componentes)


    # Encontrar camino mas corto desde kenny hasta las estaciones
    distancias = dijkstra(G,kenny)
    print(*distancias)

main()
# asumo que kenny esta en la estcion 12
"""
12 18
1 2 5
1 3 11
1 6 3
2 3 3
2 7 2
3 10 12
3 6 7
3 7 4
4 9 3
4 10 5
5 8 3
5 9 11
5 12 1
6 7 6
8 11 5
8 12 6
9 10 10
11 12 4
12
"""