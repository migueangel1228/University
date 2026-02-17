from sys import stdin
from math import sqrt

"""
    AGRA  Tarea 6
Fecha  : 24/11/25
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem: island.py

Complejidad computacional "Big-O":

Función kruskal (Algoritmo de Kruskal con DSU):

1. Creación de grafo completo: O(n²)
   - Para n islas, se generan  arpoximadamente n(n-1)/2 aristas
   - Cada arista calcula distancia entre dos islas : O(1)

2. Ordenamiento de aristas: O(E log E) donde E = n(n-1)/2
   - Simplificado: O(n² log n)

3. Procesamiento de aristas con Union-Find:
   - Para cada arista (máximo n-1 uniones en el MST):
     * findSet con path compression: O(1) amortizado
     * unionSet con union:  O(1) amortizado
   - Total: O(n² x O(1) amortizado) ≈ O(n²)
   
Complejidad global:
    Tiempo: O(n² log n)
        Dominado por el ordenamiento de las n² aristas
  
    Espacio: O(n²)
        Para almacenar todas las aristas del grafo completo
        Estructuras auxiliares (p, rango, habitantesGrupo): O(n)
"""

# Operaciones Disjoint set
def makeSet(v,p,rango):
    p[v] = v
    rango[v] = 0
    
def findSet(v,p,rango):
    if(v == p[v]):
        ans = v
    else:
        p[v] = findSet(p[v],p,rango)
        ans = p[v]
    return ans

def unionSet(u,v,p,rango,habitantesGrupo):
    u = findSet(u,p,rango)
    v = findSet(v,p,rango)
    
    if u != v:
        if rango[u] < rango[v]:
            u, v = v, u
        
        p[v] = u
        habitantesGrupo[u] += habitantesGrupo[v]
        if rango[u] == rango[v]:
            rango[u] += 1

# Kruskal modificado que calcula directamente el promedio
def kruskal(n, aristas, habitantes):
    p = [0] * n
    rango = [0] * n
    habitantesGrupo = [0] * n
    total = 0.0
    
    for i in range(n):
        makeSet(i, p, rango)
        habitantesGrupo[i] = habitantes[i]
    
    aristas.sort()
    
    for peso, u, v in aristas:
        pu = findSet(u, p, rango)
        pv = findSet(v, p, rango)
        
        if pu != pv:
            grupo0 = findSet(0, p, rango)
            
            if pu == grupo0:
                total += habitantesGrupo[pv] * peso
            if pv == grupo0:
                total += habitantesGrupo[pu] * peso
            
            unionSet(u, v, p, rango, habitantesGrupo)

    totalHabitantes = sum(habitantes)
    return total / totalHabitantes

# Calculo de la hipotenusa de las dos coordenadas
def calculoPeso(xu,yu,xv,yv):
    a = xu - xv
    b = yu - yv
    a = pow(a,2)
    b = pow(b,2)
    ans = sqrt(a + b)
    return ans

def crearAristas(coordenadas):
    n = len(coordenadas)
    aristas = []

    for u in range(n):
        xu, yu = coordenadas[u]
        # Evitar duplicados
        for v in range(u + 1, n):
            xv , yv = coordenadas[v]
            
            w = calculoPeso(xu, yu, xv, yv)
            
            aristas.append((w, u, v))
    return aristas

def main():
    numCases = 1
    case = int(stdin.readline())
    while(case != 0):
        coordenadas = []
        habitantes = []
        cnt = 0
        for _ in range(case):
            xi , yi, hi = map(int, stdin.readline().split())
            coordenadas.append((xi,yi))
            habitantes.append(hi)
            cnt += 1
        
        aristas = crearAristas(coordenadas)
        n = len(coordenadas)
        
        promedio = kruskal(n, aristas, habitantes)
        print(f"Island Group: {numCases} Average {promedio:.2f}")
        print()
        
        numCases += 1
        case = int(stdin.readline())
    
main()


"""
Sample Input
7
11 12 2500
14 17 1500
9 9 750
7 15 600
19 16 500
8 18 400
15 21 250
0
Sample Output
Island Group: 1 Average 3.20
"""