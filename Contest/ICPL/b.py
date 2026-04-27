from sys import stdin

def solution(line):
    pila = []
    pilaTamRestante = []
    i = 0
    ans = True
    tamEntrada = len(line)

    while (i < tamEntrada):
        # print(ans)
        # print("pila")
        # print(*pila)
        # print("pilaTamrestante")
        # print(*pilaTamRestante)
        num = abs(line[i])


        if ((len(pila) == 0)): #and (len(pilaTamRestante == 0))):  
            pilaTamRestante.append(num)
            pila.append(line[i])

        else: 
            ## 9
            top = len(pilaTamRestante) - 1
            # print("top")
            # print(top)
            # print("num")
            # print(num)
            
 
            if (line[i] < 0):
                pilaTamRestante[top] -= num
                if (pilaTamRestante[top] <= 0): 
                    ans = False

                pila.append(line[i])
                pilaTamRestante.append(num)
            
            elif (line[i]>0):
                if (line[i] != abs(pila[top])):
                    ans = False
                
                pila.pop()
                pilaTamRestante.pop()      
        i  += 1 
    # print("final")
    # print("pila")
    # print(*pila)
    # print("pilaTamrestante")
    # print(*pilaTamRestante)
    
    return ans    


def main():
    line = stdin.readline().strip()

    while (len(line) > 0):
        line = list(map(int,line.split()))
        ans = solution(line)

        if (ans == True): 
            print(":-) Matrioshka!")
        else: 
            print(":-( Try again.")

        line = stdin.readline().strip()

main()

"""
Sample Input
-9-7-2 2-3-2-1 1 2 3 7
9-9-7-2 2-3-1-2 2 1 3 7 9-9-7-2 2-3-1-2 3 2 1 7 9-100-50-6 6 50 100-100-50-6 6 45 100-10-5-2 2 5-4-3 3 4 10-9-5-2 2 5-4-3 3 4 9
Sample Output
:-) Matrioshka!
:-( Try again.
:-( Try again.
:-) Matrioshka!
:-( Try again.
:-) Matrioshka!
:-( Try again.
"""
