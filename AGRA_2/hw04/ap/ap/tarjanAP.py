"""
Algoritmo de Tarjan (AP)

"""

from sys import stdin

G = [[] for _ in range(50000)]
visited = [False for _ in range(50000)]
low = [-1 for _ in range(50000)]
p = [-1 for _ in range(50000)]
apNodes = set()
t, n = int(), int()

def ap():
    global low, visited, p
    for i in range(n):
        low[i] = visited[i] = p[i] = -1

    for i in range(n):
        if visited[i] == -1:
            apAux(i)

def apAux(v):
    global low, visited, p, apNodos, t
    num = 0
    t += 1
    visited[v] = low[v] = t

    for w in G[v]:
        if visited[w] == -1:
            num += 1
            p[w] = v
            apAux(w);
            low[v] = min(low[v], low[w])

            #verificar si es un punto de articulacion
            if p[v] != -1 and low[w] >= visitado[v]:
                apNodos.add(v)
                
        elif w != p[v]:
            low[v] = min(low[v], visitado[w])

    if p[v] == -1 and numHijos > 1:
        apNodos.add(v)

def main():
    global G
    
    n, m = map(int, stdin.readline().split())

    for i in range(m):
        u, v = map(int, stdin.readline().split())
        G[u].append(v)
        G[v].append(u)

    ap()

    if len(apNodos) == 0:
        print("No hay puntos de articulacion")
    else:
        print("Puntos de Articulacion:")
        print(*apNodos)

main()
