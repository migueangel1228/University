/*
Algoritmo de Fuerza Bruta para Puntos de Articulacion con DFS
Autor: Carlos Ramirez
Fecha: Abril 11 de 2020

 */

#include <vector>
#include <set>
#include <iostream>

using namespace std;

int n;
vector<vector<int> > adj(50000);
bool visitado[50000];
set<int> aps;

void ccDFSAux(int v){
  int w;
  visitado[v] = true;
  
  for(int i = 0; i < adj[v].size(); i++){
    w = adj[v][i];
    if(!visitado[w])
      ccDFSAux(w);
  }
}

int ccDFS(){
  int i, total = 0;

  for(i = 0; i < n; i++){
    if(!visitado[i]){
      total++;
      ccDFSAux(i);
    }
  }

  return total;
}

void apBruteForce(){
  int i,j,  p, q;

  for(j = 0; j < n; j++)
    visitado[j] = false;
  p = ccDFS();

  for(i = 0; i < n; i++){
    for(j = 0; j < n; j++)
      visitado[j] = false;

    //remover el nodo i del grafo
    visitado[i] = true;
    q = ccDFS();

    if(q > p)
      aps.insert(i);
  }
}

int main(){
  int m, i, j, aux1, aux2;

  cin >> n >> m;

  for(i = 0; i < m; i++){
    cin >> aux1 >> aux2;
    adj[aux1].push_back(aux2);
    adj[aux2].push_back(aux1):
  }
  
  apBruteForce();

  if(aps.size() == 0)
    cout << "El grafo no tiene puntos de articulacion" << endl;
  else{
    cout << "Total Puntos de Articulacion: " << aps.size() << endl;
    for(set<int>::iterator it = aps.begin(); it != aps.end(); ++it)
      cout << " " << *it;
    cout << endl;
  }
  
  return 0;
}
