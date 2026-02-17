"""
Nickname: Mianparito
Date:     3/1/26
Topic:    "Grafos implicitos"

https://onlinejudge.org/external/111/11110.pdf

"""

from sys import stdin
from collections import deque

def imput(N):

    matriz = [[N for _ in range(N)] for _ in range(N)]
    for j in range(0,N - 1):

        line = list(map(int,stdin.readline().split()))
        # print("_____")
        # print(line)
        # print("_____")
        for i in range(0,len(line),2):
            x = line[i] - 1
            y = line[i + 1] - 1
            matriz[x][y] = j + 1
    return matriz

# Abajo/Izquierda/Arriba/Derecha
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def generarNeighbors(matriz,v):
    x = v[0]
    y = v[1]
    result = []
    valor = matriz[x][y]
    n = len(matriz)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < n and 0 <= ny < n):

            if matriz[nx][ny] == valor:
                aux = (nx, ny)
                result.append(aux)
    return result

def bfsAux(matriz, vis, u):
    vis[u[0]][u[1]] = True
    q = deque()
    q.append(u)
    ans = 0
    while(len(q) > 0):
        v = q.popleft()
        ans += 1
        neighbors = generarNeighbors(matriz,v)
        # print("_")
        # print(*neighbors)
        # print("_")
        for nx, ny in neighbors:
            if (not vis[nx][ny]):
                # print("pochoclo")
                vis[nx][ny] = True
                q.append((nx,ny))
    return ans

def solution(matriz,N):
    isEquidivion = True
    vis = [[False for _ in range(N)] for _ in range(N)]
    numPartition = 0
    i = 0
    conjuntito = set()
    while (isEquidivion and i < N):
        j = 0
        while(isEquidivion and j < N):
            if (not vis[i][j] and (matriz[i][j] not in conjuntito)):
                conjuntito.add(matriz[i][j])
                posU = (i, j)
                num = bfsAux(matriz,vis, posU)
                # print(vis)
                numPartition += 1
                if num != N:
                    isEquidivion = False
            j += 1
        i += 1

    if numPartition != N:
        isEquidivion = False

    return isEquidivion


def main():
    N = int(stdin.readline())
    while(N != 0):
        matriz = imput(N)
        # print(matriz)
        ans = solution(matriz,N)
        if ans:
            print("good")
        else:
            print("wrong")
            
            
        N = int(stdin.readline())


main()


"""
Sample Input:
2
1 2 2 1
5
1 1 1 2 1 3 3 2 2 2
2 1 4 2 4 1 5 1 3 1
4 5 5 2 5 3 5 5 5 4
2 5 3 4 3 5 4 3 4 4
5
1 1 1 2 1 3 3 2 2 2
2 1 3 1 4 1 5 1 4 2
4 5 5 2 5 3 5 5 5 4
2 4 1 4 3 5 4 3 4 4
0
Sample Output
wrong
good
wrong
"""