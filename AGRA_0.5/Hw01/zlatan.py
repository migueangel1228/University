from sys import stdin
from heapq import heappush, heappop

"""
AGRA  Tarea 1 Enero 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem E  zlatan.cpp
"""

class Cards:
    def __init__(self,nombre,serial,repeticiones):
        self.nombre = nombre
        self.serial = serial
        self.repeticiones = repeticiones
        
    def __gt__(self, carta):
        if self.repeticiones == carta.repeticiones:
            ans = self.serial < carta.serial
        else:
            ans = self.repeticiones < carta.repeticiones
        return ans
    
    def __repr__(self):
        return f"{self.nombre} {self.repeticiones}"
    
def main():
    # debe de leer n cartas por caso, pero parar si n y k son 0
    caso = stdin.readline().split()
    while caso  != ['0', '0']:
        
        n = int(caso[0])
        k = int(caso[1])
        dicCartas = {}
                
        for i in range(1,n+1): # ejemplo carta, Wild-Dog 8 1
            carta = stdin.readline().split()
            if carta[0] in dicCartas:
                dicCartas[carta[0]].repeticiones += 1
            else:
                dicCartas[carta[0]] = Cards(carta[0],int(carta[1]),1)
        
        
        heapCartas = []
        
        for i in dicCartas.values():
            heappush(heapCartas,i)
            
        ordenPrint = [] # lista de cartas ordenadas alfabeticamente
        for _ in range(k):
            carta = heappop(heapCartas)
            ordenPrint.append(carta)
            
        ordenPrint.sort(key = lambda x: x.nombre)
        for i in ordenPrint:
            print(i)    
            
        caso = stdin.readline().split()
main()

               
