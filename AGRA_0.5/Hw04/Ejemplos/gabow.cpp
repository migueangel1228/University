/*
Algoritmo de Gabow (SCC)
Autor: Carlos Ramirez
Fecha: Marzo 23 de 2020

 */

#include <vector>
#include <stack>
#include <iostream>

using namespace std;

int n, numSCC, t;
vector<vector<int> > adj(50000);
int visitado[50000];
int sccInd[50000];
stack<int> pilaS, pilaP;

void gabowAux(int);

void gabow(){
  int i;

  for(i = 0; i < n; i++)
    sccInd[i] = visitado[i] = -1;

  for(i = 0; i < n; i++)
    if(visitado[i] == -1)
      gabowAux(i);
}

void gabowAux(int v){
  int w;
  visitado[v] = ++t;
  pilaS.push(v);
  pilaP.push(v);
  
  for(int i = 0; i < adj[v].size(); i++){
    w = adj[v][i];
    if(visitado[w] == -1)
      gabowAux(w);
    else if(sccInd[w] == -1){
      while(visitado[pilaP.top()] > visitado[w])
	pilaP.pop();
    }
  }

  if(v == pilaP.top()){
    numSCC++;
    cout << "SCC con indice " << numSCC << ": ";
    while(pilaS.top() != v){
      cout << pilaS.top() << " ";
      sccInd[pilaS.top()] = numSCC - 1;
      pilaS.pop();
    }

    cout << pilaS.top() << endl;
    sccInd[pilaS.top()] = numSCC - 1;
    pilaS.pop();
    pilaP.pop();
  }
}

int main(){
  int m, i, aux1, aux2;

  cin >> n >> m;

  for(i = 0; i < m; i++){
    cin >> aux1 >> aux2;
    adj[aux1].push_back(aux2);
  }

  gabow();
  
  return 0;
}
