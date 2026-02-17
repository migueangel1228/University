
"""
Tarea  : ADA  Tarea 1 
Fecha  : 14 Febrero 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem C - N + NOD(N)
"""

from sys import stdin

MAX = 1000010  # Dado que se tiene que incluir el 1e6 + 1, es correcto

def binarySearch(A, valueLow, valueHigh):
    # ultimo indice con A[i] <= valueLow
    lowAux, hiAux = -1, len(A)
    while hiAux - lowAux > 1:
        mid = lowAux + (hiAux - lowAux) // 2
        if A[mid] <= valueLow:
            lowAux = mid
        else:
            hiAux = mid
    lowIndx = lowAux  

    # primer indice con A[i] >= valueHigh
    lowAux, hiAux = lowIndx, len(A)
    while hiAux - lowAux > 1:
        mid = lowAux + (hiAux - lowAux) // 2
        if A[mid] < valueHigh:
            lowAux = mid
        else:
            hiAux = mid
    hiIndx = hiAux  

    return hiIndx - lowIndx - 1


def sucesion(Nod):
    # N_0 = 1; 
    # N_i = N_i-1 + NOD(N_i-1)
    N = [1]
    while N[-1] < MAX:
        anterior = N[-1]
        sigueinte = anterior + Nod[anterior]
        N.append(sigueinte)
    return N


# Encuentra el exponente de a en n tal que, n = a^b * c
def numExponent(n, a):
    ans = 0
    if n % a == 0:
        ans = 1 + numExponent(n // a, a) # se le agrega 1 a b
    return ans


def makeNodArray(criba, div):
    nodeArray = [0 for _ in range(MAX)]
    nodeArray[1] = 1
    for n in range(2, MAX):
        if criba[n]:
            nodeArray[n] = 2
        else:
            p = div[n]
            b = numExponent(n, p)
            nodeArray[n] = (b + 1) * nodeArray[n // (p ** b)] 
    return nodeArray


#Se quiere encontrar maximo exponente del divisor primo, a de n
def calculateMaxPrimeFactor():
    criba = [True for _ in range(MAX)]
    div = [None for _ in range(MAX)]
    criba[0] = criba[1] = False

    for j in range(4, MAX, 2):
        criba[j], div[j] = False, 2

    for i in range(3, MAX, 2):
        if criba[i]:
            for j in range(i * i, MAX, i):
                criba[j], div[j] = False, i
    return criba, div


def main():
    # precalculos (una sola vez)
    criba, div = calculateMaxPrimeFactor()
    nod = makeNodArray(criba, div)
    seqN = sucesion(nod)

    totalCases = int(stdin.readline())
    for casito in range(totalCases):
        low, high = map(int, stdin.readline().split())

        # binarySearch incluye al low, yal high, usamos (A-1, B+1)
        ans = binarySearch(seqN, low - 1, high + 1)
        print(f"Case {casito + 1}: {ans}")


main()



"""

Sample Input
3
1 18
1 100
3000 4000
Sample Output
Case 1: 7
Case 2: 20
Case 3: 87
"""
