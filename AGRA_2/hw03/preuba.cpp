#include <bits/stdc++.h>

using namespace std;

int gcd(int a, int b) {
    bool ans;
    if (b == 0) return a;
    return gcd(b, a % b);
}
bool isFriends(int a, int b) {
    return gcd(a, b) > 1;
}
bool compartorForLegs(const vector<int> &v, int a, int b) {
    if (v[a] != v[b]) return v[a] < v[b];
    return a < b;
}
vector<vector<int>> createGraph(const vector<int> &legs) {
    int n = legs.size();
    vector<vector<int>> graph(n);
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (isFriends(legs[i], legs[j])) {
                graph[i].push_back(j);
                graph[j].push_back(i);
            }
        }
    }
    for (int i = 0; i < n; ++i) { // buble sort manual para ordenar en cuanto al peso y no el id
        // ordenamos la lista de vecinos de cada nodo i manualmente
        int numNodes = graph[i].size();
        if (numNodes > 1) { // Solo ordenamos si hay mas de 2 nodes
            for (int k = 0; k < numNodes - 1; ++k) {
                for (int m = 0; m < numNodes - k - 1; ++m) {
                    int vecino_A = graph[i][m];
                    int vecino_B = graph[i][m + 1]; 

                    // compartorForLegs decide el orden
                    if (!compartorForLegs(legs, vecino_A, vecino_B)) {
                        // (swap) (inversion)
                        swap(graph[i][m], graph[i][m + 1]);
                    }
                }
            }
        }
    }
    return graph;
}
bool bfsAux(vector<vector<int>> &G, vector<bool> &vis, int u, int end, vector<int> &parent){
    bool ans = false;
    queue<int> q;
    vis[u] = true;
    q.push(u);

    while (!q.empty()){
        int v = q.front();
        q.pop();
        // cout << v << endl;
        for(int w = 0; w < G[v].size() && !ans;w++){
            int aux = G[v][w];
            if (!vis[aux]){
                q.push(aux);
                vis[aux] = true;
                parent[aux] = v; // guardo papa

                if (aux == end) ans = true; // se pudo concectar el start con el end
            }
        }
    }
    return ans;
}
bool bfs(vector<vector<int>> &G, int start, int end,vector<int> &parent){
    vector<bool> vis(G.size(),false);
    bool ans;

    ans = bfsAux(G,vis,start,end,parent);
    return ans;
}
int main(){
    int N;
    while (cin >> N){
        vector <int> LegsOfspiders(N);
        int auxNum;
        for(int i = 0; i < N; i++){
            cin >> auxNum;
            LegsOfspiders[i] = auxNum;
        }
        int start, end;
        cin >> start >> end;
        start--;
        end--;
        vector<vector<int>> G;
        G = createGraph(LegsOfspiders);
        vector<int> parent(G.size(), -1);
        bool respuesta = bfs(G, start, end, parent);

        if (start == end){
        cout << 1 << endl;
        cout << start + 1 << endl;
        }
        else if (!respuesta) {
            cout << -1 << endl;
        } else {
            vector<int> camino;
            for (int v = end; v != -1; v = parent[v]) camino.push_back(v + 1);

            reverse(camino.begin(), camino.end()); // ordenar de start a end

            cout << camino.size() << endl; // salida 1

            for (int i = 0; i < camino.size(); i++) {
                if(i) cout << " ";
                cout << camino[i]; // salida 2
            }
            cout << endl;
        }
    }
    return 0;
}
/*
Sample Input
7
2 14 9 6 8 15 11
5 6
7
2 14 9 6 8 15 11
5 7
7
2 14 9 6 8 15 11
5 5
22
97 193 331 269 89 157 1099 1746 1358 1076 1513 965 628 1261 314 1655 51 126 141 75 152 121
3 4
Sample Output
3
5 4 6
-1
1
5
6
3 16 20 18 10 4
*/