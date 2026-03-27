"""
Tarea  : ADA  Tarea 3
Fecha  : 25 Marzo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem A - Calculus Simplified
"""
from sys import stdin
from collections import deque

# Parsea la cadena original y devuelve una concatenacion de  '+' y '-'
def parsing(cadena):
    ans = []
    esNegativo = False
    pila = deque()
    ultimoOperador = '+'

    for c in cadena:
        if (c == '+' or c == '-'):
            ultimoOperador = c

            if (not esNegativo):
                ans.append(c)
            # Modo negativo 
            else:
                if (c == '-'):
                    ans.append('+')
                else:
                    ans.append('-')

        # Es o un parentesis o una x
        else:
            if (c == '('):
                pila.append(esNegativo)

                if (ultimoOperador == '-'):
                    esNegativo = not esNegativo

                ultimoOperador = '+'

            elif (c == ')'):
                esNegativo = pila.pop()

    return ans
            
# recibe la cadena parseada y un arreglo de numeros ordenados, y devuelve la solucion del problema (vorazmente)
def solution(cadena,A):
    ans = 0
    if (len(cadena) == 0):
        ans = max(A)
    else:
        minimo , maximo =  0, len(A) - 1
        
        ans += A[maximo]
        maximo -= 1 
        for c in cadena:
            if (c == '+'):
                ans += A[maximo]
                maximo -= 1 
            else:
                ans -= A[minimo]
                minimo += 1
    return ans  

def main():
    casos = int(stdin.readline().strip())
    for _ in range(casos):
        expression = stdin.readline().strip()
        n = int(stdin.readline())
        nums = list(map(int, stdin.readline().split()))
        
        cadenaParseada = parsing(expression)
        nums.sort()
        result = solution(cadenaParseada,nums)
        print(result)
main()

"""
Sample Input
3
x
1
2
x-x
2
-1 1
(x)+(x)-(x)
3
1 1 1
Sample Output
2
2
1
"""

"""
Sample Input Invent
1
x-(x-(x+x))-x+x
6
-3 -2 -1 2 4 8
Sample Output
18
"""

