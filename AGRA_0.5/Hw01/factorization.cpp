#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <stack>

using namespace std;

/*

AGRA  Tarea 1 Enero 2025
Nombre : Miguel Angel Padilla 
Cod    : 8988878
Problem C - Factorization - 10858
*/


// Funcion para obtener los factores de un numero mayores o iguales a un valor inicial
vector<int> obtenerFactores(int n, int inicio){
    set<int> factoresSet; // Usamos un set para mantener los factores ordenados
    if (n >= inicio) {
        factoresSet.insert(n); 
    }
    for (int i = 2; i <= sqrt(n); i++){
        if (n % i == 0) {
            if (i >= inicio) {
                factoresSet.insert(i); // Incluimos el factor i
            }
            int complemento = n / i;
            if (complemento >= inicio){
                factoresSet.insert(complemento); // Incluimos el factor complementario
            }
        }
    }
    // Convertimos el set a un vector para devolverlo
    vector<int> factores(factoresSet.begin(), factoresSet.end());
    return factores;
}

void procesarEntrada(){
    int numero;
    cin >> numero; 
    while (numero != 0){

        if (numero == 1){
            cout << "0\n"; 
        }
        else{
            vector<vector<int>> resultados; // almacena todas las factorizaciones


            stack<int> pilaInicio; // Pila para el: valor inicial de los factores
            stack<int> pilaResto;  // Pila para el: valor restante a factorizar

            stack<vector<int>> pilaActual; // Pila para el: factores acumulados

            // Inicializamos las pilas con el estado inicial
            pilaInicio.push(2);
            pilaResto.push(numero);
            pilaActual.push(vector<int>());

            while (!pilaInicio.empty()){
                int inicioActual = pilaInicio.top();
                int restoActual = pilaResto.top();
                vector<int> actual = pilaActual.top();

                // sacamos el estado actual de las pilas
                pilaInicio.pop();
                pilaResto.pop();
                pilaActual.pop();

                if (restoActual == 1){
                    // si el resto es 1 y hay al menos 2 factores,guardamos la factorizacion

                    if (actual.size() >= 2){
                        resultados.push_back(actual);
                    }
                } else {
                    vector<int> factores = obtenerFactores(restoActual, inicioActual);
                    for (vector<int>::reverse_iterator it = factores.rbegin(); it != factores.rend(); ++it){
                        int factor = *it;
                        vector<int> nuevoActual = actual;
                        nuevoActual.push_back(factor);          // agregamos el factor a la lista actual
                        pilaInicio.push(factor);               // actualizamos el inicio para el próximo factor
                        pilaResto.push(restoActual / factor);  // actualizamos el resto
                        pilaActual.push(nuevoActual);           // guardamos el nuevo estado en la pila
                    }
                }
            }
// printeamos
            cout << resultados.size() << "\n";

            for (vector<vector<int>>::iterator resIt = resultados.begin(); resIt != resultados.end(); ++resIt){

                for (vector<int>::iterator numIt = resIt->begin(); numIt != resIt->end(); ++numIt){
                    if (numIt != resIt->begin()){
                        cout << " ";
                    }
                    cout << *numIt;
                }
                cout << "\n";
            }
        }
        cin >> numero;
    }
}

int main() {
    procesarEntrada();
    return 0;
}