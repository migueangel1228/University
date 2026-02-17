#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

const int CIUDADANOS = 10000;
int p[CIUDADANOS]; 
int rango[CIUDADANOS];
int Enemies[CIUDADANOS];
void makeSet(int v){
    p[v] = v;
    rango[v] = 0;
}

int findSet(int v){
    if(v == p[v])
        return v;
    return p[v] = findSet(p[v]);
}

bool unionSets(int u, int v){
    u = findSet(u);
    v = findSet(v);

    if(u != v){
        if(rango[u] < rango[v])
            swap(u, v);

        p[v] = u;
        if(rango[u] == rango[v])
            rango[u]++;
        return true;
    }
    return false;
}

void setFriends(int x, int y) {
    int rootX = findSet(x);
    int rootY = findSet(y);

    if (rootX == rootY) { 
        return;
    }

    int enemyRootX = Enemies[rootX];
    int enemyRootY = Enemies[rootY];

    if (enemyRootX != -1 && findSet(enemyRootX) == rootY) {
        cout << -1 << "\n";
        return;
    }
    if (enemyRootY != -1 && findSet(enemyRootY) == rootX) {
         cout << -1 << "\n";
         return;
    }

    unionSets(rootX, rootY);
    int newRoot = findSet(rootX); 

    if (enemyRootX != -1 && enemyRootY != -1) {
        unionSets(enemyRootX, enemyRootY);
        Enemies[newRoot] = findSet(enemyRootX);
    } else if (enemyRootX != -1) {
        Enemies[newRoot] = enemyRootX;
    } else if (enemyRootY != -1) {
        Enemies[newRoot] = enemyRootY;
    } else {
        Enemies[newRoot] = -1;
    }

    if (rootX != newRoot) Enemies[rootX] = -1;
    if (rootY != newRoot && rootY != rootX) Enemies[rootY] = -1; 


     if (enemyRootX != -1) {
         int currentEnemyRootX = findSet(enemyRootX);
         if (currentEnemyRootX != Enemies[newRoot] && currentEnemyRootX != newRoot) {
             Enemies[enemyRootX] = -1;
         }
     }
      if (enemyRootY != -1) {
         int currentEnemyRootY = findSet(enemyRootY);
         if (currentEnemyRootY != Enemies[newRoot] && currentEnemyRootY != newRoot) {
             Enemies[enemyRootY] = -1;
         }
     }
}

void setEnemies(int x, int y) {
    int rootX = findSet(x);
    int rootY = findSet(y);

    if (rootX == rootY) { 
        cout << -1 << "\n";
        return;
    }

    int enemyRootX = Enemies[rootX];
    int enemyRootY = Enemies[rootY];

    if (enemyRootX != -1 && findSet(enemyRootX) == rootY) {
    }
    else if (enemyRootY != -1 && findSet(enemyRootY) == rootX) {
    }
    else
    {
        if (enemyRootX != -1) {
            unionSets(enemyRootX, rootY);
        } else {
        }
        if (enemyRootY != -1) {
            unionSets(enemyRootY, rootX);
        } else {
        }
        
        int currentRootX = findSet(x);
        int currentRootY = findSet(y);
        Enemies[currentRootX] = currentRootY;
        Enemies[currentRootY] = currentRootX;

        if (rootX != currentRootX && rootX != currentRootY) {
            Enemies[rootX] = -1;
        }
        if (rootY != currentRootY && rootY != currentRootX) { Enemies[rootY] = -1;
        }

        if (enemyRootX != -1) {
            int currentEnemyRootX = findSet(enemyRootX);
            if (currentEnemyRootX != currentRootY && currentEnemyRootX != currentRootX) {
                Enemies[enemyRootX] = -1;
            }
        }
        if (enemyRootY != -1) {
            int currentEnemyRootY = findSet(enemyRootY);
            if (currentEnemyRootY != currentRootX && currentEnemyRootY != currentRootY) {
                Enemies[enemyRootY] = -1;
            }
        }
    }
}

bool areFriends(int x, int y) {
    bool ans = findSet(x) == findSet(y);
    return ans;
}

bool areEnemies(int x, int y) {
    int rootX = findSet(x);
    int rootY = findSet(y);
    bool ans = (Enemies[findSet(x)] != -1 && findSet(Enemies[findSet(x)]) == findSet(y));

    return ans;
}

int main() {

    int ciudadanos;
    while (cin >> ciudadanos && ciudadanos != 0) {
        for (int i = 0; i < ciudadanos; ++i) {
            makeSet(i);
            Enemies[i] = -1;
        }

        int operacion, ciudadano1, ciudadano2;

        while (cin >> operacion >> ciudadano1 >> ciudadano2 && operacion != 0) {

            if (operacion == 1) {
                setFriends(ciudadano1, ciudadano2);
            } else if (operacion == 2) {
                setEnemies(ciudadano1, ciudadano2);
            } else if (operacion == 3) {
                if (areFriends(ciudadano1, ciudadano2)) {
                    cout << "1\n";
                } else {
                    cout << "0\n";
                }
            } else if (operacion == 4) {
                if (areEnemies(ciudadano1, ciudadano2)) {
                    cout << "1\n";
                } else {
                    cout << "0\n";
                }
            }
        }
    }

    return 0;
}
