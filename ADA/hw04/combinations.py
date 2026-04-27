
"""
Tarea  : ADA  Tarea 4
Fecha  : 4 Abril 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem E - Racing
"""

from sys import stdin
    
def main():
    
    numCases = int(stdin.readline())
    while (numCases != 0):
        for _ in range(numCases):
            aristas = []
            numNodes, numAristas = map(int,stdin.readline().split())
            total = 0
            for _ in range(numAristas):
                u , v, w = map(int, stdin.readline().split())
                u -= 1
                v -= 1
                aristas.append((-w,u,v))
                # Asumo que todas inicialmente que ninguan aritas pertence al MST 
                total += w
            resultado = kruskal(numNodes, aristas, total)
            print(resultado)
        
        numCases = int(stdin.readline())
                
main()

"""
Sample Input
abcde 2
abcd 3
aba 2
Sample Output
ab
ac
ad
ae
bc
bd
be
cd
ce
de
abc
abd
acd
bcd
aa
ab
"""