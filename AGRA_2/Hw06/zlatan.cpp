#include <bits/stdc++.h>

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

void tarjanAux(vector<vector<pair<int,int>>> &G,vector<int> &vis,vector<int> &low,vector<bool> &enP,
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

vector<int> tarjan(vector<vector<pair<int,int>>> &G,vector<int> &vis,vector<int> &low,vector<bool> &enP,stack<int> &p,vector<vector<int>> &sccNodos){
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
    vector<int> grado(n, 0);
    queue<int> colita;
    int nivelMax = 0;

    for (int i = 0; i < n; i++){
        grado[i] = G[i].size();
    }
    // hojas
    for (int i = 0; i < n; i++){
        if (grado[i] == 1){
            colita.push(i);   
        }
    }
    // BFS
    while (!colita.empty()){
        int v = colita.front();
        colita.pop();

        for (int i = 0; i < (int)G[v].size(); i++) {
            int w = G[v][i];

            grado[w]--;
            if (grado[w] == 1) {
                colita.push(w);
                nivel[w] = nivel[v] + 1;
                nivelMax = max(nivelMax, nivel[w]);
            }
        }
    }
    // nodos con nivel mayor = centros
    for (int i = 0; i < n; i++){
        if (nivel[i] == nivelMax){
            centers.insert(i);
        }
    }

    return centers;
}

vector<vector<int>> crearGrafoDeComponentes(vector<vector<pair<int,int>>> &G, vector<vector<int>> &SCCNodos, vector<int> &sccIdx){
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
/*
def dijkstra(G, s):
  dist = [INF for _ in range(len(G))] ; dist[s] = 0
  pred = [-1 for _ in range(len(G))]
  pqueue = list()
  #for u in range(len(G)): heappush(pqueue, (dist[u], u))
  heappush(pqueue, (dist[s], s))
  
  while len(pqueue)!=0:
    du,u = heappop(pqueue)
    if dist[u] == du:
      for v,duv in G[u]:
        if du+duv<dist[v]:
          dist[v] = du+duv
          pred[v] = u
          heappush(pqueue, (dist[v], v))
  return dist
*/

vector<int> dijkstra(vector<vector<pair<int,int>>> &G,int s){
    int n = G.size(); 
    vector<int> dist(n,MAX);
    dist[s] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
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
        
        // Inicializacion grafo
        vector<vector<pair<int,int>>> G(n);

        for(int i = 0; i < m; i++){
            int u, v, w;
            cin >> u >> v >> w;
            G[u].push_back({v,w});
        }
        // Crear states (scc components)
        vector<int> vis(n,-1);
        vector<int> low(n,-1); // low
        vector<bool> enP(n,false);
        stack<int> p;
        vector<vector<int>> sccNodos;
        vector<int> sccIdx;
        
        sccIdx = tarjan(G,vis,low,enP,p,sccNodos);
        // Generar caminos minimos de todos a todos (warshall)
        
            // Convertir grafo a matriz de adj
        vector<vector<int>> M(n,vector<int>(n,INT_MAX));
        
            // Costo a ir a uno mismo
        for (int i = 0; i < n; ++i){
            M[i][i] = 0;
        } 
            // copia de listAdj -> matrizAdj
        for (int i = 0; i < G.size(); i++){
            for (int j = 0; j < G[i].size(); j++){
                M[i][G[i][j].first] = G[i][j].second;
            }
        }

        vector<vector<int>> matrizWarshall;

        matrizWarshall = warshall(M);
        // Test matrizWarshall
        cout << "matrizWarshall "  << endl;
        for (int i = 0; i < matrizWarshall.size(); ++i){
            for (int j = 0; j < matrizWarshall[i].size(); ++j){

                int cost = matrizWarshall[i][j];
                if (cost != INT_MAX && i != j)
                    cout << i << " " << j << " " << cost << endl;
            }
        }
        // Obtener ciudad capital de cada state(fila minima de la matriz de todos a todos (warshall))
        vector<int> capitales(sccNodos.size());
        for (int i = 0; i < sccNodos.size(); i++){
            int min = MAX;
            int capital;

            for (int u = 0; u < sccNodos[i].size(); u++){ 
                int cnt = 0; 
                for (int v = 0; v < sccNodos[i].size(); v++){ 
                    cnt += matrizWarshall[sccNodos[i][u]][sccNodos[i][v]];
                }
                if (cnt < min) {
                    min = cnt;
                    capital = sccNodos[i][u];
                }
                else if(cnt == min){
                    if(capital > sccNodos[i][u]){
                        capital = sccNodos[i][u];
                    }
                }

            }
            capitales[i] = capital;
        }
        // TEST Capitales Estados
        cout << "TEST Capitales Estados "  << endl;
        for (int i = 0; i < capitales.size(); ++i){
            cout << i << " " << capitales[i] << endl;
        }
        vector<vector<int>> grafoSCC;
        grafoSCC = crearGrafoDeComponentes(G, sccNodos, sccIdx);
        // Test grafo scc
        cout << "Test grafo scc "  << endl;
        for (int i = 0; i < grafoSCC.size(); ++i){
            for (int j = 0; j < grafoSCC[i].size(); ++j){

                cout << i << " " << grafoSCC[i][j] << " "  << endl;
            }
        }
        // Nodos scc
        cout << "Nodos scc "  << endl;
        for (int i = 0; i < sccNodos.size(); ++i){
            for (int j = 0; j < sccNodos[i].size(); ++j){

                cout << i << " " << sccNodos[i][j] << " "  << endl;
            }
        }

        // Agregar aristas inversas entre SCCs con el doble de costo
        vector<pair<pair<int,int>, int>> aristasInversas; // Guardar las aristas ( testeo)
        
        for (int u = 0; u < n; u++) {
            int sccU = sccIdx[u];
            for (int i = 0; i < G[u].size(); i++) {
                int v = G[u][i].first;
                int peso = G[u][i].second;
                int sccV = sccIdx[v];
                
                // Si la arista conecta diferentes SCCs
                if (sccU != sccV) {
                    // Guardar la arista inversa con el doble de peso
                    aristasInversas.push_back({{v, u}, peso * 2});
                    G[v].push_back(make_pair(u,peso * 2));
                }
            }
        }
        
        // Encontrar la ciudad imperial
            // Encontrar los centros de el grafo scc
        set<int> centritos;
        centritos = centers(grafoSCC);
        set<int>::iterator itCentros;
        // Si hay varios centros, escojer la ciudad con menor indice
        int minimoCentro = MAX;
        for(itCentros = centritos.begin(); itCentros != centritos.end();itCentros++){
            if(*(itCentros) < minimoCentro) minimoCentro = *itCentros;
            cout << "*itCentros: "<< *(itCentros) << endl;
        }
        cout << "Num centritos: "<< centritos.size() << endl;
        cout << "Capital Imperial: "<< minimoCentro << endl;        

        // Agregar las aristas inversas al grafo
        cout << "Aristas inversas agregadas:" << endl;
        for (auto& arista : aristasInversas) {
            int u = arista.first.first;
            int v = arista.first.second;
            int peso = arista.second;
            G[u].push_back({v, peso});
            cout << u << " -> " << v << " peso: " << peso << endl;
        }
        cout << aristasInversas.size() << endl;
        vector<int> distancias;
        distancias = dijkstra(G,minimoCentro);
        int cnt = 0;
        for (int i = 0; i < capitales.size();i++ ){
            cnt += distancias[capitales[i]];
        }
        cout << "catrechimba "<< cnt << endl;
        /*
        for(int i = 0; i < G.size(); i++){
            for (int j = 0; j < G[i].size(); j++){
                int u = i;
                int v = G[i][j].first;
                int peso = G[i][j].second;
                G[u].push_back({v, peso});
                cout << u << " -> " << v << " peso: " << peso << endl; 
            }
            
        }
        */

        
    }
    return 0;
}


/*
Sample Input
2
11 14
0 1 1
1 2 2
2 0 3
1 3 4
3 4 2
4 3 5
3 8 3
8 9 6
9 10 7
10 9 5
4 5 5
5 6 3
6 7 4
7 5 2
5 8
0 1 5
1 0 1
1 2 4
1 3 10
2 3 4
3 2 2
2 4 6
3 4 3
Sample Output
3 46
3 13
*/

/*
Sample Input
1
25 46
4 20 15
22 20 16
12 19 9
11 14 14
20 18 22
14 2 24
3 15 41
0 5 10
15 11 5
18 17 40
13 6 42
14 10 42
21 8 38
17 4 37
24 15 40
3 2 31
19 6 5
6 23 43
20 22 17
15 16 11
19 11 20
19 24 30
23 24 35
17 20 40
10 11 35
3 8 4
2 3 46
1 7 41
7 13 40
12 9 27
10 8 6
7 18 44
5 22 44
4 13 43
24 19 19
8 2 46
11 21 21
20 7 27
8 16 32
12 11 46
9 19 37
19 12 36
2 14 48
18 20 26
22 1 46
6 19 37
Sample Output
13 942
*/

/*
Sample Imput
1
21 39
18 20 7
10 2 3
7 19 29
0 8 10
1 7 17
5 9 35
7 16 23
0 18 47
5 15 13
0 13 21
17 1 26
6 8 5
13 14 33
2 5 1 39
18 20 7
10 2 3
7 19 29
0 8 10
1 7 17
5 9 35
7 16 23
0 18 47
5 15 13
0 13 21
17 127
19 17 6
13 4 23
9 15 50
13 0 45
1 17 19
19 12 22
13 20 38
11 9 42
12 4 30
4 1 2
10 13 38
13 6 45
14 13 37
2 10 34
7 1 16
10 9 28
8 6 31
18 12 18
10 3 3
12 16 11
16 1 43
18 0 12
9 11 38
15 5 34
10 18 14
Sample Output
10 244
*/
