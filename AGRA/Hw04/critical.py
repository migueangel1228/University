"""
AGRA   : Tarea 23 marzo 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
A - Problem A critical.py 

Complejidad: 
La complejidad temporal del algoritmo es O(V + E) donde:
- V es el numero de vértices (estaciones)
- E es el numero de aristas (conexiones entre estaciones)

Esto se debe a que:
Usamos DFS para encontrar puntos de articulacion (algoritmo de Tarjan) O(V + E)
Usamos BFS para determinar componentes conexas: O(V + E)
Procesamiento final para encontrar la estacion critica: O(V)

Por lo tanto, la complejidad total es O(V + E).
"""
import sys
from collections import deque

class Graph:
    def __init__(self, n, pasajeros):
        self.n = n
        self.capacities = pasajeros  # capacidad diaria estimada para cada estacion
        # Inicializamos el diccionario con claves de 0 a n-1 y listas vacías como valores
        self.adj = {}
        for i in range(n):
            self.adj[i] = []
    
    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def getConnectedComponents(self):
        """Obtiene las componentes conexas y retorna una lista que asigna a cada nodo
        el tamaño de la componente a la que pertenece."""
        compSize = [0 for _ in range(self.n)]
        visited = [False for _ in range(self.n)]
        
        for i in range(self.n):
            if not visited[i]:
                size = 0
                q = deque([i])
                componentNodes = [i]
                visited[i] = True
                # Bandera para controlar la terminacion del ciclo
                terminarBFS = False
                while not terminarBFS:
                    if len(q) == 0:
                        terminarBFS = True
                    else:
                        cur = q.popleft()
                        size += 1
                        # Usamos un flag para recorrer los vecinos sin usar continue
                        j = 0
                        terminarFor = False
                        while not terminarFor:
                            if j >= len(self.adj[cur]):
                                terminarFor = True
                            else:
                                nei = self.adj[cur][j]
                                if not visited[nei]:
                                    visited[nei] = True
                                    q.append(nei)
                                    componentNodes.append(nei)
                                j += 1
                for node in componentNodes:
                    compSize[node] = size
        return compSize

    def dfsAux(self, u, visitados, sccIndx, parent, ap, time):
        """Funcion auxiliartarjan para puntos de articulacion"""
        adjacentes = 0  # numero de hijos en el DFS
        visitados[u] = sccIndx[u] = time
        time += 1
        i = 0
        finsh = False
        while not finsh:
            if i >= len(self.adj[u]):
                finsh = True
            else:
                v = self.adj[u][i]
                if visitados[v] == -1:  # v no ha sido visitado
                    parent[v] = u
                    adjacentes += 1
                    time = self.dfsAux(v, visitados, sccIndx, parent, ap, time)
                    sccIndx[u] = min(sccIndx[u], sccIndx[v])
                    # Si u no es raíz y no puede alcanzar un ancestro de u
                    if parent[u] != -1 and sccIndx[v] >= visitados[u]:
                        ap[u] = True
                elif v != parent[u]:
                    sccIndx[u] = min(sccIndx[u], visitados[v])
                i += 1
        # Caso especial: si u es raíz y tiene más de 1 hijo
        if parent[u] == -1 and adjacentes > 1:
            ap[u] = True
        return time

    def findArticulationPoints(self):
        """Implementa el algoritmo de Tarjan para hallar puntos de articulacion.
           Retorna una lista booleana de tamaño n, donde True indica que el nodo es crítico."""
        visitados = [-1 for _ in range(self.n)]
        sccIndx = [-1 for _ in range(self.n)]
        adj = [-1 for _ in range(self.n)]
        articulationPoints = [False for _ in range(self.n)]
        t = 0

        i = 0
        terminarFor = False
        while not terminarFor:
            if i >= self.n:
                terminarFor = True
            else:
                if visitados[i] == -1:
                    t = self.dfsAux(i, visitados, sccIndx, adj, articulationPoints, t)
                i += 1
        return articulationPoints

def main():
    results = []
    terminado = False
    # Se usa un flag para controlar la lectura de entrada sin usar break
    while not terminado:
        line = sys.stdin.readline()
        line = line.strip()
        # Flag para determinar si se pudo procesar el bloque actual
        flagBlock = True
        if line == "":
            flagBlock = False
            terminado = True
        else:
            tokens = line.split()
            if len(tokens) != 2:
                flagBlock = False
                terminado = True
            else:
                n, m = map(int, tokens)
        if flagBlock:
            # Leemos las capacidades
            cap_line = sys.stdin.readline().strip()
            if cap_line == "":
                flagBlock = False
                terminado = True
            else:
                capacities = list(map(int, cap_line.split()))
            if flagBlock:
                graph = Graph(n, capacities)
                edgeNum = 0
                # Se utiliza flag para la lectura de aristas
                procesarAristas = True
                while procesarAristas:
                    if edgeNum >= m:
                        procesarAristas = False
                    else:
                        edge_line = sys.stdin.readline().strip()
                        if edge_line == "":
                            procesarAristas = False
                            terminado = True
                        else:
                            parts = edge_line.split()
                            if len(parts) < 2:
                                procesarAristas = False
                                terminado = True
                            else:
                                u, v = map(int, parts)
                                graph.addEdge(u, v)
                                edgeNum += 1
                if flagBlock and not terminado:
                    compSize = graph.getConnectedComponents()
                    articulation = graph.findArticulationPoints()
                    
                    candidato = None  # (disconnect_count, capacity, -id) para comparar
                    candidateIndx = -1
                    i = 0
                    terminarFor = False
                    while not terminarFor:
                        if i >= n:
                            terminarFor = True
                        else:
                            if articulation[i]:
                                disconnect = compSize[i] - 1
                                current = (disconnect, graph.capacities[i], -i)
                                if candidato is None or current > candidato:
                                    candidato = current
                                    candidateIndx = i
                            i += 1
                    if candidato is None:
                        results.append("-1")
                    else:
                        results.append(f"{candidateIndx} {compSize[candidateIndx]-1}")
    print("\n".join(results))
    return

main()
