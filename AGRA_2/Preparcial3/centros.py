from collections import deque

def centers(G):
    centers = set()
    n = len(G)
    nivel = [0] * n
    gradoTotal = [0] * n
    gradoEntrada = [0] * n
    grafoInverso = [[] for _ in range(n)]
    colita = deque()
    nivelMax = 0

    # Calcular grado de salida, entrada y grafo inverso
    for i in range(n):
        gradoTotal[i] = len(G[i])  # grado de salida
        for vecino in G[i]:
            gradoEntrada[vecino] += 1
            grafoInverso[vecino].append(i)  # inverso

    # Sumar grado total (entrada + salida)
    for i in range(n):
        gradoTotal[i] += gradoEntrada[i]

    # Detectar hojas (gradoTotal <= 1)
    for i in range(n):
        if gradoTotal[i] <= 1:
            colita.append(i)

    # Si no hay hojas, todos son centros (grafo muy conectado)
    hayHojas = len(colita) > 0
    if not hayHojas:
        return set(range(n))

    # BFS pelando capas
    while colita:
        v = colita.popleft()
        
        # Vecinos salientes (v -> w)
        for w in G[v]:
            gradoTotal[w] -= 1
            if gradoTotal[w] == 1:
                colita.append(w)
                nivel[w] = nivel[v] + 1
                nivelMax = max(nivelMax, nivel[w])
        
        # Vecinos entrantes (u -> v) usando grafo inverso
        for u in grafoInverso[v]:
            gradoTotal[u] -= 1
            if gradoTotal[u] == 1:
                colita.append(u)
                nivel[u] = nivel[v] + 1
                nivelMax = max(nivelMax, nivel[u])

    # Los nodos con nivel máximo son los centros
    for i in range(n):
        if nivel[i] == nivelMax:
            centers.add(i)

    return centers
