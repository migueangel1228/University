/*
AGRA  Tarea 1 Agosto 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem C  snowflakes.py

Complejidad:
*/
#include <bits/stdc++.h>

using namespace std;

bool solve(int N, queue<int> colaExpected){
  queue<int> colaInicial;
  stack<int> pila;
  int auxNum, ElementoExpected;

  for (int i = 1; i <= N; i++){
      colaInicial.push(i);
  }
  bool flag = true, ans = true;

  ElementoExpected = colaExpected.front();
  colaExpected.pop();
  
  while (flag){
    if (pila.empty() && colaInicial.empty()){
      flag = false;
    }
    else if (!colaInicial.empty() && (ElementoExpected == colaInicial.front())){
      colaInicial.pop();
      ElementoExpected = colaExpected.front();
      colaExpected.pop();
    }
    else if (!pila.empty() && ElementoExpected == pila.top()){
      pila.pop();
      ElementoExpected = colaExpected.front();
      colaExpected.pop();
    }
    else if (!colaInicial.empty()){
      auxNum = colaInicial.front();
      colaInicial.pop();
      pila.push(auxNum);
    }
    else {
      flag = false;
      ans = false;
    }
  }
  return ans;
}

int main() {
  int N, auxNum, tamanoCase;
  bool Salida = false, cambioCase = true;
  
  while (!Salida){
    cin >> N;
    if (N == 0 && cambioCase)
      Salida = true;
      
    else if(N == 0 && !cambioCase){
      cambioCase = true;
      cout << endl;
    }
      
    else if(N != 0 && cambioCase){ // new Case
      tamanoCase = N;
      cambioCase = false;
    }
    else if(N != 0 && !cambioCase){ // result Case
      stack<int> pila;
      queue<int> colaExpected;
      bool ans;

      colaExpected.push(N);
  
      for (int i = 0 ; i < tamanoCase - 1; i++){
        cin >> auxNum;
          colaExpected.push(auxNum);
      }
      ans = solve(tamanoCase, colaExpected);
  
      if (ans) cout << "Yes" << endl;
      else     cout << "No"  << endl;
    }
  }
  return 0;
}
/*
5
1 2 3 4 5
5 4 1 2 3
0
6
6 5 4 3 2 1
0
0
*/