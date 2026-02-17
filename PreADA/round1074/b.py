from sys import stdin

def main():
    
    x = int(stdin.readline())
    for case in range(x):
        longitud = x = int(stdin.readline())
        listica = list(map(int,stdin.readline().split()))
        maximo = max(listica)
        print(maximo * longitud)
    
main()
"""
Example
Input
4
5
2 1 4 5 3
2
5 1
3
3 2 1
2
6 7
Output
25
10
9
14
"""