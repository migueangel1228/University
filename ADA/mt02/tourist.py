"""
Estudio : ADA 2026_1 Parcial Practico 2 
Fecha   : 2 Mayo 2026
Nombre  : Miguel Angel Padilla Rosero
Cod     : 8988878

Problem D - Tour Belt
"""

from sys import stdin

INF = float('inf')

# Operaciones Disjoint set
def makeSet(v, p, rango):
    p[v] = v
    rango[v] = 0

# findSet iterativo
def findSet(v, p):
    while v != p[v]:
        p[v] = p[p[v]]
        v = p[v]
    return v

def unionSet(u, v, p, rango):
    if rango[u] < rango[v]:
        u, v = v, u
    p[v] = u
    if rango[u] == rango[v]:
        rango[u] += 1

# Kruskal modificado que calcula directamente el costo de las camaras
def kruskal(n, aristas, minimoPeso, maixmoPeso):
    p = [0] * n
    rango = [0] * n
    sz = {}
    resultado = 0

    for i in range(n):
        makeSet(i, p, rango)
        sz[i] = 1

    # Mayor a menor
    aristas.sort()

    for peso, u, v in aristas:
        peso = -peso
        pu = findSet(u, p)
        pv = findSet(v, p)

        if pu != pv:
            aux = sz[pu] + sz[pv]
            unionSet(pu, pv, p, rango)
            pNew = findSet(u, p)
            sz[pNew] = aux

            menorInterna = INF
            mayorExterna = 0

            for j in range(n):
                minUV = min(minimoPeso[pu][j], minimoPeso[pv][j])
                maxUV = max(maixmoPeso[pu][j], maixmoPeso[pv][j])

                minimoPeso[pNew][j] = minUV
                minimoPeso[j][pNew] = minUV
                maixmoPeso[pNew][j] = maxUV
                maixmoPeso[j][pNew] = maxUV

                if findSet(j, p) == pNew:
                    if minUV < menorInterna:
                        menorInterna = minUV
                else:
                    if maxUV > mayorExterna:
                        mayorExterna = maxUV

            if menorInterna > mayorExterna:
                resultado += sz[pNew]

    return resultado


def main():
    numCases = int(stdin.readline())
    for _ in range(numCases):
        aristas = []
        numNodes, numAristas = map(int, stdin.readline().split())

        pesoMin = [[INF] * numNodes for _ in range(numNodes)]
        pesoMax = [[0]   * numNodes for _ in range(numNodes)]

        for _ in range(numAristas):
            u, v, w = map(int, stdin.readline().split())
            u -= 1
            v -= 1
            aristas.append((-w, u, v))
            
            pesoMin[u][v] = w
            pesoMin[v][u] = w
            pesoMax[u][v] = w
            pesoMax[v][u] = w
            
        resultado = kruskal(numNodes, aristas, pesoMin, pesoMax)
        print(resultado)


main()

"""
Sample Input
2
4 6
1 2 3
2 3 2
4 3 4
1 4 1
2 4 2
1 3 2
8 7
1 2 2
2 3 1
3 4 4
4 5 3
5 6 4
6 7 1
7 8 2
Sample Output
8
20
"""