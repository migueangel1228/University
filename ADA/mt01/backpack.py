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

def phimemo(l, k):
    global memo
    
    if memo[l][k] != -1:
        ans = memo[l][k]
    elif k == 0:
        ans = sum(distancias[l:N + 1])
        
    else:
        ans = INF
        for r in range(l + 1, N - k + 2):
            
            aux = max(sum(distancias[l:r]), phi(r ,k - 1))
            
            ans = min(ans, aux)
    
    memo[l][k] = ans
    return ans


def main():
    casito = stdin.readline().strip()
    global distancias, N, K, memo
    
    while(casito != ""):
        N, K = list(map(int,casito.split()))
        distancias = []
        for _ in range(N + 1):
            aux = int(stdin.readline())
            distancias.append(aux)
        
        memo = [[-1 for _ in range(N + 1) ] for _ in range(K + 1)]
        
        respuesta = phimemo(0,K)
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
