"""
Nickname: Mianparito
Date:     16/1/26
Topic:    "Grafos de estados (2 dimensiones)"

https://onlinejudge.org/external/108/10801.pdf

"""
from sys import stdin

from heapq import heappush,heappop

INF = float('inf')

def dijkstra(elevatorWeights, matrizPisos, k):
    n = len(elevatorWeights)
    encontrado = False
    dist = [[INF] * n for _ in range(101)]
    pq = []
    
    for e in range(n):
        if matrizPisos[e][0] == 0:
            dist[0][e] = 0
            heappush(pq,(0, 0, e)) # time actual(peso), floor, elevator
            
    while (len(pq) > 0 and not encontrado):
        time, floor, elev = heappop(pq)
        
        if dist[floor][elev] == time:
            # Caso 1: moverse dentro del mismo elevator
            for nFloor in matrizPisos[elev]:
                
                if nFloor != floor:
                    cost = abs(nFloor - floor) * elevatorWeights[elev]
                    newTime = time + cost
                    
                    if newTime < dist[nFloor][elev]:
                        dist[nFloor][elev] = newTime
                        heappush(pq, (newTime, nFloor, elev))
                        
            # Caso 2: cambiar de elevator en el mismo floor
            for e2 in range(n):
                if e2 != elev and floor in matrizPisos[e2]:
                    newTime = time + 60
                    
                    if newTime < dist[floor][e2]:
                        dist[floor][e2] = newTime
                        heappush(pq, (newTime, floor, e2))           
    ans = min(dist[k])
    if ans == INF:
        ans = "IMPOSSIBLE"
    return ans 

def main():
    
    for line in stdin:
        imput = list(map(int, line.split()))
        n, k = imput
        # Peso elevators
        elevatorWeights = list(map(int, stdin.readline().split()))
        # Piso de elvators
        matrizPisos = []
        
        for i in range(n):
            aux = list(map(int, stdin.readline().split()))
            if (aux[0] == 0):
                posInicial = i
            matrizPisos.append(aux)
        
        result = dijkstra(elevatorWeights, matrizPisos, k)
        print(result)
            
        
main()


"""
Sample Input
2 30
10 5
0 1 3 5 7 9 11 13 15 20 99
4 13 15 19 20 25 30
2 30
10 1
0 5 10 12 14 20 25 30
2 4 6 8 10 12 14 22 25 28 29
3 50
10 50 100
0 10 30 40
0 20 30
0 20 50
1 1
2
0 2 4 6 8 10
Sample Output
275
285
3920
IMPOSSIBLE
"""