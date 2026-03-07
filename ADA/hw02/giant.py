"""
Tarea  : ADA  Tarea 1 
Fecha  : 4 Marzo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem A - Best Coalitions
"""

from sys import stdin

INF = float("inf")

# k del problema | rango del problema
def phi(k,l,r):
    ans = 0
    if l > r:
        ans = 0
    elif r > l:
        min = INF
        for c in range(l,r + 1):
            aux = (phi(k, l, c - 1) + phi(k, c + 1, r) + ((c + k) * (r - l + 1)))
            if aux < min:
                min = aux
            ans = min
    return ans

mem = {}
k = 0

# def phiMem(l,r):
#     global mem
#     ans = 0
#     if (l,r) in mem: 
#         ans =  mem[(l,r)]
#     elif l >= r:
#         ans = 0
#     elif r - l == 1:
#          ans = (l + k) * 2
#     elif r - l == 2:
#          ans = (l + 1 + k) * 3
#     elif r > l:

#         minimo = INF
#         for c in range(l,r + 1):
#             aux = (phiMem(l, c - 1) + phiMem(c + 1, r) + ((c + k) * (r - l + 1)))
#             if aux < minimo:
#                 minimo = aux
#             ans = minimo
#             mem[(l,r)] = ans
#     mem[(l,r)] = ans

#     return ans
def phiMem(A,l,r):
    global mem
    ans = 0
    if (l,r) in mem: 
        ans =  mem[(l,r)]
    elif l >= r:
        ans = 0
    elif r - l == 1:
        ans = (l + k) * 2

    elif r - l == 2:
        ans = (l + 1 + k) * 3
    elif r > l:

        minimo = INF
        for c in range(l,r + 1):
            aux = (phiMem(l, c - 1) + phiMem(c + 1, r) + ((c + k) * (r - l + 1)))
            if aux < minimo:
                minimo = aux
                A.append(ans)
            ans = minimo
            mem[(l,r)] = ans
    mem[(l,r)] = ans

    return ans

def main():
    casitos = int(stdin.readline())
    global mem, k
    for caso in range(casitos):
        
        N, k = list(map(int,stdin.readline().split()))
        mem = {}

        l , r = 1 , N
        A = []
        opt = phiMem(A,l,r)
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