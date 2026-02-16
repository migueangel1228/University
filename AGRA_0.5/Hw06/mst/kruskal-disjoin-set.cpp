/*
Implementacion Algoritmo de Kruskal para MST con Disjoint Set Union
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

//operaciones disjoint set union
//**************************************
int padre[50000], rango[50000];

void makeSet(int v){
  padre[v] = v;
  rango[v] = 0;
}

int findSet(int v){
  if(v == padre[v])
    return v;
  else{
    padre[v] = findSet(padre[v]);
    return padre[v];
  }
}

void unionSet(int u, int v){
  u = findSet(u);
  v = findSet(v);

  if(u != v){
    if(rango[u] < rango[v])
      swap(u, v);
    
    padre[v] = u;
    if(rango[u] == rango[v])
      rango[u]++;
  }
}
//****************************************

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
vector<Arista> mst;

void kruskal(){
  int i, u, v, p1, p2;
  
  for(i = 0; i < n; ++i)
    makeSet(i);

  sort(aristas.begin(), aristas.end());

  for(vector<Arista>::iterator it = aristas.begin(); it != aristas.end(); ++it){
    u = it->u;
    v = it->v;

    if(findSet(u) != findSet(v)){
      mst.push_back(*it);
      total += it->peso;
      unionSet(u, v);
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
