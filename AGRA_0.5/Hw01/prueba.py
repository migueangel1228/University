"""

Samuel Alberto Mateo Bonilla Franco
Cd. 8984165
Problem E - Zlatan

https://www.delftstack.com/es/howto/python/lambda-functions-in-sort/
Como ordenar ocn lambda
"""
from sys import stdin

class Carta:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.duplicados = 1

    def getName(self):
        return self.name
    def getId(self):
        return self.id
    def getDuplicados(self):
        return self.duplicados
    def addDuplicados(self):
        self.duplicados += 1

    def __lt__(self, other):
        out = False
        if self.getDuplicados() < other.getDuplicados():
            out = True
        elif self.getDuplicados() == other.getDuplicados():
            out = self.getId() < other.getId()
        return out

    def __str__(self):
        return f'{self.getName()} {self.getDuplicados()}'

#Var

def main():
    # Lectura
    raw = stdin.readline().split()
    has = 1
    while has != 0:
        cardCollected = {}
        lista = []
        has = int(raw[0])
        sells = int(raw[1])
        i = 0
        while i < has:
            rawCard = stdin.readline().split()
            if rawCard[0] in cardCollected:
                cardCollected[rawCard[0]].addDuplicados()
            else:
                cardCollected[rawCard[0]]  = Carta(rawCard[0], int(rawCard[1]))
            i += 1

        for card in cardCollected:
            lista.append(cardCollected[card])
        lista.sort() #N LOG(N)
        salida = sorted(lista[(sells * -1):], key=lambda x: x.getName().lower())

        #Impresion
        for e in salida:
            print(e)
            
        raw = stdin.readline().split()







if __name__ == "__main__":
    main()