from sys import stdin

MAX = 10000
adj = [[] for i in range(MAX)]
visitado = [0 for i in range(MAX)]
sccInd = [-1 for i in range(MAX)]
n, t, numSCC = int(), 0, 0
sccNodos, pilaS, pilaP = [], [], []

def gabow():
    for i in range(n):
        sccInd[i], visitado[i] = -1, -1

    for i in range(n):
        if visitado[i] == -1:
            gabowAux(i)

def gabowAux(v):
    global t, numSCC
    t += 1
    visitado[v] = t
    pilaS.append(v)
    pilaP.append(v)

    for i in range(len(adj[v])):
        w = adj[v][i];
        if visitado[w] == -1:
            gabowAux(w)
        elif sccInd[w] == -1:
            while visitado[pilaP[-1]] > visitado[w]:
                pilaP.pop()

    if v == pilaP[-1]:
        numSCC += 1
        sccNodos.append([])
        print("SCC con indice %d: " % numSCC, end = '')
        while pilaS[-1] != v:
            a = pilaS.pop()
            print("%d " % a, end = '')
            sccInd[a] = numSCC - 1
            sccNodos[numSCC - 1].append(a)

        a = pilaS.pop()
        print("%d " % a)
        sccInd[a] = numSCC - 1
        sccNodos[numSCC - 1].append(a)
        pilaP.pop()

def main():
    global n
    n, m = list(map(int, stdin.readline().split()))

    for i in range(m):
        u, v = list(map(int, stdin.readline().split()))
        adj[u].append(v)

    print("Grafo")
    for i in range(n):
        print("Nodo %d:" % i)
        for j in range(len(adj[i])):
            print("%d" % adj[i][j], end = ' ')
        print("")

    print("Componentes Fuertemente Conexos:")
    gabow()

main()

    
    
