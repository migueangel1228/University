"""
Nombre: Maria Lucía Castillo García 
Código: 8989484
Fecha: 04/05/26
Parcial 2: Tour Belt
"""

from sys import stdin

INF = float("inf")

padre = []
rango = []
tamComponente = []
sinergiaMin = []
sinergiaMax = []


def makeSet(isla):
    padre[isla] = isla
    rango[isla] = 0
    tamComponente[isla] = 1


def findSet(isla):
    ans = isla
    while ans != padre[ans]:
        padre[ans] = padre[padre[ans]]
        ans = padre[ans]
    return ans


def unionSet(compA, compB):
    if rango[compA] < rango[compB]:
        aux = compA
        compA = compB
        compB = aux
    padre[compB] = compA
    tamComponente[compA] += tamComponente[compB]
    if rango[compA] == rango[compB]:
        rango[compA] += 1
    return compA


def merge(izq, der):
    ans = []
    i = 0
    j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            ans.append(izq[i])
            i += 1
        else:
            ans.append(der[j])
            j += 1
    while i < len(izq):
        ans.append(izq[i])
        i += 1
    while j < len(der):
        ans.append(der[j])
        j += 1
    return ans


def mergeSort(A):
    ans = A
    if len(A) > 1:
        mitad = len(A) // 2
        izq = mergeSort(A[0:mitad])
        der = mergeSort(A[mitad:len(A)])
        ans = merge(izq, der)
    return ans


def ordenarPorMayorSinergia(aristas):
    ordenado = mergeSort(aristas)
    i = 0
    while i < len(aristas):
        aristas[i] = ordenado[i]
        i += 1



def fusionarYEvaluar(n, compA, compB, nuevaComponente):
    menorInterna = INF
    mayorExterna = 0

    j = 0
    while j < n:
        if sinergiaMin[compA][j] < sinergiaMin[compB][j]:
            minAB = sinergiaMin[compA][j]
        else:
            minAB = sinergiaMin[compB][j]

        if sinergiaMax[compA][j] > sinergiaMax[compB][j]:
            maxAB = sinergiaMax[compA][j]
        else:
            maxAB = sinergiaMax[compB][j]

        sinergiaMin[nuevaComponente][j] = minAB
        sinergiaMin[j][nuevaComponente] = minAB
        sinergiaMax[nuevaComponente][j] = maxAB
        sinergiaMax[j][nuevaComponente] = maxAB
        
        if findSet(j) == nuevaComponente:
            if minAB < menorInterna:
                menorInterna = minAB
        else:
            if maxAB > mayorExterna:
                mayorExterna = maxAB
        j += 1
    return menorInterna, mayorExterna



def resolver(n, aristas):
    sumaTamCandidatos = 0
    isla = 0
    while isla < n:
        makeSet(isla)
        isla += 1
    ordenarPorMayorSinergia(aristas)
    i = 0
    while i < len(aristas):
        islaA = aristas[i][1]
        islaB = aristas[i][2]
        compA = findSet(islaA)
        compB = findSet(islaB)
        if compA != compB:
            nuevaComponente = unionSet(compA, compB)
            menorInterna, mayorExterna = fusionarYEvaluar(n, compA, compB, nuevaComponente)
            if menorInterna > mayorExterna:
                sumaTamCandidatos += tamComponente[nuevaComponente]
        i += 1
    return sumaTamCandidatos



def main():
    global padre, rango, tamComponente, sinergiaMin, sinergiaMax
    casos = int(stdin.readline())
    caso = 0
    while caso < casos:
        n, m = map(int, stdin.readline().split())
        padre = [0 for _ in range(n)]
        rango = [0 for _ in range(n)]
        tamComponente = [0 for _ in range(n)]
        sinergiaMin = [[INF for _ in range(n)] for _ in range(n)]
        sinergiaMax = [[0 for _ in range(n)] for _ in range(n)]
        aristas = []

        i = 0
        while i < m:
            u, v, k = map(int, stdin.readline().split())
            aristas.append((-k, u - 1, v - 1))
            sinergiaMin[u - 1][v - 1] = k
            sinergiaMin[v - 1][u - 1] = k
            sinergiaMax[u - 1][v - 1] = k
            sinergiaMax[v - 1][u - 1] = k
            i += 1
        print(resolver(n, aristas))
        caso += 1
main()