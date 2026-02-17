/*
Algoritmo de Tarjan (AP)
Autor: Carlos Ramirez
Fecha: Abril 3 de 2020

*/

#include <vector>
#include <stack>
#include <iostream>
#include <set>

using namespace std;

int n, t;
vector<vector<int> > adj(50000);
int visitado[50000];
int low[50000];
int padre[50000];
set<int> apNodos;

void apAux(int);

void ap(){
  int i;

  for(i = 0; i < n; i++)
    low[i] = visitado[i] = padre[i] =-1;

  for(i = 0; i < n; i++)
    if(visitado[i] == -1)
      apAux(i);
}

void apAux(int v){
  int w, numHijos = 0;
  visitado[v] = low[v] = ++t;

  for(int i = 0; i < adj[v].size(); i++){
    w = adj[v][i];
    if(visitado[w] == -1){
      numHijos++;
      padre[w] = v;
      apAux(w);
      low[v] = min(low[v], low[w]);

      //verificar si es un punto de articulacion
      if(padre[v] != -1 && low[w] >= visitado[v])
	apNodos.insert(v);
    }
    else if(w != padre[v])
      low[v] = min(low[v], visitado[w]);
  }

  if(padre[v] == -1 && numHijos > 1)
    apNodos.insert(v);
}

int main(){
  int m, i, aux1, aux2;

  cin >> n >> m;

  for(i = 0; i < m; i++){
    cin >> aux1 >> aux2;
    adj[aux1].push_back(aux2);
    adj[aux2].push_back(aux1);
  }

  ap();

  if(apNodos.size() == 0)
    cout << "No hay puntos de articulacion" << endl;
  else{
    cout << "Puntos de Articulacion:";
    for(set<int>::iterator it = apNodos.begin(); it != apNodos.end(); ++it)
      cout << " " << *it;
    cout << endl;
  }
  
  return 0;
}
