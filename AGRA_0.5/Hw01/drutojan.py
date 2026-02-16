from sys import stdin
from collections import deque

"""
AGRA  Tarea 1 Enero 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem D  drutojan.py - 11797
"""

def main():
    listaPasajeros = ["Ja", "Sam", "Sha", "Sid", "Tan"]
    cases = int(stdin.readline())
    
    for case in range(cases):
        lis = stdin.readline().split()
        seatTime = int(lis[0])
        totalTime = int(lis[1])
        personaSentada = lis[2]

        personas = {
            
            "Ja": [deque(), 0],
            "Sam": [deque(), 0],
            "Sha": [deque(), 0],
            "Sid": [deque(), 0],
            "Tan": [deque(), 0]
        }

# leer nombres
        
        for j in listaPasajeros:
            ListNames = stdin.readline().split()
            index = 1
            while index < len(ListNames):
                personas[j][0].append(ListNames[index])
                index += 1

        # 
        actualTime = 0
        while actualTime < totalTime:
            
            if (seatTime + actualTime > totalTime):
                rest = seatTime + actualTime - totalTime
                personas[personaSentada][1] += seatTime - rest
            
            else:    
                personas[personaSentada][1] += seatTime

            if (len(personas[personaSentada][0]) != 0):
                auxPersonaSentada = personas[personaSentada][0].popleft()
                personas[personaSentada][0].append(auxPersonaSentada)
                personaSentada = auxPersonaSentada

            actualTime += seatTime + 2

        # Printear
        print(f"Case {case + 1}:")
        for i in listaPasajeros:
            print(f"{i} {personas[i][1]}")
        

if __name__ == "__main__":
    main()
