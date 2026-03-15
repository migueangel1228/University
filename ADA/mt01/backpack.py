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

def phiTabOpt3():
    
    tab = [INF for _ in range(N + 1)]

    sumaPorPartes = [0 for _ in range(N + 2)]
    
    # caso base: k = 0
    for i in range(N, -1, -1):
        sumaPorPartes[i] = distancias[i] + sumaPorPartes[i + 1]
        tab[i] = sumaPorPartes[i]

    # llenar resto de tab
    for k in range(1, K + 1):
        for l in range(0, N + 1):   # ascendente para no dañar tab[r]
            if N - l < k:
                tab[l] = INF
            else:
                ans = INF
                for r in range(l + 1, N - k + 2):
                    aux = max((sumaPorPartes[l] - sumaPorPartes[r]), tab[r])
                    ans = min(ans, aux)
                tab[l] = ans

    return tab[0]


def main():
    casito = stdin.readline().strip()
    global distancias, N, K, memo, tab
    
    while(casito != ""):
        N, K = list(map(int,casito.split()))
        distancias = []
        for _ in range(N + 1):
            aux = int(stdin.readline())
            distancias.append(aux)
        
        respuesta = phiTabOpt3()
        print(respuesta)

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
