"""
Implementación Búsqueda Primero en Amplitud (BFS)
Agosto 22 de 2024

"""
from collections import deque

def bfsAux(u, G, vis):
  queue = deque()
  vis[u] = True
  queue.append(u)

  while len(queue) > 0:
    v = queue.popleft()
    print(v)
    for w in G[v]:
      if not vis[w]:
        vis[w] = True
        queue.append(w)

def bfs(G):
  vis = [False for _ in range(len(G))]
  for u in range(len(G)):
    if not vis[u]:
      bfsAux(u, G, vis)

def main():
  # Grafo en las anotaciones de clase
  G = [[4, 2], [0], [3, 1], [4], [5, 0, 1, 6], [4, 2, 3], [], [8, 9], [], []]
  bfs(G)
  
main()
