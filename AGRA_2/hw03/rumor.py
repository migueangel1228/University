"""
    AGRA  Tarea 2
Fecha  : 25 Agosto 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem B  souvenirs.py

Complejidad computacional "Big-O":

Función solveBinarySearch:

Usa búsqueda binaria sobre k → O(log n) iteraciones.
En cada iteración:

Construcción de listaAux: O(n).
Ordenamiento de listaAux: O(n log n).

Complejidad global:
  + Tiempo: O(n (log n)^2)
  + Espacio: O(n)
  
  
  FALTAAA
"""

from sys import stdin

from collections import deque

def bfsAux(G, vis,nodeId):
  queue = deque()
  vis[nodeId] = True 
  queue.append(nodeId)
  
  while len(queue) > 0:
    v = queue.popleft()
    for w in G[v]:
      if not vis[w]:
        vis[w] = True
        queue.append(w)

def bfs(G,listaCostos):
  ans = 0
  vis = [False for _ in range(len(G))]
  
  for costo, nodeId in listaCostos: # id corecto para iterar en el orden de nodos de menor peso
    if not vis[nodeId]:
      ans += costo
      bfsAux(G, vis,nodeId)
      
  return ans

def main():
    ListOfcase = list(map(int, stdin.readline().split()))
    
    while (ListOfcase[0] != 0 or ListOfcase[1] != 0 ):
        N = ListOfcase[0]
        M = ListOfcase[1]
        i = 0
        listaCostosId = [[_, _] for _ in range(N)] # lista donde cada pos es una pareja (costo,id)
        costos = list(map(int, stdin.readline().split()))
        j = 0
        
        for i in costos: # agregar costos por cada character
            listaCostosId[j][0] = i
            listaCostosId[j][1] = j
            
            j += 1
        listaCostosId.sort(key=lambda x: x[0])
        
        grafo = [[] for _ in range(N)]
        i = 0
        while i < M: # aristas
            arista = list(map(int, stdin.readline().split()))
            grafo[arista[0] - 1].append(arista[1] - 1)
            grafo[arista[1] - 1].append(arista[0] - 1)
            i += 1
        
        print(bfs(grafo,listaCostosId))

        ListOfcase = list(map(int, stdin.readline().split()))

main()

"""

Sample Input
5 2
2 5 3 4 8
1 4
4 5
10 0
1 2 3 4 5 6 7 8 9 10
10 5
1 6 2 7 3 8 4 9 5 10
1 2
3 4
5 6
7 8
9 10
0 0
Sample Output
10
55
15
"""