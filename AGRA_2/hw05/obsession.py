"""
Implementación Algoritmo Dijkstra
Octubre 1 de 2024
"""
from sys import stdin
from heapq import heappush,heappop

INF = float('inf')

# Implementación algoritmo de Dijkstra para la versión uno a uno 
def dijkstra(G, s, t):
    dist = [(INF, INF) for _ in range(len(G))] # distancias, tuplas de (distPar, distImpar)
    dist[s] = (0, INF)
    pqueue, found = list(), False
    ans = -1
    # for u in range(len(G)): heappush(pqueue, (dist[u], u))
    heappush(pqueue,(0, s, True))# (distancia, node, flag es o no par)
    
    while len(pqueue) != 0 and not found:
        du, u, flagPar  = heappop(pqueue)
        
        # se llego por camino par
        if u == t and flagPar:
            found = True
            ans = du # se que es la distancia valida, por que la flagPar es 1
        else:
            # CASO PAR
            if flagPar and dist[u][0] == du:
                for v, duv in G[u]:
                    nDist = duv + du
                    # CHANGE PAR --> IMPAR
                    if nDist < dist[v][1]:
                        dist[v] = (dist[v][0], nDist) 
                        heappush(pqueue, (nDist, v, False))
            # CASO IMPAR
            elif not flagPar and dist[u][1] == du:
                for v, duv in G[u]:
                    nDist = duv + du
                    # CHANGE IMPAR --> PAR
                    if nDist < dist[v][0]:
                        dist[v] = (nDist, dist[v][1])
                        heappush(pqueue, (nDist, v, True))
                         
    return ans


def main():
    listica = list(map(int, stdin.readline().split()))
    while(len(listica)> 0):
        n = listica[0]
        m = listica[1]
        
        grafito = [[] for _ in range(n + 1)]
        for _ in range(m):
            c1, c2, p = map(int, stdin.readline().split())
            grafito[c1].append((c2,p))
            grafito[c2].append((c1,p))
        
        ans = dijkstra(grafito,1, n)
        
        print(ans)
        listica = list(map(int, stdin.readline().split()))

main()


"""
Sample Input
4 4
1 2 2
2 3 1
2 4 10
3 4 6
5 6
1 2 3
2 3 5
3 5 2
5 1 8
2 4 1
4 5 4
Sample Output
12
-1
"""