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

void ccDFSAux(int v, int ocu1, int ocu2){
  int w;
  visitado[v] = true;
  
  for(int i = 0; i < adj[v].size(); i++){
    w = adj[v][i];
    if(!(v == ocu1 && w == ocu2) && !(v == ocu2 && w == ocu1)){
      if(!visitado[w])
	ccDFSAux(w, ocu1, ocu2);
    }
  }
}

int ccDFS(int ocu1, int ocu2){
  int i, total = 0;

  for(i = 0; i < n; i++){
    if(!visitado[i]){
      total++;
      ccDFSAux(i, ocu1, ocu2);
    }
  }

  return total;
}

void bridgesBruteForce(){
  int i, j, k, p, q;

  for(j = 0; j < n; j++)
    visitado[j] = false;
  p = ccDFS(-1, -1);

  for(i = 0; i < n; i++){
    for(j = 0; j < adj[i].size(); j++){
      for(k = 0; k < n; k++)
	visitado[k] = false;
      q = ccDFS(i, adj[i][j]);

      if(q > p)
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
