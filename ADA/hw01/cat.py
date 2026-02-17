"""
Tarea  : ADA  Tarea 1 
Fecha  : 1 Febrero 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem B - Business Center
"""

from sys import stdin
from math import log2

def simulacion(h,N):
    hHijos = h
    i = 0
    nAux = N + 1
    while (hHijos > 1):
        # print(hAux,N)
        hHijos = hHijos // nAux
        # print(hAux,N)
        i += 1
    if hHijos == 1:
        ans = i
    else:
        ans = -1
    return ans

def binaryS(h, w):
    N = -1
    i = -1
    # caso base
    if h == 1 and w == 1:
        N = 0
        i = 0
        
    max_i = int(log2(h)) + 1 # cota segura para i
    for iAux in range(1, max_i + 1):
        l, r = 1, w  # N^i = w => N <= w (para N>=1)
        
        noEncontrado = True # si sirve el i
        while l <= r and noEncontrado:
            mid = (l + r) // 2
            value = pow(mid + 1, iAux)

            if value == h:
                if pow(mid, iAux) == w:
                    N = mid; i = iAux
                noEncontrado = False  # Encontrado
                
            elif value < h:
                l = mid + 1
            else:
                r = mid - 1
    return N, i

def main():
    alturaInicial, workerCats = list(map(int,stdin.readline().split()))
    
    while (alturaInicial != 0 and workerCats != 0):
        N , i = binaryS(alturaInicial,workerCats)
        
        # Total no trabajadores
        if i == 0:
            noWorkers = 0
        else:
            noWorkers = 1
        for j in range(1,i):
            noWorkers += pow(N,j)
        # Altura Total
        hTotal = 0
        hAux = alturaInicial
        hHijos = N + 1
        for j in range(0,i + 1):
            hTotal += hAux * pow(N,j)
            
            hAux = hAux // hHijos
            j += 1
            
        print(noWorkers,hTotal)
        
        alturaInicial, workerCats = list(map(int,stdin.readline().split()))
    
    
main()

"""
Sample Input
216 125
5764801 1679616
0 0
Sample Output
31 671
335923 30275911
"""


