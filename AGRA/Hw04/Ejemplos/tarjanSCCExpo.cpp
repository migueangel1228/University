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

  for(i = 0; i < n; i++){              // visitados -1
    sccInd[i] = visitado[i] = -1;      
    enPila[i] = false;                 // Todos Nodos en la pila en false
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
  for(size_t i = 0; i < adj[v].size(); i++) {
    w = adj[v][i];
    if(visitado[w] == -1) {
        tarjanAux(w);
        if(sccInd[v] < sccInd[w]) {
            sccInd[v] = sccInd[v];
        } else {
            sccInd[v] = sccInd[w];
        }
    }
    else if(enPila[w]) {
        if(sccInd[v] < sccInd[w]) {
            sccInd[v] = sccInd[v];
        } else {
            sccInd[v] = sccInd[w];
        }
    }
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

/*
Ejemplo Input
10 15
0 1
1 2
2 3
3 2
4 0
1 4
4 5
5 6
6 5
2 6
3 7
6 7
7 8
8 6
8 9

0 -> A
1 -> B
2 -> C
3 -> D
4 -> E
5 -> F
6 -> G
7 -> H
8 -> I
9 -> J

Expected Output
SCC con indice 1: 9 
SCC con indice 2: 4 1 0
SCC con indice 3: 2 3 
SCC con indice 4: 5 6 8
*/