"""
Estudio : ADA 2026_1 Tarea 4 
Fecha   : 26 Abril 2026
Nombre  : Miguel Angel Padilla Rosero
Cod     : 8988878

Problem B - Garden of Eden
"""
from sys import stdin

traductor = dict()
n = 0
target = ""
def generarRules(automata):
    dictsito = dict()
    binAutomata = format(automata, '08b')
    # crear traduccion del automata
    cnt = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                binary = (i,j,k)
                bitIdx = 7 - cnt
                dictsito[binary] = binAutomata[bitIdx]
                cnt += 1
                
    return dictsito

def check(A, isComplete):
    ans = True

    # validar solo el ultimo triple que se acaba de crear
    if len(A) >= 3:
        i = len(A) - 2
        actual = traductor[(A[i - 1], A[i], A[i + 1])]
        if actual != target[i]:
            ans = False

    # validar extremos circulares (solo cuando ya esta completo)
    if isComplete and ans:
        actual = traductor[(A[-1], A[0], A[1])]
        if actual != target[0]:
            ans = False

        actual = traductor[(A[-2], A[-1], A[0])]
        if actual != target[-1]:
            ans = False

    return ans

def backtrack(sol):
    ans = 0
    isComplete = False
    if len(sol) == n:
        isComplete = True
        if check(sol, isComplete):
           ans = True
        else:
            ans = False
            
    elif len(sol) < n:
        i = 0
        while i < 2 and not ans:
            sol.append(i)
            if check(sol, isComplete):
                ans = backtrack(sol)                
            sol.pop()
            i += 1
    return ans
    
def main():
    global traductor, n, target
    
    casito = stdin.readline().strip()

    while(len(casito)):
        idAutomata, n, target = casito.split()
        idAutomata = int(idAutomata)
        n = int(n)

        traductor = generarRules(idAutomata)
        if backtrack([]):
            print("REACHABLE")
        else:
            print("GARDEN OF EDEN")
        
        casito = stdin.readline().strip()
main()


"""
Sample Input
0 4 1111
204 5 10101
255 6 000000
154 16 1000000000000000
Sample Output
GARDEN OF EDEN
REACHABLE
GARDEN OF EDEN
GARDEN OF EDEN
"""


