"""
AGRA  Tarea 1 Agosto 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem C  snowflakes.py
"""

from sys import stdin

def solve(lista):
    conjunto = set()
    max = 0
    posIzq = 0
    posDer = 0
    conjunto.add(lista[posDer])
    posDer += 1
    while (posDer < len(lista)):
        if(lista[posDer] not in conjunto):
            conjunto.add(lista[posDer])
            posDer += 1
        else:
            if (max < len(conjunto)):
                max = len(conjunto)
            conjunto.remove(lista[posIzq])
            posIzq += 1
            
        if (max < len(conjunto)):
            max = len(conjunto)
    return max

def main():
    casos = int(stdin.readline())
    while (casos > 0):
        NumLineas = int(stdin.readline())
        listaOrigin = []
        while (NumLineas > 0):
            aux = int(stdin.readline())
            listaOrigin.append(aux)
            NumLineas = NumLineas - 1

        print(solve(listaOrigin))
        
        casos = casos - 1

main()

""""
CASE 1
Sample Input
1
5
1
2
3
2
1
Sample Output
3
CASE 2
Sample Input
1
10
1
2
3
1
4
5
2
6
7
8
Sample Output
8
CASE 3
1
18
296
734
748
463
992
23
463
992
371
357
250
324
94
296
357
101
644
371
Sample Output
9
"""