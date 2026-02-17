/*
Nickname: Mianparito
Date:     1/1/26
Topic:    "Grafos implicitos"

https://onlinejudge.org/external/4/469.pdf

*/

#include <bits/stdc++.h>

using namespace std;
// llena el mapa, obtiene las posicones iniciales de los rios, y la ultima linea del siguietne caso la guarda en 's'.
void imput(vector<string> &m, string &s, vector<tuple<int,int>> &posLakes, bool tienePrimeraLinea, string primeraLineaExistente){ 
    string linea;
    
    if(tienePrimeraLinea){
        linea = primeraLineaExistente;
        if(linea.length() == 0 && !cin.eof()) getline(cin, linea);
    } else {
        getline(cin, linea);
    }

    while (linea.length() == 0 && !cin.eof()) getline(cin, linea);

    while (linea.length() > 0 && (linea[0] == 'L' || linea[0] == 'W')){
        m.push_back(linea);
        getline(cin, linea);
    }
    if(linea.length() > 0 && isdigit(linea[0])){
        // Encontrar espacio 
        int espacio = linea.find(' ');
        if(espacio >= 0 && espacio < (int)linea.length()){  // Verificar que encontró el espacio
            // Sacar primera parte (fila)
            string filaStr = linea.substr(0, espacio);
            // Sacar segunda parte (columna)
            string colStr = linea.substr(espacio + 1);
            // Convertir a enteros solo si no están vacías
            if(filaStr.length() > 0 && colStr.length() > 0){
                int row = stoi(filaStr);
                int col = stoi(colStr);
                posLakes.push_back(make_tuple(row, col));
            }
        }
        getline(cin, linea);
    }

    while (linea.length() > 0 && linea[0] != 'L' && linea[0] != 'W'){
        // encontrar, dividir, convertir
        int espacio = linea.find(' ');
        if(espacio >= 0 && espacio < (int)linea.length()){  // Verificar que encontró el espacio
            string filaStr = linea.substr(0, espacio);
            string colStr = linea.substr(espacio + 1);
            // Convertir a enteros solo si no están vacías
            if(filaStr.length() > 0 && colStr.length() > 0){
                int row = stoi(filaStr);
                int col = stoi(colStr);
                posLakes.push_back(make_tuple(row, col));
            }
        }
        getline(cin, linea);
    }
    // cout << "m" << m.size() << endl;
    // cout << "posLakes" << posLakes.size() << endl;
    while (linea.length() == 0 && getline(cin, linea)){}
    s = linea;
    // cout << "s" << s << endl;

}

// adelante/izquierda/abajo/derecha /arri_der/arri_izq/abaj_der/abaj_izq
vector<int> dr = {-1,0,1,0,1,-1,1,-1};
vector<int> dc = {0,-1,0,1,1,1,-1,-1};

vector<tuple<int,int>> generateNeighbors(vector<string> &mapa,tuple<int,int> u){
    vector<tuple<int,int>> neighbors;
    int nx = get<0>(u), ny = get<1>(u),auxX,auxY;

    for(int i = 0; i < 8; i++){
        auxX = nx + dr[i], auxY = ny + dc[i];
        if(0 <= auxX && auxX < mapa.size() && 0 <= auxY && auxY < mapa[0].size()){
            if(mapa[auxX][auxY] == 'W'){
                neighbors.push_back(make_tuple(auxX,auxY));
            }
        }
    }
    return neighbors;
}

int bfsAux(vector<string> &mapa,tuple<int,int> u){
    int ans = 0; 
    int rowU = get<0>(u), colU = get<1>(u);
    int rowV, colV;
    vector<vector<bool>> vis(mapa.size(),vector<bool>(mapa[0].size(),false));
    vis[rowU][colU] = true;
    ans++; 
    tuple<int,int> v,neighbor;
    queue<tuple<int,int>> q;
    q.push(u);
    
    while (!q.empty()){
        v = q.front();
        q.pop();
        int row = get<0>(v), col = get<1>(v);
        vector<tuple<int,int>> neighbors;
        neighbors = generateNeighbors(mapa,v);
        for (int i = 0; i < neighbors.size(); i++){
            neighbor = neighbors[i];
            int rowN = get<0>(neighbor), colN = get<1>(neighbor);
            if(!vis[rowN][colN]){
                q.push(neighbor);
                vis[rowN][colN] = true;
                ans++;
            }
        }  
    }
    return ans;
}

void bfs(vector<string> &mapa,vector<tuple<int,int>> lakes){
    int ans;
    tuple<int,int> auxLake;
    for(int i = 0; i < lakes.size(); i++){
        auxLake = lakes[i];
        ans = bfsAux(mapa,auxLake);
        cout << ans << endl;
    }
}

int main(){
    string cases, primeraLinea = "";
    int intCases;
    getline(cin, cases);
    

    
    intCases = stoi(cases);
    getline(cin, cases); // leer lInea en blanco
    bool flag;
    for(int caso = 0; caso < intCases; caso++){
        vector<string> mapa;
        vector<tuple<int,int>> posLakes;
        
        // Primer caso lee normalmente, casos siguientes usan primeraLinea guardada
        imput(mapa, primeraLinea, posLakes, caso > 0, primeraLinea);

        for(int i = 0; i < posLakes.size(); i++){
            int row = get<0>(posLakes[i]) - 1;
            int col = get<1>(posLakes[i]) - 1;
            posLakes[i] = make_tuple(row, col);
        }
        
        bfs(mapa, posLakes);
        
        if(caso < intCases - 1) cout << endl;
    }

    return 0;
}


/*
Sample Input
1
LLLLLLLLL
LLWWLLWLL
LWWLLLLLL
LWWWLWWLL
LLLWWWLLL
LLLLLLLLL
LLLWWLLWL
LLWLWLLLL
LLLLLLLLL
3 2
7 5
Sample Output
12
4
*/

/*
Sample Input
2
LLLLLLLLL
LLWWLLWLL
LWWLLLLLL
LWWWLWWLL
LLLWWWLLL
LLLLLLLLL
LLLWWLLWL
LLWLWLLLL
LLLLLLLLL
3 2
7 5

LWL
WLW
LWL
2 1
Sample Output
12
4
*/