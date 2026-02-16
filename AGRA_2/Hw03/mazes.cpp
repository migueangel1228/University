#include <bits/stdc++.h>

using namespace std;


/*
Algoritmo de Tarjan (Bridges)
Autor: Carlos Ramirez
Fecha: Abril 4 de 2020

*/
bool bfsAux(vector<vector<int>> &matriz,set<pair<int, int>> &bridges,vector<bool> &visBfs,int aux,int start, int end){
    bool auxAns = false;
    visBfs[aux] = true;
    queue<int>  q;
    q.push(aux);
    int v,u;
    while (!q.empty() && !auxAns){
        v = q.front();
        q.pop();
        for(int i = 0;i < matriz[v].size() && !auxAns;i++){
            u = matriz[v][i];
            if (!visBfs[u]){
                if(u == end){
                    auxAns = true;
                }
                else if (bridges.find(make_pair(v, u)) != bridges.end() || bridges.find(make_pair(u, v)) != bridges.end()){
                    q.push(u);
                }
            }
        }
    }
    return auxAns;

}
bool bfs(vector<vector<int>> &matriz,set<pair<int, int>> &bridges,int start, int end){
    bool ans = false;
    int n = matriz.size();
    vector<bool> visBfs(n,false);
    int aux;

    for(int u = 0; start < matriz[start].size(); u++){
        aux = matriz[start][u];
        if(!visBfs[aux]){
            ans = bfsAux(matriz,bridges,visBfs,aux,start,end);
        }
    }

    return ans;
}


void bridgesAux(vector<vector<int>> &matriz,vector<int> &visitado,vector<int> &low,vector<int> &padre,set<pair<int, int>> &bridges, int v,int &t){
    int w;
    visitado[v] = low[v] = ++t;

    for(int i = 0; i < matriz[v].size(); i++){
        w = matriz[v][i];
        if(visitado[w] == -1){
            padre[w] = v;
            bridgesAux(matriz, visitado,low,padre,bridges,w,t);
            low[v] = min(low[v], low[w]);

            //verificar si es un puente
            if(low[w] > visitado[v]){
                bridges.insert(make_pair(v, w));
                bridges.insert(make_pair(w, v));
            }
        }

        else if(w != padre[v])
            low[v] = min(low[v], visitado[w]);
    }
}

void bridgesTarjan(vector<vector<int>> &matriz,vector<int> &visitado,vector<int> &low,vector<int> &padre,set<pair<int, int>> &bridges){
    int i;
    int t = 0;
    int n = matriz.size();
    for(i = 0; i < n; i++){
        if(visitado[i] == -1)
            bridgesAux(matriz, visitado,low,padre,bridges,i,t);
    }
}

int main(){
    int numSCC, t;
    int n, m;

    cin >> n >> m; // DATA

    vector<vector<int>> matriz(n);
    vector<int> visitado(n,-1);
    vector<int> low(n,-1);
    vector<int> padre(n,-1);

    set<pair<int, int>> bridges;

    int i, aux1, aux2;
    for(i = 0; i < m; i++){
        cin >> aux1 >> aux2;
        matriz[aux1 - 1].push_back(aux2 - 1);
        matriz[aux2 - 1].push_back(aux1 - 1);
    }

    bridgesTarjan(matriz,visitado,low,padre,bridges);
    //cout puentes
        if(bridges.size() == 0)
            cout << "El grafo no tiene puentes" << endl;
        else{
            cout << "Total de Puentes: " << bridges.size() << endl;
            for(set<pair<int, int> >::iterator it = bridges.begin(); it !=  bridges.end(); ++it)
            cout << " (" << it->first << ", " << it->second << ")";
            cout << endl;
        }
    int start, end;
    cin >> start >> end;
    bool respuesta = bfs(matriz,bridges,start,end);
    //output
    if(respuesta)
        cout << "Y" << endl;
    else
        cout << "N" << endl;

    return 0;
}

/*
Sample Imput:
12 28
1 12
12 1
1 2
2 1
1 3
3 1
2 6
6 2
2 5
5 2
3 4
4 3
3 5
5 3
4 6
6 4
4 7
7 4
7 9
9 7
7 8
8 7
7 10
10 7
8 10
10 8
8 11
11 8

6 5
1 2
2 3
2 4
2 5
4 5
Sample Output:
Total de Puentes: 3
(4, 7) (7, 9) (8, 11)
Total de Puentes: 2
 (0, 1) (1, 2)

*/