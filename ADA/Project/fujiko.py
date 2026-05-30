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
pesoPadre = []
nodeTipo = []
order = []
sz = []
f = []
bestRoot = []

def contruccion(n, edges, rnode=0):
    global children, parent, pesoPadre, order, sz

    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    children = [[] for _ in range(n)]
    parent = [-1] * n
    pesoPadre = [0] * n
    order = []

    stack = [rnode]
    parent[rnode] = rnode

    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                pesoPadre[v] = w
                children[u].append(v)
                stack.append(v)

    order.reverse()
    
    sz = [0] * n
    for u in order:
        if nodeTipo[u] == 1:
            sz[u] = 1
        for v in children[u]:
            sz[u] += sz[v]

def phiTab(n, m):
    global f, bestRoot
    
    f = [[INF] * (m + 1) for _ in range(n)]
    bestRoot = [[INF] * (m + 1) for _ in range(n)]

    for u in order:
        dp = [[INF] * (m + 1) for _ in range(3)]
        
        if nodeTipo[u] == 1:
            dp[0][1] = 0
            actualSz = 1
        else:
            dp[0][0] = 0
            actualSz = 0

        for v in children[u]:
            w = pesoPadre[v]
            newDP = [row[:] for row in dp]

            limitK = min(m, actualSz)
            limitJ = min(m, sz[v])

            for c in range(3):
                for k in range(limitK + 1):
                    if dp[c][k] != INF:
                        for j in range(1, limitJ + 1):
                            if f[v][j] != INF and k + j <= m:
                                nc = min(2, c + 1)
                                nk = k + j
                                val = dp[c][k] + f[v][j] + w
                                if val > newDP[nc][nk]:
                                    newDP[nc][nk] = val

            dp = newDP
            actualSz += sz[v]

        for k in range(min(m, actualSz) + 1):
            mx = max(dp[0][k], dp[1][k], dp[2][k])
            f[u][k] = mx
            
            if nodeTipo[u] == 1:
                bestRoot[u][k] = mx
            else:
                bestRoot[u][k] = dp[2][k]

def solve(n, m, edges, nodeTipos, queries):
    global nodeTipo
    nodeTipo = nodeTipos

    contruccion(n, edges, 0)
    phiTab(n, m)

    ans = []
    for x in queries:
        if x <= 1 or x > m:
            ans.append(0)
        else:
            best = 0
            for v in range(n):
                if bestRoot[v][x] > best:
                    best = bestRoot[v][x]

            ans.append(best)

    return ans

def main():
    data = list(map(int, stdin.read().split()))
    idx = 0
    flag = True

    while flag and idx + 2 < len(data):
        n = data[idx]
        m = data[idx + 1]
        q = data[idx + 2]
        idx += 3

        edges = []
        need = (n - 1) * 3
        if idx + need > len(data):
            flag = False
        else:
            for _ in range(n - 1):
                u = data[idx]
                v = data[idx + 1]
                w = data[idx + 2]
                edges.append((u, v, w))
                idx += 3

            nodeTipos = [0] * n
            if idx + m > len(data):
                flag = False
            else:
                for _ in range(m):
                    nodeTipos[data[idx]] = 1
                    idx += 1

                queries = []
                if idx + q > len(data):
                    flag = False
                else:
                    for _ in range(q):
                        queries.append(data[idx])
                        idx += 1

                    res = solve(n, m, edges, nodeTipos, queries)

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
"""

"""
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

"""
Sample Input 3
64 17 9
34 43 97
18 51 379
55 31 3
59 41 214
51 5 20
42 21 288
44 20 342
49 34 311
26 39 321
18 14 117
47 0 439
26 32 47
40 9 457
36 19 216
32 61 310
23 35 349
54 7 165
8 59 398
55 25 348
14 8 412
56 46 470
28 33 190
8 40 341
10 58 409
27 38 283
42 52 483
11 22 164
34 3 469
7 28 428
44 27 363
32 1 49
51 2 249
18 54 470
22 45 253
27 18 277
2 12 2
56 4 362
61 47 287
7 29 33
21 17 141
7 11 51
51 49 84
32 30 106
25 15 450
56 13 262
21 23 332
21 53 3
61 44 412
6 42 297
8 36 87
49 50 325
40 37 62
39 62 275
40 60 74
59 48 126
34 56 279
14 16 459
44 10 331
36 57 48
55 63 197
27 6 238
49 55 169
38 24 85
62 35 4 51 14 46 24 45 5 13 16 12 25 63 33 53 10
0 19 39 32 34 57 12 43 54
Sample Output 3
0
0
0
0
0
0
0
0
0
"""

