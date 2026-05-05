"""
Estudio : ADA 2026_1 Parcial Practico 2 
Fecha   : 3 Mayo 2026
Nombre  : Miguel Angel Padilla Rosero
Cod     : 8988878

Problem A - Robots on Ice
"""

from sys import stdin

# Datos globales
totalCheckIn = 3
destiny = (0,1)

targets = []
m, n = 0, 0
solutions = 0
checkInTimes = []

grado = []   # matriz de grados (vecinos no visitados)

# Generar tiempos de checkpoints
def generarTiemposCheckIn(m,n):
    global checkInTimes
    checkInTimes = []
    for i in range(1, totalCheckIn + 1):
        aux = n * m * i
        checkInTimes.append(aux // 4 - 1)
    return checkInTimes

# Movimientos: up, right, down, left (fila, columna) 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def generarVecinos(m,n,x,y):
    result = []
    for i in range(len(dx)):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < m and 0 <= ny < n):
            result.append((nx, ny))
    return result

def distancia(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Poda restantes y poda camino par (Si la diferencia entre pasos disponibles y distancia es impar, es imposible)
def check(u, step, ri):
    total = m * n
    flag = False

    if ri < totalCheckIn:
        target = targets[ri]
        tiempo = checkInTimes[ri]
        faltan = tiempo - step
        dist = distancia(u, target)
        if dist > faltan or (faltan - dist) % 2 != 0:
            flag = True

    if ri == totalCheckIn:
        faltan = (total - 1) - step
        dist = distancia(u, destiny)
        if dist > faltan or (faltan - dist) % 2 != 0:
            flag = True

    return flag

# Poda ramas que dejan alguna casilla no visitada (exepto destino) que tiene menos de 2 casilas adyacentes posibles
def esCallejonSinSalida(visited, actual):
    ans = False
    ux, uy = actual
    
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited and (i, j) != destiny:
                cnt = grado[i][j]
                for _ in range(len(dx)):
                    if abs(i - ux) + abs(j - uy) == 1:
                        cnt += 1
                if cnt < 2:
                    ans = True
    return ans

def dfsAux(u, step, ri, visited):
    global solutions
    ux, uy = u
    continuar = True

    # Validar check In exacto
    if ri < totalCheckIn and step == checkInTimes[ri]:
        if u != targets[ri]:
            continuar = False
        else:
            ri += 1
    elif ri < totalCheckIn and u == targets[ri]:
        continuar = False

    # Llegar al destino antes de tiempo
    if u == destiny and step != (m * n - 1):
        continuar = False

    # Llegar al destino tarde
    if continuar and check(u, step, ri):
        continuar = False

    # Poda por callejon sin salida
    if continuar:
        if esCallejonSinSalida(visited, u):
            continuar = False
                  
    # Caso final
    if continuar and step == m * n - 1:
        if u == destiny and ri == totalCheckIn:
            solutions += 1
        continuar = False
    
    if continuar:
        for vecino in generarVecinos(m, n, ux, uy):
            if vecino not in visited:
                vx, vy = vecino
                # Actulizar grados
                for k in range(len(dx)):
                    di, dj = dx[k], dy[k]
                    ni, nj = vx + di, vy + dj
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                        grado[ni][nj] -= 1
                visited.add(vecino)
                dfsAux(vecino, step + 1, ri, visited)
                
                visited.remove(vecino)
                # Restaurar grados
                for k in range(len(dx)):
                    di, dj = dx[k], dy[k]
                    ni, nj = vx + di, vy + dj
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                        grado[ni][nj] += 1

def solve():
    global solutions, grado
    solutions = 0
    generarTiemposCheckIn(m, n)

    visited = set()
    start = (0, 0)
    visited.add(start)

    # Inicializar grado con el total de vecinos (todos los demas estan no visitados)
    grado = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            for k in range(len(dx)):
                di, dj = dx[k], dy[k]
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    grado[i][j] += 1

    # Como start ya esta visitado, restamos 1 a los grados de sus vecinos no visitados
    for k in range(len(dx)):
        di, dj = dx[k], dy[k]
        ni, nj = start[0] + di, start[1] + dj
        if 0 <= ni < m and 0 <= nj < n:
            grado[ni][nj] -= 1

    dfsAux(start, 0, 0, visited)

def main():
    global targets, solutions, m, n
    caseNum = 1
    m, n = map(int, stdin.readline().split())
    while n != 0 and m != 0:
        targets = []
        targetsAux = list(map(int, stdin.readline().split()))
        for i in range(0, totalCheckIn * 2, 2):
            ri, ci = targetsAux[i], targetsAux[i + 1]
            targets.append((ri, ci))

        solve()
        print(f"Case {caseNum}: {solutions}")
        caseNum += 1
        m, n = map(int, stdin.readline().split())

main()

"""
Sample Input
3 6
2 1 2 4 0 4
4 3
2 0 3 2 0 2
0 0
Sample Output
Case 1: 2
Case 2: 0
"""
