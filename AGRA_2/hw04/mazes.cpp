#include <bits/stdc++.h>

using namespace std;


/*
Algoritmo de Tarjan (Bridges)
Autor: Carlos Ramirez
Fecha: Abril 4 de 2020

*/
bool bfsAux(vector<vector<int>> &matriz,set<tuple<int, int>> &bridges,vector<bool> &visBfs,int start, int end){
    bool auxAns = false;
    visBfs[start] = true;
    queue<int>  q;
    q.push(start);
    int v,u;
    while (!q.empty() && !auxAns){
        v = q.front();
        q.pop();
        visBfs[v] = true;
        for(int i = 0; i < matriz[v].size() && !auxAns; i++){
            u = matriz[v][i];
            if (!visBfs[u]){
                if (bridges.find(make_pair(v, u)) != bridges.end() || bridges.find(make_pair(u, v)) != bridges.end()){
                    q.push(u);
                    if(u == end){
                        auxAns = true;
                    }
                }
            }
        }
    }
    return auxAns;
}

bool bfs(vector<vector<int>> &matriz,set<tuple<int, int>> &bridges,int start, int end){
    bool ans = false;
    int n = matriz.size();
    vector<bool> visBfs(n,false);

    ans = bfsAux(matriz,bridges,visBfs,start,end);

    return ans;
}


void bridgesAux(vector<vector<int>> &matriz,vector<int> &visitado,vector<int> &low,vector<int> 
        &padre,set<tuple<int, int>> &bridges, int v,int &t){
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

void bridgesTarjan(vector<vector<int>> &matriz,vector<int> &visitado,vector<int> &low,vector<int> 
    &padre,set<tuple<int, int>> &bridges){

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
    int n, m, q;

    while (cin >> n >> m >> q, n != 0){
        vector<vector<int>> matriz(n);
        vector<int> visitado(n,-1);
        vector<int> low(n,-1);
        vector<int> padre(n,-1);

        set<tuple<int, int>> bridges;

        int i, aux1, aux2;
        for(i = 0; i < m; i++){
            cin >> aux1 >> aux2;
            matriz[aux1 - 1].push_back(aux2 - 1);
            matriz[aux2 - 1].push_back(aux1 - 1);
        }

        bridgesTarjan(matriz,visitado,low,padre,bridges);
        int start, end;
        for (int i = 0; i < q; i++){
            cin >> start >> end;
            bool respuesta = bfs(matriz,bridges,start - 1,end - 1);
            //output
            if(respuesta)
                cout << "Y" << endl;
            else
                cout << "N" << endl;
        }
        cout << "-" << endl;
    }
    return 0;
}

/*
Sample Input
6 5 3
1 2
2 3
2 4
2 5
4 5
1 3
1 5
2 6
4 2 3
1 2
2 3
1 4
1 3
1 2
0 0 0

Sample Output
Y
N
N
-
N
Y
Y

*/