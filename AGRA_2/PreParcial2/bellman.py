"""
Implementación Algoritmo Bellman Ford Moore
Octubre 1 de 2024

"""

from sys import stdin

INF = float("inf")

# Retornar True o False dependiendo de si el grafo tiene o no
# ciclos negativos

# Complejidad: n = |V|, m = |E|  ---> O(n * m)
def bellmanFordMoore(G, s, dist):
    N = len(G)
    dist = [INF for _ in range(N)]
    pred = [-1 for _ in range(N)]
    dist[s] = 0
    i = 0
    while i < N - 1:
        for u in range(N):
            for (v, duv) in G[u]:
                if dist[u] + duv < dist[v]:
                    dist[v] = dist[u] + duv
                    pred[v] = u
            i += 1
    u, ans = 0, False
    while u < N and not ans:
        j = 0
        while j < len(G[u]) and not ans:
            v, duv = G[u][j]
            if dist[u] + duv < dist[v]:
                ans = True
            j += 1
        u += 1
    return ans
def bellmanFordDetCic(G, s, dist):
    N, ciclo = len(G), []
    dist, pred = [float('inf') for _ in range(n)], [-1 for _ in range(n)]
    dist[s] = 0
    for i in range(n):
        t = -1
        for u in range(len(G)):
            for (v, duv) in G[u]:
                if dist[v] > dist[u] + duv:
                    dist[v], pred[v] = dist[u] + duv, u
                    t = v
    if t != -1:
        for i in range(n):
            t = p[t]
            cur, ciclo = t, []
            while cur != t or len(ciclo) == 0:
                ciclo.append(cur)
                cur = p[cur]
    return ciclo
  