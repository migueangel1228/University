"""
Tarea  : ADA  Tarea 2
Fecha  : 8 Marzo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem E - Ingredients
"""

from sys import stdin

INF = float("inf")

memo = {}
# inc[v] = lista de (u, cost, prestige)
inc = {}   
# mejor receta por nodo del grafo

# 1. tiene menor costo
# 2. si el costo empata, tiene mayor prestigio
def isUOptimo(u, v):
    ans = False
    costU, prestigeU = u
    costV, prestigeV = v
    if costU < costV :
        ans = True
    elif (costU == costV):
        if prestigeU > prestigeV:
            ans = True 
    return ans

# optimo para knapsack
def isUOptimo2(u, v):
    ans = False
    costU, prestigeU = u
    costV, prestigeV = v
    if prestigeU > prestigeV:
        ans = True
    elif (prestigeU == prestigeV):
        if costU < costV:
            ans = True 
    return ans

def phi(v):
    global memo, inc
    ans = 0
    if v in memo:
        ans = memo[v]
    # Caso base ninguno incide en el
    elif len(inc[v]) == 0:
        memo[v] = (0, 0)
        ans = memo[v]
    else:
        ans = (INF, -INF)
        # inc[v] contiene todas las recetas que producen a v
        # cada una tiene la forma (baseDish, addedCost, addedPrestige)
        for u, cost, prestige in inc[v]:
            costU, prestigeU = phi(u)
            cand = (costU + cost, prestigeU + prestige)

            if isUOptimo(cand, ans):
                ans = cand
    memo[v] = ans
    
    return ans

def parsing():
    line = stdin.readline()

    # saltar lineas vacias si llegan a aparecer
    while line and line.strip() == "":
        line = stdin.readline()

    if not line:
        return None

    B = int(line.strip())
    N = int(stdin.readline().strip())

    dishes = set()
    local_inc = {}

    for _ in range(N):
        derived, base, addition, cost, prestige = stdin.readline().split()
        cost = int(cost)
        prestige = int(prestige)

        dishes.add(derived)
        dishes.add(base)

        # inc[derived] = lista de recetas que llegan a derived
        if derived not in local_inc:
            local_inc[derived] = []
        local_inc[derived].append((base, cost, prestige))

        # para que exista la llave del plato base si es base
        if base not in local_inc:
            local_inc[base] = []

    return B, dishes, local_inc

def generatePlatos(dishes, B):
    # convierte cada plato v en un item (coste, prestigio)
    # usando phi(v)
    platos = []

    for dish in dishes:
        cost, prestige = phi(dish)


        # los platos basees quedan (0,0), no aportan nada
        # también descartamos platos que ya cuestan mas que el presupuesto
        if prestige > 0 and cost <= B:
            platos.append((cost, prestige))

    return platos

def KnapsackMem(i, b, platos, mem):
    
    if i == len(platos) or b == 0:
        ans = 0

    if (i, b) in mem:
        ans = mem[(i, b)]

    cost, prestige = platos[i]
    # no tomar plato
    ans = KnapsackMem(i + 1, b, platos, mem)   
    # tomar plato
    if cost <= b:
        ans = max(ans, prestige + KnapsackMem(i + 1, b - cost, platos, mem))  

    mem[(i, b)] = ans
    
    return ans

"""
def phi_tab_opt1(B, W, N, C):
  tab = [ [ 0 for _ in range(C+1) ] for _ in range(2) ]
  n,c,prev,curr = 1,0,0,1
  while n!=N+1:
    if c==C+1: n,c,prev,curr = n+1,0,1-prev,1-curr
    else:
      if W[n-1]>c: tab[curr][c] = tab[prev][c]
      else: tab[curr][c] = max(tab[prev][c], tab[prev][c-W[n-1]]+B[n-1])
      c += 1
  return tab[prev][C]
"""

def KnapsackTab(u, b, platos):
    # tab[r][c] guarda (coste_total, prestigio_total) optimo con capacidad c
    tab = [[(0, 0) for _ in range(b + 1)] for _ in range(2)]

    n, prev, curr = 0, 0, 1

    while n < len(platos):
        costU, prestigeU = platos[n]
        c = 0
        while c <= b:
            # no tomar plato
            best = tab[prev][c]

            # tomar plato
            if costU <= c:
                prevCost, prevPrestige = tab[prev][c - costU]
                cand = (prevCost + costU, prevPrestige + prestigeU)
                if isUOptimo2(cand, best):
                    best = cand

            tab[curr][c] = best
            c += 1

        n, prev, curr = n + 1, curr, prev

    c, p = tab[prev][b]
    return (p, c)


def main():
    global inc, memo
    
    isEOF = False
    while not isEOF:
        case = parsing()
        if case is None:
            isEOF = True
        else: 

            B, dishes, inc = case
            memo = {}

            # 1) phi; para encontrar el valor optimo de cada nodo
            platos = generatePlatos(dishes, B)
            mem = dict()
            # mochilero; escoge la mejor seleccion sin repetir plato
            max_prestige, min_cost = KnapsackTab(0, B, platos)
            
            print(max_prestige)
            print(min_cost)

main()


"""
Sample Input
15
6
pizza_tomato pizza_base tomato 1 2
pizza_cheese pizza_base cheese 5 10
pizza_classic pizza_tomato cheese 5 5
pizza_classic pizza_cheese tomato 1 2
pizza_salami pizza_classic salami 7 6
pizza_spicy pizza_tomato chili 3 1

Sample Output
25
15
"""
