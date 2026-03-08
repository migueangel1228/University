"""
Tarea  : ADA  Tarea 1 
Fecha  : 4 Marzo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem A - Best Coalitions
"""

from sys import stdin


INF = float("inf")

mem = []
k = 0

def phiMem(l,r):
    global mem
    ans = 0
    if mem[l][r]  != -1: 
        ans = mem[l][r]
    elif l >= r:
        ans = 0
    elif r - l == 1:
        ans = (l + k) * 2
    elif r - l == 2:
        ans = (l + k + 1) * 3
    elif r > l:

        minimo = INF
        for c in range(l,r + 1):
            aux = (phiMem(l, c - 1) + phiMem(c + 1, r) + ((c + k) * (r - l + 1)))
            if aux < minimo:
                minimo = aux
            ans = minimo
            
    mem[l][r] = ans

    return ans

def phiTab(l,r):
    global mem, k

    n = r   # porque en main la vas a llamar como phiTab(1, N)

    # Caso base T[i][i-1] = 0   
    # Caso base l >= r, T[i][i] = 0
    # Caso base r - l == 1, ans = l * (r - l + 1)
    # Caso base r - l == 2, ans = l + 1 * (r - l + 1)
    
    for i in range(1, n + 2):
        mem[i][i] = 0
        if i - 1>= 0:
            mem[i][i - 1] = 0 
        if i + 1 <= n:
            mem[i][i + 1] = (i + k) * 2
        if i + 2 <= n:
            mem[i][i + 2] = (i + k + 1) * 3

    # Llenado de izquierda a derecha de abajo a arriba(por columnas)
    for R in range(4, n + 1):
        for L in range(R, 0, -1):

        # solo calcular casos generales
            if R - L >= 3:
                minimo = INF

                for c in range(L, R + 1):
                    aux = mem[L][c - 1] + mem[c + 1][R] + ((c + k) * (R - L + 1))
                    if aux < minimo:
                        minimo = aux

                mem[L][R] = minimo

    return mem[l][r]



def main():
    casitos = int(stdin.readline())
    global mem, k
    for caso in range(casitos):
        
        N, k = list(map(int,stdin.readline().split()))
        mem = [[-1 for _ in range(N + 2)] for _ in range(N + 2)]
        # mem = {}
        l , r = 1 , N
        # opt = phiMem(l,r)
        opt = phiTab(l,r)
        print(f"Case {caso + 1}: {opt}")

main()



"""
Sample Input
5
2 0
3 0
4 0
5 0
10 20
Sample Output
Case 1: 2
Case 2: 6
Case 3: 13
Case 4: 22
Case 5: 605
"""
"""
Imput Prueba Time
1
600 99
Output Prueba Time
Case 1: 1861756
"""
