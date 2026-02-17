/*
Nickname: Mianparito
Date:     9/1/26
Topic:    "Binary Search"

https://onlinejudge.org/external/107/10706.pdf

Estrategia:
1. La secuencia es: 1 12 123 1234 12345...
2. Precalcular longitudes acumuladas de cada bloque
3. Usar búsqueda binaria para encontrar el bloque donde está el i-ésimo dígito
4. Dentro del bloque, encontrar el número específico
*/

#include <bits/stdc++.h>

using namespace std;

const int MAXN = 31300; // suficiente para cubrir i <= 2^31-1
long long cumSum[MAXN];  // suma acumulada total de dígitos hasta el bloque k
long long cumLen[MAXN];  // longitud acumulada del bloque k (ej: bloque 3 = "123" tiene 3 dígitos)

// calcula cuántos dígitos tiene un número n
int countDigits(int n){
    int count = 0;
    bool terminado = false;
    
    if(n == 0){
        count = 1;
        terminado = true;
    }
    
    while(!terminado){
        if(n == 0){
            terminado = true;
        }
        else{
            count++;
            n = n / 10;
        }
    }
    
    return count;
}

// precalcula las longitudes acumuladas
void precalculate(){
    cumLen[0] = 0;
    cumSum[0] = 0;
    bool overflow = false;
    
    for(int k = 1; k < MAXN && !overflow; k++){
        cumLen[k] = cumLen[k-1] + countDigits(k);
        cumSum[k] = cumSum[k-1] + cumLen[k];
        
        if(cumSum[k] > 2147483647LL){
            overflow = true;
        }
    }
}

// encuentra el dígito en la posición pos del número n (1-indexed)
int getDigit(int n, int pos){
    string s = to_string(n);
    return s[pos-1] - '0';
}

int solve(long long i){
    // encontrar en qué bloque k está el i-ésimo dígito
    int k = lower_bound(cumSum, cumSum + MAXN, i) - cumSum;
    
    // encontrar la posición dentro del bloque k
    long long posInBlock = i - cumSum[k-1];
    
    // encontrar en qué número dentro del bloque está
    int num = lower_bound(cumLen, cumLen + k + 1, posInBlock) - cumLen;
    
    // encontrar el dígito específico dentro del número
    long long posInNum = posInBlock - cumLen[num-1];
    
    return getDigit(num, posInNum);
}

int main(){
    precalculate();
    
    int cases;
    cin >> cases;

    while(cases--){
        long long i;
        cin >> i;
        cout << solve(i) << endl;
    }
    
    return 0;
}

/*
Sample Input
2
8
3

Sample Output
2
2
*/