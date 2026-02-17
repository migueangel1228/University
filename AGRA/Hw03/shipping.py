from collections import deque
import sys

def construir_grafo(codigos, conexiones):
    mapeo_codigos = {}


    for indice in range(len(codigos)):
        mapeo_codigos[codigos[indice]] = indice
    
    total_almacenes = len(codigos)
    grafo = [[] for _ in range(total_almacenes)]
    
    for origen, destino in conexiones:
        idx_origen = mapeo_codigos[origen]
        idx_destino = mapeo_codigos[destino]
        grafo[idx_origen].append(idx_destino)
        grafo[idx_destino].append(idx_origen)
    
    return grafo, mapeo_codigos

def calcular_pasos(grafo, inicio, fin):
    if inicio == fin:
        pasos = 0
    else:
        total_nodos = len(grafo)
        visitados = [False] * total_nodos
        cola = deque([(inicio, 0)])
        visitados[inicio] = True
        pasos = -1
        encontrado = False
        
        while cola and not encontrado:
            nodo_actual, distancia = cola.popleft()
            
            for vecino in grafo[nodo_actual]:
                if vecino == fin:
                    pasos = distancia + 1
                    encontrado = True
                elif not visitados[vecino]:
                    visitados[vecino] = True
                    cola.append((vecino, distancia + 1))
        
    return pasos

def procesar_solicitudes(grafo, mapeo, solicitudes):
    resultados = []
    for solicitud in solicitudes:
        tamaño, origen, destino = solicitud
        mensaje = "NO SHIPMENT POSSIBLE"
        
        if origen in mapeo and destino in mapeo:
            idx_origen = mapeo[origen]
            idx_destino = mapeo[destino]
            num_pasos = calcular_pasos(grafo, idx_origen, idx_destino)
            
            if num_pasos != -1:
                costo = tamaño * num_pasos * 100
                mensaje = f"${costo}"
        
        resultados.append(mensaje)
    
    return resultados

def main():
    lineas = sys.stdin.read().splitlines()
    indice = 0
    num_datasets = int(lineas[indice])
    indice += 1
    
    print("SHIPPING ROUTES OUTPUT")

    for dataset_id in range(1, num_datasets + 1):
        M, N, P = map(int, lineas[indice].split())
        indice += 1
        
        codigos_almacenes = lineas[indice].split()
        indice += 1
        
        conexiones = []
        for _ in range(N):
            partes = lineas[indice].split()
            conexiones.append((partes[0], partes[1]))
            indice += 1
        
        peticiones = []
        for _ in range(P):
            datos = lineas[indice].split()
            peticiones.append((int(datos[0]), datos[1], datos[2]))
            indice += 1
        
        grafo, mapeo = construir_grafo(codigos_almacenes, conexiones)
        resultados = procesar_solicitudes(grafo, mapeo, peticiones)
        
        print(f"\nDATA SET {dataset_id}\n")
        for res in resultados:
            print(res)
    
    print("\nEND OF OUTPUT")

main()