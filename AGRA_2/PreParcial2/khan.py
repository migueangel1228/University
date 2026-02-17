"""
Implementación Algoritmo de Kahn Orden Topológico
Septiembre 19 de 2025

"""
from sys import stdin
from collections import deque

def topoSort(G, inc):
  q, topo = deque(), []
  for i in range(len(G)):
    if inc[i] == 0:
      q.append(i)

  while len(q) != 0:
    u = q.popleft()
    topo.append(u)

    for i in range(len(G[u])):
      v = G[u][i]
      inc[v] -= 1
      if inc[v] == 0:
        q.append(v)
  if len(topo) != len(G): topo = []
  return topo

def main():
  n, m = list(map(int, stdin.readline().split()))
  G, inc = [[] for _ in range(n)], [0 for _ in range(n)]

  for i in range(n):
    vals = list(map(int, stdin.readline().split()))
    u = vals[0]
    for j in range(u):
      v = vals[j + 1]
      G[i].append(v)
      inc[v] += 1

  print("Grafo")
  for i in range(len(G)):
    print("Nodo %d:" % i)
    for j in range(len(G[i])):
      print("%d" % G[i][j], end = ' ')
    print("")

  print("Ordenamiento Topológico:")
  topo = topoSort(G, inc)

  print(*topo)
  #for i in range(len(G)):
    #print("%d" % topo[i], end = ' ')
  #print("")

main()
