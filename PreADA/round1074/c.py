from sys import stdin
#Encuentra el tamano de la subcandena consecutiva mas larga de la cadena
def solution(l):
    anterior = l[0]
    maximo = 1
    cnt = 1
    for i in range(1,len(l)):
        aux = l[i]
        if (not (anterior == (aux - 1)) and (not (anterior == aux))):
            cnt = 1

        elif(anterior == (aux - 1)):
            cnt += 1
            if cnt > maximo:
                maximo = cnt
        
        anterior = aux

    return maximo

def main():
    casitos = int(stdin.readline())
    for _ in range(casitos):
        n = int(stdin.readline())
        lista = list(map(int,stdin.readline().split()))
        lista.sort()
        ans  = solution(lista)
        
        print(ans)
        
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