#include <bits/stdc++.h>
using namespace std;
int MAX = INT_MAX;

void tarjanAux(vector<vector<tuple<int,int>>> &G,vector<int> &vis,vector<int> &low,vector<bool> &enP,
    stack<int> &p,vector<vector<int>> &sccNodos,int &t,int &numSCC,int v,vector<int> &sccIdx){
    int w;
    vis[v] = low[v] = ++t;
    p.push(v);
    enP[v] = true;
    for(int i= 0; i < G[v].size(); ++i){
        w = G[v][i].first;
        if(vis[w] == -1){
            tarjanAux(G,vis,low,enP,p,sccNodos,t,numSCC,w,sccIdx);
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
            sccIdx[p.top()] = numSCC - 1;
            p.pop();
        }
        enP[p.top()] = false;
        sccNodos[numSCC - 1].push_back(p.top());
        sccIdx[p.top()] = numSCC - 1;
        p.pop();
    }
}
vector<int> tarjan(vector<vector<tuple<int,int>>> &G,vector<int> &vis,vector<int> &low,vector<bool> &enP,stack<int> &p,vector<vector<int>> &sccNodos){
    int n = G.size();
    int numSCC = 0, t = 0;
    vector<int> sccIdx(n);
    for(int i = 0; i < n; i++)
        if(vis[i] == -1)
            tarjanAux(G,vis,low,enP,p,sccNodos,t,numSCC,i,sccIdx);
    return sccIdx;
}
set<int> centers(vector<vector<int>> &G){
    set<int> centers;
    int n = G.size();
    vector<int> nivel(n, 0);
    vector<int> gradoTotal(n, 0);
    vector<int> gradoEntrada(n, 0);
    vector<vector<int>> grafoInverso(n); // Lista de adyacencia inversa
    queue<int> colita;
    int nivelMax = 0;
    for (int i = 0; i < n; i++){
        gradoTotal[i] = G[i].size(); // grado de salida
        for (int j = 0; j < G[i].size(); j++){
            int vecino = G[i][j];
            gradoEntrada[vecino]++;
            grafoInverso[vecino].push_back(i); // i apunta a vecino, entonces vecino <- i
        }
    }
    for (int i = 0; i < n; i++){
        gradoTotal[i] += gradoEntrada[i];
    }
    for (int i = 0; i < n; i++){
        if (gradoTotal[i] <= 1){
            colita.push(i);   
        }
    }
    bool hayHojas = !colita.empty();
    if (!hayHojas){
        for (int i = 0; i < n; i++){
            centers.insert(i);
        }
    }
    while (hayHojas && !colita.empty()){
        int v = colita.front();
        colita.pop();
        for (int i = 0; i < (int)G[v].size(); i++) {
            int w = G[v][i];
            gradoTotal[w]--;
            if (gradoTotal[w] == 1) {
                colita.push(w);
                nivel[w] = nivel[v] + 1;
                nivelMax = max(nivelMax, nivel[w]);
            }
        }
        for (int i = 0; i < (int)grafoInverso[v].size(); i++){
            int u = grafoInverso[v][i];
            gradoTotal[u]--;
            if (gradoTotal[u] == 1) {
                colita.push(u);
                nivel[u] = nivel[v] + 1;
                nivelMax = max(nivelMax, nivel[u]);
            }
        }
    }
    for (int i = 0; i < n; i++){
        if (nivel[i] == nivelMax){
            centers.insert(i);
        }
    }
    return centers;
}
vector<vector<int>> crearGrafoDeComponentes(vector<vector<tuple<int,int>>> &G, vector<vector<int>> &SCCNodos, vector<int> &sccIdx){
    int n = SCCNodos.size();
    vector<vector<int>> grafoSCC(n);
    vector<set<int>> vis(n);
    for (int v = 0; v < G.size(); v++){
        int componenteV = sccIdx[v];
        for (int u = 0; u < G[v].size(); u++){
            int w = G[v][u].first;
            int componenteU = sccIdx[w];
            if (componenteV != componenteU && vis[componenteV].find(componenteU) == vis[componenteV].end()){
                vis[componenteV].insert(componenteU);
                grafoSCC[componenteV].push_back(componenteU);
            }
        }
    }
    return grafoSCC;
}
void debugResultadoFinal(int capitalImperial, vector<int> &distancias, vector<int> &capitales){
    int sumaTotal = 0;
    for (int i = 0; i < capitales.size(); i++){
        int dist = distancias[capitales[i]];
        if (dist == INT_MAX){
            //cout << "INALCANZABLE" << endl;
        } else {
            //cout << dist << endl;
            sumaTotal += dist;
        }
    }
    cout << capitalImperial << " " << sumaTotal <<  endl;
}
vector<int> dijkstra(vector<vector<tuple<int,int>>> &G,int s){
    int n = G.size(); 
    vector<int> dist(n,MAX);
    dist[s] = 0;
    priority_queue<tuple<int,int>, vector<tuple<int,int>>, greater<tuple<int,int>>> pq;
    pq.push(make_pair(0, s));
    int u, du,v,duv;
    while (!pq.empty()){
        du = pq.top().first;
        u = pq.top().second;
        pq.pop();
        if(dist[u] == du){ // Ya procesamos este nodo con una distancia menor
            for (int i = 0; i < G[u].size(); i++){
                v = G[u][i].first;
                duv = G[u][i].second;
                
                if(du + duv < dist[v]){
                    dist[v] = du + duv;
                    pq.push(make_pair(dist[v], v));
                }
            }
        }
    }
    return dist;
}
int main(){
    int casitos;
    cin >> casitos;
    while (casitos--){
        int n, m;
        cin >> n >> m;
        vector<vector<tuple<int,int>>> G(n);
        for(int i = 0; i < m; i++){
            int u, v, w;
            cin >> u >> v >> w;
            G[u].push_back({v,w});
        }
        vector<int> vis(n,-1);
        vector<int> low(n,-1); // low
        vector<bool> enP(n,false);
        stack<int> p;
        vector<vector<int>> sccNodos;
        vector<int> sccIdx;
        sccIdx = tarjan(G,vis,low,enP,p,sccNodos);
        vector<int> capitales(sccNodos.size());
        for (int i = 0; i < sccNodos.size(); i++){
            int minSuma = MAX;
            int capital = sccNodos[i][0];
            for (int u = 0; u < sccNodos[i].size(); u++){
                int nodoActual = sccNodos[i][u];
                vector<int> dist = dijkstra(G, nodoActual);
                int suma = 0;
                bool alcanzable = true;
                for (int v = 0; v < sccNodos[i].size() && alcanzable; v++){
                    int nodoDestino = sccNodos[i][v];
                    if (dist[nodoDestino] == MAX){
                        alcanzable = false;
                    }
                    if (alcanzable){
                        suma += dist[nodoDestino];
                    }
                }
                if (alcanzable){
                    if (suma < minSuma || (suma == minSuma && nodoActual < capital)){
                        minSuma = suma;
                        capital = nodoActual;
                    }
                }
            }
            capitales[i] = capital;
        }
        vector<vector<int>> grafoSCC;
        grafoSCC = crearGrafoDeComponentes(G, sccNodos, sccIdx);
        vector<tuple<tuple<int,int>, int>> aristasInversas; // Guardar las aristas ( testeo) 
        for (int u = 0; u < n; u++) {
            int sccU = sccIdx[u];
            for (int i = 0; i < G[u].size(); i++) {
                int v = G[u][i].first;
                int peso = G[u][i].second;
                int sccV = sccIdx[v];
                if (sccU != sccV) {
                    aristasInversas.push_back({{v, u}, peso * 2});
                }
            }
        }
        set<int> centritos;
        centritos = centers(grafoSCC);
        set<int>::iterator itCentros;
        int minimoCentro = MAX;
        for(itCentros = centritos.begin(); itCentros != centritos.end();itCentros++){
            if(capitales[*itCentros] < minimoCentro) minimoCentro = capitales[*itCentros];
        }
        for (int idx = 0; idx < aristasInversas.size(); idx++) {
            int u = aristasInversas[idx].first.first;
            int v = aristasInversas[idx].first.second;
            int peso = aristasInversas[idx].second;
            G[u].push_back(make_pair(v, peso));
        }
        vector<int> distancias;
        distancias = dijkstra(G,minimoCentro);
        debugResultadoFinal(minimoCentro, distancias, capitales);
    }
    return 0;
}