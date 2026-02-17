#include <vector>
#include <map>
#include <string>
#include <cstdio>
#include <iostream>

using namespace std;

int n;
int adj[1000][1000];
bool visitados[1000];
int p[1000];


void dfsAux(int u){
  int i;
  visitados[u] = true;
  printf("%d\n", u);

  for(i = 0; i < n; ++i){
    if(adj[u][i] == 1)
      if(!visitados[i]){
	//p[i] = u;
	dfsAux(i);
      }
  }
}

void dfs(){
  int i;

  //fill(visitados, visitados + n, false);
  for(i = 0; i < n; ++i){
    visitados[i] = false;
    //p[i] = -1;
  }

  for(i = 0; i < n; ++i){
    if(!visitados[i])
      dfsAux(i);
  }
}


int main(){
  int m, u, v, i, j;
  cin >> n >> m;

  for(i = 0; i < n; ++i){
    cin >> u;
    for(j = 0; j < u; ++j){
      cin >> v;
      adj[i][v] = 1;
    }
  }

  cout << "Grafo" << endl;

  for(i = 0; i < n; ++i){
    for(j = 0; j < n; ++j)
      cout << adj[i][j] << " ";
    cout << endl;
  }


  cout << "DFS" << endl;
  dfs();

  for(i = 0; i < n; ++i)
    cout << p[i] << " ";
  cout << endl;
  
  return 0;
}
