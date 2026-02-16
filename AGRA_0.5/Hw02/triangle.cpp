/*
AGRA   : Tarea 1 Enero 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
B - Problem B triangle

Complejidad 

La complejidad temporal del programa es: [ O(log n) ] 
donde n es el tamano del lado del triangulo 'AB'  

*/

#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

double calcularRelacion(double AB, double AD) {
    double r = AD / AB; // Relacion de lados
    double areaADE = r * r; // Relacion de (ADE / ABC)
    double areaBDEC = 1.0 - areaADE; // Area de BDEC / ABC

    return areaADE / areaBDEC; // RelaciOn de ADE / BDEC
}

// Funcion para encontrar AD con biseccion
double encontrarAD(double AB, double ratio) {
    double limiteInferior = 0.0, limiteSuperior = AB, puntoMedio = 0.0;

    while (limiteSuperior - limiteInferior > 0.00000000001) {
        double puntoMedio = (limiteInferior + limiteSuperior) / 2.0; // Punto medio
        double relacionActual = calcularRelacion(AB, puntoMedio); // calculamos la relacion

        if (relacionActual < ratio) {
            limiteInferior = puntoMedio; // AD esta en la mitad superior
        } 
        else {
            limiteSuperior = puntoMedio; // AD esta en la mitad inferior
        }
    }
    puntoMedio = (limiteInferior + limiteSuperior) / 2.0;

    return (puntoMedio); 
}

int main() {
    int casos;
    cin >> casos; 
    for (int casoActual = 1; casoActual <= casos; ++casoActual) {
        double AB, AC, BC, ratio;
        cin >> AB >> AC >> BC >> ratio; 
        double AD = encontrarAD(AB, ratio); // Encontramos AD
        
        // Imprimimos el resultado

        if (casoActual != casos )
            printf("Case %d: %.6f\n", casoActual, AD);
        else {
            printf("Case %d: %.6f", casoActual, AD);
        }
    }
    return 0;
}