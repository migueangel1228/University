/*
Algoritmo de Kosaraju (SCC)
Autor: Carlos Ramirez
Fecha: Marzo 23 de 2020

En esta version se utiliza un vector en el cual se van agregando
los elementos al final mientras se realiza el primer recorrido.
De esta manera en el vector ord se almacena el orden topologico
del grafo al reves. Ademas, se utiliza una variable que almacena
la cantidad de SCC y otra que almacena los nodos en cada SCC.
 */

#include <vector>
#include <list>
#include <iostream>

using namespace std;

int n, numSCC;
vector<vector<int> > adj(5000);
vector<vector<int> > adjT(5000);
bool visitados[5000];
vector<int> ord;
int sccInd[5000];
vector<vector<int> > sccNodos;

void kosarajuAux(int);
void asignar(int, int);

void kosaraju(){
  int i;

  // primer DFS --> O(n + m)
  for(i = 0; i < n; i++)
    kosarajuAux(i);

  numSCC = 0;
  // O(n)
  for(i = 0; i < n; i++)
    sccInd[i] = -1;

  // segundo DFS --> (n + m)
  for(i = n - 1; i >= 0; i--){
    if(sccInd[ord[i]] == -1){
      numSCC++;
      sccNodos.push_back(vector<int>());
      asignar(ord[i], numSCC - 1);
    }
  }
}

void kosarajuAux(int v){
  if(!visitados[v]){
    visitados[v] = true;
    
    for(int i = 0; i < adj[v].size(); i++)
      kosarajuAux(adj[v][i]);

    ord.push_back(v);
  }
}

void asignar(int u, int num){
  sccInd[u] = num;
  sccNodos[numSCC - 1].push_back(u);

  for(int i = 0; i < adjT[u].size(); i++){
    if(sccInd[adjT[u][i]] == -1)
      asignar(adjT[u][i], num);
  }
}

int main(){
  int m, i, j, aux1, aux2;

  cin >> n >> m;

  for(i = 0; i < m; i++){
    cin >> aux1 >> aux2;
    adj[aux1].push_back(aux2);
    adjT[aux2].push_back(aux1);
  }

  kosaraju();

  cout << "Total SCC: " << numSCC << endl;

  for(i = 0; i < numSCC; i++){
    cout << "SCC " << i + 1 << ": ";
    for(j = 0; j < sccNodos[i].size(); j++)
      cout << sccNodos[i][j] << " ";
    cout << endl;
  }
  
  for(i = 0; i < n; i++){
    cout << sccInd[i] << " ";
  }

  cout << endl;
  
  return 0;
}
