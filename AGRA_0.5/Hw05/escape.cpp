/*
B - Problem BSource file name: escape.cpp
Time limit: 1 second
Poor Kianoosh! 6 weeks since he was officially accepted as a citizen of Barareh and during this time he has had nothing but
Nochophskew for his breakfast, lunch and dinner. And nowadays, during the nights, he dreams of nothing but a small piece
of bread, some cheese and a glass of milk to have for his breakfast. And during the days, he thinks of nothing but a great
escape from this weird city in order to turn his night-time dreams into reality.
After carefully checking all the potential ways out of the city, he concluded that there are only three such possible ways.
The first one is through the city gate which is of course guarded by fully-armed guards, ready to kill any creature trying
to go through the gate without permission. The second way is passing through the northern walls of the city and going
through a jungle which contains nothing but those deadly snakes called NeshimanGazes (And be sure that Kianoosh does
not like to repeat his creepy experience with them again).
Finally, the third and the last (and of course the only feasible) way is passing through a secret door in the famous so called
HezarDaroon Castle (means a castle with thousands of doors). Unfortunately, the problem with this castle is that no one
actually knows the way to reach this secret door.
After spending some time gathering information about the castle, Kianoosh found out that HezarDaroon can actually be
modeled as an M×N grid with each cell representing a room in the castle. There is always a door between two neighboring
rooms but there are some rooms which contain a NeshimanGaz ready to serve anyone trying to enter the room with its
poisonous bites.
There are also some rooms which contain a rotating door. A rotating door is actually a cylinder positioned at the center of
the room with a slice removed from it. In Figure 1, you can see a room with a rotating door with its removed slice facing
towards west.
As it can be seen, one can only enter the room from the neighbor to which the removed slice is facing. And once Kianoosh
enters the room, he can rotate the door clockwise or counter-clockwise in order to reach the other doors in the room. For
example, in the configuration of figure 1, if he rotates the door clockwise by 90 degrees, he can reach the door to the north
and if he continues rotating the door by another 90 degrees in the same direction, he can reach the door to east.
Another important fact about the rotating doors is that associated to each door is a number weightDoor which is the amount of time,
measured in seconds, that it takes for a normal human-being(like Kianoosh) to rotate the door by 90 degrees. You may also
assume that going from a room to its neighbor room takes exactly 1 second.
Today, after spending a noticeable amount of money, Kianoosh managed to buy a map of the castle from underground
shops of Barareh. Taking a look at the map, he found that the entrance to the castle is located at the lower-left corner and
the secret door is located at the upper-right corner of the grid. He can also see the position and the origenChar configuration of
the rotating doors and the coordinates of rooms containing the deadly NeshimanGazes to which Kianoosh does not like to
enter.
Kianoosh is happy. He is only one step away from his dreams coming true. But how can he find his way to the secret door?
Yes! He needs help! And as a genius problem-solver, you should help him find the path with the minimum required time to
reach the secret passage from the lower-left corner of the castle.
Input
The first line of the input contains an integer cases which is the number of test cases. Each test case begins with a line
containing 1 ≤N ≤150 (the number of rows) and 1 ≤M ≤150 (the number of columns) followed by N lines, with the i-th
line containing M characters, the j-th character of which representing the status of the j-th cell in the i-th row of the grid
(counted from north). Each character may have six different values. A ’.’ character represents a normal room while a
’#’ represents a room containing a NeshimanGaz and ’N’, ’W’, ’E’, ’S’ represent a room with a rotating door facing
north, west, east, and south respectively. The map is followed by D integers, the k-th of which is equal to dk for the k-th
door, counting the doors from the north-west corner in a row major order. You can assume that D (which is the number of
rotating doors in the castle) is no more than 500, and the entrance (room at lower-left corner) and the room containing the
secret door (room at upper-right corner) does not contain NeshimanGazes or rotating doors.
The input must be read from standard input.
Output
For each test case, your program should output a line containing a single integer which is the minimum amount of time
required for Kianoosh to reach the secret door. In the case the secret door is not reachable with respect to the given map
and rules, a line containing the phrase ’Poor Kianoosh’ should be printed.
The output must be written to standard output.
Sample Input
1
3 3
.#.
..W
...
10
Sample Output
14
*/
#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <cmath>
using namespace std;

int INF = 50000; // infinito representado como un numero NO alcanceble para el para el problema

// INICIALIZO las Direcciones
//  N, E, S, W
int dFila[4] = {-1, 0, 1, 0}; // vertical
int dColumna[4] = {0, 1, 0, -1}; // horizontal 
char dirChar[4] = {'N', 'E', 'S', 'W'};

// Calcular el costo de rotacion minimo (en unidades de 90°)
int obtenerCostoRotacion(char origenChar, char destinoChar, int weightDoor) {
    // Mapear letra a indice: N=0, E=1, S=2, W=3.
    int origenIdx, destinoIndx;
    for (int i = 0; i < 4; i++) {
        if (dirChar[i] == origenChar) origenIdx = i;
        if (dirChar[i] == destinoChar) destinoIndx = i;
    }
    int posicionDiff = abs(origenIdx - destinoIndx);
    // remplaza 
    if (posicionDiff > 4 - posicionDiff) {
        posicionDiff = 4 - posicionDiff;
    }
    return posicionDiff * weightDoor;
}

