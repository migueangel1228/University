from sys import stdin
from collections import deque

from sys import stdin

def apAux(G,vis,low,p,apNodes,v,t):
    num = 0
    t[0] += 1
    vis[v] = low[v] = t[0]
    for w in G[v]:
        if vis[w] == -1:
            num += 1
            p[w] = v
            apAux(G,vis,low,p,apNodes,w,t)
            low[v] = min(low[v], low[w])
            #verificar si es un punto de articulacion
            if p[v] != -1 and low[w] >= vis[v]:
                apNodes.add(v)
        elif w != p[v]:
            low[v] = min(low[v], vis[w])
    if p[v] == -1 and num > 1:
        apNodes.add(v)
def AP(G,vis,low,p,apNodes):
    n = len(G)
    t = []
    t.append(0)
    for i in range(n):
        if vis[i] == -1:
            apAux(G,vis,low,p,apNodes,i,t)

def bfsAux(G,apNodes,visited,v,distMax):
    visited[v] = True
    q = deque()
    q.append(v)
    capa = 0
    while(len(q) > 0):
        for _ in range(len(q)):
            v = q.popleft()
            for u in G[v]:
                if(not visited[u]):
                    visited[u] = True
                    q.append(u)
                    if (u in apNodes and u != v):
                        if (distMax < capa + 1):
                            distMax = capa + 1

        capa += 1
    return distMax 
def bfs(G,apNodes,listicaApNodes):
    n = len(G)
    ans = 0
    for i in listicaApNodes:
        visited = [False for _ in range(n)]
        distMax = 0
        auxAns = bfsAux(G,apNodes,visited,i,distMax)
        if ans < auxAns:
            ans = auxAns
    return ans
def main():
    lista = list(map(int, stdin.readline().split()))
    
    while (lista and lista[0] != 0 and lista[1] != 0):
        n = lista[0]
        m = lista[1]
        k = list(map(int, stdin.readline().split()))
        G = [[] for _ in range(n)]
        visited = [-1 for _ in range(n)]
        low = [-1 for _ in range(n)]
        p = [-1 for _ in range(n)]
        apNodes = set()

        for _ in range(m):
            u, v = map(int, stdin.readline().split())
            G[u].append(v)
            G[v].append(u)

        AP(G,visited,low,p,apNodes)

        listicaApNodes = []
        for ap in apNodes:
            listicaApNodes.append(ap)
     
        ans = bfs(G,apNodes,listicaApNodes)
        print(ans * k[0])
        lista = list(map(int, stdin.readline().split()))

main()

"""
Sample Input
16 21
100
1 2
1 3
2 3
1 6
6 3
6 7
7 2
3 10
13 10
10 4
9 4
9 10
5 9
5 12
11 15
8 12
11 12
11 8
8 5
0 13
14 13
0 0
Sample Output
500
"""

"""
16 21
1 2
1 3
2 3
1 6
6 3
6 7
7 2
3 10
13 10
10 4
9 4
9 10
5 9
5 12
11 15
8 12
11 12
11 8
8 5
0 13
14 13
"""