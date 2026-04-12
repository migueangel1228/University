"""
Estudio : ADA 2025_2 Tarea 4 
Fecha   : 11 Febrero 2026
Nombre  : Miguel Angel Padilla Rosero
Cod     : 8988878

Problem A - Determine the Combination
""" 

from sys import stdin
cadena = []
N = 0
r = 3
result = []
# Donde voy en la cadena original y la cadena generada hasta el momento
# invariante: el tamañno de la cadena siempre es menor o igual que r 
def solutionBactrack(i, cad):
    global result, r, N, cadena
    if len(cad) == r:
        result.append("".join(cad))
        return
    elif (i < N and len(cad) < r):
            
        for j in range(i, N):
            cad.append(cadena[j])
            solutionBactrack(j + 1, cad)
            cad.pop()


def ordenarStr(cad):
    ans = []
    for c in cad:
        ans.append(c)
    ans.sort()
    return ans

def main():
    global cadena, r, N, result
    
    entrada = stdin.readline().strip()
    
    while (len(entrada) > 0):
        cadenaOriginal, rOriginal = entrada.split()
        r = int(rOriginal)
        cadena = ordenarStr(cadenaOriginal)
        N = len(cadena)
        result = []
        solutionBactrack(0,[])

        for line in result:
            print(line)
        
        entrada = stdin.readline().strip()
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

sample Output
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