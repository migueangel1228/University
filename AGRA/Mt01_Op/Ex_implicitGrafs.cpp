/*
Grafos Implícitos
24 de Febrero de 2025
Árboles y Grafos





Mi código implementa un BFS en una cuadrícula (matriz A[][]), buscando la menor cantidad de movimientos 
desde una posición inicial (rSim, cSim) hasta una posición objetivo (rCaf, cCaf), evitando obstáculos.

Esto es un grafo implícito, pero está diseñado para una matriz 2D con movimientos 
en cuatro direcciones (arriba, derecha, abajo, izquierda). Sin embargo, el problema de Zlatan 
no es una cuadrícula (2D),sino un espacio 4D donde cada número de cuatro cifras representa un nodo y 
cada cambio de dígito es una arista.

¿Qué debes cambiar?
Mi código no resuelve el problema de Zlatan porque:

Trabaja en una matriz 2D (A[r][c]), mientras que el problema necesita una representación 
en un espacio de estados 4D. Los movimientos no son correctos, porque en lugar de moverte en una cuadrícula, 
debes modificar los dígitos de un número de 4 cifras.
El BFS debe operar en strings/números, no en coordenadas r, c.
*/

#include <cstdio>
#include <cstdlib>
#include <queue>

using namespace std;

struct tripleta{
  int r, c, p;
};

int n, m;
int A[1005][1005];
//bool vis[1005][1005];
int dr[] = {-1, 0, 1, 0};  // arriba, derecha, abajo, izquierda
int dc[] = {0, 1, 0, -1};

int bfs(int r, int c, int rCaf, int cCaf){
  int ans = -1, i, nr, nc;
  queue<tripleta> q;
  tripleta aux;
  q.push({r, c, 0});
  //vis[r][c] = true;
  A[r][c] = -1;

  while(!q.empty()){
    aux = q.front();
    q.pop();

    if(aux.r == rCaf && aux.c == cCaf){
      ans = aux.p;
    }
    else{
      for(i = 0; i < 4; ++i){
	nr = aux.r + dr[i];
	nc = aux.c + dc[i];
	if(nr >= 0 && nr < n && nc >= 0 && nc < m && A[nr][nc] != -1 && A[nr][nc] != 2){
	  q.push({nr, nc, aux.p + 1});
	  //vis[nr][nc] = true;
	  A[nr][nc] = -1;
	}
      }
    }
  }

  return ans;
}


int main(){
  int i, j, rSim, cSim, rCaf, cCaf;

  while(scanf("%d %d", &n, &m) != EOF){
    rSim = cSim = rCaf = cCaf = -1;
    for(i = 0; i < n; ++i){
      for(j = 0; j < m; ++j){
	scanf("%d", &A[i][j]);
	if(A[i][j] == 1){
	  rSim = i;
	  cSim = j;
	}
	if(A[i][j] == 3){
	  rCaf = i;
	  cCaf = j;
	}
      }
    }

    int res = bfs(rSim, cSim, rCaf, cCaf);
    if(res != -1)
      printf("El simio encontrará el cafecito sagrado en %d pasos.\n", res);
    else
      printf("El simio morirá de abstinencia\n");
  }

  return 0;
}