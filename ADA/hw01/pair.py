"""
Tarea  : ADA  Tarea 1 
Fecha  : 17 Febrero 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem D - The Closest Pair Problem
"""
from sys import stdin
from math import sqrt


# Distancia euclidiana
def calculateDistance(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    ans = dx*dx + dy*dy
    return ans


def mergeByY(izqArr, derArr):
    i = 0
    j = 0
    merged = []

    while (i < len(izqArr)) and (j < len(derArr)):
        if izqArr[i][1] <= derArr[j][1]:
            merged.append(izqArr[i])
            i += 1
        else:
            merged.append(derArr[j])
            j += 1

    while i < len(izqArr):
        merged.append(izqArr[i])
        i += 1

    while j < len(derArr):
        merged.append(derArr[j])
        j += 1

    return merged


# Retorna (distancia minima, arreglo ordenado en cuanto a y, para que sea mas eficiente) en A[l:r]

def phi(A, l, r):
    size = r - l
    minimo = 10**30
    ArrSortEnY = []

    # Caso base 2 o 3 puntos
    if (size <= 3):
        segment = A[l:r]
        ArrSortEnY = sorted(segment, key=lambda p: p[1])
        # todos con todos
        i = 0
        while i < size:
            j = i + 1
            while j < size:
                dist = calculateDistance(segment[i], segment[j])
                if dist < minimo:
                    minimo = dist
                j += 1
            i += 1

    # Paso inductivo
    if size > 3:
        mid = (l + r) // 2
        midX = A[mid][0]

        minLeft, leftSortedByY = phi(A, l, mid)
        minRight, rightSortedByY = phi(A, mid, r)

        if minLeft < minRight:
            minimo = minLeft
        else:
            minimo = minRight

        ArrSortEnY = mergeByY(leftSortedByY, rightSortedByY)

        # rectangulo, candidatos tales que (x - midX)^2 < minimo
        canditos = []
        k = 0
        while k < len(ArrSortEnY):
            dx = ArrSortEnY[k][0] - midX
            
            if dx*dx < minimo:
                canditos.append(ArrSortEnY[k])
            k += 1

        # Comparaciones en franja (Por y)
        
        i = 0
        while i < len(canditos):
            j = i + 1
            flag = True

            while (j < len(canditos)) and (flag == True):
                dy = canditos[j][1] - canditos[i][1]
                
                if dy*dy < minimo:
                    dist = calculateDistance(canditos[i], canditos[j])
                    if dist < minimo:
                        minimo = dist
                    j += 1
                else:
                    flag = False

            i += 1
    return (minimo, ArrSortEnY)

def main():
    totalNodes = int(stdin.readline())

    while (totalNodes != 0):
        A = []
        for nodes in range(totalNodes):
            xi, yi = map(float, stdin.readline().split())
            A.append((xi, yi))

        # orden por x
        A.sort()

        ans, _ = phi(A, 0, len(A))

        # 10000^2 = 100000000
        if ans >= 100000000:
            print("INFINITY")
        else:
            print(f"{sqrt(ans):.4f}")

        totalNodes = int(stdin.readline())


main()

"""
Sample Input
3
0 0
10000 10000
20000 20000
5
0 2
6 67
43 71
39 107
189 140
0
Sample Output
INFINITY
36.2215
"""