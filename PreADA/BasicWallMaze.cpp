/*
Nickname: Mianparito
Date:     9/1/26
Topic:    "Grafos implicitos"

https://onlinejudge.org/external/110/11049.pdf

*/  
#include <bits/stdc++.h>

using namespace std;
// north , west, south, east 
vector<char> dname = {'N','W','S','E'};  // north(-1), west(0), south(+1), east(0)
vector<int> dr = {-1,0,1,0};  // north(-1), west(0), south(+1), east(0)
vector<int> dc = {0,-1,0,1};  // north(0), west(-1), south(0), east(+1)

void imprimirMapa(const vector<vector<char>> &m){
    cout << "\n=== MAPA ===" << endl;
    for (int i = 0; i < m.size(); i++){
        for (int j = 0; j < m[i].size(); j++){
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
    cout << "============\n" << endl;
}

void imput(vector<vector<char>> &m, int cS,int rS, int cE,int rE){
    m[rS][cS] = 'S';
    m[rE][cE] = 'E';

    int numWalls = 3;
    int colInicial, rowInicial, colFinal, rowFinal;

    for (int i = 0; i < numWalls; i++){
        cin >> colInicial >>  rowInicial >> colFinal >> rowFinal;
        int direccion;
        if (rowInicial < rowFinal) // se expande hacia el south
            direccion = 2;
        else if (rowInicial > rowFinal) // se expande hacia el north
            direccion = 0;
        else{ // se expande hacia el east o west       
            if (colInicial < colFinal) // se expande hacia el west
                direccion = 3;
            else if (colInicial > colFinal) // se expande hacia el east
                direccion = 1;
        }
        int nR = rowInicial, nC = colInicial;
        // cout << " no mori 1" << endl;
        nR = nR * 2;
        nC = nC * 2;
        rowFinal = rowFinal * 2;
        colFinal = colFinal * 2;
        // cout << " no mori 2" << endl;

        while (nR != rowFinal || nC != colFinal){
            // cout << " no mori while" << endl;
            m[nR][nC] = '#';
            nR = nR + dr[direccion];
            nC = nC + dc[direccion];
        }
        // cout << " no mori #" << endl;
        m[nR][nC] = '#';
    }
}

vector<tuple<int,int>> generateNeighbors(vector<vector<char>> &map, vector<vector<char>> &vis, tuple<int,int> v ){
    vector<tuple<int,int>> neighbors;
    int row = get<0>(v) , col = get<1>(v);
    int rows = map.size(), cols = map[0].size();
    int nx, ny;
    
    for(int i = 0; i < 4; i++){
        nx = row + dr[i];
        ny = col + dc[i];
        
        // revisar limites
        bool valido = true;
        if(nx < 0 || nx >= rows || ny < 0 || ny >= cols)
            valido = false;
        
        // si ya fue visitado
        if(valido && vis[nx][ny] != 'F')
            valido = false;

        // revisar map
        if(valido){
            
            if(map[nx][ny] != '#'){
                neighbors.push_back(make_tuple(nx, ny));
                vis[nx][ny] = dname[i];
            }
        }
    }
    return neighbors;
}

string bfs(vector<vector<char>>mapa, int startR, int startC, int endR, int endC){
    vector<vector<char>> vis(13,vector<char>(13,'F')); // Guarda la direccion en la que se descubrio 'N','E,'S,'W' sino guarda 'F'
    vis[startR][startC] = 'V';
    string ans;
    bool encontrado = false;
    tuple<int,int> v, u = make_tuple(startR,startC), end = make_tuple(endR,endC);
    queue<tuple<int,int>> q;
    q.push(u);
    while (!q.empty() && !encontrado){
        v = q.front();
        q.pop();
        vector<tuple<int,int>> neighbors;
        
        if (v == end)
            encontrado = true;
        else{
            neighbors = generateNeighbors(mapa,vis,v);
        }
        for (int i = 0; i < neighbors.size(); i++){
            u = neighbors[i];
            q.push(u);
        }
    
    }
     
    int currentR = endR;
    int currentC = endC;
    char direction;
    int i = 0;
    while (currentR != startR || currentC != startC){
        direction = vis[currentR][currentC];
        
        if(i % 2 == 0)
            ans += direction;
        
        // retroceder en la dirección opuesta
        if (direction == 'N')
            currentR += 1; // Si llegamos por N, venimos de S
        
        else if (direction == 'S')
            currentR -= 1; // Si llegamos por S, venimos de N
        
        else if (direction == 'E')
            currentC -= 1; // Si llegamos por E, venimos de W
        
        else if (direction == 'W')
            currentC += 1; // Si llegamos por W, venimos de E
        i += 1;
    }
    
    // Invertir el string porque lo construimos de atrás hacia adelante
    reverse(ans.begin(), ans.end());
    
    return ans;
}

int main(){
    int colS, rowS, colE, rowE;
    while (cin >> colS >> rowS, colS != 0 || rowS != 0){ 
        cin >> colE >> rowE;
        vector<vector<char>> mapa(13,vector<char>(13,'.'));
        colS = colS * 2 - 1,rowS = rowS * 2 - 1;
        colE = colE * 2 - 1,rowE = rowE * 2 - 1;
        imput(mapa,colS, rowS,colE, rowE);
        
        // Imprimir el mapa para verificar
        // imprimirMapa(mapa);
        
        // Ejecutar BFS
        string resultado = bfs(mapa, rowS, colS, rowE, colE);
        cout << resultado << endl;
    }
}

/*
Sample Input
1 6
2 6
0 0 1 0
1 5 1 6
1 5 3 5
0 0
Sample Output
NEEESWW
*/