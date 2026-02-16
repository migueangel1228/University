from sys import stdin
from heapq import heappush

"""
AGRA  Tarea 1 Enero 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem D  cakey.py - 13282
"""

class Time:
    def __init__(self,tiempo,repeticiones):
        self.tiempo = tiempo
        self.repetici
        ones = repeticiones
        
    def __gt__(self, Time):
        
        if self.repeticiones == Time.repeticiones:
            ans =  self.tiempo > Time.tiempo
        else:
            ans = self.repeticiones < Time.repeticiones   
        return ans
    def __repr__(self):
        return f"{self.tiempo}"
     
def main():

    dato = stdin.readline()
    while (dato != ""):
        stdin.readline()
    #   Los tiempos de entrada y salida estan ordenados de menor a mayor
    
        tiempoDeEntrada = stdin.readline().split()
        for i in range(len(tiempoDeEntrada)):
            tiempoDeEntrada[i] = int(tiempoDeEntrada[i])
            
        tiempoDeSalida = stdin.readline().split()
        for i in range(len(tiempoDeSalida)):
            tiempoDeSalida[i] = int(tiempoDeSalida[i])

        i = 0
        # solo deberia ingresar al diccionario, si -(entrada - salida) es mayor a 0
        posicionValida = 0 # es la posicion incial, para que no restar casos innecesaros
        maximo = Time(0,0)
        dictTime = {}
        while (i < len(tiempoDeEntrada)): # N*M
            j = posicionValida # actualiza la posicion de salida
            while (j < len(tiempoDeSalida)):
                resta = tiempoDeEntrada[i] - tiempoDeSalida[j]
                if (resta > 0):
                    posicionValida += 1
                    
                else:
                    resta = -resta
                    if (resta in dictTime):
                        dictTime[resta].repeticiones += 1 
                    else:
                        dictTime[resta] = Time(resta,1)
              
                j += 1           
            i += 1        
        i = 0
        heapTime = []     
        for i in dictTime.values():
            heappush(heapTime,i)
        
        if heapTime:
            print(heapTime[0])

            
        dato = stdin.readline()      
main()