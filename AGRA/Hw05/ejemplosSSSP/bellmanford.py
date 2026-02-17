"""
Implementación Algoritmo de Bellman-Ford-Moore

"""

from collections import deque

"""
G = [[1, 2], [2, 3], [1, 3], []]
w = [[0, 4, 5, float('inf')], [float('inf'), 0, -1, 1], [float('inf'), 2, 0, -1], [float('inf'), float('inf'), float('inf'), float('inf')]]
"""

"""
G = [[1, 2], [2, 3], [3], []]
w = [[0, 5, 3, float('inf')], [float('inf'), 0, -3, 2], [float('inf'), float('inf'), 0, 2], [float('inf'), float('inf'), float('inf'), float('inf')]]
"""

G = [[1, 2], [2, 3], [3, 4], [], [1]]
w = [[0, 5, 3, float('inf'), float('inf')], [float('inf'), 0, -3, 2, float('inf')], [float('inf'), float('inf'), 0, 2, -2], [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')], [float('inf'), 4, float('inf'), float('inf'), 0]]

d, p, ciclo = [], [], []

# Complejidad Temporal = O(n * m)
# Complejidad Espacial = O(n * n)
def bellmanFord(s):
    global d, p
    n, ans = len(G), True
    d = [[float('inf') for _ in range(n)] for _ in range(n)]
    p = [-1 for _ in range(n)]
    
    d[0][s] = 0
    for i in range(1, n):
        for v in range(n):
            d[i][v] = min(d[i][v], d[i - 1][v])
            for u in G[v]:
                if d[i][u] > d[i - 1][v] + w[v][u]:
                    d[i][u] = d[i - 1][v] + w[v][u]
                    p[u] = v
    
    u = 0
    while ans and u < len(G):
        i = 0
        while ans and i < len(G[u]):
            v = G[u][i]
            if d[n - 1][v] > d[n - 1][u] + w[u][v]:
                ans = False
            i += 1
        u += 1

    return ans

# Complejidad Temporal = O(n * m)
# Complejidad Espacial = O(n)
def bellmanFordOpt(s):
    global d, p
    n, ans = len(G), True
    d = [float('inf') for _ in range(n)]
    p = [-1 for _ in range(n)]
    d[s] = 0

    for i in range(1, n):
        for u in range(len(G)):
            for v in G[u]:
                if d[v] > d[u] + w[u][v]:
                    d[v] = d[u] + w[u][v]
                    p[v] = u

    u = 0
    while ans and u < len(G):
        i = 0
        while ans and i < len(G[u]):
            v = G[u][i]
            if d[v] > d[u] + w[u][v]:
                ans = False
            i += 1
        u += 1
    return ans

def bellmanFordOpt2(s):
    global d, p
    n, ans, cola = len(G), True, deque()
    d = [float('inf') for _ in range(n)]
    p = [-1 for _ in range(n)]
    enCola = [False for _ in range(n)]
    conteo = [0 for _ in range(n)]
    d[s] = 0
    cola.append(s)
    enCola[s] = True

    while ans and len(cola) > 0:
        u = cola.popleft()
        enCola[u] = False

        for v in G[u]:
            if d[v] > d[u] + w[u][v]:
                d[v], p[v] = d[u] + w[u][v], u

                if not enCola[v]:
                    cola.append(v)
                    enCola[v] = True
                    conteo[v] += 1

                    if conteo[v] > n:
                        ans = False
    return ans

def bellmanFordDetCic(s):
    global d, p, ciclo
    n, ans = len(G), True
    d = [float('inf') for _ in range(n)]
    p = [-1 for _ in range(n)]
    d[s] = 0

    for i in range(n):
        t = -1
        for u in range(len(G)):
            for v in G[u]:
                if d[v] > d[u] + w[u][v]:
                    d[v], p[v] = d[u] + w[u][v], u
                    t = v

    if t != -1:
        for i in range(n):
            t = p[t]
        cur, ciclo = t, []
        while cur != t or len(ciclo) == 0:
            ciclo.append(cur)
            cur = p[cur]
        ans = False
    return ans

def main():
    if bellmanFord(0):
        print(d, p)
    else:
        print("El grafo tiene ciclos negativos")
    if bellmanFordOpt(0):
        print(d, p)
    else:
        print("El grafo tiene ciclos negativos")
    if bellmanFordOpt2(0):
        print(d, p)
    else:
        print("El grafo tiene ciclos negativos")

    if bellmanFordDetCic(0):
        print(d, p)
    else:
        print("El grafo tiene ciclos negativos")
        print(ciclo)

main()
