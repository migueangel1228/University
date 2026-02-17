from sys import stdin

MAX = 10000
adj = [[] for i in range(MAX)]
visitado, low = [0 for i in range(MAX)], [-1 for i in range(MAX)]
enPila = [False for i in range(MAX)]
n, t, numSCC = int(), 0, 0
sccNodos, pila = [], []

def tarjan():
    for i in range(n):
        low[i], visitado[i], enPila[i] = -1, -1, False

    for i in range(n):
        if visitado[i] == -1:
            tarjanAux(i)

def tarjanAux(v):
    global t, numSCC
    t += 1
    visitado[v], low[v] = t, t
    pila.append(v)
    enPila[v] = True

    for i in range(len(adj[v])):
        w = adj[v][i]
        if visitado[w] == -1:
            tarjanAux(w)
            low[v] = min(low[v], low[w])
        elif enPila[w]:
            low[v] = min(low[v], visitado[w]);

    if low[v] == visitado[v]:
        print("SCC con índice %d: " % low[v], end = '')
        sccNodos.append([])
        numSCC += 1
        while pila[-1] != v:
            a = pila.pop()
            print("%d " % a, end = '')
            enPila[a] = False
            sccNodos[numSCC - 1].append(a)

        a = pila.pop()
        print("%d " % a)
        enPila[a] = False
        sccNodos[numSCC - 1].append(a)

import random

# Constantes y variables globales
MAX = 10000
adj = [[] for _ in range(MAX)]
visitado = [-1 for _ in range(MAX)]
low = [-1 for _ in range(MAX)]
enPila = [False for _ in range(MAX)]
n, t, numSCC = 0, 0, 0
sccNodos = []
pila = []

# Función Tarjan
def tarjan():
    global t, numSCC, sccNodos, pila
    t = 0
    numSCC = 0
    sccNodos = []
    pila = []

    for i in range(n):
        low[i], visitado[i], enPila[i] = -1, -1, False

    for i in range(n):
        if visitado[i] == -1:
            tarjanAux(i)

def tarjanAux(v):
    global t, numSCC
    t += 1
    visitado[v] = low[v] = t
    pila.append(v)
    enPila[v] = True

    for w in adj[v]:
        if visitado[w] == -1:
            tarjanAux(w)
            low[v] = min(low[v], low[w])
        elif enPila[w]:
            low[v] = min(low[v], visitado[w])

    if low[v] == visitado[v]:
        print(f"SCC con índice {low[v]}: ", end='')
        sccNodos.append([])
        numSCC += 1
        while pila[-1] != v:
            a = pila.pop()
            print(f"{a} ", end='')
            enPila[a] = False
            sccNodos[numSCC - 1].append(a)
        a = pila.pop()
        print(f"{a}")
        enPila[a] = False
        sccNodos[numSCC - 1].append(a)

# Generador de grafos aleatorios (dirigidos)
def generar_grafo_tarjan(num_nodos, num_aristas, dirigido=True):
    global n, adj
    n = num_nodos
    adj = [[] for _ in range(MAX)]

    aristas = set()
    while len(aristas) < num_aristas:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v and (u, v) not in aristas:
            adj[u].append(v)
            aristas.add((u, v))
            if not dirigido:
                adj[v].append(u)
                aristas.add((v, u))

# Construcción del grafo condensado
def construir_grafo_condensado():
    sccId = [-1 for _ in range(MAX)]
    for i in range(numSCC):
        for nodo in sccNodos[i]:
            sccId[nodo] = i

    sccAdj = [[] for _ in range(numSCC)]
    sccSet = [set() for _ in range(numSCC)]

    for u in range(n):
        for v in adj[u]:
            if sccId[u] != sccId[v] and sccId[v] not in sccSet[sccId[u]]:
                sccAdj[sccId[u]].append(sccId[v])
                sccSet[sccId[u]].add(sccId[v])

    print("\nGrafo condensado (DAG de SCCs):")
    for i in range(numSCC):
        print(f"SCC {i} -> {sccAdj[i]}")

# -----------------------
# 🔽 Main
# -----------------------

# Genera grafo con 8 nodos y 12 aristas
generar_grafo_tarjan(num_nodos=8, num_aristas=12)

# Muestra el grafo original
print("Grafo original:")
for i in range(n):
    print(f"{i} -> {adj[i]}")

# Ejecuta Tarjan
print("\nComponentes Fuertemente Conexas:")
tarjan()

# Construye el grafo condensado
construir_grafo_condensado()

def main():
    global n
    n, m = list(map(int, stdin.readline().split()))

    for i in range(m):
        u, v = list(map(int, stdin.readline().split()))
        adj[u].append(v)

    print("Grafo")
    for i in range(n):
        print("Nodo %d:" % i)
        for j in range(len(adj[i])):
            print("%d" % adj[i][j], end = ' ')
        print("")

    print("Componentes Fuertemente Conexos:")
    tarjan()

main()

    
    
