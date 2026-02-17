#include <vector>
#include <string>
#include <iostream>
#include <stack>
#include <algorithm>

using namespace std;

/*
AGRA   : Tarea 3 febrero 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
B - Problem B forest.cpp 

*/

// Función DFS para explorar un groves de trees
pair<string, int> explorarGrove(int fila_inicio, int columna_inicio, 
                               vector<vector<pair<string, int> > >& matrizEspeciesAlturas,
                               vector<vector<bool> >& visitados,
                               int total_filas, int total_columnas) {
    
    string especieGrove = matrizEspeciesAlturas[fila_inicio][columna_inicio].first;
    int maxHeight = matrizEspeciesAlturas[fila_inicio][columna_inicio].second;
    
    stack<pair<int, int>> Stack;
    Stack.push(make_pair(fila_inicio, columna_inicio));
    visitados[fila_inicio][columna_inicio] = true;

    // direcciones  izquierda   ,  derecha 
    //              arriba      ,   abajo,  
    


    pair<int, int> direcciones[4] = {make_pair(-1, 0), make_pair(1, 0), 
                                     make_pair(0, -1), make_pair(0, 1)};

    while (!Stack.empty()) {
        pair<int, int> treeActual = Stack.top();
        Stack.pop();
        
        int fila_actual = treeActual.first;
        int columna_actual = treeActual.second;

        // Explorar todas las direcciones posibles (horizontales y verticales)
        for (int d = 0; d < 4; ++d) {
            int newRow = fila_actual + direcciones[d].first;
            int newCol = columna_actual + direcciones[d].second;

            // Verificar todos los limites de la matriz (direcciones)
            if (newRow >= 0 && newRow < total_filas && 
                newCol >= 0 && newCol < total_columnas) {
                
                // verificar si (no ha sido visitado) y (es la misma especie)
                if ((!visitados[newRow][newCol]) && 
                    (matrizEspeciesAlturas[newRow][newCol].first == especieGrove)) {
                    
                    visitados[newRow][newCol] = true;
                    
                    // actualizar la altura maxima del grove
                    if (matrizEspeciesAlturas[newRow][newCol].second > maxHeight) {
                        maxHeight = matrizEspeciesAlturas[newRow][newCol].second;
                    }
                    
                    Stack.push(make_pair(newRow, newCol));
                }
            }
        }
    }
    
    return make_pair(especieGrove, maxHeight);
}

int main() {
    int totalCases;
    cin >> totalCases;

    for (int casoActual = 1; casoActual <= totalCases; ++casoActual) {
        int filas, columnas;
        cin >> filas >> columnas;

        // inicializo estructuras de datos
        vector<vector<pair<string, int> > > matrizEspeciesAlturas(filas, vector<pair<string, int> >(columnas));
        vector<vector<bool> > visitados(filas, vector<bool>(columnas, false));

        // leer datos de entrada
        for (int i = 0; i < filas; ++i) {
            for (int j = 0; j < columnas; ++j) {
                string entrada;
                cin >> entrada;
    
                string especie = "";
                int altura = 0;
                int k = 0; // indice para recorrer la cadena
    
                // Extraccion de la especie
                while (k < entrada.size() && entrada[k] != '#') {
                    especie += entrada[k];
                    k++;
                }
    
                // Saltar el '#'
                k++;
    
                // Extraccion de la altura con ascii
                while (k < (entrada.size())) {
                    altura = altura * 10 + (entrada[k] - '0');
                    k++;
                }
    
                matrizEspeciesAlturas[i][j].first = especie;
                matrizEspeciesAlturas[i][j].second = altura;
            }
        }

        vector<pair<string, int> > resultados;

        // Procesar cada tree de la matriz
        for (int i = 0; i < filas; ++i) {
            for (int j = 0; j < columnas; ++j) {
                if (!visitados[i][j]) {
                    pair<string, int> resultadoGrove = explorarGrove(i, j, matrizEspeciesAlturas, visitados, filas, columnas);
                    resultados.push_back(resultadoGrove);
                }
            }
        }

        // Ordenar resultados segun las especificaciones
        sort(resultados.begin(), resultados.end());

        // Printear resultados
        cout << "Forest #" << casoActual << "\n";
        for (int indice = 0; indice < resultados.size(); ++indice) {
            cout << resultados[indice].first << " " << resultados[indice].second << "\n";
        }
    }

    return 0;
}
