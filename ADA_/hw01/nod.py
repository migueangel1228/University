"""
Tarea  : ADA  Tarea 1 
Fecha  : 14 Febrero 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem C - N + NOD(N)
"""
from sys import stdin
from math import pow

#Binary Search

def binarySearch(A,valueLow,valueHigh):
    ans = 0
    lowIndx , hiIndx = -1 ,-1 
    lowAux , hiAux = 0,len(A) 
    while ( hiAux - lowAux > 1):
        mid = lowAux + (hiAux - lowAux) / 2;

        if A[mid] <= valueLow:
            lowAux = mid
        else:
            hiAux = mid
    lowIndx  = lowAux
    
    lowAux , hiAux = lowIndx, len(A) 
    while ( hiAux - lowAux > 1):
        mid = lowAux + (hiAux - lowAux) / 2;

        if A[mid] < valueHigh:
            lowAux = mid
        else:
            hiAux = mid
    hiIndx = hiAux
    
    ans = hiIndx - lowIndx  
        
    return ans

def crearSusecion(Nod):
    N = []
    for i in range(1e6 - 1):
        if i == 0:
            N[i] = 1
        else:
            N[i] = Nod[i - 1] + i - 1
    return N


def Nod():
    x = x


def main():
    n = int(stdin.readline())
    for casito in range(n):
        low , high = list(map(int,stdin.readline.split()))
        
        



"""

Sample Input
3
1 18
1 100
3000 4000
Sample Output
Case 1: 7
Case 2: 20
Case 3: 87
"""
