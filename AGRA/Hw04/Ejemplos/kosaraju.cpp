/*
Algoritmo de Kosaraju (SCC)
Autor: Carlos Ramirez
Fecha: Marzo 23 de 2020

En esta version se utiliza una lista en la cual se van agregando
los elementos al inicio mientras se realiza el primer recorrido.
Ademas, con esta implementacion se debe recorrer el arreglo sccInd
para saber cuantos SCC resultaron y los nodos que componen cada SCC.
 */

#include <vector>
#include <list>
#include <iostream>

using namespace std;

int n;
vector<vector<int> > adj(500, vector<int>());
vector<vector<int> > adjT(500, vector<int>());
bool visitados[500];
list<int> ord;
int sccInd[500];

void kosarajuAux(int);
void asignar(int, int);

void kosaraju(){
  int i, num = 0;

  for(i = 0; i < n; i++)
    visitados[i] = false;

  for(i = 0; i < n; i++)
    kosarajuAux(i);

  for(i = 0; i < n; i++)
    sccInd[i] = -1;

  for(list<int>::iterator it = ord.begin(); it != ord.end(); it++){
    if(sccInd[*it] == -1){
      asignar(*it, num++);
    }
  }
}

void kosarajuAux(int v){
  if(!visitados[v]){
    visitados[v] = true;
    
    for(int i = 0; i < adj[v].size(); i++)
      kosarajuAux(adj[v][i]);

    ord.push_front(v);
  }
}

void asignar(int u, int num){
  sccInd[u] = num;

  for(int i = 0; i < adjT[u].size(); i++){
    if(sccInd[adjT[u][i]] == -1)
      asignar(adjT[u][i], num);
  }
}

int main(){
  int m, i, u, v;

  cin >> n >> m;

  for(i = 0; i < m; i++){
    cin >> u >> v;
    adj[u].push_back(v);
    adjT[v].push_back(u);
  }

  kosaraju();

  for(i = 0; i < n; i++){
    cout << sccInd[i] << " ";
  }

  cout << endl;
  
  return 0;
}
