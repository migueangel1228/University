"""
Tarea  : ADA  Tarea 2 
Fecha  : 3 Marzo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem D - Hippity Hopscotch
"""

from sys import stdin


def generarCandidatos(M,k,r,c):
    candidatos = []
    N = len(M)
    valor_actual = M[r][c]

    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in direcciones:
        for paso in range(1, k + 1):
            nr = r + dr * paso
            nc = c + dc * paso

            if 0 <= nr < N and 0 <= nc < N:
                if M[nr][nc] > valor_actual:
                    candidatos.append((nr, nc))
    
    return candidatos
    

def phi(M,k,r,c):
    ans = 0
    candidatos = generarCandidatos(M,k,r,c)
    if len(candidatos) == 0:
        ans = M[r][c]

    maxLuka = 0
    for ri, ci in candidatos:
        aux = phi(M,k,ri,ci)
        if aux > maxLuka:
            maxLuka = aux

    ans = maxLuka + M[r][c]
    return ans


def phiMem(M,k,r,c,mem):
    ans = 0
    candidatos = generarCandidatos(M,k,r,c)
    if len(candidatos) == 0:
        ans = M[r][c]

    maxLuka = 0
    for ri, ci in candidatos:
        if (ri,ci) in mem:
            aux = mem[(ri,ci)]
        else:
               aux = phiMem(M,k,ri,ci,mem)
               mem[ri,ci] = aux 
        if aux > maxLuka:
            maxLuka = aux

    ans = maxLuka + M[r][c]
    return ans

def main():
    casitos = int(stdin.readline())

    for casos in range(casitos):
        voiD = stdin.readline()
        N, K = list(map(int,stdin.readline().split()))
        
        mapita = [[0 for _ in range(N)] for _ in range(N)]
        
        for i in range(N):
            auxList = list(map(int,stdin.readline().split()))
            mapita[i] = auxList
        dictsito = {}
        LukaMaxima = phiMem(mapita,K,0,0,dictsito)
        print(LukaMaxima)
        
        if casos != casitos -1:
            print()
    
        

main()


"""
Sample Input
1

3 1
1 2 5
10 11 6
12 12 7
Sample Output
37
"""