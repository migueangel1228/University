/*
Algoritmo de Fuerza Bruta para Puentes con DFS
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
set<tuple<int, int> > bridges;

bool ccDFSAux(int u, int ocu1, int ocu2){
  int w;
  visitado[u] = true;

  if(u == ocu2)
    return true;
  
  for(int i = 0; i < adj[u].size(); i++){
    w = adj[u][i];

    if(!(u == ocu1 && w == ocu2) && !(u == ocu2 && w == ocu1))
      if(!visitado[w] && ccDFSAux(w, ocu1, ocu2))
	return true;
  }

  return false;
}

void bridgesBruteForce(){
  int i, j, k;
  bool res;

  for(i = 0; i < n; i++){
    for(j = 0; j < adj[i].size(); j++){
      for(k = 0; k < n; k++)
	visitado[k] = false;

      res = ccDFSAux(i, i, adj[i][j]);

      if(!res)
	bridges.insert(make_pair(min(i, adj[i][j]), max(i, adj[i][j])));
    }
  }
}

int main(){
  int m, i, j, aux1, aux2;

  cin >> n >> m;

  for(i = 0; i < m; i++){
    cin >> aux1 >> aux2;
    adj[aux1].push_back(aux2);
  }
  
  bridgesBruteForce();

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
