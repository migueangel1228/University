/*
1 Generar grafo Full

1.1 Econtrar ISs, y garerar VecIss

2 Hacer BFS para SSSP, con cada VecIss[i] que pare Cada IS si cuando se ha ya visitado.

2.1 Voy actualizando una variable "best" que es el min(BFS(VecISS[i])

3 Imprimo best.

Sample Input
1
18
10 15
16 14 3
0 1 5
1 4 -2
10 7 1
1 2 2
14 17 -1
8 6 3
2 3 1
6 5 2
9 10 6
15 16 8
6 14 1
3 4 1
2 0 -3
17 15 4
4 0 -1
11 13 1
4 5 4
13 12 -2
5 6 6
11 6 4
7 8 3
14 15 5
12 11 5
8 9 2
-1 -1 -1
Sample Output
26
*/
#include <iostream>
#include <vector>
#include <limits>
#include <climits>
#include <string>
#include <map>
using namespace std;

int n; // número de ciudades
vector<vector<pair<int, int>>> G; // grafo: G[u] = vector de (v, costo)
vector<vector<int>> d; // matriz de distancias: d[i][j] es la menor distancia a j usando como máximo i vuelos

// Función Bellman-Ford que llena la matriz d
// s es el índice del nodo de origen (Calgary)
void bellmanFord(int s) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            d[i][j] = INT_MAX;
        }
    }
    d[0][s] = 0;

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n; j++) {
            d[i][j] = d[i - 1][j];
        }
        
        for (int u = 0; u < n; u++) {
            bool canRelax = (d[i - 1][u] != INT_MAX);
            for (int k = 0; k < G[u].size() && canRelax; k++) {
                int v = G[u][k].first;
                int costo = G[u][k].second;
                if (d[i - 1][u] + costo < d[i][v]) {
                    d[i][v] = d[i - 1][u] + costo;
                }
            }
        }
    }
}

int main() {
    int cases;
    cin >> cases;
    
    for (int actualCase = 1; actualCase <= cases; actualCase++) {
        cin >> n;
        vector<string> ciudades(n);
        map<string, int> mapCiudades;

        for (int i = 0; i < n; i++) {
            cin >> ciudades[i];
            mapCiudades[ciudades[i]] = i;
        }
        
        int m;
        cin >> m;
        G = vector<vector<pair<int, int>>>(n);
        for (int i = 0; i < m; i++) {
            string origen, destino;
            int costo;
            cin >> origen >> destino >> costo;
            int u = mapCiudades[origen];
            int v = mapCiudades[destino];
            G[u].push_back(make_pair(v, costo));
        }
        
        d = vector<vector<int>>(n, vector<int>(n, INT_MAX));
        bellmanFord(0);
        
        int q;
        cin >> q;
        cout << "Scenario #" << actualCase << "\n";
        
        for (int i = 0; i < q; i++) {
            int stopovers;
            cin >> stopovers;
            int vuelosPermitidos = stopovers + 1;
            if (vuelosPermitidos >= n) {
                vuelosPermitidos = n - 1;
            }
            
            bool hasValidFlight = (d[vuelosPermitidos][n - 1] != INT_MAX);
            if (hasValidFlight) {
                cout << "Total cost of flight(s) is $" << d[vuelosPermitidos][n - 1] << "\n";
            } else {
                cout << "No satisfactory flights" << "\n";
            }
        }
        
        if (actualCase < cases) {
            cout << "\n";
        }
    }
    return 0;
}
