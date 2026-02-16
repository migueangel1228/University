"""
    AGRA  Tarea 2
Fecha  : 24 Agosto 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem C  souvenirs.py
"""

from sys import stdin

def main():
    imputlist = stdin.readline().split()
    n = imputlist[0]

    while n != "": # each case
        S = int(imputlist[1])
        i = 0
        
        orginal = map(int(stdin.readline().split()))
        while (i < int(n)):
            
            i += 1

        imputlist = stdin.readline().split()
        n = imputlist[0]


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