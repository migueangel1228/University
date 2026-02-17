/*
Implementacion Algoritmo de Kruskal para MST
Autor: Carlos Ramirez
Fecha: Abril 30 de 2020

Dado que el algoritmo de kruskal trabaja explicitamente con las aristas del
grafo resulta muy conveniente representar el grafo mediante una lista de aristas.

*/

#include <climits>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

struct Arista{
  int u, v, peso;

  Arista(){}

  Arista(int x, int y, int p){
    u = x;
    v = y;
    peso = p;
  }

  bool operator<(Arista& a){
    return peso < a.peso;
  }
};

int n, total;
vector<Arista> aristas;
vector<int> idArbol(50000);
vector<Arista> mst;

void kruskal(){
  int i, u, v, p1, p2;
  
  for(i = 0; i < n; ++i)
    idArbol[i] = i;

  sort(aristas.begin(), aristas.end());

  for(vector<Arista>::iterator it = aristas.begin(); it != aristas.end(); ++it){
    u = it->u;
    v = it->v;

    if(idArbol[u] != idArbol[v]){
      mst.push_back(*it);
      total += it->peso;

      p1 = idArbol[u];
      p2 = idArbol[v];
      for(i = 0; i < n; ++i)
	if(idArbol[i] == p2)
	  idArbol[i] = p1;
    }
  }
}

int main(){
  int m, i, aux1, aux2, peso;

  cin >> n >> m;

  for(i = 0; i < m; i++){
    cin >> aux1 >> aux2 >> peso;
    aristas.push_back(Arista(aux1, aux2, peso));
  }

  kruskal();

  cout << "El peso del arbol de recubrimiento minimo es " << total << endl;
  cout << "Aristas:" << endl;

  for(i = 0; i < mst.size(); ++i)
    cout << "(" << mst[i].u << ", " << mst[i].v << ")" << endl;
  
  return 0;
}
