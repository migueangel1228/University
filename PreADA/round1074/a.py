from sys import stdin

def main():
    
    x = int(stdin.readline())
    for case in range(x):
        aux = int(stdin.readline())
        ans = []
        for i in range(1,aux + 1):
            ans.append(i)
        print(*ans)
    
main()
"""
Example
InputCopy
3
1
2
5
OutputCopy
1
2 4
2 102 43 1 21
"""