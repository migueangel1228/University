import sys
import math

def makeSet(v):
    p[v], rango[v] = v, 0

def findSet(v):
    ans = None
    if v == p[v]: 
        ans = v
    else:
        p[v] = findSet(p[v])
        ans = p[v]
    return ans

def unionSet(u, v):
    u, v = findSet(u), findSet(v)
    if u != v:
        if rango[u] < rango[v]: 
            u, v = v, u
        p[v] = u
        habComp[u] += habComp[v]
        if rango[u] == rango[v]: 
            rango[u] += 1

def dist(i, j):
    dx = pos[i][0] - pos[j][0]
    dy = pos[i][1] - pos[j][1]
    return math.sqrt(dx * dx + dy * dy)

def kruskal(aristas, n):
    global sumNum
    
    for i in range(n):
        makeSet(i)
        habComp[i] = hab[i]
    
    aristas.sort()
    print(*aristas)
    print(*habComp)
    for d, u, v in aristas:
        pu = findSet(u)
        pv = findSet(v)
        
        if pu != pv:
            p0 = findSet(0)
            
            if pu == p0:
                sumNum += habComp[pv] * d
                print(sumNum,habComp[pv],d)
            if pv == p0:
                sumNum += habComp[pu] * d
                print(sumNum,habComp[pu],d)
            
            unionSet(u, v)

def main():
    global p, rango, pos, habComp, hab, sumNum
    caso = 1
    n = int(input())
    
    while n != 0:
        pos = []
        hab = []
        
        for i in range(n):
            x, y, m = map(int, input().split())
            pos.append((x, y))
            hab.append(m)
        
        aristas = []
        for i in range(n):
            for j in range(i + 1, n):
                d = dist(i, j)
                aristas.append((d, i, j))
        
        p = [0] * n
        rango = [0] * n
        habComp = [0] * n
        
        sumNum = 0.0
        sumDen = sum(hab)
        
        kruskal(aristas, n)
        avg = sumNum / sumDen
        print(sumNum, sumDen,avg)
        
        print(f"Island Group: {caso} Average {avg:.2f}")
        print()
        
        caso += 1
        n = int(input())

main()