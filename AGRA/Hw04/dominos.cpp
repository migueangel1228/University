/*
AGRA   : Tarea 15 marzo 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
B - Problem B dominos.cpp 

Complejidad: 
La complejidad del algoritmo es O(N + M)

Dado que se realiza un (DFS) e para ordenar los nodos por tiempo de finalización ademas se 
realiza otro dfs para  generar el grafo transpuesto y por ultimo Se realiza un tercer DFS 
en el grafo transpuesto para asignar los nodos a sus componentes fuertemente conectados. 
Cada dfs toma O(N + M) tiempo, donde N es el numero de dominos  y M es el número de aristas en el grafo.

*/
#include <vector>
#include <list>
#include <iostream>
#include <algorithm>

using namespace std;

// Función DFS para ordenar los nodos por tiempo de finalización
void dfsOrdenar(int nodoActual, vector<vector<int>>& listaAdyacencia, vector<bool>& visitados, list<int>& ordenFinal) {
    visitados[nodoActual] = true;
    // Explorar todos los vecinos del nodo actual
    for (int i = 0; i < listaAdyacencia[nodoActual].size(); ++i) {
        int vecino = listaAdyacencia[nodoActual][i];
        if (!visitados[vecino]) {
            dfsOrdenar(vecino, listaAdyacencia, visitados, ordenFinal);
        }
    }
    ordenFinal.push_front(nodoActual);
}

// Función para asignar nodos a su componente fuertemente conectado
void asignarComponente(int nodoActual, int numComponente, vector<vector<int>>& listaAdyacenciaTranspuesta, vector<int>& componentes) {
    componentes[nodoActual] = numComponente;
    // Recorrer vecinos en el grafo transpuesto
    for (int i = 0; i < listaAdyacenciaTranspuesta[nodoActual].size(); ++i) {
        int vecino = listaAdyacenciaTranspuesta[nodoActual][i];
        if (componentes[vecino] == -1) {
            asignarComponente(vecino, numComponente, listaAdyacenciaTranspuesta, componentes);
        }
    }
}

// Algoritmo de Kosaraju para encontrar componentes fuertemente conectados
vector<int> kosaraju(vector<vector<int>>& listaAdyacencia, vector<vector<int>>& listaAdyacenciaTranspuesta, int totalNodos) {
    vector<bool> visitados(totalNodos, false);
    list<int> ordenFinal;
    vector<int> componentes(totalNodos, -1);
    int contadorComponentes = 0;

    // Primer paso: Ordenar por tiempo de finalización
    for (int nodo = 0; nodo < totalNodos; ++nodo) {
        if (!visitados[nodo]) {
            dfsOrdenar(nodo, listaAdyacencia, visitados, ordenFinal);
        }
    }

    // Segundo paso: Asignar componentes en el grafo transpuesto
    list<int>::iterator it;
    for (it = ordenFinal.begin(); it != ordenFinal.end(); ++it) {
        int nodo = *it;
        if (componentes[nodo] == -1) {
            asignarComponente(nodo, contadorComponentes, listaAdyacenciaTranspuesta, componentes);
            contadorComponentes++;
        }
    }

    return componentes;
}

int main() {
    int casos;
    cin >> casos;

    for (int casoActual = 1; casoActual <= casos; casoActual++) {
        int totalNodos, totalAristas;
        cin >> totalNodos >> totalAristas;

        vector<vector<int>> listaAdyacencia(totalNodos);
        vector<vector<int>> listaAdyacenciaTranspuesta(totalNodos);

        // Construir grafo y grafo transpuesto
        for (int i = 0; i < totalAristas; ++i) {
            int origen, destino;
            cin >> origen >> destino;
            origen--; destino--; // Ajustar índices
            listaAdyacencia[origen].push_back(destino);
            listaAdyacenciaTranspuesta[destino].push_back(origen);
        }

        // Obtener componentes fuertemente conectados
        vector<int> componentes = kosaraju(listaAdyacencia, listaAdyacenciaTranspuesta, totalNodos);

        // Calcular número de componentes
        int totalComponentes = 0;
        if (!componentes.empty()) {
            int maxComponente = *max_element(componentes.begin(), componentes.end());
            totalComponentes = maxComponente + 1;
        }

        // Construir grafo entre componentes y calcular grados de entrada
        vector<vector<int>> listaAdyacenciaComponentes(totalComponentes);
        vector<int> gradoEntrada(totalComponentes, 0);

        // Procesar todas las aristas para construir conexiones entre componentes
        for (int origen = 0; origen < totalNodos; ++origen) {
            for (int i = 0; i < listaAdyacencia[origen].size(); ++i) {
                int destino = listaAdyacencia[origen][i];
                int componenteOrigen = componentes[origen];
                int componenteDestino = componentes[destino];

                if (componenteOrigen != componenteDestino) {
                    listaAdyacenciaComponentes[componenteOrigen].push_back(componenteDestino);
                }
            }
        }

        // Eliminar duplicados y actualizar grados de entrada
        for (int comp = 0; comp < totalComponentes; ++comp) {
            // Ordenar y eliminar duplicados
            sort(listaAdyacenciaComponentes[comp].begin(), listaAdyacenciaComponentes[comp].end());
            auto ultimo = unique(listaAdyacenciaComponentes[comp].begin(), listaAdyacenciaComponentes[comp].end());
            listaAdyacenciaComponentes[comp].erase(ultimo, listaAdyacenciaComponentes[comp].end());

            // Actualizar grados de entrada para los vecinos
            for (int i = 0; i < listaAdyacenciaComponentes[comp].size(); ++i) {
                int componenteDestino = listaAdyacenciaComponentes[comp][i];
                gradoEntrada[componenteDestino]++;
            }
        }

        // Contar componentes con grado de entrada cero
        int dominosManuales = 0;
        for (int comp = 0; comp < totalComponentes; ++comp) {
            if (gradoEntrada[comp] == 0) {
                dominosManuales++;
            }
        }

        cout << dominosManuales << endl;
    }
    
    return 0;
}
/*
Sample Input
2
3 2
1 2
2 3
6 2
2 1
4 1
Sample Output
1
5
4
 ́*/



