from sys import stdin

"""
AGRA   : Tarea 1 Enero 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
A - Problem A - bit.cpp - 13282
"""

def main():
    numeroParejas = stdin.readline()
    
    
    s = set([])
    while  numeroParejas != "":
        s = set([])
        listaCase = []
        i = 0
        
        listaCase.append(stdin.readline().split())
        listaCase.append('#')
        listaCase.append(stdin.readline().split())
       
        for i in listaCase:
            s.add(i)

        listaNumerosSinRepetir = [0]
        for k in s:
            listaNumerosSinRepetir.append(int(k))
            
        ordenada = True
        itsOver = False
        
        while not itsOver:
            mid = (len(listaNumerosSinRepetir) // 2)
            midNum = listaNumerosSinRepetir[mid]
            j = 0
            parejaActual = 0
            while j < len(listaCase) and not itsOver:
                
                if listaCase[j] != '#' and  listaCase[j] > midNum :
                    # caso donde se acaba de empezar a revisar un pareja de pesas
                    if parejaActual == 0:
                        parejaActual = listaCase[j]
                    else:
                        # caso donde compruebo si mi pareja de pesas esta ordenadas
                        if parejaActual == listaCase[j]:
                            parejaActual = 0 # reinicio mi varible que guara parejas
                        # caso donde hay al menos una pareja desordenada 
                        else:
                            ordenada = False
                j = j + 1
            if len(listaNumerosSinRepetir) != 1:
                itsOver = True
            elif ordenada:
                ultimoMid = mid
                listaNumerosSinRepetir = listaNumerosSinRepetir[0:(len(listaNumerosSinRepetir) // 2)]
            else:
                listaNumerosSinRepetir = listaNumerosSinRepetir[(len(listaNumerosSinRepetir) // 2):ultimoMid]

        print(listaNumerosSinRepetir,"/n")
main()

