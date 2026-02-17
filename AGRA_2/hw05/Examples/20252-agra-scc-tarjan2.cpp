/*
Algoritmo de Tarjan (SCC)
Autor: Carlos Ramirez
Fecha: Marzo 23 de 2020

El vaciado de la pila en el procedimiento tarjanAux permite agregar
los elementos de los diferentes SCC.
 */

#include <vector>
#include <stack>
#include <iostream>

using namespace std;

int n, numSCC, t;
vector<vector<int> > adj(50000);
int visitado[50000];
int low[50000]; // low
bool enPila[50000];
stack<int> pila;
vector<vector<int> > sccNodos;

void tarjanAux(int);

void tarjan(){
  int i;

  for(i = 0; i < n; i++){
    low[i] = visitado[i] = -1;
    enPila[i] = false;
  }

  for(i = 0; i < n; i++)
    if(visitado[i] == -1)
      tarjanAux(i);
}

void tarjanAux(int v){
  int w;
  visitado[v] = low[v] = ++t;
  pila.push(v);
  enPila[v] = true;

  for(int i = 0; i < adj[v].size(); i++){
    w = adj[v][i];
    if(visitado[w] == -1){
      tarjanAux(w);
      low[v] = min(low[v], low[w]);
    }
    else if(enPila[w])
      low[v] = min(low[v], visitado[w]);
  }

  if(low[v] == visitado[v]){
    cout << "SCC con indice " << low[v] << ": ";
    sccNodos.push_back(vector<int>());
    numSCC++;
    while(pila.top() != v){
      cout << pila.top() << " ";
      enPila[pila.top()] = false;
      sccNodos[numSCC - 1].push_back(pila.top());
      pila.pop();
    }

    cout << pila.top() << endl;
    enPila[pila.top()] = false;
    sccNodos[numSCC - 1].push_back(pila.top());
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
