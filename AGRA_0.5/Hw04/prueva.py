from collections import deque
import sys
sys.setrecursionlimit(1 << 25)

def tarjan_aux(grafo, u, tiempo, disc, low, en_pila, pila, id_componente):
    disc[u] = low[u] = tiempo
    tiempo += 1
    pila.append(u)
    en_pila[u] = True
    
    for v in grafo.get(u, []):  # Usamos .get() para evitar KeyError
        if disc[v] == -1:
            tiempo = tarjan_aux(grafo, v, tiempo, disc, low, en_pila, pila, id_componente)
            low[u] = min(low[u], low[v])
        elif en_pila[v]:
            low[u] = min(low[u], disc[v])
    
    if low[u] == disc[u]:
        while True:
            w = pila.pop()
            en_pila[w] = False
            id_componente[w] = u
            if w == u:
                break
    return tiempo

def tarjan_scc(grafo, n):
    disc = [-1] * (n + 1)
    low = [-1] * (n + 1)
    en_pila = [False] * (n + 1)
    pila = []
    id_componente = [-1] * (n + 1)
    
    tiempo = 0
    for i in range(1, n + 1):
        if disc[i] == -1:
            tiempo = tarjan_aux(grafo, i, tiempo, disc, low, en_pila, pila, id_componente)
    return id_componente

def bfs_camino_minimo(grafo_componentes, start, end):
    if start == end:
        return 0
    
    visitado = set()
    cola = deque([(start, 0)])
    visitado.add(start)
    
    while cola:
        actual, dist = cola.popleft()
        for vecino in grafo_componentes.get(actual, set()):  # Usamos .get()
            if vecino == end:
                return dist + 1
            if vecino not in visitado:
                visitado.add(vecino)
                cola.append((vecino, dist + 1))
    return 0  # Asume que siempre hay camino según el problema

def process_test_case(lines):
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        
        zlatan, objetivo = map(int, lines[index + 1].strip().split())
        index += 2
        
        if zlatan < 1 or zlatan > n or objetivo < 1 or objetivo > n:
            print("Zlatan will need the object to pass through 0 groups.")
            index += m
            continue
        
        grafo = {}
        for _ in range(m):
            p, q = map(int, lines[index].strip().split())
            grafo.setdefault(p, []).append(q)  # Reemplazo de defaultdict
            index += 1
        
        id_componente = tarjan_scc(grafo, n)
        
        zlatan_comp = id_componente[zlatan]
        objetivo_comp = id_componente[objetivo]
        
        # Construir grafo de componentes optimizado
        grafo_componentes = {}
        componentes = set(id_componente[1: n+1])
        for comp in componentes:
            grafo_componentes[comp] = set()
        
        for u in grafo:
            u_comp = id_componente[u]
            for v in grafo[u]:
                v_comp = id_componente[v]
                if u_comp != v_comp:
                    grafo_componentes.setdefault(u_comp, set()).add(v_comp)  # Reemplazo de defaultdict
        
        distancia = bfs_camino_minimo(grafo_componentes, zlatan_comp, objetivo_comp)
        print(f"Zlatan will need the object to pass through {distancia} groups.")

def main():
    lines = sys.stdin.readlines()
    process_test_case(lines)

if __name__ == "__main__":
    main()