int main(){
    
    int cases;
    cin >> cases;
    while(cases--){
        int N, M;
        cin >> N >> M;
        vector<string> grid(N);
        for (int i = 0; i < N; i++){
            cin >> grid[i];
        }
        
        // Asignar el valor weightDoor para cada puerta giratoria en orden de fila (de norte a sur) y de izquierda a derecha
        vector<int> doorD;
        for (int i = 0; i < N; i++){ //fila
            for (int j = 0; j < M; j++){ // columna
                if(grid[i][j]=='N'|| grid[i][j]=='E'|| grid[i][j]=='S'|| grid[i][j]=='W'){
                    int weightDoor;
                    cin >> weightDoor;
                    doorD.push_back(weightDoor);
                }
            }
        }
        // Crear una matriz para almacenar el costo minimo hasta cada celda
        vector<vector<int>> distanceResult(N, vector<int>(M, INF));
        
        // Dijkstra: usamos priority_queue, removed typedef
        priority_queue<pair<int, pair<int,int>>, vector<pair<int, pair<int,int>>>, greater<pair<int, pair<int,int>>>> pq;
        
        // Punto de inicio: esquina inferior izquierda
        int startFil = N - 1, startCol = 0;
        distanceResult[startFil][startCol] = 0;
        pq.push({0, {startFil, startCol}});
        
        // indice para las puertas giratorias (para asignar el costo weightDoor a cada una)
        vector<vector<int>> doorIndx(N, vector<int>(M, -1));
        int idx = 0;
        for (int i = 0; i < N; i++){
            for (int j = 0; j < M; j++){
                if(grid[i][j]=='N'|| grid[i][j]=='E'|| grid[i][j]=='S'|| grid[i][j]=='W'){
                    doorIndx[i][j] = idx++;
                }
            }
        }
        
        while(!pq.empty()){
            auto [time, pos] = pq.top();
            int i = pos.first, j = pos.second;
            pq.pop();
            
            if(time != distanceResult[i][j]) {
            } else if(!(i == 0 && j == M - 1)) { 

                // Depende del tipo de celda actual:
                if(grid[i][j]=='N'|| grid[i][j]=='E'|| grid[i][j]=='S'|| grid[i][j]=='W'|| grid[i][j]=='#'|| grid[i][j]=='.'){
                    
                    // si la celda actual NO es puerta giratoria, simplemente podemos moverse a celdas adjacentes.
                    if(grid[i][j] == '.'){
                        // Movimiento normal: 4 direcciones
                        for (int weightDoor = 0; weightDoor < 4; weightDoor++){
                            int ni = i + dFila[weightDoor], nj = j + dColumna[weightDoor];
                            bool validCell = (ni >= 0 && ni < N && nj >= 0 && nj < M && grid[ni][nj] != '#');
                            
                            if(validCell) {
                                // si la celda destino es una puerta giratoria, se debe verificar que se ingresa desde la direccion PERMITIDA
                                if(grid[ni][nj]=='N' || grid[ni][nj]=='S' || grid[ni][nj]=='E' || grid[ni][nj]=='W'){
                                    // direccion PERMITIDA = se viene desde la celda que esta en la direccion de la letra
                                    bool canEnter = false;
                                    if(grid[ni][nj]=='N' && i == ni - 1 && j == nj) canEnter = true;
                                    if(grid[ni][nj]=='S' && i == ni + 1 && j == nj) canEnter = true;
                                    if(grid[ni][nj]=='E' && i == ni && j == nj + 1) canEnter = true;
                                    if(grid[ni][nj]=='W' && i == ni && j == nj - 1) canEnter = true;
                                    
                                    if(canEnter && time + 1 < distanceResult[ni][nj]){
                                        distanceResult[ni][nj] = time + 1;
                                        pq.push({distanceResult[ni][nj], {ni, nj}});
                                    }
                                } else {
                                    // Celda normal
                                    if(time + 1 < distanceResult[ni][nj]){
                                        distanceResult[ni][nj] = time + 1;
                                        pq.push({distanceResult[ni][nj], {ni, nj}});
                                    }
                                }
                            }
                        }
                    }
                    
                    if(grid[i][j]=='N' || grid[i][j]=='S' || grid[i][j]=='E' || grid[i][j]=='W'){
                        int door_d = doorD[doorIndx[i][j]];
                        // Desde la puerta, probar 4 posibles direcciones posibles
                        for (int weightDoor = 0; weightDoor < 4; weightDoor++){
                            int ni = i + dFila[weightDoor], nj = j + dColumna[weightDoor];
                            bool validCell = (ni >= 0 && ni < N && nj >= 0 && nj < M && grid[ni][nj] != '#');
                            
                            if(validCell) {
                                // Calcular costo de rotacion para que la puerta apunte en la direccion deseada.
                                char destinoChar = dirChar[weightDoor];
                                int costRot = obtenerCostoRotacion(grid[i][j], destinoChar, door_d);
                                int newTime = time + costRot + 1; // 1 time para mover
                                
                                // Si la celda destino es otra puerta giratoria, hay que verificar la regla de entrada.
                                bool canEnter = true;
                                if(grid[ni][nj]=='N' || grid[ni][nj]=='S' || grid[ni][nj]=='E' || grid[ni][nj]=='W'){
                                    canEnter = false;
                                    if(grid[ni][nj]=='N' && i == ni - 1 && j == nj) canEnter = true;
                                    if(grid[ni][nj]=='S' && i == ni + 1 && j == nj) canEnter = true;
                                    if(grid[ni][nj]=='E' && i == ni && j == nj + 1) canEnter = true;
                                    if(grid[ni][nj]=='W' && i == ni && j == nj - 1) canEnter = true;
                                }
                                
                                if(canEnter && newTime < distanceResult[ni][nj]){
                                    distanceResult[ni][nj] = newTime;
                                    pq.push({newTime, {ni, nj}});
                                }
                            }
                        }
                    }
                }
            }
        }
        
        if(distanceResult[0][M-1] == INF)
            cout << "Poor Kianoosh" << endl;
        else
            cout << distanceResult[0][M-1] << endl;
    }
    return 0;
}
