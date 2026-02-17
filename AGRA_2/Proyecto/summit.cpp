#include<bits/stdc++.h>

using namespace std;

const int INF = INT_MAX;

// Verifica si una coordenada esta dentro de los limites
bool InRange(int r, int c, int N) {
    bool ans = false;
    if (r >= 0 && r < N && c >= 0 && c < N)
        ans = true;
    return ans;
}

// arriba, abajo, izquierda, derecha
vector<int> dr = {-1, 1, 0, 0};
vector<int> dc = {0, 0, -1, 1};

// Genera las coordenadas del vecino en direccion i
tuple<int,int> generarVecinos(int r, int c, int direccion) {
    int nr = r + dr[direccion];
    int nc = c + dc[direccion];
    return make_pair(nr, nc);
}

// Actualiza el mapa acumulando costos y sumando el ID del lider al verificador
void dijkstra(vector<vector<int>>& M, int sr, int sc, int T, map<tuple<int,int>, tuple<int,int>>& resultados, int Fi) {
    
    int N = M.size();
    vector<vector<int>> costo(N, vector<int>(N, INF));
    
    // Cola de prioridad: (pasos, costo, fila, columna)
    priority_queue<tuple<int,int,int,int>, vector<tuple<int,int,int,int>>, greater<tuple<int,int,int,int>>> pq;
    
    // Inicializar 
    costo[sr][sc] = M[sr][sc];
    // (pasos, costo, r, c)
    // se prioriza los pasos, dado que es necesaro marcar todos los candidatos
    pq.push(make_tuple(0, M[sr][sc], sr, sc)); 
    
    while (!pq.empty()) {
        int actualPasos = get<0>(pq.top());
        int actualCost = get<1>(pq.top());
        int r = get<2>(pq.top());
        int c = get<3>(pq.top());
        pq.pop();
        
        // verf si es estado es valido (no es obsoleto)
        bool stateValido = (actualCost <= costo[r][c]);
        
        if (stateValido) {
            // Explorar vecinos solo si tiene pasos menores a T
            bool tienePasos = false;
            if (actualPasos < T)
                tienePasos = true;
            
            if (tienePasos) {
                for (int i = 0; i < 4; i++) {
                    tuple<int,int> vecino = generarVecinos(r, c, i);
                    int nr = vecino.first;
                    int nc = vecino.second;
                    
                    // Verificar limites
                    bool validLimites = InRange(nr, nc, N);
                    
                    if (validLimites) {
                        int newCost = actualCost + M[nr][nc];
                        int newPasos = actualPasos + 1;
                        
                        // Verificar si encontramos un camino mejor (menor costo)
                        bool esMejor = (newCost < costo[nr][nc]);
                        
                        if (esMejor) {
                            costo[nr][nc] = newCost;
                            pq.push(make_tuple(newPasos, newCost, nr, nc));
                        }
                    }
                }
            }
        }
    }
    // Registrar todas las celdas alcanzables
    // Esta es la unica forma de garantizar que registramos el costo optimo
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            bool esAlcanzable = (costo[i][j] < INF);
            
            if (esAlcanzable) {
                tuple<int,int> coordenada = make_pair(i, j);
                
                // Acumular el ID del lider en el verificador (first)
                resultados[coordenada].first += Fi;
                
                // Acumular el costo en el total (second)
                // Restar el costo de la coordenada destino porque lo paga Zlatan
                int costSinDestino = costo[i][j] - M[i][j];
                resultados[coordenada].second += costSinDestino;
            }
        }
    }
}

// Busca la mejor coordenada e imprime el resultado
void imprimirResultado(map<tuple<int,int>, tuple<int,int>>& resultados_globales, int F,vector<vector<int>> &M) {
    // Calcular la sumatoria esperada: 1 + 2 + ... + F
    int sumatoria = (F * (F + 1)) / 2;
    
    int minimoCosto = INF;
    tuple<int,int> mayorCoordenada = make_pair(-1, -1);
    bool encontrado = false;
    
    // Iterar sobre el mapa resultados_globales
    map<tuple<int,int>, tuple<int,int>>::iterator it;
    for (it = resultados_globales.begin(); it != resultados_globales.end(); it++) {
        tuple<int,int> coordenada = it->first;
        int verificador = it->second.first;
        int totalCost = (it->second.second);
        bool esCandidato = false, esMejorCost = false , mismoCost = false , mayorRow = false, equalRow = false, mayorColum = false;
        // Filtrar candidatos (solo celdas donde llegaron todos los lideres)
        if (verificador == sumatoria)
            esCandidato = true;

        if (esCandidato && (totalCost <= minimoCosto)) {
            encontrado = true; /// almenos hay un canditado
            
            // Encontrar el minimo costo entre los candidatos
            if (totalCost < minimoCosto){

                minimoCosto = totalCost;
                mayorCoordenada = coordenada;

            }
            else if (minimoCosto == totalCost) { // hay empate
                // Dado que hay empate, hay que elegir la lexicograficamente mayor
                if (coordenada.first > mayorCoordenada.first)
                    mayorRow = true;
                
                if (coordenada.first == mayorCoordenada.first)
                    equalRow = true;

                if (coordenada.second > mayorCoordenada.second);
                    mayorColum = true;

                if (mayorRow) {
                    mayorCoordenada = coordenada;
                } 
                else if (equalRow && mayorColum) { // segundo desempate
                    mayorCoordenada = coordenada;
                }
            }
        }
    }
    
    // Pirnt
    if (encontrado) {
        // Ajustar a indice 1 
        int r = mayorCoordenada.first + 1;
        int c = mayorCoordenada.second + 1;
        cout << "The Galactic Summit will be held at sector (" << r << "," << c << ") with total energy cost = " << minimoCosto << endl;
    }
    else {
        cout << "Zlatan is disappointed" << endl;
    }
}

int main(){
    int N, F, T;
    
    while(cin >> N >> F >> T, N != 0, F != 0, T != 0){
        vector<vector<int>> M(N,vector<int>(N));
        int aux;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                cin >> aux;
                M[i][j] = aux;
            }
        }
        vector<tuple<int,int>> lideres;
        int r, c;
        for (int i = 0; i < F; i++){
            cin >> r >> c;
            lideres.push_back(make_pair(r - 1, c - 1)); // Ajustar a indice 0
        }
        
        // Mapa global que acumula informacion de todos los lideres
        // first: suma de IDs de lideres que llegaron (verificador)
        // second: suma acumulada de costos desde todos los lideres
        map<tuple<int,int>, tuple<int,int>> resultados_globales;
        
        // Ejecutar Dijkstra desde cada lider
        for (int i = 0; i < F; i++){
            int r = lideres[i].first;
            int c = lideres[i].second;
            dijkstra(M, r, c, T, resultados_globales, i + 1);
        }
        
        // Imprimir resultado
        imprimirResultado(resultados_globales, F,M);
    }
    return 0;
}


/*
Sample Input
3 2 3
1 2 3
2 1 3
3 3 1
1 1 3 3
4 3 3
4 5 10 20
40 30 40 10
18 53 4 32
52 37 42 43
1 1 1 4 3 4
4 3 2
4 5 10 20
40 30 40 10
18 53 4 32
52 37 42 43
1 1 1 4 3 4
0 0 0
Sample Output
The Galactic Summit will be held at sector (3,2) with total energy cost = 5
The Galactic Summit will be held at sector (1,4) with total energy cost = 61
Zlatan is disappointed
*/