#include <bits/stdc++.h>

using namespace std;

/*
    AGRA  Tarea 6
Fecha  : 16/11/25
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878 
Problem   money.cpp

Complejidad computacional "Big-O":

Algoritmo de Balance de Deudas con Union-Find:

1. Inicialización: O(personas)
   - Crear conjuntos disjuntos (makeSet para cada persona)
   - Leer deudas/créditos de cada persona

2. Procesar Relaciones (Union-Find): O(relaciones × α(personas))
   - Para cada relación de amistad, unir sus componentes
   - unionSet con path compression y union by rank
   - α(n) es la función inversa de Ackermann ≈ O(1)

3. Verificar Balance por Componente: O(personas²)
   - Para cada persona no visitada, encontrar su componente
   - Sumar todas las deudas dentro del mismo componente
   - Verificar si la suma es cero (componente balanceada)

Complejidad global:
    Tiempo: O(personas²)
        - Inicialización: O(personas)
        - Union-Find: O(relaciones × α(personas)) ≈ O(relaciones)
        - Verificación: O(personas²) ← Domina
  
    Espacio: O(personas)
        - Arrays p, rango, deudas, visitados: O(personas)

*/

//operaciones disjoint set union
//**************************************

void makeSet(int v,vector<int> &p, vector<int> &rango){
  p[v] = v;
  rango[v] = 0;
}


int findSet(int v,vector<int> &p, vector<int> &rango){
  int ans;
  if(v == p[v])
    ans = v;
  else{
    p[v] = findSet(p[v],p,rango);
    ans = p[v];
  }
  return ans;
}

void unionSet(int u, int v,vector<int> &p, vector<int> &rango){
  u = findSet(u,p,rango);
  v = findSet(v,p,rango);

  if(u != v){
    if(rango[u] < rango[v])
      swap(u, v);
    
    p[v] = u;
    if(rango[u] == rango[v])
      rango[u]++;
  }
}

int main(){

    int casitos;
    cin >> casitos;
    while (casitos--){
        int n,m;
        cin >> n >> m;
        map<int,int> deudas;
        vector<int> p(n);
        vector<int> rango(n);
        int aux;

        for(int i = 0; i < n; i++){ // deudas
            cin >> aux;
            deudas[i] = aux;
            makeSet(i,p,rango);
        }
        int x, y;
        for(int i = 0; i < m; i++){ // relaciones
            cin >> x >> y;
            unionSet(x,y,p,rango);
        }
        int sum, papi, actual;
        bool esPosible = true;
        vector<bool> vis(n,false);
        for(int i = 0; i < n && esPosible; i++){
            if(!vis[i]){
                sum = 0;
                actual = findSet(i, p, rango);
                for(int j = 0; j < n; j++){
                    if(!vis[j]){
                        vis[j] = true;
                        if(actual == findSet(j, p, rango))  sum += deudas[j];
                    }
                }
                if (sum != 0 ) esPosible = false;
            }
        }
        if(esPosible == false) cout << "IMPOSSIBLE" << endl;
        else cout << "POSSIBLE" << endl;
    }
  
    return 0;
}

/*
Sample Input
2
5 3
100
-75
-25
-42
42
0 1
1 2
3 4
4 2
15
20
-10
-25
0 2
1 3
Sample Output
POSSIBLE
IMPOSSIBLE
*/