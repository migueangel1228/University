from sys import stdin
import math

#operaciones disjoint set union
#**************************************
p, rango = [0 for _ in range(13)], [0 for _ in range(13)]

def makeSet(v):
    p[v], rango[v] = v, 0

def findSet(v):
    ans = None
    if v == p[v]: ans = v
    else:
        p[v] = findSet(p[v])
        ans = p[v]
    return ans

def unionSet(u, v):
    u, v = findSet(u), findSet(v)

    if u != v:
        if rango[u] < rango[v]: u, v = v, u
        p[v] = u
        if rango[u] == rango[v]: rango[u] += 1

#****************************************

def main():
    for i in range(1, 13):
        makeSet(i)

    print("Valores p:", *p[1:])
    print("Valores rango:", *rango[1:])
    unionSet(4, 5)
    print("Después de unir 4 y 5")
    print("Valores p:", *p[1:])
    print("Valores rango:", *rango[1:])
    unionSet(6, 8)
    print("Después de unir 6 y 8")
    print("Valores p:", *p[1:])
    print("Valores rango:", *rango[1:])
    unionSet(1, 12)
    print("Después de unir 1 y 12")
    print("Valores p:", *p[1:])
    print("Valores rango:", *rango[1:])
    unionSet(5, 1)
    print("Después de unir 5 y 1")
    print("Valores p:", *p[1:])
    print("Valores rango:", *rango[1:])
    aux = findSet(12)
    print("12 pertenece al conjunto con id", aux)
    print("Despues de comprimir el camino de 12")
    print("Valores p:", *p[1:])
    print("Valores rango:", *rango[1:])
    unionSet(10, 8)
    print("Después de unir 10 y 8")
    print("Valores p:", *p[1:])
    print("Valores rango:", *rango[1:])
    unionSet(2, 6)
    print("Después de unir 2 y 6")
    print("Valores p:", *p[1:])
    print("Valores rango:", *rango[1:])
    aux = findSet(10)
    print("10 pertenece al conjunto con id", aux)
    print("Despues de comprimir el camino de 10")
    print("Valores p:", *p[1:])
    print("Valores rango:", *rango[1:])
    unionSet(10, 1)
    print("Despues de unir 10 y 1")
    print("Valores p:", *p[1:])
    print("Valores rango:", *rango[1:])
    aux = findSet(8)
    print("8 pertenece al conjunto con id ", aux)
    print("Despues de comprimir el camino de 8")
    print("Valores p:", *p[1:])
    print("Valores rango:", *rango[1:])

main()
