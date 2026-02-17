#include <iostream>
#include <vector>
#include <deque>
#include <set>
#include <sstream>

using namespace std;

/*

AGRA  Tarea 1, Febrero 2025
Nombre    : Miguel Angel Padilla Rosero 
Cod       : 8988878
Problem C - 10-20-30 - 246
*/

struct Estado {
    deque<int> baraja;
    vector<deque<int>> pilas;
};

string convertirEstadoToString(const Estado& estado) {
    string resultado;

    // agregar cartas de la baraja
    for (int i = 0; i < estado.baraja.size(); i = i + 1) 
        resultado += to_string(estado.baraja[i]) + ";";

    resultado += ":"; // separador entre la baraja y las stacks

    // sgregar cartas de las  pilas
    for (int i = 0; i < estado.pilas.size(); i = i + 1) {
        for (int j = 0; j < estado.pilas[i].size(); j = j + 1) 
            resultado += to_string(estado.pilas[i][j]) + ";";

        resultado += "."; // difenciador entre pilas
    }

    return resultado;
}


vector<int> buscarCombinaciones(deque<int>& stack) {
    vector<int> combinacion;
    if (stack.size() < 3){
    }
    // Caso 1 (primeros dos y ultimo)
    else if (   stack[0] + stack[1] + stack.back() == 10 ||
                stack[0] + stack[1] + stack.back() == 20 ||
                stack[0] + stack[1] + stack.back() == 30) {
        combinacion = {stack[0], stack[1], stack.back()};
        stack.pop_front();
        stack.pop_front();
        stack.pop_back();
    }

    // Caso 2 (primero y ultimos dos)
    else if (   stack[0] + stack[stack.size()-2] + stack.back() == 10 ||
                stack[0] + stack[stack.size()-2] + stack.back() == 20 ||
                stack[0] + stack[stack.size()-2] + stack.back() == 30) {
        combinacion = {stack[0], stack[stack.size()-2], stack.back()};
        stack.pop_front();
        stack.pop_back();
        stack.pop_back();
    }

    // Caso 3 (ultimos tres)
    else if (   stack[stack.size()-3] + stack[stack.size()-2] + stack.back() == 10 ||
                stack[stack.size()-3] + stack[stack.size()-2] + stack.back() == 20 ||
                stack[stack.size()-3] + stack[stack.size()-2] + stack.back() == 30) {
        combinacion = {stack[stack.size()-3], stack[stack.size()-2], stack.back()};
        stack.pop_back();
        stack.pop_back();
        stack.pop_back();
    }

    return combinacion;
}

void procesarJuego(vector<int> imput) {
    Estado estado;
    estado.baraja.assign(imput.begin(), imput.end());
    estado.pilas.resize(7);

    for (int i = 0; i < 7; ++i) {
        estado.pilas[i].push_back(estado.baraja.front());
        estado.baraja.pop_front();
    }

    int movimientos = 7;
    int pilaActual = 0;
    set<string> estadosVistos;
    string estadoInicial = convertirEstadoToString(estado);
    estadosVistos.insert(estadoInicial);

    bool juegoTerminado = false;
    string resultado;

    while (!juegoTerminado) {
        // Buscar siguiente pila no vacía
        int stackSiguiente = -1;
        bool stackEncontrada = false;

        for (int i = 0; i < 7 && !stackEncontrada; ++i) {
            int indice = (pilaActual + i) % 7;
            if (!estado.pilas[indice].empty()) {
                stackSiguiente = indice;
                stackEncontrada = true;
            }
        }

        // Verificar victoria
        if (stackSiguiente == -1) {
            resultado = "Win : " + to_string(movimientos);
            juegoTerminado = true;
        } 
        // Verificar si no hay cartas para repartir
        else if (estado.baraja.empty()) {
            resultado = "Loss: " + to_string(movimientos);
            juegoTerminado = true;
        } 
        // Continuar el juego si no se ha terminado
        else {
            // Repartir carta
            int carta = estado.baraja.front();
            estado.baraja.pop_front();
            estado.pilas[stackSiguiente].push_back(carta);
            ++movimientos;

            // Procesar combinaciones
            bool cambio = true;
            while (cambio) {
                cambio = false;
                vector<int> combinacion = buscarCombinaciones(estado.pilas[stackSiguiente]);
                if (!combinacion.empty()) {
                    for (int c : combinacion) estado.baraja.push_back(c);
                    cambio = true;
                }
            }

            // Verificar empate
            string estadoActual = convertirEstadoToString(estado);
            if (estadosVistos.count(estadoActual)) {
                resultado = "Draw: " + to_string(movimientos);
                juegoTerminado = true;
            } else {
                estadosVistos.insert(estadoActual);
                pilaActual = (stackSiguiente + 1) % 7;
            }
        }
    }

    cout << resultado << endl;
}

int main() {
    vector<int> baraja;
    int carta;
    while (cin >> carta && carta != 0) {
        baraja.push_back(carta);
        if (baraja.size() == 52) {
            procesarJuego(baraja);
            baraja.clear();
        }
    }
    return 0;
}