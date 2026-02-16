#include <bits/stdc++.h>

using namespace std;

/*
Complejidad del algoritmo:

- Obtener los centros (peeling de hojas tipo topological trim):
    O(n)  — cada arista y nodo se procesa una sola vez.
- BFS desde cada centro:
    Si hay 1 o 2 centros (propiedad de los árboles), son 1–2 BFS.
    Cada BFS = O(n)
    Total BFS = O(n)

Complejidad total:
    O(n)

Es óptimo para árboles grandes.

--------------------------------------------------------------------

1.  Obtengo centros, dado que los centros son los best nodes
2.  Hago un bfs desde cada centros marcando la distancia desde cada
    centro a los demas nodos y obtengo la distancia maxima desde el 
    centro a una hoja
3.  Guardo como un WorstNode cada nodo cuya distancia a un centro
    sea la distancia maxima de ese centro
*/
/*
1.  Obtengo centros, dado que los centros son los best nodes
2.  Hago un bfs desde cada centros marcanco la distancia desde cada
    centros a los demas nodesy obtengo la distancia maxima desde el 
    centro a una hoja
3.  Guardo como un WorstNode, cada nodos que su distantcia a un centro
    sea la distancia maxima de ese centro


*/
unordered_set<int> centers(vector<vector<int>> &G){
    unordered_set<int> centers;
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

unordered_set<int> nodosMalos(vector<vector<int>> &G, unordered_set<int> &centers){

    int n = G.size() - 1;
    unordered_set<int> nodosMalos;
    unordered_set<int>::iterator it;
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
        unordered_set<int> centersSet;
        unordered_set<int> leafsSet;

        centersSet = centers(G);
        leafsSet = nodosMalos(G,centersSet);
        sort(centersSet.begin(),centersSet.end());
        sort(leafsSet.begin(),leafsSet.end());
        
        cout << "Best Roots : ";
        for (unordered_set<int>::iterator it = centersSet.begin(); it != centersSet.end(); ++it) {
            cout << " " << *it;
        }
        cout << endl;
        cout << "Worst Roots : ";
        for (unordered_set<int>::iterator it = leafsSet.begin(); it != leafsSet.end(); ++it) {
            cout << " " << *it;
            }

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