"""
    AGRA  Tarea 2
Fecha  : 25 Agosto 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem B  souvenirs.py

Complejidad computacional "Big-O":

Función solveBinarySearch:

Usa búsqueda binaria sobre k → O(log n) iteraciones.
En cada iteración:

Construcción de listaAux: O(n).
Ordenamiento de listaAux: O(n log n).

Complejidad global:
  + Tiempo: O(n (log n)^2)
  + Espacio: O(n)
"""

from sys import stdin

def verificarVector(listaAux, k, dinero):
    total = sum(listaAux[:k])
    
    if total <= dinero:
        ans = total  
    else:
        ans = -1
        
    return ans 
    
def solveBinarySearch(S, n, orginal):
    ans = [0 , 0]
    left = 0
    right = n + 1
    minimunCost = 0

    while (right - left > 1):
        mid = (right + left) // 2   
        
        listaAux = []
        for j in range(n):
            valor = orginal[j] + (j + 1) * mid
            listaAux.append(valor)
        
        listaAux.sort()
        aux = verificarVector(listaAux, mid, S)
        
        if aux != -1:  # se pudo comprar mid souvenirs
            left = mid
            minimunCost = aux
        else:
            right = mid
            
    ans[0] = left
    ans[1] = minimunCost
    
    return ans



def main():
    seguir = True
    while seguir:
        
        line = stdin.readline().strip()
        
        if line != "": # vaina pa que funciones
            n, S = map(int, line.split())
            orginal = list(map(int, stdin.readline().split()))
            
            ans = solveBinarySearch(S, n, orginal)
            print(ans[0], ans[1])
            
        else:
            seguir = False
    
    
main()

"""
Sample Input
3 11
2 3 5
5 20
1 10 3 2 5

Sample Output
2 11
2 12
"""