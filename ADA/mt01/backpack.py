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

def phi(l, k):
    ans = INF
    if N - l < k:
        ans = INF
    elif k == 0:
        ans = sum(distancias[l:N + 1])
    else:
        for r in range(l + 1, N - k + 2):
            
            aux = max(sum(distancias[l:r]), phi(r ,k - 1))
            
            ans = min(ans, aux)
    return ans

def phiMemo(l, k):
    global memo
    
    if memo[l][k] != -1:
        ans = memo[l][k]
    elif k == 0:
        ans = sum(distancias[l:N + 1])
        
    else:
        ans = INF
        for r in range(l + 1, N - k + 2):
            
            aux = max(sum(distancias[l:r]), phiMemo(r ,k - 1))
            
            ans = min(ans, aux)
    
    memo[l][k] = ans
    return ans

def phiTab():
    global tab

    # Inicializar tab,con caso base, K = 0
    for l in range(N, -1, -1):
        tab[l][0] = sum(distancias[l:N + 1])

    # llenar reto de tab
    for k in range(1, K + 1):
        for l in range(N, -1, -1):
            if N - l < k :
                tab[l][k] = INF
            else:
                ans = INF
                for r in range(l + 1, N - k + 2):
                    aux = max(sum(distancias[l:r]), tab[r][k - 1])
                    ans = min(ans, aux)
                tab[l][k] = ans

    return tab[0][K]


def phiTabOpt():
    prev = [INF for _ in range(N + 1)]
    curr = [INF for _ in range(N + 1)]

    # Inicializar tab,con caso base, K = 0
    for l in range(N, -1, -1):
        prev[l] = sum(distancias[l:N + 1])

    # llenar reto de tab
    for k in range(1, K + 1):
        for l in range(N, -1, -1):
            if N - l < k:
                curr[l] = INF
            else:
                ans = INF
                for r in range(l + 1, N - k + 2):
                    aux = max(sum(distancias[l:r]), prev[r])
                    ans = min(ans, aux)
                curr[l] = ans

        prev, curr = curr, prev

    return prev[0]

def phiTabOpt2():
    
    tab = [INF for _ in range(N + 1)]

    # Inicializar tab,con caso base, K = 0
    for l in range(N, -1, -1):
        tab[l] = sum(distancias[l:N + 1])

    # llenar reto de tab
    for k in range(1, K + 1):
        for l in range(0, N + 1):   # en ascendente pa que no se me chotee
            if N - l < k:
                tab[l] = INF
            else:
                ans = INF
                for r in range(l + 1, N - k + 2):
                    aux = max(sum(distancias[l:r]), tab[r])
                    ans = min(ans, aux)
                tab[l] = ans

    return tab[0]

def phiTabOpt3():
    
    tab = [INF for _ in range(N + 1)]

    # suffix sums
    sumaPorPartes = [0 for _ in range(N + 1)]
    for i in range(N, -1, -1):
        if i == N:
            sumaPorPartes[i] = N
        else:
            sumaPorPartes[i] = distancias[i] + sumaPorPartes[i + 1]

    # caso base: k = 0
    for l in range(N, -1, -1):
        tab[l] = sumaPorPartes[l]

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
