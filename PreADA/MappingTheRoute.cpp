/*
Nickname: Mianparito
Date:     4/1/26
Topic:    "DFS"

https://onlinejudge.org/external/6/614.pdf

*/

#include <bits/stdc++.h>

using namespace std;

// Oeste/Norte/Este/Sur
vector<int> dr = {0, -1, 0, 1};
vector<int> dc = {-1, 0, 1, 0};

vector<tuple<int,int>> generateNeighbors(vector<vector<int>> &muros, vector<vector<int>> &vis, int row, int col){
    vector<tuple<int,int>> neighbors;
    int rows = muros.size(), cols = muros[0].size();
    int nx, ny;
    
    for(int i = 0; i < 4; i++){
        nx = row + dr[i];
        ny = col + dc[i];
        
        // revisar limites
        bool valido = true;
        if(nx < 0 || nx >= rows || ny < 0 || ny >= cols){
            valido = false;
        }
        // si ya fue visitado
        if(valido && vis[nx][ny] != 0){
            valido = false;
        }
        // revisar muros
        if(valido){
            bool pared = false;
            if(i == 0){ // Oeste
                // revisar si la celda a la izquierda tiene muro al este
                if(ny >= 0 && (muros[row][ny] & 1)){
                    pared = true;
                }
            }
            else if(i == 1){ // Norte
                // revisar si la celda arriba tiene muro al sur
                if(nx >= 0 && (muros[nx][col] & 2)){
                    pared = true;
                }
            }
            else if(i == 2){ // Este
                // revisar si celda actual tiene muro al este
                if(muros[row][col] & 1){
                    pared = true;
                }
            }
            else if(i == 3){ // Sur
                // revisar si celda actual tiene muro al sur
                if(muros[row][col] & 2){
                    pared = true;
                }
            }
            
            if(!pared){
                neighbors.push_back(make_tuple(nx, ny));
            }
        }
    }
    return neighbors;
}

bool dfsAux(vector<vector<int>> &muros, vector<vector<int>> &vis, vector<vector<int>> &camino, int row, int col, int goalRow, int goalCol, int &cont){
    vis[row][col] = 1;
    cont++;
    camino[row][col] = cont;
    bool encontrado = false;
    
    if(row == goalRow && col == goalCol){
        encontrado = true;
    }
    else{
        vector<tuple<int,int>> neighbors = generateNeighbors(muros, vis, row, col);
        
        for(int i = 0; i < neighbors.size(); i++){
            if(!encontrado){
                int nx = get<0>(neighbors[i]);
                int ny = get<1>(neighbors[i]);
                
                if(dfsAux(muros, vis, camino, nx, ny, goalRow, goalCol, cont)){
                    encontrado = true;
                }
            }
        }
    }
    if(!encontrado){
        camino[row][col] = -1;
        cont--;
    }
    return encontrado;
}

void imprimirMaze(vector<vector<int>> &muros, vector<vector<int>> &camino, int mazeNum){
    int rows = muros.size(), cols = muros[0].size();
    
    cout << "Maze " << mazeNum << "\n\n";
    
    // imprimir borde superior
    cout << "+";
    for(int c = 0; c < cols; c++){
        cout << "---+";
    }
    cout << "\n";
    
    for(int r = 0; r < rows; r++){
        // imprimir celdas
        cout << "|";
        for(int c = 0; c < cols; c++){
            if(camino[r][c] > 0){
                printf("%3d", camino[r][c]);
            }
            else if(camino[r][c] == -1){
                cout << "???";
            }
            else{
                cout << "   ";
            }
            
            // imprimir muro este o espacio
            if(c < cols - 1){
                if(muros[r][c] & 1){
                    cout << "|";
                }
                else{
                    cout << " ";
                }
            }
            else{
                cout << "|";
            }
        }
        cout << "\n";
        
        // imprimir borde inferior de esta fila
        cout << "+";
        for(int c = 0; c < cols; c++){
            if(r < rows - 1){
                if(muros[r][c] & 2){
                    cout << "---";
                }
                else{
                    cout << "   ";
                }
            }
            else{
                cout << "---";
            }
            cout << "+";
        }
        cout << "\n";
    }
    cout << "\n";
    cout << "\n";
}

int main(){
    int rows, cols, startRow, startCol, goalRow, goalCol;
    int mazeNum = 1;
    
    while(cin >> rows >> cols >> startRow >> startCol >> goalRow >> goalCol, rows != 0){
        
        vector<vector<int>> muros(rows, vector<int>(cols, 0));
        vector<vector<int>> vis(rows, vector<int>(cols, 0));
        vector<vector<int>> camino(rows, vector<int>(cols, 0));
        
        // leer muros
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                cin >> muros[r][c];
            }
        }
        
        // convertir a indices base 0
        startRow--;
        startCol--;
        goalRow--;
        goalCol--;
        
        int cont = 0;
        dfsAux(muros, vis, camino, startRow, startCol, goalRow, goalCol, cont);
        
        imprimirMaze(muros, camino, mazeNum);
        
        mazeNum++;
    }
    
    return 0;
}

/*
Sample Input
2 3 1 1 1 3
1 1 0
0 0 0

4 3 3 2 4 3
0 3 0
0 2 0
0 3 0
0 1 0
0 0 0 0 0 0
Sample Output
Maze 1

+---+---+---+
|  1|???|  5|
+   +   +   +
|  2   3   4|
+---+---+---+



Maze 2

+---+---+---+
|??? ???|???|
+   +---+   +
|  3   4   5|
+   +---+   +
|  2   1|  6|
+   +---+   +
|       |  7|
+---+---+---+


*/
