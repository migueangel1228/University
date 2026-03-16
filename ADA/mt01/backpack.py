"""
Tarea  : ADA  Parcial Practico
Fecha  : 13 Marzo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem A - Winterim Backpacking Trip

"""

from sys import stdin

distancias = []
N = 0
K = 0
INF = float('inf')
memo = []
tab = []

# devuelve un bool que corresponde a "¿se puede hacer un recorrido sin que ninguna dia se walkee mas de 'w' miles?"
def isPossible(n):
    k, i, cnt, paila = K, 0, 0, False

    while (i < N + 1) and (not paila):
        if cnt + distancias[i] > n:
            if k > 0:
                k -= 1
                cnt = distancias[i]
            else:
                paila = True
        else:
            cnt += distancias[i]
        
        i += 1
    if paila:
        ans = False
    else:
        ans = True
        
    return ans
def main():
    casito = stdin.readline().strip()
    global distancias, N, K, memo, tab
    
    while(casito != ""):
        N, K = list(map(int,casito.split()))
        distancias = []
        for _ in range(N + 1):
            aux = int(stdin.readline())
            distancias.append(aux)
            
        r = sum(distancias)
        l = max(distancias)
        ans = 0
        while r - l >= 1 :
            candidato = (l + r) // 2

            if (isPossible(candidato)):
                r = candidato
            else:
                l = candidato + 1

        print(l)

        casito = stdin.readline().strip()

main()




"""
Sample Input
4 3
7
2
6
4
5
Sample Output
8
"""
