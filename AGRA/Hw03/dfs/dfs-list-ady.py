from sys import stdin

MAX = 10000
adj = [[] for i in range(MAX)]
visitado = [0 for i in range(MAX)]
p = [-1 for i in range(MAX)]
d, f = [-1 for _ in range(MAX)], [-1 for _ in range(MAX)]
n, t = int(), 0

# 0 = no visitado, 1 = visitado
def dfsAux(u):
    global t
    d[u] = t
    t += 1
    visitado[u] = 1
    print(u)

    for v in adj[u]:
        if visitado[v] == 0:
            p[u] = v
            dfsAux(v)
    f[v] = t
    t += 1

def dfs():
    for i in range(n):
        visitado[i] = 0
        p[i] = -1
        d[i] = -1
        f[i] = -1

    for i in range(n):
        if visitado[i] == 0:
            dfsAux(i)

def main():
    global n
    n, m = list(map(int, stdin.readline().split()))

    for i in range(n):
        vals = list(map(int, stdin.readline().split()))
        u = vals[0]
        for j in range(u):
            adj[i].append(vals[j + 1])

    print("Grafo")
    for i in range(n):
        print("Nodo %d:" % i)
        for j in range(len(adj[i])):
            print("%d" % adj[i][j], end = ' ')
        print("")

    print("Recorrido en profundidad grafo:")
    dfs()
    print("Predecesores:")
    for i in range(n):
        print("El predecesor de %d es %d" % (i, pred[i]))

main()

    
    
