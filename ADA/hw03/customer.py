"""
Tarea  : ADA  Tarea 3
Fecha  : 25 Marzo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem C - Keep the Customer Satisfied
"""

from sys import stdin
from heapq import heappush, heappop


# recibe los pedidos ordenados por "fecha entrega" y devuelve el maximo numero de pedidos aceptados
def solution(pedidos):
    tiempoGlobal = 0
    elegidos = []

    for d, q in pedidos:
        if (tiempoGlobal + q <= d):
            heappush(elegidos, (-q, d))
            tiempoGlobal += q

        # si el mas largo aceptado es menor que el nuevo
        # saco el mas largo que habia aceptado y meto el nuevo
        elif (len(elegidos) > 0) and (q < -elegidos[0][0]):
            qMax = -elegidos[0][0]
            tiempoGlobal += q - qMax
            heappop(elegidos)
            heappush(elegidos, (-q, d))

    return len(elegidos)


def main():
    numCasos = int(stdin.readline())
    ans = []
    
    vacio = stdin.readline()
    
    for _ in range(numCasos):
        n = int(stdin.readline())
        tareas = []

        for _ in range(n):
            qAux, dAux = map(int, stdin.readline().split())
            tareas.append((dAux, qAux))

        tareas.sort()
        print(solution(tareas))



main()

"""
Sample Input
1

6
7 15
8 20
6 8
4 9
3 21
5 22
Sample Output
4
"""
