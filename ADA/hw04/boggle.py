"""
Estudio : ADA 2026_1 Tarea 4 
Fecha   : 24 Abril 2026
Nombre  : Miguel Angel Padilla Rosero
Cod     : 8988878

Problem A - Boggle Blitz
"""

from sys import stdin

words = set()

# up ,up-der, der, der-down, down, down-left, left, left-up 
dx = [0, 1, 1, 1, 0, -1,-1,-1]
dy = [1, 1, 0,-1,-1, -1, 0, 1]

def generarVecinos(m,n,x,y):
    result = []
    aux = ()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < m and 0 <= ny < n):
            aux = (nx, ny)
            result.append(aux)
    return result

def dfsAux(u, word, vis, G):
    global words
    n = len(G)
    ux, uy = u
    listVecinos = generarVecinos(n, n, ux, uy)
    for vecino in listVecinos:
        vx, vy = vecino
        # verificar que solo avanze si es mayor lexicograficamente (poda)
        if G[ux][uy] < G[vx][vy]: 
            if vecino not in vis:
                vis.add(vecino)
                word.append(G[vx][vy])
                if (len(word) > 2):
                    words.add("".join(word))
                dfsAux(vecino,word,vis,G)
                word.pop()
                vis.remove(vecino)

def dfs(G):
    for x in range (len(G)):
        for y in range(len(G[x])):
            word = []
            vis = set()
            v = (x,y)
            vis.add(v)
            word.append(G[x][y])
            dfsAux(v,word,vis,G)


def main():
    global words
    numCases = int(stdin.readline())
    
    for i in range(numCases):
        voidLine = stdin.readline()
        n = int(stdin.readline())
        M = []
        words = set()
        for _ in range(n):
            line = stdin.readline().strip()
            M.append(line)
        dfs(M)
         
        for word in sorted(sorted(words), key=len):
            print(word)
        if i != numCases-1:
            print()
        
main()

"""
Sample Input
2

3
one
top
dog

4
abcd
bcda
cdab
dabc
Sample Output
dop
dot
eno
enp
ent
eop
eot
gop
got
nop
not
enop
enot

abc
abd
acd
bcd
abcd
"""
