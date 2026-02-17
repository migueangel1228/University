#include <climits>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

//operaciones disjoint set union
//**************************************
int p[15], rango[15];

void makeSet(int v){
  p[v] = v;
  rango[v] = 0;
}

int findSet(int v){
  if(v == p[v])
    return v;
  else{
    p[v] = findSet(p[v]);
    return p[v];
  }
}

void unionSet(int u, int v){
  u = findSet(u);
  v = findSet(v);

  if(u != v){
    if(rango[u] < rango[v])
      swap(u, v);
    
    p[v] = u;
    if(rango[u] == rango[v])
      rango[u]++;
  }
}
//****************************************

int main(){
  int m, i, aux;

  for(i = 1; i <= 12; i++)
    makeSet(i);

  cout << "Valores p:" << endl;
  for(i = 1; i <= 12; i++)
    cout << p[i] << " ";
  cout << endl;

  cout << "Valores rango:" << endl;
  for(i = 1; i <= 12; i++)
    cout << rango[i] << " ";
  cout << endl;

  unionSet(4, 5);

  cout << endl << "Despues de unir 4 y 5" << endl;
  cout << "Valores p:" << endl;
  for(i = 1; i <= 12; i++)
    cout << p[i] << " ";
  cout << endl;

  cout << "Valores rango:" << endl;
  for(i = 1; i <= 12; i++)
    cout << rango[i] << " ";
  cout << endl;

  unionSet(6, 8);

  cout << endl << "Despues de unir 6 y 8" << endl;
  cout << "Valores p:" << endl;
  for(i = 1; i <= 12; i++)
    cout << p[i] << " ";
  cout << endl;

  cout << "Valores rango:" << endl;
  for(i = 1; i <= 12; i++)
    cout << rango[i] << " ";
  cout << endl;
  
  unionSet(1, 12);

  cout << endl << "Despues de unir 1 y 12" << endl;
  cout << "Valores p:" << endl;
  for(i = 1; i <= 12; i++)
    cout << p[i] << " ";
  cout << endl;

  cout << "Valores rango:" << endl;
  for(i = 1; i <= 12; i++)
    cout << rango[i] << " ";
  cout << endl;
  
  unionSet(5, 1);

  cout << endl << "Despues de unir 5 y 1" << endl;
  cout << "Valores p:" << endl;
  for(i = 1; i <= 12; i++)
    cout << p[i] << " ";
  cout << endl;

  cout << "Valores rango:" << endl;
  for(i = 1; i <= 12; i++)
    cout << rango[i] << " ";
  cout << endl;

  aux = findSet(12);
  cout << 12 << " pertenece al conjunto con id " << aux << endl;

  cout << "Despues de comprimir el camino de 12" << endl;
  cout << "Valores p:" << endl;
  for(i = 1; i <= 12; i++)
    cout << p[i] << " ";
  cout << endl;

  cout << "Valores rango:" << endl;
  for(i = 1; i <= 12; i++)
    cout << rango[i] << " ";
  cout << endl;

  unionSet(10, 8);

  cout << endl << "Despues de unir 10 y 8" << endl;
  cout << "Valores p:" << endl;
  for(i = 1; i <= 12; i++)
    cout << p[i] << " ";
  cout << endl;

  cout << "Valores rango:" << endl;
  for(i = 1; i <= 12; i++)
    cout << rango[i] << " ";
  cout << endl;
  
  unionSet(2, 6);

  cout << endl << "Despues de unir 2 y 6" << endl;
  cout << "Valores p:" << endl;
  for(i = 1; i <= 12; i++)
    cout << p[i] << " ";
  cout << endl;

  cout << "Valores rango:" << endl;
  for(i = 1; i <= 12; i++)
    cout << rango[i] << " ";
  cout << endl << endl;

  aux = findSet(10);
  cout << "10 pertenece al conjunto con id " << aux << endl << endl;

  cout << "Despues de comprimir el camino de 10" << endl;
  cout << "Valores p:" << endl;
  for(i = 1; i <= 12; i++)
    cout << p[i] << " ";
  cout << endl;

  cout << "Valores rango:" << endl;
  for(i = 1; i <= 12; i++)
    cout << rango[i] << " ";
  cout << endl << endl;

  unionSet(10, 1);

  cout << "Despues de unir 10 y 1" << endl;
  cout << "Valores p:" << endl;
  for(i = 1; i <= 12; i++)
    cout << p[i] << " ";
  cout << endl;

  cout << "Valores rango:" << endl;
  for(i = 1; i <= 12; i++)
    cout << rango[i] << " ";
  cout << endl << endl;

  aux = findSet(8);
  cout << "8 pertenece al conjunto con id " << aux << endl << endl;

  cout << "Despues de comprimir el camino de 8" << endl;
  cout << "Valores p:" << endl;
  for(i = 1; i <= 12; i++)
    cout << p[i] << " ";
  cout << endl;

  cout << "Valores rango:" << endl;
  for(i = 1; i <= 12; i++)
    cout << rango[i] << " ";
  cout << endl << endl;
  
  return 0;
}
