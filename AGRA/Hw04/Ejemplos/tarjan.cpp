/*
Algoritmo de Tarjan (SCC)
Autor: Carlos Ramirez
Fecha: Marzo 23 de 2020

El vaciado de la pila en el procedimiento tarjanAux permite imprimir
los elementos de los diferentes SCC.
 */

#include <vector>
#include <stack>
#include <iostream>

using namespace std;

int n, numSCC, t;
vector<vector<int> > adj(50000);
int visitado[50000];
int sccInd[50000];
bool enPila[50000];
stack<int> pila;

void tarjanAux(int);

void tarjan(){
  int i;

  for(i = 0; i < n; i++){
    sccInd[i] = visitado[i] = -1;
    enPila[i] = false;
  }

  for(i = 0; i < n; i++)
    if(visitado[i] == -1)
      tarjanAux(i);
}

void tarjanAux(int v){
  int w;
  visitado[v] = sccInd[v] = ++t;
  pila.push(v);
  enPila[v] = true;

  for(int i = 0; i < adj[v].size(); i++){
    w = adj[v][i];
    if(visitado[w] == -1){
      tarjanAux(w);
      sccInd[v] = sccInd[v] < sccInd[w] ? sccInd[v] : sccInd[w];
    }
    else if(enPila[w])
      sccInd[v] = sccInd[v] < sccInd[w] ? sccInd[v] : sccInd[w];
  }

  if(sccInd[v] == visitado[v]){
    cout << "SCC con indice " << sccInd[v] << ": ";
    while(pila.top() != v){
      cout << pila.top() << " ";
      enPila[pila.top()] = false;
      pila.pop();
    }

    cout << pila.top() << endl;
    enPila[pila.top()] = false;
    pila.pop();
  }
}

int main(){
  int m, i, aux1, aux2;

  cin >> n >> m;

  for(i = 0; i < m; i++){
    cin >> aux1 >> aux2;
    adj[aux1].push_back(aux2);
  }

  tarjan();
  
  return 0;
}
