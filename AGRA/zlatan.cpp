#include<bits/stdc++.h>
#include<iostream>

using namespace std;

/*
Preguntar tuki punto D
Prefuntar la vulet de krustal y Prim , que monido monda cuando mondo mndea
*/
/*
Center Python:
"""
Radio y centro arbol n-ario representacion listas de adyacencia
Autor: Carlos Ramirez
Fecha: Septiembre 14 de 2023

"""

from sys import stdin
from collections import deque

distMax, nodoMax = None, None

def dfsAux(v, p, dist):
  global distMax, nodoMax
  dist += 1
  if dist > distMax: distMax, nodoMax = dist, v
  for w in  G[v]:
    if w != p:
      dfsAux(w, v, dist)

def diameter():
  global distMax
  distMax = 0

  #se escoge arbitrariamente iniciar en el nodo 0
  #el resultado seria el mismo asi se inicie en un nodo diferente
  dfsAux(0, -1, -1)
  dfsAux(nodoMax, -1, -1)
  return distMax

def radio():
  diam = diameter()
  ans = (diam + 1) // 2
  return ans

def center():
  nivelMax = 0
  nivel = [0 for _ in range(len(G))]
  grado = [len(G[v]) for v in range(len(G))]
  queue = deque()
  nodosCentro = set()

  for i in range(len(G)):
    if grado[i] == 1:
      queue.append(i)

  while len(queue) > 0:
   v = queue.popleft()
   for w in G[v]:
     grado[w] -= 1
     if grado[w] == 1:
       queue.append(w)
       nivel[w] = nivel[v] + 1
       nivelMax = max(nivelMax, nivel[w])
  for i in range(len(G)):
    if nivel[i] == nivelMax:
      nodosCentro.add(i)

  radio = nivelMax + 1 if len(nodosCentro) == 2 else  nivelMax
  if len(nodosCentro) == 2: diametro = 2 * radio - 1
  else: diametro = 2 * radio

  return radio, diametro, nodosCentro
*/

unordered_set<int> centers(vector<vector<pair<int,int>>> &G){
    unordered_set<int> centers;
    int nivelMax = 0;
    int n = G.size();
    vector<int> nivel(n,0);
    vector<int> grado(n,0);
    queue<int> colita;
    // iniciar monda
    cout << "carenalga" << endl;

    for (int i = 0; i < n; i++){
        nivel[i] = 0;
        grado[i] = G[i].size();
    }
    cout << "carenalga1" << endl;

    // iniciar colita
    for (int i = 0; i < n; i++){
        if (grado[i] == 1){
            colita.push(i);
        }
    }
    cout << "carenalga2" << endl;

    // super colita
    while (!colita.empty()){
        int v = colita.front();
        colita.pop();
        for (int w = 0; w < G[v].size(); w++){
            int node;
            node = G[v][w].first;
            nivel[w] = nivel[v] + 1;
            if (nivelMax < nivel[w]){
                nivelMax = nivel[w];
            }
        }
        for (int i = 0; i < n ; i++){
            if(nivel[i] == nivelMax);
            centers.insert(i);
        }
    }
    cout << "carenalga3" << endl;


    return centers;
}

int main(){
    int casitos;

    cin >> casitos;
    cout << "carenalga" << endl;
    while (casitos--){
        cout << "wh" << endl;

        int n, m;
        cin >> n >> m;
        cout << "n m" << endl;

        vector<vector<pair<int,int>>> G(n + 1);
        int node1, node2, weight;
        
        cout << "n1 n2" << endl;

        for(int i = 0; i < m; i++){
            cin >> node1 >> node2 >> weight;
            cout << "entro linea" << endl;

            G[node1].push_back({node2,weight});
            G[node2].push_back({node1, weight});
        }
        cout << "antes de centers" << endl;

        unordered_set<int> res = centers(G);
        cout << "despues de calcular centers" << endl;

        for (int x : res) cout << " sdfasdf" << x;
                cout << "bucle output" << endl;

        cout << "\n";
        
    }
    return 0;
}

/*
1
1 2
*/