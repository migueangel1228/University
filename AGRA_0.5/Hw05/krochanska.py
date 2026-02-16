"""
D - Problem DSource file name: krochanska.cpp
Time limit: x seconds
This is a problem about spies and counter-spies in the old days of the Iron Curtain. CONTROL, the secret intelligence
agency of the free world, must fight against KAOS, the international organization of evil.
CONTROL agents 82 through 85 have all diedattempting to deliver the payroll for Control’s freelance agents located
behind the Iron Curtain. They all were killed by the mysterious and sinister KAOS agent Cirilo Krochanska, while traveling
aboard the Orient Express. You are Maxwell Smart, agent 86, and you must board the train, make contact with agent
B-12, give him the encrypted message “tnih sevig cilc thgir”, deliver the payroll, and avoid becoming Krochanska’s fifth
victim!
But, where is Krochanska? We know he always travel by train; he is in some important train station in Europe, and is ready
to reach immediately any destination where he is required.
The railway network of Europe consists of a number of lines. Each line goes between two different stations; and there are
also some intermediate stations uniformly distributed in each line. For example, if we enumerate the stations from 1 to 13,
we can have the following three lines:
•Line 1. 1 - 2 - 3 - 4 - 5 - 6 - 7.
•Line 2. 8 - 9 - 4 - 10 - 13.
•Line 3. 11 - 2 - 12 - 9 - 6 - 7.
Trains travel in both directions of the lines. The time to travel from a station to the following (or the previous) station of
the line is always 2 hours. As you can observe, some stations are used by different lines —we call them the important
stations—, while other stations are only used by one line —the secondary stations—.
We believe Krochanska is situated in an important station where he can travel faster to any other station. In particular, he
tries to minimize the average of the minimum times from his station to the rest of important stations. You can assume that
there is no loss of time to switch from one line to another at a station.
You have to find out where Cirilo Krochanska is.
Input
The input will contain several test cases. The first line indicates the number of test cases.
For each test case, the first line contains two integers: N and S . N is the total number of existing stations, and S is the
number of lines. Stations are numbered from 1 to N; N is not greater than 10000; and S is not greater than 100. Next, we
have S lines, one for each train line. These lines consist of a list of stations, separated by blank spaces, ending with a
’0’.
There will be between 1 and 100 important stations, inclusive. There is always a path between any pair of stations.
The input must be read from standard input.
Output
For each test case, you have to output the number of the resulting station, in the following format:
Krochanska is in: X
where X is the number of the station. If there are more than one important station with the minimum distance, then you
have to output the one with the smallest number.
The output must be written to standard output.
7
 ́Arboles y Grafos Tarea 5 2025-1
Sample Input
4
13 3
1 2 3 4 5 6 7 0
8 9 4 10 13 0
11 2 12 9 6 7 0
6 2
2 5 3 6 1 4 0
4 1 6 3 5 2 0
5 2
1 2 3 4 5 0
3 5 1 4 2 0
7 2
3 5 1 2 4 7 6 0
3 6 1 0
Sample Output
Krochanska is in: 9
Krochanska is in: 3
Krochanska is in: 4
Krochanska is in: 6
"""

from collections import deque
from sys import stdin

# Implementación con un único origen s.
# Se evita el uso del arreglo de visitados ya que cuando un elemento no ha
# sido descubiero su costo es infinito, optimizacion sin 
def ssspBFS(G, s, arrISs):
    q = deque()
    n = len(G)
    d = []
    for _ in range(n):
      d.append(float("inf"))
    p = []
    for _ in range(n):
      p.append(-1)
    d[s] = 0
    q.append(s)

    # arreglo booleano de estaciones importantes
    esIS = []
    for _ in range(n):
      esIS.append(False)
    
    
    for i in arrISs:
        esIS[i - 1] = True

    # cuántas estaciones importantes faltan por visitar (excluyendo la de inicio si es importante) 
    if esIS[s]:
      ISsRestantes = sum(esIS) - 1 
    else:
      ISsRestantes = sum(esIS)

    flag = False
    while q and not flag:
        v = q.popleft()
        for u in G[v]:
            if d[u] == float("inf"):
                d[u] = d[v] + 1
                p[u] = v
                q.append(u)
                if esIS[u]:
                    ISsRestantes -= 1
                    if ISsRestantes == 0:
                        flag = True  # bandera para salir del while
    return d, p

def main():
  cases = int(stdin.readline())
  actualCase = 0
  while actualCase < cases:
    entrada = stdin.readline().split()
    nodes = entrada[0]
    aristas = entrada[1]
    graph = [[] for _ in range(int(nodes))]
    ISs = set()  # Important Stations
    stations = set()  # Todas las estaciones

    for _ in range(int(aristas)):
      line = list(map(int, stdin.readline().split()))
      line = line[:-1]  # Se elimina el 0 final
      for i in range(len(line) - 1):
        graph[line[i] - 1].append(line[i + 1] - 1)
        graph[line[i + 1] - 1].append(line[i] - 1)
        if line[i] in stations:
          ISs.add(line[i])
        else:
          stations.add(line[i])
      # Se procesa la última estación de la línea
      if line[-1] in stations:
        ISs.add(line[-1])
      else:
        stations.add(line[-1])
      
    ISs = sorted(ISs)  # Ahora es una lista ordenada
    bestIS = 0
    bestTime = float("inf")
    
    for station in ISs:
      distances, _ = ssspBFS(graph, station - 1,ISs)
      if len(ISs) > 1:
        timePromedio = 0
        for other in ISs:
            if other != station:
              timePromedio += distances[other - 1]
        timePromedio = timePromedio / (len(ISs) - 1)
      else:
        timePromedio = 0  # evitar divi por cero cuando solo hay una IS. melo
      
      if timePromedio < bestTime or (timePromedio == bestTime and station < bestIS):
        bestTime = timePromedio
        bestIS = station
    
    print(f"Krochanska is in: {bestIS}")
    actualCase += 1

main()
