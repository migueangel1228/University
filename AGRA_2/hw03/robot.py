"""
        AGRA  Tarea 3
Fecha  : 7 Septiembre 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem B  robot.py

El algoritmo es un BFS sobre un espacio 2d de n filas y m columnas, que es la posicion (x,y), 
y solo por eso hay n * m posibiles estados a procesar, Dado que proicesar un estado se asume como O(1), 
entonces eso en complejidad temporal O(n*m).

Pero por la existencia de el turbo, y dado que en esta implementacion se modela de tal forma que por cada posicion del mapa 
uno puede llegar en el peor caso con una fraccion del turbo gastado( kActual), entonces da como resultado que la complejiad sea:

El valor de kActual (que puede variar desde 0 hasta KMAX, (el turbo maximo)).

Por lo tanto, el número máximo de estados distintos es:

O(𝑚⋅𝑛⋅(KMAX))

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
posicion 2d , kActual 

Transicion:
"""