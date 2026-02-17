#include <vector>
#include <list>
#include <iostream>

using namespace std;

void kosarajuAux(int v, const vector<vector<int>>& adj, vector<bool>& visitados, list<int>& ord) {
    visitados[v] = true;
    for (int vecino : adj[v]) {
        if (!visitados[vecino]) {
            kosarajuAux(vecino, adj, visitados, ord);
        }
    }
    ord.push_front(v);
}

void asignar(int u, int num, const vector<vector<int>>& adjT, vector<int>& sccInd) {
    sccInd[u] = num;
    for (int vecino : adjT[u]) {
        if (sccInd[vecino] == -1) {
            asignar(vecino, num, adjT, sccInd);
        }
    }
}

vector<int> kosaraju(const vector<vector<int>>& adj, const vector<vector<int>>& adjT, int n) {
    vector<bool> visitados(n, false);
    list<int> ord;
    vector<int> sccInd(n, -1);
    int num = 0;

    // Primer recorrido para obtener el orden
    for (int i = 0; i < n; ++i) {
        if (!visitados[i]) {
            kosarajuAux(i, adj, visitados, ord);
        }
    }

    // Asignación de componentes
    for (int u : ord) {
        if (sccInd[u] == -1) {
            asignar(u, num, adjT, sccInd);
            num++;
        }
    }

    return sccInd;
}

int main() {
    int cases, caso, aristas, nodes , n, m, u, v;


    cin >> cases;
    caso = 1;
    while (caso < cases + 1) {

        cin >> nodes >> aristas;
        cin >> n >> m;

        vector<vector<int>> adj(nodes);
        vector<vector<int>> adjT(nodes);

        for (int i = 0; i < aristas; ++i) {
            cin >> u >> v;
            adj[u].push_back(v);
            adjT[v].push_back(u);
        }

        vector<int> componentes = kosaraju(adj, adjT, nodes);

        for (int i = 0; i < nodes; ++i) {
            cout << componentes[i] << " ";
        }
        cout << endl;
    caso++;

    return 0;
}
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