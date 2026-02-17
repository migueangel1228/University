#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <limits>
#include <list>
#include <queue>
#include <set>

using namespace std;

const int INF = numeric_limits<int>::max();

void imprimirGrafoConPesos(const vector<vector<tuple<int, int>>>& grafo) {
    for (int u = 0; u < grafo.size(); ++u) {
        for (int j = 0; j < grafo[u].size(); j++) {
            cout << u << " --(" << grafo[u][j].second << ")--> " << grafo[u][j].first << endl;
        }
    }
}

void imprimirGrafo(const vector<vector<int>>& grafo) {
    for (int u = 0; u < grafo.size(); ++u) {
        cout << u <<":";
        for (int j = 0; j < grafo[u].size(); j++) {
            cout << " " << grafo[u][j];
        }
        cout<<endl;
    }
}

void kosarajuAux(int v, list<int> &ord, bool* visitados, vector<vector<tuple<int, int>>> &G){
    visitados[v] = true;
    for(int i = 0; i < G[v].size(); i++)
      if(!visitados[G[v][i].first])
        kosarajuAux(G[v][i].first, ord, visitados, G);
  
    ord.push_front(v);
}

void asignar(int u, int num, vector<int> &sccInd, vector<vector<tuple<int,int>>> &GT, vector<vector<int>> &sccNodos, vector<vector<int>> &G2, vector<vector<tuple<int, int>>> &G, set<tuple<int, int>> &mi_set){
    int aux;
    sccInd[u] = num;
    sccNodos[num].push_back(u);
    for(int i = 0; i < GT[u].size(); i++){ 
        if(sccInd[GT[u][i].first] == -1)
            asignar(GT[u][i].first, num, sccInd, GT, sccNodos, G2, G, mi_set);
        else{
            if(sccInd[GT[u][i].first] != num){
                if(mi_set.find({sccInd[GT[u][i].first], num}) == mi_set.end()){
                    mi_set.insert({sccInd[GT[u][i].first], num});
                    mi_set.insert({num, sccInd[GT[u][i].first]});
                    G2[sccInd[GT[u][i].first]].push_back(num);
                    G2[num].push_back(sccInd[GT[u][i].first]);
                }
                aux = GT[u][i].second * 2;
                //cout<<GT[u][i].first <<"->"<< u << ": " <<aux<<" " <<endl;
                G[u].push_back({GT[u][i].first, aux});
            }
        }
    }
}

void kosaraju(vector<vector<tuple<int, int>>>&G, vector<vector<tuple<int,int>>> &GT, vector<int> &sccInd, vector<vector<int>> &sccNodos, vector<vector<int>> &G2){
    int i, num = 0, n = G.size();
    bool visitados[n];
    list<int> ord;

    for(i = 0; i < n; i++){ 
        visitados[i] = false;
        sccInd[i] = -1;
    }

    for(i = 0; i < n; i++)
        if(!visitados[i])
            kosarajuAux(i, ord, visitados, G);
    set<tuple<int, int>> mi_set;
    for(list<int>::iterator it = ord.begin(); it != ord.end(); it++){
        if(sccInd[*it] == -1){
            sccNodos.push_back({});
            G2.push_back({});
            asignar(*it, num++, sccInd, GT, sccNodos, G2, G, mi_set); 
        }
    }
}

int floyd(vector<vector<int>> &sccNodos, vector<vector<tuple<int, int>>> &G, vector<int> &sccInd, int num, vector<int> &id){
    int min = INF, n = sccNodos[num].size(), capital = -1, aux;
    vector<vector<int>> w(n, vector<int>(n,INF)), d, nex(n, vector<int>(n, -1));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < G[sccNodos[num][i]].size(); j++){
            if(sccInd[G[sccNodos[num][i]][j].first] == num)
               w[id[sccNodos[num][i]]][id[G[sccNodos[num][i]][j].first]] = G[sccNodos[num][i]][j].second;
        }
    }

    d = w;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (w[i][j] != INF) {
                nex[i][j] = j;
            }
        }
        d[i][i] = 0;
        nex[i][i] = i;
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (d[i][k] != INF && d[k][j] != INF && d[i][k] + d[k][j] < d[i][j]) {
                    d[i][j] = d[i][k] + d[k][j];
                    nex[i][j] = nex[i][k];
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        aux = 0;
        for (int j = 0; j < n; j++) {
            if (d[id[sccNodos[num][i]]][j] != INF)
                aux += d[id[sccNodos[num][i]]][j];
                //cout<<sccNodos[num][i]<<"-> "<< aux<<endl;
        }
        if(aux < min || (aux == min && capital > sccNodos[num][i])){
            min = aux;
            capital = sccNodos[num][i];
            //cout<<"min: "<< min <<" nodo "<< capital<<endl;
        }
    }
    
    return capital;
}

