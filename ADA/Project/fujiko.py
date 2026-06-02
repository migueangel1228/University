"""
Tarea  : ADA  Proyecto 
Fecha  : 1 junio 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem - A - FujikoMine
"""

"""
Código de honor

Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali, los valores éticos y la integri-
dad son tan importantes como la excelencia académica. En este curso se espera que los estudiantes se comporten ética

y honestamente, con los más altos niveles de integridad escolar. En particular, se asume que cada estudiante adopta el
siguiente código de honor:
Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
Integridad académica se refiere a ser honesto, dar crédito a quien lo merece y respetar el trabajo de los demás. Por eso
es importante evitar plagiar, engañar, 'hacer trampa', etc. En particular, el acto de entregar un programa de computador
ajeno como propio constituye un acto de plagio; cambiar el nombre de las variables, agregar o eliminar comentarios
y reorganizar comandos no cambia el hecho de que se está copiando el programa de alguien más. Para más detalles
consultar el Reglamento de Estudiantes, Sección VI.
"""

from sys import stdin

# Valor usado para representar un estado imposible en la DP.
INF = -float("inf")

# Conjunto global que guarda los nodos de transmisión del caso actual.
nodesTrans = set()

# Lista de adyacencia del árbol del caso actual.
graph = []

# Recibe:
#   n: número total de nodos del árbol.
#   G: lista de adyacencia del árbol.
# Hace:
#   Identifica cuál nodo es la raíz del árbol.
#   Como las aristas están dadas en dirección padre -> hijo, la raíz es el único
#   nodo que no aparece como hijo de ningún otro.
# Devuelve:
#   El índice del nodo raíz.
def find_root(n, G):
    has_parent = [False] * n
    i = 0
    root = -1
    found = False

    for u in range(n):
        for v, _ in G[u]:
            has_parent[v] = True

    while i < n and not found:
        if not has_parent[i]:
            root = i
            found = True
        i += 1
    return root

# Recibe:
#   root: raíz del árbol.
#   G: lista de adyacencia del árbol.
# Hace:
#   Genera un recorrido postorden del árbol.
#   Esto permite procesar primero los hijos y luego el padre, que es lo
#   necesario para construir la programación dinámica sobre árboles.
# Devuelve:
#   Una lista con los nodos en orden postorden.
def generate_postorder(root, G):
    order = []
    stack = [root]
    while stack:
        u = stack.pop()
        order.append(u)
        for v, _ in G[u]:
            stack.append(v)

    result = []
    while order:
        result.append(order.pop())
    return result

# Recibe:
#   u: nodo actual.
#   children: hijos directos de u con sus pesos.
#   max_trans: máximo número de nodos de transmisión que se pueden usar en
#             el subárbol de u.
#   sizes: arreglo con la cantidad de nodos de transmisión por subárbol.
#   tab: tabla DP ya calculada para los nodos hijos.
# Hace:
#   Construye la tabla DP del nodo u combinando uno por uno los resultados de
#   sus hijos.
#   La idea es guardar, para cada cantidad de transmisiones, la mejor ganancia
#   posible en el subárbol conectado que contiene a u.
# Devuelve:
#   Una lista dp_u donde dp_u[k] es la mejor ganancia usando exactamente k
#   transmisiones dentro del subárbol de u.
def merge_children(u, children, max_trans, sizes, tab):
    is_trans = u in transmission_nodes
    dp_u = [INF] * (max_trans + 1)

    if is_trans:
        trans_used = 1
        if max_trans >= 1:
            dp_u[1] = 0
    else:
        trans_used = 0
        dp_u[0] = 0

    for v, w in children:
        child = tab[v]
        size_v = sizes[v]
        total_trans = min(max_trans, trans_used + size_v)

        while total_trans >= 0:
            lim = min(size_v, total_trans)
            j = 1
            while j <= lim:
                parent = dp_u[total_trans - j]
                if child[j] != INF and parent != INF:
                    val = parent + child[j] + w
                    if val > dp_u[total_trans]:
                        dp_u[total_trans] = val
                j += 1
            total_trans -= 1

        trans_used += size_v

    return dp_u

# Recibe:
#   root: raíz del árbol.
#   G: lista de adyacencia del árbol.
#   sizes: arreglo con el número de transmisiones por subárbol.
# Hace:
#   Calcula toda la tabla DP del árbol en postorden.
#   Para cada nodo, guarda la mejor solución para cada cantidad posible de
#   transmisiones dentro de su subárbol.
# Devuelve:
#   La tabla completa DP del árbol.
def phi_tab(root, G, sizes):
    order = generate_postorder(root, G)
    tab = [None] * len(G)

    for u in order:
        children = G[u]
        max_trans = sizes[u]

        if len(children) == 0:
            tab[u] = [INF] * (max_trans + 1)
            if u in transmission_nodes:
                if max_trans >= 1:
                    tab[u][1] = 0
            else:
                tab[u][0] = 0
        else:
            tab[u] = merge_children(u, children, max_trans, sizes, tab)

    return tab

# Recibe:
#   root: raíz del árbol.
#   G: lista de adyacencia del árbol.
#   subtree_sizes: arreglo donde se guardará el número de transmisiones de cada
#                 subárbol.
# Hace:
#   Calcula cuántos nodos de transmisión hay en cada subárbol.
#   Esta información sirve para limitar los estados de la DP y evitar calcular
#   casos imposibles.
# Devuelve:
#   No devuelve nada; llena el arreglo subtree_sizes.
def compute_transmission_sizes(root, G, subtree_sizes):
    stack = [root]
    order = []

    while len(stack) > 0:
        u = stack.pop()
        order.append(u)
        for v, _ in G[u]:
            stack.append(v)

    i = len(order) - 1
    while i >= 0:
        u = order[i]
        ans = 1
        if u in transmission_nodes:
            ans = 1
        else:
            ans = 0
        for v, _ in G[u]:
            ans += subtree_sizes[v]
        subtree_sizes[u] = ans
        i -= 1

