#B. Blackslex and Showering

from sys import stdin

INF = float("inf")
memoria = {}

def solve(A):
    n = len(A)
    
    calculoDiferencias = 0
    for i in range(n - 1):
        calculoDiferencias += abs(A[i] - A[i + 1])
        
    ans = calculoDiferencias
    
    ans = min(ans, calculoDiferencias - abs(A[0] - A[1]))
    ans = min(ans, calculoDiferencias - abs(A[n - 2] - A[n -1]))

    for i in range(1, n-1):
        actual = calculoDiferencias
        # quito los dos
        actual -= abs(A[i - 1] - A[i])
        actual -= abs(A[i] - A[i + 1])
        
        actual += abs(A[i - 1] - A[i + 1]) 
        ans = min(ans, actual)
    
    return ans

def solucion(listica, i, prev, borrado):
    key = (i, prev, borrado)

    if key in memoria:
        return memoria[key]

    if i == len(listica):
        return 0

    tomar = abs(listica[i] - listica[prev]) + solucion(listica, i + 1, i, borrado)
    mejor = tomar

    if borrado == 0:
        noTomar = solucion(listica, i + 1, prev, 1)
        mejor = tomar if tomar < noTomar else noTomar

    memoria[key] = mejor
    return mejor
    

def main():
    casitos = int(stdin.readline())
    for i in range(casitos):
        n = int(stdin.readline())
        memoria.clear()
        
        listica = list(map(int, stdin.readline().split()))
                
        
        #result = solucion(listica, 0, 0, 0)
        
        result = solve(listica)
        print(result)
main()

"""
Input
3
5
4 15 1 7 9
3
2 4 8
6
11 13 17 19 23 29
Output
11
2
12
"""