int centro(vector<vector<int>> &G2, vector<int> &capitals){
    int nivelMax = 0, node, hoja, capital = 5000;
    vector<int> nivel(G2.size(), 0);
    vector<int> grado(G2.size(), 0);
    queue<int> q;
    for (int i = 0; i < G2.size(); i++) { 
        grado[i] = G2[i].size();
        //cout <<"grado "<<i<<" "<<grado[i]<< endl;
        if (grado[i] == 1) {
            q.push(i);
        }
    }
    while (!q.empty()) {
        node = q.front();
        q.pop();
       // cout<<"node "<<node<<endl;
        for (int i = 0; i <G2[node].size(); i++) {
            hoja = G2[node][i];
            //cout<<"hoja "<<hoja<<" "<< grado[hoja];
            grado[hoja]--;
            //cout<<" "<<grado[hoja]<<endl;
            if(grado[hoja] == 1) {
                q.push(hoja);
                nivel[hoja] = nivel[node] + 1;
                //cout<<hoja<<" nivel "<< nivel[hoja] << "- " << node << " nivel" << nivel[node]<<endl;
                nivelMax = max(nivelMax, nivel[hoja]);
            }
        }
    }
    //cout << "Nivel max "<<nivelMax<<endl;
    for(int i = 0; i < G2.size(); i++){
       //cout << i << " " << capitals[i]<<" "<<nivel[i]<<endl;
        if (nivel[i] == nivelMax && capital > capitals[i] ) {
            capital	= capitals[i];
        }
    }
    return capital;
}


vector<int> dijkstra(vector<vector<tuple<int, int>>>&G, int s) {
    int u, du, duv, v, n = G.size();
    vector<int> dist(n, INF);
    priority_queue<tuple<int, int>, vector<tuple<int, int>>, greater<tuple<int, int>>> pqueue;
    tuple<int,int> aux;
    dist[s] = 0;
    pqueue.push({dist[s], s});

    while (!pqueue.empty()) {
        aux  = pqueue.top();
        pqueue.pop();
        u = aux.second;
        du = aux.first;

        if (dist[u] == du) {
            for (int i = 0; i < G[u].size(); i++) {
                v = G[u][i].first;
                duv = G[u][i].second;
                if (du + duv < dist[v]) {
                    dist[v] = du + duv;
                    pqueue.emplace(dist[v], v);
                }
            }
        }
    }
    return dist;
}

int main() {
    int cases, n, m, aux1, aux2, pAux, ans, stateCenter;
    cin >> cases;

    while(cases--){
        cin >> n >> m;
        vector<vector<tuple<int, int>>> G(n), GT(n);
        for(int i = 0; i < m; i++){
            cin >> aux1 >> aux2 >> pAux;
            G[aux1].push_back({aux2, pAux});
            GT[aux2].push_back({aux1, pAux});
        }
        vector<int> sccInd(n), d;
        vector<vector<int>> sccNodos, G2;
        //imprimirGrafoConPesos(G);

        kosaraju(G, GT, sccInd, sccNodos, G2);

        /*for(int i = 0; i < sccNodos.size(); i++){
            cout<<"\nComponente "<<i<<": ";
            for(int j = 0; j < sccNodos[i].size(); j++){
                cout<< sccNodos[i][j] <<" "; 
            }
        }
        imprimirGrafoConPesos(G);*/

        vector<int> capitals(sccNodos.size(), -1), id(n);
        for(int i = 0; i < sccNodos.size(); i++){
            for(int j = 0; j < sccNodos[i].size(); j++)
                id[sccNodos[i][j]] = j;
        }
        for(int i = 0; i < sccNodos.size(); i++){
            capitals[i] = floyd(sccNodos, G, sccInd, i, id);
        }

        /*for(int i = 0; i < sccNodos.size(); i++){
            cout<< "componente "<< i <<" "<<capitals[i];
        }
        imprimirGrafo(G2);*/
        stateCenter = centro(G2, capitals);
        //cout << " empireCpital "<<stateCenter<<endl;
        d = dijkstra(G, stateCenter);
        
        ans = 0;
        for(int i = 0; i < capitals.size(); i++){
           //cout<<"node "<<i << "capital "<<capitals[i]<< " distancia "<< d[capitals[i]]<<endl;
            ans += d[capitals[i]];
        }
        cout <<stateCenter <<" "<< ans << endl;
    }
    return 0;
}