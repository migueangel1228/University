"""
Algoritmo de Tarjan (Bridges)

"""

from sys import stdin

G = [[] for _ in range(50000)]
visited = [False for _ in range(50000)]
low = [-1 for _ in range(50000)]
p = [-1 for _ in range(50000)]
bridgesSet = set()
t, n = int(), int()

def bridgesTarjan():
    global low, visited, p
    for i in range(n):
        low[i] = visited[i] = p[i] = -1

    for i in range(n):
        if visited[i] == -1:
            bridgesAux(i)

def bridgesAux(v):
    global low, visited, p, bridgesSet, t
    t += 1
    visited[v] = low[v] = t

    for w in G[v]:
        if visited[w] == -1:
            p[w] = v
            bridgesAux(w);
            low[v] = min(low[v], low[w])

            #verificar si es un puente
            if low[w] > visitado[v]:
                bridgesSet.add((v, w))
                
        elif w != p[v]:
            low[v] = min(low[v], visitado[w])

def main():
    global G
    
    n, m = map(int, stdin.readline().split())

    for i in range(m):
        u, v = map(int, stdin.readline().split())
        G[u].append(v)
        G[v].append(u)

    bridgesTarjan()

    if len(bridgesSet) == 0:
        print("El grafo no tiene puentes")
    else:
        print("Total puentes:", len(bridgesSet))
        print(*bridgesSet)

main()
