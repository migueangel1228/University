"""
Tarea  : ADA  Tarea 1 
Fecha  : 4 Marzo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem A - Best Coalitions

"""

from sys import stdin

# lista de todas las acciones| porcentaje del  'socio'| limiteinferior que se va reduciendo (DVC)| Suma total 
def phi(A,p,L,s):
    ans = 0
    if (s > 50.00):
        ans = p / s
    elif( L == len(A)):
        ans = 0.0
    else:
        ans = max(phi(A, p, L+1,s + A[L]), phi(A, p, L+1, s)) 
    return ans

def phiMem(A,p,L,s,mem):
    ans = 0
    if (L,s) in mem:
        ans = mem[(L,s)]
    else:    
        if (s > 50.00):
            ans = p / s
        elif( L == len(A)):
            ans = 0.0
        else:          
            ans = max(phiMem(A, p, L+1,s + A[L],mem), phiMem(A, p, L+1, s,mem)) 
        mem[(L,s)] = ans    
    return ans


def main():
    n, pi = list(map(int,stdin.readline().split()))
    while ( n != 0 and pi != 0):
        porcentajes = []
        for i in range(n):
            aux = float(stdin.readline())
            if i != pi - 1:
                porcentajes.append(aux)
            else:
                p = aux
        dictsito = {}
        respuesta = phiMem(porcentajes, p , 0, p, dictsito)
        
        respuesta = respuesta * 100
        print(f"{respuesta:.2f}")
        n, pi = list(map(int,stdin.readline().split()))

main()


"""
Sample Input
5 5
20.00
12.00
29.00
14.00
25.00
2 1
56.87
43.13
2 2
56.87
43.13
3 1
10.00
45.00
45.00
0 0
Sample Output
49.02
100.00
43.13
18.18
"""
