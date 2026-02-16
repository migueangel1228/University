#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

// Clase para resolver el problema usando el algoritmo de Tarjan
class TarjanSCC {
private:
    int n;                          // Número de nodos
    vector<vector<int>> graph;      // Grafo dirigido almacenado como lista de adyacencia
    vector<int> visitados;               // Tiempo de descubrimiento de cada nodo
    vector<int> sccIndx;                // Valor sccIndx de cada nodo
    vector<bool> enPila;           // Si el nodo está actualmente en la pila
    stack<int> stact;                  // Pila utilizada por el algoritmo de Tarjan
    int time;                       // Contador de tiempo
    int sccCount;                   // Contador de componentes fuertemente conexas

public:
    // Constructor
    TarjanSCC(int nodes) {
        n = nodes;
        graph.resize(n + 1);        // Los nodos están numerados de 1 a n
        visitados.resize(n + 1, -1);
        sccIndx.resize(n + 1, -1);
        enPila.resize(n + 1, false);
        time = 0;
        sccCount = 0; // 1?
    }

    // Agregar arista dirigida de u a v
    void addEdge(int u, int v) {
        graph[u].push_back(v);
    }

    // DFS para el algoritmo de Tarjan
    void tarjanAux(int u) {
        // Inicializar visitados y sccIndx para el nodo actual
        visitados[u] = sccIndx[u] = ++time;
        stact.push(u);
        enPila[u] = true;

        // Visitar todos los vecinos
        for (int i = 0; i < graph[u].size(); i++) {
            int v = graph[u][i];
            // Si v no ha sido visitado
            if (visitados[v] == -1) {
                tarjanAux(v);
                // Actualizar sccIndx[u]
                sccIndx[u] = min(sccIndx[u], sccIndx[v]);
            }
            // Si v está en la pila, entonces es parte de la SCC actual
            else if (enPila[v]) {
                sccIndx[u] = min(sccIndx[u], visitados[v]);
            }
        }

        // Si u es la raíz de una SCC
        if (sccIndx[u] == visitados[u]) {
            sccCount++;
            int v;
            do {
                v = stact.top();
                stact.pop();
                enPila[v] = false;
            } while (v != u);
        }
    }

    // Encontrar todas las SCCs en el grafo
    int findSCCs() {
        // Inicializar visitados, sccIndx, enPila para todos los nodos
        for (int i = 1; i <= n; i++) {
            visitados[i] = -1;
            sccIndx[i] = -1;
            enPila[i] = false;
        }
        time = 0;
        sccCount = 0;

        // Llamar a DFS para cada nodo no visitado
        for (int i = 1; i <= n; i++) {
            if (visitados[i] == -1) {
                tarjanAux(i);
            }
        }

        return sccCount;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, m;
    
    // Leer múltiples casos de prueba
    while (cin >> n >> m) {
        TarjanSCC graph(n);
        
        // Leer procedimientos
        for (int i = 0; i < m; i++) {
            int k;
            cin >> k;
            
            if (k == 1) {
                // Procedimiento simple: dirección única
                int u, v;
                cin >> u >> v;
                graph.addEdge(u, v);
            } else {
                // Procedimiento complejo: conexión bidireccional entre todos los grupos
                vector<int> groups(k);
                for (int j = 0; j < k; j++) {
                    cin >> groups[j];
                }
                
                // Crear aristas bidireccionales entre todos los pares de grupos
                for (int j = 0; j < k; j++) {
                    for (int l = 0; l < k; l++) {
                        if (j != l) {
                            graph.addEdge(groups[j], groups[l]);
                        }
                    }
                }
            }
        }
        
        // Verificar si todos los nodos están en una única componente fuertemente conexa
        int sccCount = graph.findSCCs();
        
        // Si hay exactamente una SCC, los procedimientos son suficientemente completos
        if (sccCount == 1) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    
    return 0;
}