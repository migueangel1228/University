/*
Algoritmo de Tarjan (Bridges)
Autor: Carlos Ramirez
Fecha: Abril 4 de 2020

 */

#include <vector>
#include <stack>
#include <iostream>
#include <set>

using namespace std;

int n, numSCC, t;
vector<vector<int> > adj(50000);
int visitado[50000];
int low[50000];
int padre[50000];
set<tuple<int, int> > bridges;

void bridgesAux(int);

void bridgesTarjan(){
  int i;

  for(i = 0; i < n; i++)
    low[i] = visitado[i] = padre[i] =-1;

  for(i = 0; i < n; i++)
    if(visitado[i] == -1)
      bridgesAux(i);
}

void bridgesAux(int v){
  int w;
  visitado[v] = low[v] = ++t;

  for(int i = 0; i < adj[v].size(); i++){
    w = adj[v][i];
    if(visitado[w] == -1){
      padre[w] = v;
      bridgesAux(w);
      low[v] = min(low[v], low[w]);

      //verificar si es un puente
      if(low[w] > visitado[v])
	bridges.insert(make_pair(v, w));
    }
    else if(w != padre[v])
      low[v] = min(low[v], visitado[w]);
  }
}

int main(){
  int m, i, aux1, aux2;

  cin >> n >> m;

  for(i = 0; i < m; i++){
    cin >> aux1 >> aux2;
    adj[aux1].push_back(aux2);
    adj[aux2].push_back(aux1);
  }

  bridgesTarjan();

  if(bridges.size() == 0)
    cout << "El grafo no tiene puentes" << endl;
  else{
    cout << "Total de Puentes: " << bridges.size() << endl;
    for(set<tuple<int, int> >::iterator it = bridges.begin(); it !=  bridges.end(); ++it)
      cout << " (" << it->first << ", " << it->second << ")";
    cout << endl;
  }
  
  return 0;
}
