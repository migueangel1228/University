from sys import stdin

from collections import deque
# arriba derecha izquierda abajo
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def crearMovimientos(n, m , r, c):
    ans = []
    for i in range (4):
        if 0 <= r + dr[i] < n and 0 <= c + dc[i] < m:
            nr = r + dr[i]
            nc = c + dc[i]
            ans.append((nr, nc))
    return ans


def bfsAux(r, c, mapa, vis, n, m, dic):
    q = deque()
    vis[r][c] = True
    q.append((r,c))
    
    while (len(q) > 0):
        nr, nc = q.popleft()
        listaPosibilidades = crearMovimientos(n, m, nr, nc)
        for movimientoR ,movimientoC in listaPosibilidades:
            if not vis[movimientoR][movimientoC] and mapa[movimientoR][movimientoC] == mapa[r][c]:

                vis[movimientoR][movimientoC] = True
                q.append((movimientoR,movimientoC))

def bfs(mapa, n, m):
    vis = [[False for _ in range(m)] for _ in range(n)]
    dic = {}
    for r in range(n):
        for c in range(m): 
            if (not vis[r][c]):   
                if (mapa[r][c] in dic):
                    dic[mapa[r][c]] += 1
                else:
                    dic[mapa[r][c]] = 1
                bfsAux(r, c, mapa, vis, n, m, dic)
    return dic

def main():
    cases = stdin.readline()
    for _ in range(int(cases)):
            n , m = map(int, stdin.readline().split())
    
            # Llenar el mapa
            mapa = []
            for _ in range(n):
                    line = stdin.readline()
                    mapa.append(line) # mapa de strings
            print(mapa)
            dicionario = {}
            dicionario = bfs(mapa, n, m)
            print(dicionario)
main()



"""
Sample Input
2
4 8
ttuuttdd
ttuuttdd
uuttuudd
uuttuudd
9 9
bbbbbbbbb
aaaaaaaab
bbbbbbbab
baaaaacab
bacccccab
bacbbbcab
bacccccab
baaaaaaab
bbbbbbbbb

Sample Output
World #1
t: 3
u: 3
d: 1
World #2
b: 2
a: 1
c: 1
"""