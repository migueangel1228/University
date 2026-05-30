"""
Tarea  : ADA  Proyecto 
Fecha  : 27 Mayo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem - A - FujikoMine
"""

from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)

INF = -10**18

children = []
parent = []
weight_to_parent = []
node_type = []
order = []
sz = []
f = []
best_root = []

def build_tree(n, edges, root_node=0):
    global children, parent, weight_to_parent, order, sz

    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    children = [[] for _ in range(n)]
    parent = [-1] * n
    weight_to_parent = [0] * n
    order = []

    stack = [root_node]
    parent[root_node] = root_node

    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                weight_to_parent[v] = w
                children[u].append(v)
                stack.append(v)

    order.reverse()
    
    # Precalcular la cantidad máxima de nodos de transmisión en cada subárbol
    sz = [0] * n
    for u in order:
        if node_type[u] == 1:
            sz[u] = 1
        for v in children[u]:
            sz[u] += sz[v]

def phiTab(n, m):
    global f, best_root
    
    # f[u][k] almacena el peso máximo de una rama descendente válida desde 'u'
    f = [[INF] * (m + 1) for _ in range(n)]
    # best_root[u][k] almacena el peso si 'u' es la raíz del Árbol de Steiner
    best_root = [[INF] * (m + 1) for _ in range(n)]

    for u in order:
        # dp[c][k]: c = ramas usadas (0, 1, o >=2), k = nodos de transmisión
        dp = [[INF] * (m + 1) for _ in range(3)]
        
        if node_type[u] == 1:
            dp[0][1] = 0
            current_sz = 1
        else:
            dp[0][0] = 0
            current_sz = 0

        for v in children[u]:
            w = weight_to_parent[v]
            new_dp = [row[:] for row in dp]

            # Optimización O(N^2): Iterar solo hasta los nodos disponibles reales
            limit_k = min(m, current_sz)
            limit_j = min(m, sz[v])

            for c in range(3):
                for k in range(limit_k + 1):
                    if dp[c][k] != INF:
                        # Exigimos j >= 1, previniendo ramas muertas (dead-ends)
                        for j in range(1, limit_j + 1):
                            if f[v][j] != INF and k + j <= m:
                                nc = min(2, c + 1)
                                nk = k + j
                                val = dp[c][k] + f[v][j] + w
                                if val > new_dp[nc][nk]:
                                    new_dp[nc][nk] = val

            dp = new_dp
            current_sz += sz[v]

        for k in range(min(m, current_sz) + 1):
            mx = max(dp[0][k], dp[1][k], dp[2][k])
            f[u][k] = mx
            
            if node_type[u] == 1:
                # Nodo transmisión: puede ser raíz conectando cualquier cantidad de ramas >= 0
                best_root[u][k] = mx
            else:
                # Nodo puente: PARA SER RAÍZ VÁLIDA, debe conectar estricamente >= 2 ramas
                best_root[u][k] = dp[2][k]

def solve_case(n, m, q, edges, nodeTipos, queries):
    global node_type
    node_type = nodeTipos

    build_tree(n, edges, 0)
    phiTab(n, m)

    ans = []
    for x in queries:
        if x <= 1 or x > m:
            ans.append(0)
        else:
            best = 0
            for v in range(n):
                if best_root[v][x] > best:
                    best = best_root[v][x]

            ans.append(best)

    return ans

def main():
    data = list(map(int, stdin.read().split()))
    idx = 0
    more_cases = True

    while more_cases and idx + 2 < len(data):
        n = data[idx]
        m = data[idx + 1]
        q = data[idx + 2]
        idx += 3

        edges = []
        need = (n - 1) * 3
        if idx + need > len(data):
            more_cases = False
        else:
            for _ in range(n - 1):
                u = data[idx]
                v = data[idx + 1]
                w = data[idx + 2]
                edges.append((u, v, w))
                idx += 3

            nodeTipos = [0] * n
            if idx + m > len(data):
                more_cases = False
            else:
                for _ in range(m):
                    nodeTipos[data[idx]] = 1
                    idx += 1

                queries = []
                if idx + q > len(data):
                    more_cases = False
                else:
                    for _ in range(q):
                        queries.append(data[idx])
                        idx += 1

                    res = solve_case(n, m, q, edges, nodeTipos, queries)

                    for val in res:
                        print(val)

main()


"""
Sample Input 1
16 9 5
0 1 20
0 9 30
1 10 40
1 2 20
1 11 100
9 12 25
9 13 5
10 3 30
10 4 10
2 5 15
11 14 40
12 6 25
13 7 5
7 8 5
7 15 10
0 1 2 3 4 5 6 7 8
1 2 3 4 16
2 1 1
1 0 2
1
1
Sample Output 1
0
80
100
170
0
0

Sample Input 2
59 41 15
9 54 223
49 11 348
47 48 113
54 34 417
22 30 361
23 58 360
9 8 99
6 24 453
28 53 105
55 38 225
22 21 188
45 42 89
9 6 399
37 47 84
4 46 152
54 10 347
0 23 284
36 43 312
52 13 468
11 15 203
19 31 21
25 33 34
47 50 239
47 32 318
52 28 259
27 17 243
37 12 22
18 35 135
42 3 173
52 0 325
1 25 448
42 44 3
11 9 500
37 36 349
14 45 490
56 1 146
1 40 493
36 41 133
53 20 475
16 49 494
28 27 446
25 16 24
18 37 71
49 52 363
46 56 186
6 2 37
36 57 44
18 19 90
23 26 337
6 29 476
56 22 377
19 55 301
5 4 453
3 18 424
35 39 335
53 51 461
22 14 74
53 7 399
13 1 21 20 25 5 24 53 28 30 19 54 35 44 55 57 10 33 8 31 41 6 4 12 42 49 45 43 26 51 58 0 46 9 22 47 27 32 3 11 16
4 39 57 51 24 24 27 41 45 41 7 44 5 33 22
Sample Output 2
1826
12224
0
0
9601
9601
10439
12248
0
12248
3142
0
2294
11757
8903
"""
