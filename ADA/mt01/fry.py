"""
Tarea  : ADA  Parcial Practico
Fecha  : 15 Marzo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem C - Philip J. Fry Problem
"""

from sys import stdin

N = None
popos = []
distancias = []
sumaPorPartes = []
memo = []

def phiMemo(i,p):
    global memo

    p = min(p, N)
    if memo[i][p] != -1:
        return memo[i][p]

    if i >= N:
        ans = 0
    # elif p >= N - i + 1:
    #     ans = (sumaPorPartes[i] - sumaPorPartes[N]) / 2
    else:
        ans = distancias[i] + phiMemo(i + 1, p + popos[i])
        if p > 0:
            ans = min(ans, (distancias[i] // 2) + phiMemo(i + 1, p - 1 + popos[i]))

    memo[i][p] = ans
    return ans

def main():
    global N, popos, distancias, sumaPorPartes, memo
    
    nViajes = int(stdin.readline())
    while nViajes != 0:
        N = nViajes
        distancias = [0 for _ in range(N)]
        popos = [0 for _ in range(N)]
        memo = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
        for i in range(N):
            d, p = map(int, stdin.readline().split())
            distancias[i] = d
            popos[i] = p

        # lista para consultar suma constante
        sumaPorPartes = [0 for _ in range(N + 1)]
        for i in range(N - 1, -1, -1):
            sumaPorPartes[i] = distancias[i] + sumaPorPartes[i + 1]

        # solve
        resultado = phiMemo(0,0)
        print(resultado)
        nViajes = int(stdin.readline())

main()





"""
Sample Input
2
24 1
10 0
2
10 1
24 0
3
10 0
24 0
38 0
3
10 1
24 0
14 0
3
10 1
24 0
38 0
3
10 1
24 1
38 0
3
10 3
24 0
38 1
0
Sample Output
29
22
72
36
53
41
41
"""
