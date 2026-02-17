
"""
AGRA   : Tarea 24 marzo 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
D - Problem D tingo-tingo-tango.py 

Complejidad: 
La complejidad del algoritmo es O(N + M)

Dado que se usa DFS para asignar tiempos de descubrimiento y determinar componentes fuertemente conexas.
Cada DFS (para el orden, grafo transpuesto y asignación de componentes) toma O(N + M), 
donde N es el número de nodos y M el número de aristas.

"""

from collections import deque
import sys
sys.setrecursionlimit(1 << 25)

def tarjanAux(grafo, u, tiempo, disc, low, enPila, pila, idComponente):
    disc[u] = low[u] = tiempo
    tiempo += 1
    pila.append(u)
    enPila[u] = True
    
    if u in grafo:
        for v in grafo[u]:
            if disc[v] == -1:
                tiempo = tarjanAux(grafo, v, tiempo, disc, low, enPila, pila, idComponente)
                low[u] = min(low[u], low[v])
            elif enPila[v]:
                low[u] = min(low[u], disc[v])
    
    if low[u] == disc[u]:
        flag = True
        while flag:
            w = pila.pop()
            enPila[w] = False
            idComponente[w] = u
            if w == u:
                flag = False
    return tiempo

def tarjanScc(grafo, n):
    visitado = [-1] * (n + 1)
    low = [-1] * (n + 1)
    enPila = [False] * (n + 1)
    pila = []
    idComponente = [-1] * (n + 1)
    
    tiempo = 0
    for i in range(1, n + 1):
        if visitado[i] == -1:
            tiempo = tarjanAux(grafo, i, tiempo, visitado, low, enPila, pila, idComponente)
    return idComponente

def bfsCaminoMinimo(grafoComponentes, start, end):
    resultado = 0
    encontrado = False
    # para si 0 0
    if start != end:  
        visitado = set()
        cola = deque([(start, 0)])
        visitado.add(start)
        while cola and not encontrado:
            
            actual, remoteness = cola.popleft()
            
            if actual in grafoComponentes:
                for vecino in grafoComponentes[actual]:
                    
                    if not encontrado:  
                        if vecino == end:
                            resultado = remoteness + 1
                            encontrado = True
                        elif vecino not in visitado:
                            visitado.add(vecino)
                            cola.append((vecino, remoteness + 1))
    
    return resultado

def main():
    lines = sys.stdin.readlines()
    index = 0
    shouldExit = False
    
    while index < len(lines) and not shouldExit:
        line = lines[index].strip()
        processCase = True
        
        if not line:
            index += 1
            processCase = False
        else:
            n, m = map(int, line.split())
            if n == 0 and m == 0:
                shouldExit = True
                processCase = False
            
        if processCase:
            zlatan, objetivo = map(int, lines[index + 1].strip().split())
            index += 2
            
            if zlatan < 1 or zlatan > n or objetivo < 1 or objetivo > n:
                print("Zlatan will need the object to pass through 0 groups.")
                index += m
            else:
                grafo = {}
                for _ in range(m):
                    p, q = map(int, lines[index].strip().split())
                    if p not in grafo:
                        grafo[p] = []
                    grafo[p].append(q)
                    index += 1
                
                idComponente = tarjanScc(grafo, n)
                zlatanComp = idComponente[zlatan]
                objetivoComp = idComponente[objetivo]
                
                # Construir grafo Scc 
                grafoComponentes = {}
                
                componentes = set(idComponente[1: n + 1])
                for comp in componentes:
                    grafoComponentes[comp] = set()
                
                for u in grafo:
                    uComp = idComponente[u]
                    for v in grafo[u]:
                        vComp = idComponente[v]
                        if uComp != vComp:
                            if uComp not in grafoComponentes:
                                grafoComponentes[uComp] = set()
                            grafoComponentes[uComp].add(vComp)
                
                remoteness = bfsCaminoMinimo(grafoComponentes, zlatanComp, objetivoComp)
                print(f"Zlatan will need the object to pass through {remoteness} groups.")
main()
