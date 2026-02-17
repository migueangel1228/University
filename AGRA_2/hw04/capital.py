from sys import stdin

def tarjan(G, low, vis, enP, sccNodos, p):
    n = len(G)
    t = [0]         
    numSCC = [0]   
    sccIdx = [-1 for _ in range(n)]
    for i in range(n):
        if vis[i] == -1:
            tarjanAux(i, G, low, vis, enP, p, sccNodos, t, numSCC, sccIdx)
    return sccNodos, sccIdx

def tarjanAux(v, G, low, vis, enP, p, sccNodos, t, numSCC, sccIdx):
    t[0] += 1
    vis[v], low[v] = t[0], t[0]
    p.append(v)
    enP[v] = True

    for w in G[v]:
        if vis[w] == -1:
            tarjanAux(w, G, low, vis, enP, p, sccNodos, t, numSCC, sccIdx)
            low[v] = min(low[v], low[w])
        elif enP[w]:
            low[v] = min(low[v], vis[w])

    if low[v] == vis[v]:
        sccNodos.append([])
        numSCC[0] += 1
        fin = False
        while not fin:
            a = p.pop()
            enP[a] = False
            sccNodos[numSCC[0] - 1].append(a)
            sccIdx[a] = numSCC[0] - 1
            if a == v: fin = True

def crearGrafoDeComponentes(G, SCCNodos, sccIdx):
    n = len(SCCNodos)
    grafoSCC = [[] for _ in range(n)]
    vis = [set() for _ in range(n)]

    for v in range(len(G)):
        comp_v = sccIdx[v]  
        for u in G[v]:
            comp_u = sccIdx[u]
            if comp_v != comp_u and comp_u not in vis[comp_v]:
                vis[comp_v].add(comp_u)
                grafoSCC[comp_v].append(comp_u)

    return grafoSCC


def main():
    listica = list(map(int, stdin.readline().split()))
    while listica:
        n = listica[0]
        m = listica[1]
        matriz = [[] for _ in range(n)]
        visitado, low = [-1 for _ in range(n)], [-1 for _ in range(n)]
        enPila = [False for _ in range(n)]

        sccNodos, pila = [], []

        for i in range(m):
            u, v = list(map(int, stdin.readline().split()))
            matriz[u - 1].append(v - 1)

        nodosSCC, sccIdx = tarjan(matriz,low,visitado,enPila,sccNodos,pila)

        SCCGraph = crearGrafoDeComponentes(matriz,nodosSCC,sccIdx)
        
        flagCnt = 0
        for v in range(len(SCCGraph)):
            if len(SCCGraph[v]) < 1:
                componenteAns = v
                flagCnt += 1
        if flagCnt == 1:
            listAns = []
            for i in nodosSCC[componenteAns]:
                listAns.append(i + 1)
            print(len(listAns))
            listAns.sort()
            print(*listAns)
        else:
            print(0)
        listica = list(map(int, stdin.readline().split()))
        
        

main()
"""
Sample Input
4 4
1 2
3 2
4 3
2 1
5 5
1 2
4 5
4 3
2 4
3 2
Sample Output
2
1 2
1
5
"""