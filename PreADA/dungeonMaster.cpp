/*
Nickname: Mianparito
Date:     21/12/25
Topic:    "Grafos implicitos"

https://onlinejudge.org/external/5/532.pdf

*/

#include <bits/stdc++.h>

using namespace std;

void imput(int l, int r, int c, vector<vector<string>> &M, tuple<int,int,int>&posS, tuple<int,int,int>&posE){
    char aux;
    for(int i = 0; i < l; i++){
        for(int j = 0; j < r; j++){
            for(int k = 0; k < c; k++){
                cin >> aux;
                if( aux == 'S'){
                    posS = make_tuple(i,j,k);
                    // cout << get<0>(posS) << " " << get<1>(posS) << " " << get<2>(posS);
                }
                else if( aux == 'E'){
                    posE = make_tuple(i,j,k);
                    // cout << get<0>(posE) << " " << get<1>(posE) << " " << get<2>(posE);
                }
                M[i][j][k] = aux;
            }
        }
    }
}

void imprimirMatriz(vector<vector<string>> &M,int levels, int rows, int colums){
    
    for(int i = 0; i < levels; i++){
        for(int j = 0; j < rows; j++){
            for(int k = 0; k < colums; k++){
                cout << M[i][j][k] << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
}

// Atras/Izquierda/Adelante/Derecha/Arriba/Abajo. Desplazamiento en X,Y y Z
vector<int> dr = {0, -1, 0, 1, 0, 0};
vector<int> dc = {-1, 0, 1, 0, 0 ,0};
vector<int> dz = {0, 0, 0, 0, 1, -1};

vector<tuple<int,int,int>> generateNeighbors(vector<vector<string>> &M, int level ,int row ,int colum){
    vector<tuple<int,int,int>> neighbors;
    int nx, ny, nz;
    //cout << " entro "   << endl;
    for(int i = 0; i < 6; i++){
        //cout << " itero "  <<  i << endl;
        nx = dr[i] + colum;
        ny = dc[i] + row;
        nz = dz[i] + level;
        //cout << " entro 2"   << endl;
        if((0 <= nz && nz < M.size()) && (0 <= ny && ny < M[0].size()) && (0 <= nx && nx < M[0][0].size())){
            //cout << " entro 3"  <<  endl;
            //cout << nz << " nz " << ny << " ny " << nx << " nx" << endl;
            //cout << M[nz][ny][nx] << endl;
            if(M[nz][ny][nx] != '#'){
                //cout << " entro 4"   << endl;
                neighbors.push_back(make_tuple(nz,ny,nx));
            }
        }
    }
    return neighbors;
}

int bfsAux(vector<vector<string>> &M, tuple<int,int,int>posS, tuple<int,int,int>posE){
    int levels = M.size(), rows = M[0].size(), colums = M[0][0].size();
    //cout << " entro "  <<  levels << endl;
    vector<vector<vector<int>>> vis(levels,vector<vector<int>>(rows, vector<int>(colums,-1)));
    vis[get<0>(posS)][get<1>(posS)][get<2>(posS)] = 0; // posicion inicial, visitada
    int resultado = -1 , dist = 0;
    queue<tuple<int,int,int>> q;
    //cout << " q "  <<  q.size() << endl;
    q.push(posS);
    int lvl, col, row;
    bool encontrado = false;
    tuple<int,int,int> u;
    tuple<int,int,int> v;
     //cout << " encontrado "  <<  encontrado << endl;
    vector<tuple<int,int,int>> neighbors;
    while (!q.empty() && !encontrado){
        //cout << " tamano q "  <<  q.size() << endl;   
        u = q.front();
        q.pop();
        lvl = get<0>(u);
        row = get<1>(u);
        col = get<2>(u);
        //cout << "posE " << get<0>(posE) << get<1>(posE) << get<2>(posE) << endl;
        if (u == posE){
            resultado = vis[get<0>(u)][get<1>(u)][get<2>(u)];
            encontrado = true;
            //cout << " encontrado "  <<  encontrado << endl;
        }
        else{
            //cout << " entro else "  <<  "" << endl;
            neighbors = generateNeighbors(M,lvl,row,col); 
            //cout << " entro negiih"  <<  neighbors.size() << endl; 
            for(int i = 0; i < neighbors.size(); i++){
                v = neighbors[i];
                if (vis[get<0>(v)][get<1>(v)][get<2>(v)] == -1){
                    q.push(v);
                    vis[get<0>(v)][get<1>(v)][get<2>(v)] = vis[get<0>(u)][get<1>(u)][get<2>(u)] + 1;
                }
            }
        }
    }
    
    return resultado;

}

int main(){
    int levels, rows, colums;

    while (cin >> levels >> rows >> colums, levels != 0, rows != 0, colums != 0){

        vector<vector<string>> matriz(levels,vector<string>(rows,string(colums,' ')));
        tuple<int,int,int> posStart,posEnd;

        imput(levels,rows,colums,matriz,posStart,posEnd);
        
        // cout << "posE " << get<0>(posEnd) << get<1>(posEnd) << get<2>(posEnd) << endl;
        // cout << "posS " << get<0>(posStart) << get<1>(posStart) << get<2>(posStart) << endl;

        //imprimirMatriz(matriz, levels, rows, colums);
        int ans = 69; // nice

        ans = bfsAux(matriz, posStart, posEnd);
        //cout << ans << endl;

        if (ans == -1)
            cout << "Trapped!" << endl;
        else{
            cout << "Escaped in " << ans << " minute(s)." << endl;
        }
    }

    return 0;

}

/*
Sample Input
3 4 5
S....
.###.
.##..
###.#
#####
#####
##.##
##...
#####
#####
#.###
####E
1 3 3
S##
#E#
###
0 0 0
Sample Output
Escaped in 11 minute(s).
Trapped!
*/