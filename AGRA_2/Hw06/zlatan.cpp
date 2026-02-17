#include <bits/stdc++.h>

using namespace std;

/*
    AGRA  Tarea 6
Fecha  : 15/11/25
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem   zlatan.cpp

Complejidad computacional "Big-O":

Algoritmo en 5 pasos principales:

1. Identificar Estados (Tarjan SCC): O(ciudades + carreteras)
   - Componentes fuertemente conexas del grafo

2. Capital de cada Estado (Dijkstra múltiple): O(ciudades × (ciudades + carreteras) log ciudades)
   - Para cada estado, probar todos sus nodos como capital candidata
   - Ejecutar Dijkstra desde cada candidato

3. Grafo de Estados: O(carreteras × log carreteras)
   - Crear DAG con aristas entre estados diferentes

4. Capital Imperial (Tree Centers): O(estados + carreteras_entre_estados)
   - Agregar aristas bidireccionales (doble costo) entre estados
   - Tree trimming para encontrar centro(s) del grafo

5. Costos Totales (Dijkstra final): O((ciudades + carreteras) log ciudades)
   - Desde capital imperial a todas las demás capitales

Complejidad global:
    Tiempo: O(ciudades × (ciudades + carreteras) log ciudades)
        Dominado por el paso 2 (Dijkstra múltiple)
  
    Espacio: O(ciudades + carreteras)
        Grafos, estructuras auxiliares y priority queues

*/

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

    // Calcular grado de salida, entrada y construir grafo inverso
    for (int i = 0; i < n; i++){
        gradoTotal[i] = G[i].size(); // grado de salida
        for (int j = 0; j < G[i].size(); j++){
            int vecino = G[i][j];
            gradoEntrada[vecino]++;
            grafoInverso[vecino].push_back(i); // i apunta a vecino, entonces vecino <- i
        }
    }
    // Sumar grado total (entrada + salida)
    for (int i = 0; i < n; i++){
        gradoTotal[i] += gradoEntrada[i];
    }
    // hojas (nodos con grado total <= 1)
    for (int i = 0; i < n; i++){
        if (gradoTotal[i] <= 1){
            colita.push(i);   
        }
    }
    // Si no hay hojas, todos son centros (grafo fuertemente conexo)
    bool hayHojas = !colita.empty();
    if (!hayHojas){
        for (int i = 0; i < n; i++){
            centers.insert(i);
        }
    }
    // BFS pelando capas
    while (hayHojas && !colita.empty()){
        int v = colita.front();
        colita.pop();
        // Decrementar grado de vecinos salientes (v -> w)
        for (int i = 0; i < (int)G[v].size(); i++) {
            int w = G[v][i];
            gradoTotal[w]--;
            if (gradoTotal[w] == 1) {
                colita.push(w);
                nivel[w] = nivel[v] + 1;
                nivelMax = max(nivelMax, nivel[w]);
            }
        }
        // Decrementar grado de vecinos entrantes (i -> v)
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
    // nodos con nivel mayor = centros
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


void debugGrafoSCC(vector<vector<int>> &grafoSCC, vector<vector<int>> &sccNodos, vector<int> &capitales){
    cout << "Numero de componentes: " << grafoSCC.size() << endl;
    
    // Mostrar nodos de cada componente
    cout << " Nodos por componente " << endl;
    for (int i = 0; i < sccNodos.size(); i++){
        cout << "SCC " << i << endl;
        for (int j = 0; j < sccNodos[i].size(); j++){
            cout << sccNodos[i][j];
            if (j < sccNodos[i].size() - 1) cout << " ";
        }
    }
    
    // Mostrar aristas del grafo SCC
    cout << " Aristas entre componentes " << endl;
    int totalAristas = 0;
    for (int i = 0; i < grafoSCC.size(); i++){
        if (grafoSCC[i].size() > 0){
            cout << "SCC " << i << " ";
            for (int j = 0; j < grafoSCC[i].size(); j++){
                cout << grafoSCC[i][j];
                if (j < grafoSCC[i].size() - 1) cout << " ";
                totalAristas++;
            }
            cout << endl;
        }
    }
    cout << "Total de aristas: " << totalAristas << endl;
    
    // Calcular grados
    cout << " Grados de cada componente " << endl;
    vector<int> gradoEntrada(grafoSCC.size(), 0);
    vector<int> gradoSalida(grafoSCC.size(), 0);
    
    for (int i = 0; i < grafoSCC.size(); i++){
        gradoSalida[i] = grafoSCC[i].size();
        for (int j = 0; j < grafoSCC[i].size(); j++){
            gradoEntrada[grafoSCC[i][j]]++;
        }
    }
    
    for (int i = 0; i < grafoSCC.size(); i++){
        cout << "SCC " << i << "entrada" << gradoEntrada[i] << "salida " << gradoSalida[i] << endl;
    }
    
}

void debugCapitales(vector<int> &capitales, vector<vector<int>> &sccNodos, vector<vector<tuple<int,int>>> &G){
    cout << " DEBUG CAPITALES " << endl;
    cout << "Numero de estados SCCs " << capitales.size() << endl;
    
    cout << " Capital de cada estado " << endl;
    for (int i = 0; i < capitales.size(); ++i){
        cout << "Estado " << i << " Capital:  " << capitales[i];
        cout << " Nodos: " << sccNodos[i].size() << endl;
    } 
}

void debugAristasInversas(vector<tuple<tuple<int,int>, int>> &aristasInversas){
    cout << " DEBUG ARISTAS INVERSAS "  << endl;
    cout << "Numero de aristas inversas agregadas: " << aristasInversas.size() << endl;
    
    for (int idx = 0; idx < aristasInversas.size(); idx++) {
        int u = aristasInversas[idx].first.first;
        int v = aristasInversas[idx].first.second;
        int peso = aristasInversas[idx].second;
        cout << u << " -> " << v << " " << peso << endl;
    }
}

void debugCentros(vector<vector<int>> &grafoSCC, set<int> &centros, vector<int> &capitales){
    cout << " DEBUG CENTROS " << endl;
    cout << "Numero de centros encontrados: " << centros.size() << endl;
    // AYUDA
    // Calcular niveles usando BFS desde hojas
    int n = grafoSCC.size();
    vector<int> nivel(n, 0);
    vector<int> grado(n, 0);
    queue<int> colita;
    
    for (int i = 0; i < n; i++){
        grado[i] = grafoSCC[i].size();
    }
    
    // Identificar hojas
    cout << " Hojas (grado 1) " << endl;
    for (int i = 0; i < n; i++){
        if (grado[i] == 1){
            cout << "SCC " << i << endl;
            colita.push(i);   
        }
    }
    
    // BFS para calcular niveles
    int nivelMax = 0;
    while (!colita.empty()){
        int v = colita.front();
        colita.pop();

        for (int i = 0; i < (int)grafoSCC[v].size(); i++) {
            int w = grafoSCC[v][i];
            grado[w]--;
            if (grado[w] == 1) {
                colita.push(w);
                nivel[w] = nivel[v] + 1;
                nivelMax = max(nivelMax, nivel[w]);
            }
        }
    }
    
    // Mostrar niveles de todos los nodos
    cout << " Niveles de cada componente " << endl;
    for (int i = 0; i < n; i++){
        cout << "SCC " << i << " Capital: " << capitales[i] << " nivel" << nivel[i];
        if (nivel[i] == nivelMax) cout << " CENTRO";
        cout << endl;
    }
    
    cout << "Nivel maximo: " << nivelMax << endl;
    //JUPUTAAAAAAAAAAAAAAAA
    // Mostrar centros
    cout << " Centros del grafo " << endl;
    for (set<int>::iterator it = centros.begin(); it != centros.end(); it++){
        cout << "SCC " << *it << " Capital: " << capitales[*it] << endl;
    }
    
    // Encontrar el centro con capital :;(())
    int capitalImperial = MAX;
    int sccImperial = -1;
    for (set<int>::iterator it = centros.begin(); it != centros.end(); it++){
        if (capitales[*it] < capitalImperial){
            capitalImperial = capitales[*it];
            sccImperial = *it;
        }
    }
    
    if (sccImperial != -1){
        cout << "Capital Imperial seleccionada: " << capitalImperial 
             << " SCC " << sccImperial << "" << endl;
    }
    
    
}
void debugResultadoFinal(int capitalImperial, vector<int> &distancias, vector<int> &capitales){
    //cout << "Capital Imperial seleccionada: " << capitalImperial << endl;
    //cout << "distancias desde Capital Imperial" << endl;
    int sumaTotal = 0;
    for (int i = 0; i < capitales.size(); i++){
        int dist = distancias[capitales[i]];
        //cout << "Hacia capital del Estado " << i << ;
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
        
        // Inicializacion grafo
        vector<vector<tuple<int,int>>> G(n);

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
        
        // Obtener ciudad capital de cada SCC usando Dijkstra individual
        vector<int> capitales(sccNodos.size());
        
        for (int i = 0; i < sccNodos.size(); i++){
            int minSuma = MAX;
            int capital = sccNodos[i][0];
            
            // Para cada nodo candidato en el SCC
            for (int u = 0; u < sccNodos[i].size(); u++){
                int nodoActual = sccNodos[i][u];
                
                // Ejecutar Dijkstra desde este nodo
                vector<int> dist = dijkstra(G, nodoActual);
                
                // Sumar distancias solo a nodos del mismo SCC
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
                
                // Si es alcanzable y tiene mejor suma, o mismo suma pero menor índice
                if (alcanzable){
                    if (suma < minSuma || (suma == minSuma && nodoActual < capital)){
                        minSuma = suma;
                        capital = nodoActual;
                    }
                }
            }
            
            capitales[i] = capital;
        }
        
        // Debug capitales de cada estado
        //debugCapitales(capitales, sccNodos, G);
        
        vector<vector<int>> grafoSCC;
        grafoSCC = crearGrafoDeComponentes(G, sccNodos, sccIdx);
        
        // Debug completo del grafo SCC
        //debugGrafoSCC(grafoSCC, sccNodos, capitales);
        
        // Identificar aristas inversas entre SCCs con el doble de costo
        vector<tuple<tuple<int,int>, int>> aristasInversas; // Guardar las aristas ( testeo)
        
        for (int u = 0; u < n; u++) {
            int sccU = sccIdx[u];
            for (int i = 0; i < G[u].size(); i++) {
                int v = G[u][i].first;
                int peso = G[u][i].second;
                int sccV = sccIdx[v];
                
                // Si la arista conecta diferentes SCCs
                if (sccU != sccV) {
                    // Guardar la arista inversa con el doble de peso (NO agregarla aún)
                    aristasInversas.push_back({{v, u}, peso * 2});
                }
            }
        }
        
        // Encontrar la ciudad imperial
            // Encontrar los centros de el grafo scc
        set<int> centritos;
        centritos = centers(grafoSCC);
        
        // Debug completo de los centros
        //debugCentros(grafoSCC, centritos, capitales);
        
        set<int>::iterator itCentros;
        // Si hay varios centros, escojer la ciudad con menor indice
        int minimoCentro = MAX;
        for(itCentros = centritos.begin(); itCentros != centritos.end();itCentros++){
            if(capitales[*itCentros] < minimoCentro) minimoCentro = capitales[*itCentros];
        }
        
        // Debug aristas inversas
        //debugAristasInversas(aristasInversas);
        
        // Agregar las aristas inversas al grafo
        for (int idx = 0; idx < aristasInversas.size(); idx++) {
            int u = aristasInversas[idx].first.first;
            int v = aristasInversas[idx].first.second;
            int peso = aristasInversas[idx].second;
            G[u].push_back(make_pair(v, peso));
        }
        vector<int> distancias;
        distancias = dijkstra(G,minimoCentro);
        
        // Debug resultado final
        debugResultadoFinal(minimoCentro, distancias, capitales);

        
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
