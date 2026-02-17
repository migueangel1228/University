#include <bits/stdc++.h>

using namespace std;

/*
    AGRA  Tarea 6
Fecha  : 18/11/25
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem  root.cpp

"Big-O":

Pasos del algoritmo:

1. Calcular grados ady de todos los nodos: O(n)
2. Meter a la cola las hojas : O(n)
3. BFS eliminando hojas capa por capa:
   - Cada nodo se procesa exactamente una vez
   - Cada arista se examina exactamente una vez
   - Total: O(n + aristas) = O(n) para arboles (aristas = n-1)

Función nodosMalos (BFS desde centros):

Para cada centro encontrado (maximo 2 centros):
- BFS completo: O(n + aristas) = O(n)
- Identificar nodos a distancia maxima: O(n)
- Total: O(k × n) donde k ≤ 2, entonces O(n)

Complejidad global:
    Tiempo: O(n)
        - Obtener centros: O(n)
        - BFS desde centros (maximo 2): O(n)
        - Total: O(n) + O(n) = O(n)
  
    Espacio: O(n)
        - Listas de adyacencia: O(n)
        - Vectores auxiliares (nivel, grado, visitado): O(n)
        - Cola BFS: O(n) en el peor caso
*/


set<int> centers(vector<vector<int>> &G){
    set<int> centers;
    int n = G.size() - 1;
    vector<int> nivel(n + 1, 0);
    vector<int> grado(n + 1, 0);
    queue<int> colita;
    int nivelMax = 0;

    for (int i = 1; i <= n; i++){
        grado[i] = G[i].size();
    }
    // hojas
    for (int i = 1; i <= n; i++){
        if (grado[i] == 1){
            colita.push(i);
        }
    }
    // BFS
    while (!colita.empty()){
        int v = colita.front();
        colita.pop();

        for (int i = 0; i < G[v].size(); ++i) {
            int w = G[v][i];

            grado[w]--;
            if (grado[w] == 1){
                colita.push(w);
                nivel[w] = nivel[v] + 1;
                nivelMax = max(nivelMax, nivel[w]);
            }
        }
    }
    
    // nodos con nivel mayor = centros
    for (int i = 1; i <= n; i++){
        if (nivel[i] == nivelMax){
            centers.insert(i);
        }
    }
    return centers;
}

int bfsAux(vector<vector<int>> &G,vector<bool> &vis,vector<int> &nivel,int u){
    int maxLevel = 0, v;
    queue<int> q;
    q.push(u);
    nivel[u] = 0;
    vis[u] = true;

    while (!q.empty()){
        v = q.front();
        q.pop();
    
        for (int i = 0; i < G[v].size(); i++){
            int w = G[v][i];
            if (!vis[w]){
                vis[w] = true;
                nivel[w] = nivel[v] + 1;
                
                if (nivel[w] > maxLevel) maxLevel = nivel[w];
                q.push(w);
            }
        }    
    }
    return maxLevel;
}

set<int> nodosMalos(vector<vector<int>> &G, set<int> &centers){

    int n = G.size() - 1;
    set<int> nodosMalos;
    set<int>::iterator it;
    int max;

    for (it = centers.begin();it != centers.end();it++){
        vector<bool> visitado(n + 1,false);
        vector<int> nivel(n + 1,-1);

        max = bfsAux(G,visitado,nivel,*it);

        for (int i = 1; i <= n; i++){
            if(nivel[i] == max){
                nodosMalos.insert(i);
            }
        } 
    }
    return nodosMalos;
}

int main(){

    int n;
    while (cin >> n){
        vector<vector<int>> G(n + 1);

        for(int i = 1; i < n + 1; i++){
            int numNodes , nodeAdj;
            cin >> numNodes;
        
            for (int  j = 0; j < numNodes; j++){
                cin >> nodeAdj;
                G[i].push_back(nodeAdj);
            }
        }
        set<int> centersSet;
        set<int> leafsSet;

        centersSet = centers(G);
        leafsSet = nodosMalos(G,centersSet);
        
        cout << "Best Roots  :";
        for (set<int>::iterator it = centersSet.begin(); it != centersSet.end(); ++it) {
            cout << " " << *it;
        }
        cout << endl;
        cout << "Worst Roots :";
        for (set<int>::iterator it = leafsSet.begin(); it != leafsSet.end(); ++it) {
            cout << " " << *it;
        }
        cout << endl;

    }

    return 0;
}

/*
Sample Input
7
2 2 3
3 1 6 7
3 1 4 5
1 3
1 3
1 2
1 2
7
3 2 3 6
2 1 7
3 1 4 5
1 3
1 3
1 1
1 2
Sample Output
Best Roots : 1
Worst Roots : 4 5 6 7
Best Roots : 1
Worst Roots : 4 5 7
*/