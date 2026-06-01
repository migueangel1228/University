"""
Tarea  : ADA  Proyecto 
Fecha  : 27 Mayo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem - A - FujikoMine
"""

from sys import stdin

INF = -10**18

nodosTrans = set()
grafito = []

def encontrarRoot(n, G):
    tienePapa = [False] * n
    i = 0
    root = -1
    encontrado = False

    for u in range(n):
        for v, _ in G[u]:
            tienePapa[v] = True

    while i < n and not encontrado:
        if not tienePapa[i]:
            root = i
            encontrado = True
        i += 1
    return root


def phiMem(u, t, G, mem, sz):
    ans = INF
    estadaoActual = (u, t)
    isTrans = u in nodosTrans

    if estadaoActual in mem:
        ans = mem[estadaoActual]
    else:
        if len(G[u]) == 0:
            if isTrans and t == 1:
                ans = 0
            elif not isTrans and t == 0:
                ans = 0
            else:
                ans = INF
        else:
            mCases = [INF] * (t + 1)

            if isTrans:
                if t >= 1:
                    mCases[1] = 0
                    tUsed = 1
                else:
                    tUsed = 1
            else:
                mCases[0] = 0
                tUsed = 0

            for v, w in G[u]:
                tMax = sz[v]
                avilableNode = min(t, tUsed + tMax)

                node = avilableNode
                while node >= 0:
                    cAvilableNode = min(node, tMax)
                    j = 1
                    while j <= cAvilableNode:
                        hijo = phiMem(v, j, G, mem, sz)
                        papa = mCases[node - j]
                        if hijo != INF and papa != INF:
                            posCoins = papa + hijo + w
                            if posCoins > mCases[node]:
                                mCases[node] = posCoins
                        j += 1
                    node -= 1
                tUsed += tMax
            ans = mCases[t]
        mem[estadaoActual] = ans

    return ans

def findTransmi(root, G, tSize):
    orden = []
    pila = [root]

    while len(pila) > 0:
        u = pila.pop()
        orden.append(u)
        for v, _ in G[u]:
            pila.append(v)

    i = len(orden) - 1
    while i >= 0:
        u = orden[i]
        ans = 1 
        if u in nodosTrans:
            ans = 1
        else:
            ans = 0
        for v, _ in G[u]:
            ans += tSize[v]
        tSize[u] = ans
        i -= 1

def solve_case(n, m, G, queries):
    root = encontrarRoot(n, G)
    size = [0] * n
    findTransmi(root, G, size)

    mem = {}
    res = []
    i = 0
    while i < len(queries):
        query = queries[i]
        maxCoins = 0

        if query <= m:
            if query <= 1:
                maxCoins = 0
            else:
                posStart = 0
                while posStart < n:
                    if posStart in nodosTrans:
                        coins = phiMem(posStart, query, G, mem, size)
                        if coins != INF and coins > maxCoins:
                            maxCoins = coins
                    posStart += 1

        res.append(maxCoins)
        i += 1

    return res


def main():
    global nodosTrans, grafito
    linea = stdin.readline().split()
    while len(linea) > 0:
        n = int(linea[0])
        m = int(linea[1])
        q = int(linea[2])

        grafito = [[] for _ in range(n)]
        i = 0
        while i < n - 1:
            n1, n2, p = map(int, stdin.readline().split())
            grafito[n1].append((n2, p))
            i += 1

        nodosTrans = set(map(int, stdin.readline().split()))
        queries = list(map(int, stdin.readline().split()))

        res = solve_case(n, m, grafito, queries)
        for val in res:
            print(val)

        linea = stdin.readline().split()


if __name__ == "__main__":
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
"""

"""
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