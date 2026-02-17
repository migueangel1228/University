#include <bits/stdc++.h>
#include <iostream>
#include <vector>

#define sz(x) (int) x.size()

using namespace std;

int MAX = INT_MAX;

vector<vector<int>> warshall(vector<vector<int>> &M) {
    int n = M.size();
    vector<vector<int>> d = M;

    // Inicializamos la diagonal a 0
    for (int i = 0; i < n; ++i) {
        d[i][i] = 0;
    }

    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (d[i][k] != MAX && d[k][j] != MAX) {

                    if (d[i][k] > MAX - d[k][j]) {
                    }
                    else {
                        int nueva_distancia = d[i][k] + d[k][j];
                        d[i][j] = min(d[i][j], nueva_distancia);
                    }
                }
            }
        }
    }
    return d;
}

void tarjanAux(vector<vector<tuple<int,int>>> &G,vector<int> &vis,vector<int> &low,vector<bool> &enP,
    stack<int> &p,vector<vector<int>> &sccNodos,int &t,int &numSCC,int v){

    int w;
    vis[v] = low[v] = ++t;
    p.push(v);
    enP[v] = true;
    for(int i= 0; i < G[v].size(); ++i){
        w = G[v][i].first;
        if(vis[w] == -1){
            tarjanAux(G,vis,low,enP,p,sccNodos,t,numSCC,w);
            low[v] = min(low[v], low[w]);
        }
        else if(enP[w])  low[v] = min(low[v], vis[w]);
    }

    if(low[v] == vis[v]){
        sccNodos.push_back(vector<int>());
        numSCC++;
        while(p.top() != v){
            enP[p.top()] = false;
            sccNodos[numSCC - 1].push_back(p.top());
            p.pop();
        }

        enP[p.top()] = false;
        sccNodos[numSCC - 1].push_back(p.top());
        p.pop();
    }
}

void tarjan(vector<vector<tuple<int,int>>> &G,vector<int> &vis,vector<int> &low,vector<bool> &enP,stack<int> &p,vector<vector<int>> &sccNodos){
    int n = G.size();
    int numSCC = 0, t = 0;

    for(int i = 0; i < n; i++)
        if(vis[i] == -1)
            tarjanAux(G,vis,low,enP,p,sccNodos,t,numSCC,i);
}

int main(){

    int n, m;
    bool primeraVez = true;
    while (cin >> n >> m, n != 0 && m != 0){
        n++;
        vector<vector<tuple<int,int>>> G(n);
        vector<int> vis(n,-1);
        vector<int> low(n,-1); // low
        vector<bool> enP(n,false);
        stack<int> p;
        vector<vector<int>> sccNodos;

        for(int i = 0; i < m ; ++i){
            int u, v, w;
            cin >> u >> v >> w;
            G[u].push_back(make_pair(v,w));
        }
        int k;
        cin >> k;

        tarjan(G,vis,low,enP,p,sccNodos);

        // encontrar ciudad de kenny
        vector<int> ciudadKenny;
        bool encontrado = false;
        for (int i = 0; i < sccNodos.size() && !encontrado; i++){
            ciudadKenny.clear();
            for(int j = 0; j < sccNodos[i].size(); j++){

                ciudadKenny.push_back(sccNodos[i][j]);
                if (sccNodos[i][j] == k){
                    encontrado = true;
                }
            }
        }
        // asegurar Orden
        sort(ciudadKenny.begin(), ciudadKenny.end());

        // mapeo todos los nodos originales
        unordered_map<int,int> setComponente;
        for (int i = 0; i < ciudadKenny.size(); ++i){
            setComponente[ciudadKenny[i]] = i;
        }

        // convertir lista de ady a matriz de adyacencia
        int tamanoComp = ciudadKenny.size();
        vector<vector<int>> MatrizAdj(tamanoComp,vector<int>(tamanoComp,INT_MAX));
        
        // costo a ir a uno mismo
        for (int i = 0; i < tamanoComp; ++i){
            MatrizAdj[i][i] = 0;
        } 

        for (int i = 0; i < tamanoComp; i++){
            int aux = ciudadKenny[i];
            for (int j = 0; j < (int)G[aux].size(); j++){
                if (setComponente.find(G[aux][j].first) != setComponente.end()){
                    int node = setComponente[G[aux][j].first]; // índice reducido
                    int w  = G[aux][j].second;
                    if (w < MatrizAdj[i][node]) MatrizAdj[i][node] = w; // si hay paralelas, tomamos la mínima
                }
            }
        }
        
        vector<vector<int>> d;
        d = warshall(MatrizAdj);
        
        // imprimir en orden lexicográfico por nodos originales (u luego v)
        
        if(!primeraVez){
            cout << endl;
        }
        else {
            primeraVez = false;
        }
        
        for (int i = 0; i < ciudadKenny.size(); ++i){
            for (int j = 0; j < ciudadKenny.size(); ++j){
                int u = ciudadKenny[i];
                int v = ciudadKenny[j];
                int cost = d[i][j];
                if (cost != INT_MAX && v != u)
                    cout << u << " " << v << " " << cost << endl;
            }
        }

        



    }

    return 0;
}

/*
Sample Input
12 14
1 3 2
3 2 1
2 6 5
6 7 1
7 1 3
10 4 2
4 9 1
9 10 4
5 12 6
12 8 2
8 11 1
11 5 3
3 10 8
4 8 7
3
0 0
Sample Output
1 2 3
1 3 2
1 6 8
1 7 9
2 1 9
2 3 11
2 6 5
2 7 6
3 1 10
3 2 1
3 6 6
3 7 7
6 1 4
6 2 7
6 3 6
6 7 1
7 1 3
7 2 6
7 3 5
7 6 11
*/