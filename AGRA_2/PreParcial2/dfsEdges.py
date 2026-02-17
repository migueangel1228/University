def dfsAux(u, G, vis, estado, desc, t, edge):
  # estado: 0 = no visitado, 1 = en proceso, 2 = completado
  vis[u] = True
  estado[u] = 1 
  t[0] += 1
  desc[u] = t[0]
  
  for v in G[u]:
    if not vis[v]:
      edge[(u, v)] = "tree edge"
      dfsAux(v, G, vis, estado, desc, t, edge)
    elif estado[v] == 1:
      edge[(u, v)] = "back edge"
    elif estado[v] == 2:
      if desc[u] < desc[v]:
        edge[(u, v)] = "forward edge"
      else:
        edge[(u, v)] = "cross edge"
  estado[u] = 2  # Marcamos como "completado"
  t[0] += 1

def dfs(G):
  n = len(G)
  vis = [False] * n
  estado = [0] * n  # 0: no visitado, 1: en proceso, 2: completado
  desc = [0] * n
  t = [0]  # Usamos lista para pasar por referencia
  edges = {}  # Diccionario para almacenar clasificación
  for u in range(n):
    if not vis[u]:
      dfsAux(u, G, vis, estado, desc, t, edges)
  return edges

# Función para imprimir los resultados de manera legible
def imprimir_clasificacion(G):
  aristas = dfs(G)
  
  print("Clasificación de aristas:")
  print("-" * 40)
  
  # Agrupar por tipo
  tipos = {}
  for arista, tipo in aristas.items():
    if tipo not in tipos:
      tipos[tipo] = []
    tipos[tipo].append(arista)
  
  for tipo in ["tree edge", "back edge", "forward edge", "cross edge"]:
    if tipo in tipos:
      print(f"\n{tipo.upper()}:")
      for u, v in tipos[tipo]:
        print(f"  ({u} → {v})")


# Ejemplo de uso
def main():
  # Ejemplo 1: Grafo dirigido simple
  G1 = [
    [1, 2],     # 0 → 1, 2
    [3],        # 1 → 3
    [1, 3],     # 2 → 1, 3
    []          # 3 → 
  ]
  
  print("Grafo 1:")
  imprimir_clasificacion(G1)
  
  print("\n" + "="*40 + "\n")
  
  # Ejemplo 2: Grafo con ciclo
  G2 = [
    [1],        # 0 → 1
    [2],        # 1 → 2
    [0, 3],     # 2 → 0, 3
    []          # 3 →
  ]
  
  print("Grafo 2 (con ciclo):")
  imprimir_clasificacion(G2)
main()