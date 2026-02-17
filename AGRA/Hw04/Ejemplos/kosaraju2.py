from sys import stdin
from collections import deque

MAX = 10000
adj, adjT = [[] for i in range(MAX)], [[] for i in range(MAX)]
visitados, sccInd = [False for i in range(MAX)], [-1 for i in range(MAX)]
n, numSCC = int(), 0
sccNodos, ord = [], deque()

# Complejidad Temporal : O(n + m)
# Complejidad Espacial : O(n)
def kosaraju():
    global numSCC
    
    # primer DFS --> O(n + m)
    for i in range(n): kosarajuAux(i)

    #O(n)
    for i in range(n): sccInd[i] = -1

    #segundo DFS --> O(n + m)
    numSCC = 0
    for i in range(n):
        if sccInd[ord[i]] == -1:
            numSCC += 1
            sccNodos.append([])
            asignar(ord[i], numSCC)

def kosarajuAux(v):
    if not visitados[v]:
        visitados[v] = True

        for i in range(len(adj[v])):
            kosarajuAux(adj[v][i])

        ord.appendleft(v)

def asignar(u, num):
    sccInd[u] = num
    sccNodos[num - 1].append(u)

    for i in range(len(adjT[u])):
        if sccInd[adjT[u][i]] == -1:
            asignar(adjT[u][i], num)

def main():
    global n
    n, m = list(map(int, stdin.readline().split()))

    for i in range(m):
        u, v = list(map(int, stdin.readline().split()))
        adj[u].append(v)
        adjT[v].append(u)

    print("Grafo")
    for i in range(n):
        print("Nodo %d:" % i)
        for j in range(len(adj[i])):
            print("%d" % adj[i][j], end = ' ')
        print("")

    kosaraju()
    print("Total SCC: %d" % numSCC)

    for i in range(numSCC):
        print("SCC %d: "% (i + 1), end = '')
        print(sccNodos[i])

    for i in range(n):
        print("%d " % sccInd[i], end = '')
    print("")

main()

    
    
