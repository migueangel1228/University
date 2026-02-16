/*
Implementacion Algoritmo Bellman-Ford para SSSP
Autor: Carlos Ramirez
Fecha: Abril 24 de 2020

*/

#include <climits>
#include <vector>
#include <iostream>

using namespace std;

int n;
vector<vector<pair<int, int> > > adj(500);
vector<int> p(500);
vector<int> d(500);

bool bellmanFord(int s){
  int i, j, u, v, peso;
  bool ans = true;

  for(i = 0; i < n; ++i){
    p[i] = -1;
    d[i] = INT_MAX;
  }

  d[s] = 0;
  for(i = 1; i <= n; ++i){
    for(v = 0; v < n; v++){
      for(j = 0; j < adj[v].size(); ++j){
	u = adj[v][j].first;
	peso = adj[v][j].second;
	if(d[u] != INT_MAX && d[u] > d[v] + peso){
	  d[u] = d[v] + peso;
	  p[u] = v;
	}
      }
    }
  }

  u = 0;
  while(ans && u < n){
    i = 0;
    while(ans && i < adj[u].size()){
      v = adj[u][i].first;
      peso = adj[u][i].second;
      if(d[v] > d[u] + peso)
	ans = false;
      i += 1;
    }
    u += 1;
  }

  return ans;
}

int main(){
  int m, i, aux1, aux2, peso;

  cin >> n >> m;

  for(i = 0; i < m; i++){
    cin >> aux1 >> aux2 >> peso;
    adj[aux1].push_back(make_pair(aux2, peso));
  }

  if(bellmanFord(0)){
    for(i = 0; i < n; ++i)
      cout << "Distancia a nodo " << i << ": " << d[i] << endl;

    for(i = 0; i < n; ++i)
      cout << "Predecesor nodo " << i << ": " << p[i] << endl;
  }
  else
    cout << "El grafo tiene ciclos negativos" << endl;
  
  return 0;
}
