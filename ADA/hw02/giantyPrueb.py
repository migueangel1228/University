from sys import stdin

INF = float("inf")

# k del problema | rango del problema
def phi(k,l,r):
    ans = 0
    if l > r:
        ans = 0
    elif r > l:
        min = INF
        for c in range(l,r + 1):
            aux = (phi(k, l, c - 1) + phi(k, c + 1, r) + ((c + k) * (r - l + 1)))
            if aux < min:
                min = aux
            ans = min
    return ans

mem = {}
k = 0

def phiMem(A, l, r):
    global mem, k
    # A: diccionario pasado por referencia para guardar la elección óptima (l,r) -> c
    if (l, r) in mem:
        return mem[(l, r)]
    if l >= r:
        mem[(l, r)] = 0
        return 0
    if r - l == 1:
        ans = (l + k) * 2
        mem[(l, r)] = ans
        A[(l, r)] = l            # elección trivial: elegir l
        return ans
    if r - l == 2:
        ans = (l + 1 + k) * 3
        mem[(l, r)] = ans
        A[(l, r)] = l + 1        # elección trivial aproximada
        return ans

    minimo = INF
    best = None
    for c in range(l, r + 1):
        left = phiMem(A, l, c - 1)
        right = phiMem(A, c + 1, r)
        aux = left + right + ((c + k) * (r - l + 1))
        if aux < minimo:
            minimo = aux
            best = c
    mem[(l, r)] = minimo
    A[(l, r)] = best
    return minimo

def reconstruct_choices(A, l, r, res):
    # recorrido pre-order de las elecciones guardadas
    if l > r:
        return
    c = A.get((l, r))
    if c is None:
        return
    res.append(c)
    reconstruct_choices(A, l, c - 1, res)
    reconstruct_choices(A, c + 1, r, res)

def main():
    casitos = int(stdin.readline())
    global mem, k
    for caso in range(casitos):
        N, k = list(map(int, stdin.readline().split()))
        mem = {}
        l, r = 1, N
        A = {}                    # diccionario que se pasa por referencia
        opt = phiMem(A, l, r)
        print(f"Case {caso + 1}: {opt}")
        # si quieres ver las elecciones (orden root-left-right):
        elecciones = []
        reconstruct_choices(A, l, r, elecciones)
        print("Choices:", elecciones)

main()