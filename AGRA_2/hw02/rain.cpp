/*
AGRA  Tarea 22 Agosto 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem A  rain.cpp

Complejidad:
Biseccion:
  Tiempo: O(1) por que siempre son ≈ 60–70 iteraciones debido a EPS = 1e-9.
  Espacio: O(1)

Complejidad global:
  Tiempo: O(1)
  Espacio: O(1)
*/

#include <bits/stdc++.h>

using namespace std;

double EPS = 1e-9;

double aux(double L, double R, double K, double T1, double T2){
    double ans = L + (R - K) * (T1 - (L/R)) - (K * T2);// ;)
    return ans;
}

tuple <double,double> biseccion(double L,double K,double T1,double T2,double H, bool casoInferiorLeak){
    tuple <double,double> ans;
    double left = 0, right = 10000000000; // ejemplo borachin, razonablemente grande 
    double midPosibleR;
    if (casoInferiorLeak) {
        get<0>(ans) = H;
        get<1>(ans) = H;
    }
    else{
        get<0>(ans) = H; // i have FE, only in the case H = L
        while (right - left > EPS){
            midPosibleR = (left + right) / 2;
            double result = aux(L,midPosibleR,K, T1, T2);

            if (result > H) right = midPosibleR;
            else left = midPosibleR;
        }
        get<1>(ans) = midPosibleR;
    }
    return ans;
}
int main(){
    double cases;
    cin >> cases;

    for (double i = 0; i < cases; i++){
        double L,K,T1,T2,H;
        cin >> L >> K >> T1 >> T2 >> H;
        bool casoInferiorLeak = false, casoEqualLeak = false;
        if (H < L) casoInferiorLeak = true;
        else if (H == L) casoEqualLeak = true;
        tuple <double,double> ans; // < Minima altura, Maxima altura>
        ans = biseccion(L,K,T1,T2,H,casoInferiorLeak);

        if (casoInferiorLeak) printf("%.4f %.4f\n", get<0>(ans), get<1>(ans));
        
        else if (casoEqualLeak = false) printf("%.4f %.4f\n", get<1>(ans) * T1, get<1>(ans) * T1);

        else printf("%.4f %.4f\n", get<0>(ans), get<1>(ans) * T1);
    
    }
    return 0;
}
/*
L is where the leak is (mm)
K is the rate at which water leaks (mm/h)
T1 is the duration of the rainfall (h)
T2 is the time between the end of the rainfall and the observation of the water level (h)
H is the water level in the tube when we observe it (mm)
*/
/*
Sample Input
2
80.00 0.50 2.00 1.50 80.00
150.00 1.00 100.00 150.00 100.00
*/
/*
Sample Output
80.000000 80.759403
100.000000 100.000000
*/