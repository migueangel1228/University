/*
Implementacion Algoritmo de Prim para MST
Autor: Carlos Ramirez
Fecha: Abril 30 de 2020

Se representan los grafos a traves de listas de adyacencia.

*/

#include <climits>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int n, total;
vector<vector<pair<int, int> > > adj(50000);
vector<int> d(50000);
vector<int> p(50000);

void prim(int s){
  priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > cola;
  vector<bool> visitado(n, false);
  int i, u, v, peso, pesoAux;

  for(i = 0; i < n; ++i){
    d[i] = INT_MAX;
    p[i] = -1;
  }

  total = 0;
  d[s] = 0;
  cola.push(make_pair(0, s));

  while(!cola.empty()){
    u = cola.top().second;
    peso = cola.top().first;
    visitado[u] = true;
    cola.pop();

    if(peso == d[u]){
      total += peso;
      for(i = 0; i < adj[u].size(); ++i){
	v = adj[u][i].first;
	pesoAux = adj[u][i].second;

	if(!visitado[v] && pesoAux < d[v]){
	  p[v] = u;
	  d[v] = pesoAux;
	  cola.push(make_pair(d[v], v));
	}
      }
    }
  }
}

int main(){
  int m, i, aux1, aux2, peso;

  cin >> n >> m;

  for(i = 0; i < m; i++){
    cin >> aux1 >> aux2 >> peso;
    adj[aux1].push_back(make_pair(aux2, peso));
    adj[aux2].push_back(make_pair(aux1, peso));
  }

  prim(0);

  cout << "El peso del arbol de recubrimiento minimo es " << total << endl;
  cout << "Aristas:" << endl;

  for(i = 0; i < n; ++i)
    if(p[i] != -1)
      cout << "(" << p[i] << ", " << i << ")" << endl;
  
  return 0;
}
