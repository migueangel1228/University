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
    if l == r:
        ans = 0
    elif r > l:
        min = INF
        for c in range(l,r):
            aux = (phi(k, l, c) + phi(k, c + 1, r) + ((c + k) * (r - l + 1)))
            if aux < min:
                min = aux
            ans = min
    return ans

def main():
    casitos = int(stdin.readline())

    for caso in range(casitos):
        
        N, K = list(map(int,stdin.readline().split()))
        
        l , r = 0 , N
        opt = phi(K,l,r)
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