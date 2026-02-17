"""
Implementación Algoritmo Caminos más Cortos para DAG

Octubre 1 de 2024

"""
from collections import deque
INF = float("inf")

def toposort(G):
  q, topo, inc = deque(), [], [0 for _ in range(len(G))]
  for u in range(len(G)):
    for v in G[u]:
      inc[v] += 1
  for u in range(len(G)):
    if inc[u] == 0:
      q.append(u)
  while len(q) != 0:
    u = q.popleft()
    topo.append(u)
    for v in G[u]:
      inc[v] -= 1
      if inc[v] == 0:
        q.append(v)
  return topo

# Complejidad: n = |V|, m = |E| ---> O(n + m)
def ssspDAG(G, s):
    dist, pred = [INF for _ in range(len(G))], [-1 for _ in range(len(G))]
    dist[s] = 0
    topo = toposort(G)
    for u in topo:
        for (v, duv) in G[u]:
            if dist[u] + duv < dist[v]:
                dist[v] = dist[u] + duv
                pred[v] = u
    return dist, pred