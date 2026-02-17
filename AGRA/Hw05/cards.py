"""
A - Problem ASource file name: cards.cpp
Time limit: x seconds
In the age of television, not many people attend theater performances. Antique Comedians of Malidinesia are aware of
this fact. They want to propagate theater and, most of all, Antique Comedies. They have printed invitation cards with
all the necessary information and with the programme. A lot of students were hired to distribute these invitations among
the people. Each student volunteer has assigned exactly one bus stop and he or she stays there the whole day and gives
invitation to people travelling by bus. A special course was taken where students learned how to influence people and what
is the difference between influencing and robbery.
The transport system is very special: all lines are unidirectional and connect exactly two stops. Buses leave the originating
stop with passengers each half an hour. After reaching the destination stop they return empty to the originating stop, where
they wait until the next full half an hour, e.g. X:00 or X:30, where ‘X’ denotes the hour. The fee for transport between two
stops is given by special tables and is payable on the spot. The lines are planned in such a way, that each round trip (i.e., a
journey starting and finishing at the same stop) passes through a Central Checkpoint Stop (CCS) where each passenger has
to pass a thorough check including body scan.
All the ACM student members leave the CCS each morning. Each volunteer is to move to one predetermined stop to invite
passengers. There are as many volunteers as stops. At the end of the day, all students travel back to CCS. You are to
write a computer program that helps ACM to minimize the amount of money to pay every day for the transport of their
employees.
Input
The input consists of N cases. The first line of the input contains only positive integer N. Then follow the cases. Each case
begins with a line containing exactly two integers P and Q, 1 ≤P,Q ≤1 000 000. P is the number of stops including CCS
and Q the number of bus lines. Then there are Q lines, each describing one bus line. Each of the lines contains exactly
three numbers —the originating stop, the destination stop, and the price. The CCS is designated by number 1. Prices are
positive integers the sum of which is smaller than 1 000 000 000. You can also assume it is always possible to get from any
stop to any other stop.
The input must be read from standard input.
Output
For each case, print one line containing the minimum amount of money to be paid each day by ACM for the travel costs of
its volunteers.
The output must be written to standard output.
Sample Input
2
2 2
1 2 13
2 1 33
4 6
1 2 10
2 1 60
1 3 20
3 4 10
2 4 5
4 1 50
Sample Output
46
210
"""
from heapq import heappush, heappop
import sys
INF = float('inf')

def dijkstra(G, s):
    n = len(G)
    dist = [INF] * n
    for i in range(n):
        dist[i] = INF
    dist[s] = 0
    pqueue = [(0, s)]

    while pqueue:
        du, u = heappop(pqueue)
        if dist[u] == du:
            for v, duv in G[u]:
                if du + duv < dist[v]:
                    dist[v] = du + duv
                    heappush(pqueue, (dist[v], v))
    return dist

def main():
    cases = int(sys.stdin.readline())
    resultsCases = []

    for _ in range(cases):
        P, Q = map(int, sys.stdin.readline().split())
        graph = [[] for _ in range(P + 1)]
        graphTRANS = [[] for _ in range(P + 1)]

        for _ in range(Q):
            origen, destino, price = map(int, sys.stdin.readline().split())
            graph[origen].append((destino, price))
            graphTRANS[destino].append((origen, price))

        distanceIDA = dijkstra(graph, 1)
        distanceVuelta = dijkstra(graphTRANS, 1)

        costoTotal = 0
        for node in range(1, P + 1):
            costoTotal += distanceIDA[node] + distanceVuelta[node]

        costoTotal -= (distanceIDA[1] + distanceVuelta[1])
        resultsCases.append(costoTotal)

    for result in resultsCases:
        print(result)

main()
