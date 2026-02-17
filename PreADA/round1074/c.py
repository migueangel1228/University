from sys import stdin

def main():
    
    numCasos = int(stdin.readline())
    for case in range(numCasos):
        aux = int(stdin.readline())
        ans = []
        for i in range(1,aux + 1):
            ans.append(i)
        print(*ans)
    
main()

"""
Input
6
1
4
5
0 1 1 2 3
2
1 1
4
4 2 3 6
5
2 4 1 0 -1
6
-1 1 2 3 5 6
Output
1
4
1
3
4
3
"""