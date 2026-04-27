"""
Estudio : ADA 2026_1 Tarea 4 
Fecha   : 23 Abril 2026
Nombre  : Miguel Angel Padilla Rosero
Cod     : 8988878

Problem E - Mapping the Swaps
""" 

from sys import stdin

INF = float("inf")
opt = INF
numOpts = 0

# Verfica si ya esta ordenado y ademas cuenta el numero minimo de swaps para ordenar, con las inversiones
def inversiones(A):
    opt = 0
    for i in range(len(A)):

        if A[i] < A[i - 1]:
            ans = False

        for j in range(i + 1, len(A)):
            if A[j] < A[i]:
                opt += 1
    return opt, ans

def backtrack(n, A):
    global opt, numOpts
    hayInversiones = False
    
    if n < opt:
        sz = len(A)

        for i in range(1, sz):
                if A[i - 1] > A[i]:
                    hayInversiones = True
                    n = n + 1
                    A[i - 1], A[i] = A[i], A[i - 1]
                    backtrack(n, A) 
                    n = n - 1
                    A[i - 1], A[i] = A[i], A[i - 1]
    if not hayInversiones:
        if n == opt:
            numOpts += 1
        elif n < opt:
            opt = n
            numOpts = 1   

def main():
    global opt, numOpts
    casito = list(map(int, stdin.readline().split()))
    caseNum = 0
    while(casito != [0]):
        opt, flag = inversiones(casito)
        numOpts = 0
        caseNum += 1
        casito = casito[1:]
        if not flag:
            backtrack(0, casito)
        
        print(f"There are {numOpts} swap maps for input data set {caseNum}.")
        
        casito = list(map(int, stdin.readline().split()))
        

main()
"""
Sample Input
2 9 7
2 12 50
3 3 2 1
3 9 1 5
0
Sample Output
There are 1 swap maps for input data set 1.
There are 0 swap maps for input data set 2.
There are 2 swap maps for input data set 3.
There are 1 swap maps for input data set 4.
"""
