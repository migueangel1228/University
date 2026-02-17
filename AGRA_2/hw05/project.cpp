#include<bits/stdc++.h>

using namespace std;

void decode(string &caso, vector<vector<int>> &grafito, unordered_map<char,int> &mapita, int &cnt, vector<int> &w){
    // la tarea main depende de las tareas secundarias

    // reviso si ya decodifique la main task
    if (mapita.find(caso[0]) == mapita.end()){
        mapita[caso[0]] = cnt;
        cnt++;
    }
    // busco donde termina el numero (primer espacio despues del indice 2)
    int i = 2;
    while (i < caso.size() && isdigit(caso[i])){
        i++;
 
 
    }
    // extraer el peso de la tarea
    int peso = stoi(caso.substr(2, i - 2));
    w[mapita[caso[0]]] = peso;

    // salto los espacios entre el numero y las dependencias
    while (i < caso.size() && caso[i] == ' '){
        i++;
    }
    // desde aqui empiezan las dependencias (revisar)
    while (i < caso.size()){
        char taskSecondary = caso[i];

        // reviso si ya decodifique la tarea secundaria
        if (mapita.find(taskSecondary) == mapita.end()){
            mapita[taskSecondary] = cnt;
            cnt++;
        }
        int DecTaskMain = mapita[caso[0]];
        int DecTaskSecondary = mapita[taskSecondary];

        grafito[DecTaskSecondary].push_back(DecTaskMain);

        i++;
    }
}
vector<int> khan(vector<vector<int>>&G, vector<int> &inc, vector<int> &w ,int &n){
    queue<int> q;
    vector<int> costTask(n);
    // llenar los costos de las tareas
    for (int i = 0; i < n; ++i){
        costTask[i] = w[i];
    } 
    for(int i = 0; i < n; i++){
        if (inc[i] == 0){
            q.push(i);
        }
    }
    int u, v;
    while(!q.empty()){
        u = q.front();
        q.pop();
        for (int i = 0; i < G[u].size(); i++){
            v = G[u][i];
            inc[v]--;
            costTask[v] = max(costTask[v], costTask[u] + w[v]);
            if (inc[v] == 0){
                q.push(v);       
            }
        }
    }
    return costTask;
}


int main(){
    string casitos;
    getline(cin,casitos);
    int casos = stoi(casitos);
    cin.ignore();

    while (casos--){
        string taskString = "";
        getline(cin,taskString);
        
        vector<vector<int>> G(26);
        vector<int> weights(26,0);
        vector<int> inc(26,0);
        vector<int> costTask;

        unordered_map<char,int> mapita;
        int numeroTasks = 0;
        while (taskString != ""){
            decode(taskString, G, mapita, numeroTasks, weights);

            taskString = "";
            getline(cin,taskString);
        }
        for (int i = 0; i < numeroTasks; i++) {
            for (int j = 0; j < G[i].size(); j++) {
                inc[G[i][j]]++;
            }
        }

        costTask = khan(G, inc, weights, numeroTasks); // obtener vector de los costos de las tareas, considerando las prelaciones

        int maxi = -1; // costo de la tarea mas grande
        for (int i = 0; i < costTask.size();i++){
            if (maxi < costTask[i]){
                maxi = costTask[i];
            }
        }
        cout << maxi << endl;
        cout << endl;

        /*
        Print G
        for(int i = 0; i < G.size(); i++){
            cout << "Aristas de " << i << endl;
            for(int j = 0; j < G[i].size(); j++){
                cout << " " <<  G[i][j] << " " << endl;

            }
        }
        */
    }
    return 0;
}


/*
Sample Input
3

A 5
B 3 A
D 2 A
C 2 B
F 2 CE
E 4 DC

A 5
B 3 A
D 2 A
C 2 B
F 2 CE
E 4 DC

A 362 PMJWFSRGI
B 347 
C 272 FYBLXV
D 897 GIV
E 478 JWFIBL
F 721 RGIV
G 122 X
H 85 WFRDQBLXV
I 167 V
J 110 SGX
K 262 OEHNFSDQGL
L 250 V
M 488 NFSRYGBV
N 943 FQBL
O 763 MRIXV
P 104 TCHJRIV
Q 351 GBV
R 107 BL
S 926 QGBXV
T 317 EWGIBLX
U 288 CHSGILXV


V 591 
W 128 YDILV
X 70 
Y 836 QXV
Sample Output
16

16

4125
*/