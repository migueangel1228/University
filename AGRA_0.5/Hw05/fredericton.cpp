/*
1 Generar grafo Full

1.1 Econtrar ISs, y garerar VecIss

2 Hacer BFS para SSSP, con cada VecIss[i] que pare Cada IS si cuando se ha ya visitado.

2.1 Voy actualizando una variable "best" que es el min(BFS(VecISS[i])

3 Imprimo best.
After being inspired by Salvador Dali’s artwork, Brett decided he would like to travel to Fredericton, New Brunswick to
visit the Beaverbrook Art Gallery.
Brett lives in Calgary, and would like to find the cheapest flight or flights that would take him to Fredericton. He knows that
a direct flight from Calgary to Fredericton, if one exists, would be absurdly expensive, so he is willing to tolerate a certain
number of stopovers. However, there are multiple airlines in Canada with so many different flights between different cities
now, which makes it very difficult for Brett to find the least expensive way to Fredericton! Can you write a program to help
Brett plan his route?
Map showing a sample of the flights that would take Brett to Fredericton.
You will be given a list of cities between and including Calgary and Fredericton. The cities will be given in order of
“nearest” to “farthest”. The first city will always be “Calgary” and the last “Fredericton”.
You will also be given a list of flights between pairs of cities, and the associated cost for each flight, taxes included. There
will never be a flight from a farther city to a nearer city — Brett has already discarded those flights, deeming them to be a
waste of time and money. Bear in mind, however, that there may be more than one flight between any two cities, as Brett is
considering flights from all airlines.
Finally, you are presented with a number of queries. Each query is a single integer indicating the maximum number of
stopovers Brett will tolerate. For each query, your program must calculate the least total cost of flights that would take Brett
from Calgary to Fredericton with no more than the requested number of stopovers.
Input
The first line of input contains a single number indicating the number of scenarios to process. A blank line precedes each
scenario.
Each scenario begins with a number N (2 ≤N ≤100), the number of cities, followed by N lines containing the names of
the cities. A city name is a string of up to 20 uppercase and lowercase letters. Next is a number M (0 ≤M ≤1000), the
number of flights available, followed by M lines describing the flights. Each flight is described by its departure city, its
destination city, and an integer representing its cost in dollars. The final line starts with Q (1 ≤Q ≤10), the number of
queries, followed by Q numbers indicating the maximum number of stopovers.
The input must be read from standard input.
Output
For each scenario, your program should output the scenario number, followed by the least total cost of the flights for each
query. Follow the format of the sample output. If no flights can satisfy a query, write ’No satisfactory flights’.
Output a blank line between scenarios.
The output must be written to standard output.

2

4
Calgary
Winnipeg
Ottawa
Fredericton
6
Calgary Winnipeg 125
Calgary Ottawa 300
Winnipeg Fredericton 325
Winnipeg Ottawa 100
Calgary Fredericton 875
Ottawa Fredericton 175
3 2 1 0

3
Calgary
Montreal
Fredericton
2
Calgary Montreal 300
Montreal Fredericton 325
1 0


Sample Output
Scenario #1
Total cost of flight(s) is $400
Total cost of flight(s) is $450
Total cost of flight(s) is $875
Scenario #2
No satisfactory flights
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
