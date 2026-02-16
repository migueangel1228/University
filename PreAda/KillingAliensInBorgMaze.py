"""
/*
Nickname: Mianparito
Date:     21/1/26
Topic:    "Grafos implicitos"

https://onlinejudge.org/external/103/10307.pdf

*/

"""
from sys import stdin

from collections import deque


def makeSet(v,p,rango):
    p[v], rango[v] = v, 0

def findSet(v,p):
    ans = None
    if v == p[v]: ans = v
    else:
        p[v] = findSet(p[v],p)
        ans = p[v]
    return ans

def unionSet(u, v,p,rango):
    u, v = findSet(u,p), findSet(v,p)

    if u != v:
        if rango[u] < rango[v]: u, v = v, u
        p[v] = u
        if rango[u] == rango[v]: rango[u] += 1

def kruskal(aristas, p, rango,n):
    total = 0
    for i in range(n):
        makeSet(i, p, rango)
    aristas.sort()

    for a in aristas:
        w, u, v = a
        fu = findSet(u,p)
        fv = findSet(v,p)

        if findSet(u,p) != findSet(v,p):
            total += w
            unionSet(u, v,p,rango)
    return total

# Abajo/Izquierda/Arriba/Derecha
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def generarVecinos(m, v):
    x, y = v
    rows = len(m)
    result = []
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= ny < rows and 0 <= nx < len(m[ny]) and m[ny][nx] != '#':
            result.append((nx, ny))
    return result

def bfsAux(matriz,G,vis,u,dicNodes):
  queue = deque()
  xu , yu = u
  vis[yu][xu] = 0
  queue.append(u)
  posU = dicNodes[(xu,yu)]

  while len(queue) > 0:
    v = queue.popleft()
    xv , yv = v
    neighbors = generarVecinos(matriz, v)
    for n in neighbors:
        xn, yn = n  
        if vis[yn][xn] == -1:
            cost = vis[yv][xv] + 1
            vis[yn][xn] = cost
            queue.append(n)
            if matriz[yn][xn] == 'A' or matriz[yn][xn] == 'S':
                posN = dicNodes[(xn,yn)]
                # G[posU].append((posN,cost))
                G.append((cost,posU,posN))              
# BFS Todos a todos (siendo todos los aliens y el borg)
def generarGrafo(matriz,posS,posAliens):
    nodos = []
    dicNodes = {}
    i = 0
    nodos.append(posS)
    dicNodes[posS] = i; i += 1
    for a in posAliens:
        nodos.append(a)
        dicNodes[a] = i; i += 1

    n = len(nodos)
    # print(n)
    # G = [[] for _ in range(n)]
    G = []
    for u in nodos:
        vis = [[-1 for _ in fila] for fila in matriz]
        bfsAux(matriz,G,vis,u,dicNodes)
        # print(G)
    return G

def imput(x,y):
    ans = []
    for _ in range(y):
        row = list(stdin.readline().rstrip("\r\n"))
        ans.append(row)
    posStart = ()
    posAliens = []
    
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if (ans[i][j] == 'A'):
                posAliens.append((j,i))
            elif (ans[i][j] == 'S'):
                posStart = (j,i)
    return ans, posStart, posAliens

def main():
    casitos = int(stdin.readline())
    for i in range(casitos):
        x, y = map(int,stdin.readline().split())
        matriz = []
        posAliens = []
        posStart = ()
        matriz, posStart, posAliens = imput(x,y)
        # print(matriz)
        totalNodes = len(posAliens) + 1
        G = generarGrafo(matriz,posStart,posAliens) # grafo lista de aristas
        p, rango = [0 for _ in range(totalNodes)], [0 for _ in range(totalNodes)]
        ans = kruskal(G, p , rango,totalNodes)
        print(ans)
main()

"""
Sample Input
2
6 5
#####
#A#A##
# # A#
#S  ##
#####
7 7
#####
#AAA###
#    A#
# S ###
#     #
#AAA###
#####
Sample Output
8
11
"""