# Recibe:
#   n: número de nodos.
#   m: número de nodos de transmisión.
#   G: lista de adyacencia del árbol.
#   queries: lista de consultas x.
# Hace:
#   Resuelve todas las consultas del caso actual.
#   Primero calcula la raíz, luego preprocesa tamaños y la DP del árbol,
#   y finalmente responde cada query usando la tabla ya construida.
# Devuelve:
#   Una lista con la respuesta para cada consulta.
def solution(n, m, G, queries):
    root = find_root(n, G)
    subtree_sizes = [0] * n
    compute_transmission_sizes(root, G, subtree_sizes)
    results = []
    i = 0

    dp_table = phi_tab(root, G, subtree_sizes)

    while i < len(queries):
        query = queries[i]
        max_crypto = 0

        if query <= m:
            if query <= 1:
                max_crypto = 0
            else:
                start_node = 0
                while start_node < n:
                    if start_node in transmission_nodes and query <= subtree_sizes[start_node]:
                        crypto = dp_table[start_node][query]
                        if crypto != INF and crypto > max_crypto:
                            max_crypto = crypto
                    start_node += 1

        results.append(max_crypto)
        i += 1
    return results

# Recibe:
#   No recibe parámetros; lee directamente de la entrada estándar.
# Hace:
#   Lee todos los casos de prueba.
#   Para cada caso:
#   1. Lee n, m y q.
#   2. Construye el árbol.
#   3. Lee los nodos de transmisión.
#   4. Lee las consultas.
#   5. Llama a solution().
#   6. Imprime la respuesta de cada query.
# Devuelve:
#   No devuelve nada; solo imprime la salida del programa.
def main():
    global transmission_nodes, graph
    line = stdin.readline().split()
    while len(line) > 0:
        n = int(line[0])
        m = int(line[1])

        graph = [[] for _ in range(n)]
        i = 0

        while i < n - 1:
            n1, n2, p = map(int, stdin.readline().split())
            graph[n1].append((n2, p))
            i += 1

        transmission_nodes = set(map(int, stdin.readline().split()))
        queries = list(map(int, stdin.readline().split()))

        results = solution(n, m, graph, queries)
        for val in results:
            print(val)

        line = stdin.readline().split()

main()

"""
Sample Input 1
16 9 5
0 1 20
0 9 30
1 10 40
1 2 20
1 11 100
9 12 25
9 13 5
10 3 30
10 4 10
2 5 15
11 14 40
12 6 25
13 7 5
7 8 5
7 15 10
0 1 2 3 4 5 6 7 8
1 2 3 4 16
2 1 1
1 0 2
1
1
Sample Output 1
0
80
100
170
0
0
"""

"""
Sample Input 2
59 41 15
9 54 223
49 11 348
47 48 113
54 34 417
22 30 361
23 58 360
9 8 99
6 24 453
28 53 105
55 38 225
22 21 188
45 42 89
9 6 399
37 47 84
4 46 152
54 10 347
0 23 284
36 43 312
52 13 468
11 15 203
19 31 21
25 33 34
47 50 239
47 32 318
52 28 259
27 17 243
37 12 22
18 35 135
42 3 173
52 0 325
1 25 448
42 44 3
11 9 500
37 36 349
14 45 490
56 1 146
1 40 493
36 41 133
53 20 475
16 49 494
28 27 446
25 16 24
18 37 71
49 52 363
46 56 186
6 2 37
36 57 44
18 19 90
23 26 337
6 29 476
56 22 377
19 55 301
5 4 453
3 18 424
35 39 335
53 51 461
22 14 74
53 7 399
13 1 21 20 25 5 24 53 28 30 19 54 35 44 55 57 10 33 8 31 41 6 4 12 42 49 45 43 26 51 58 0 46 9 22 47 27 32 3 11 16
4 39 57 51 24 24 27 41 45 41 7 44 5 33 22
Sample Output 2
1826
12224
0
0
9601
9601
10439
12248
0
12248
3142
0
2294
11757
8903

"""

"""
Sample Input 3
64 17 9
34 43 97
18 51 379
55 31 3
59 41 214
51 5 20
42 21 288
44 20 342
49 34 311
26 39 321
18 14 117
47 0 439
26 32 47
40 9 457
36 19 216
32 61 310
23 35 349
54 7 165
8 59 398
55 25 348
14 8 412
56 46 470
28 33 190
8 40 341
10 58 409
27 38 283
42 52 483
11 22 164
34 3 469
7 28 428
44 27 363
32 1 49
51 2 249
18 54 470
22 45 253
27 18 277
2 12 2
56 4 362
61 47 287
7 29 33
21 17 141
7 11 51
51 49 84
32 30 106
25 15 450
56 13 262
21 23 332
21 53 3
61 44 412
6 42 297
8 36 87
49 50 325
40 37 62
39 62 275
40 60 74
59 48 126
34 56 279
14 16 459
44 10 331
36 57 48
55 63 197
27 6 238
49 55 169
38 24 85
62 35 4 51 14 46 24 45 5 13 16 12 25 63 33 53 10
0 19 39 32 34 57 12 43 54
Sample Output 3
0
0
0
0
0
0
0
0
0
"""