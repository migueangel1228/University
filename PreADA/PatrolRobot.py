"""
/*
Nickname: Mianparito
Date:     27/12/25
Topic:    "Grafos implicitos && Grafos de Estados"

https://onlinejudge.org/external/16/1600.pdf
*/

"""
from sys import stdin

from collections import deque

# Abajo/Izquierda/Arriba/Derecha
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def generarVecinos(m,n,x,y):
    result = []
    aux = ()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < m and 0 <= ny < n):
            aux = (nx, ny)
            result.append(aux)
    return result

def movement(x, y, kActual, KMAX, mapa):
    if mapa[x][y] == 0:
        kActual = KMAX
    else:
        kActual = kActual - 1 # gasta un turbo sobre los obstaculos
    ans = None   # valor por defecto
    if kActual >= 0:
        ans = (x, y, kActual)
    return ans

def bfsAux(m, n, KMAX, mapa):
    # cola (x, y, kActual, steps)
    q = deque()
    q.append((0, 0, KMAX, 0))

    # visitados tupla (x, y kActual)
    vis = set() # inicia en cero y lo voy llenando
    vis.add((0, 0, KMAX))

    encontrado = False  # flag para saber si llegamos a destino
    respuesta = -1      # valor default, para printearla en caso de no encontrar camino

    while q and not encontrado:
        x, y, kActual, pasos = q.popleft()

        # happy path
        if (x, y) == (m-1, n-1):
            encontrado = True
            respuesta = pasos
        else:
            # sad Path
            for nx, ny in generarVecinos(m, n, x, y): # cada iter es una posible pos
                nuevoState = movement(nx, ny, kActual, KMAX, mapa)
                if nuevoState is not None:
                    vx, vy, vk = nuevoState # deberia desglosar  el estado 
                    if (vx, vy, vk) not in vis:
                        vis.add((vx, vy, vk))
                        q.append((vx, vy, vk, pasos+1))
    return respuesta

def main():
    cases = stdin.readline()
    for _ in range(int(cases)):
        n , m = map(int, stdin.readline().split())
        K = int(stdin.readline())

        # Llenar el mapa
        mapa = []
        for _ in range(n):
            line = list(map(int, (stdin.readline().split())))
            mapa.append(line)
            

        print(bfsAux(n, m, K, mapa))

main()

"""
Sample Input
3
2 5
0
0 1 0 0 0
0 0 0 1 0
4 6
1
0 1 1 0 0 0
0 0 1 0 1 1
0 1 1 1 1 0
0 1 1 1 0 0
2 2
0
0 1
1 0
Sample Output
7
10
-1

Estado:
Posicion 2d , kActual 

"""