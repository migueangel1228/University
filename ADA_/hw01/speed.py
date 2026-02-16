"""
Tarea  : ADA  Tarea 1 
Fecha  : 1 Enero 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem B - Business Center
"""
from sys import stdin

def calculoTiempo(dis,vel,c):
    n = len(dis)
    cnt = 0
    for i in range(n):
        # Si velocidad efectiva es menor a 0, no tiene sentido por que no existe un tiemmpo negativo
        # (Dado que la distancia simpre es positiva)
        if ( vel[i] + c <= 0):
            cnt =  float('inf')  
        else:
            cnt += dis[i] / (vel[i] + c)
    return cnt

def solve(dis,vel,t):
    # Definir rango inicial (-infinito a 0 o 0 a infinito)
    timeOriginal = calculoTiempo(dis, vel, 0)
    if timeOriginal > t:
        low = 0
        high = 1e6
    else:
        low = -1e9
        high = 0
        
    while (high - low > 1e-12):
        mid = (high + low) / 2
        aux = calculoTiempo(dis,vel,mid)
        if (aux < t):
            high = mid
        else:
            low = mid
    return mid
        
def main():
    for line in stdin:
        imput = list(map(int,line.split()))
        n, t = imput
        distancias = []
        velocidades = []
        for i in range(n):
            di, vi = list(map(int,stdin.readline().split()))
            distancias.append(di)
            velocidades.append(vi)
        
        ans = solve(distancias,velocidades,t)
        print(f"{ans:.9f}")

    
main()

"""
Sample Input
3 5
4 -1
4 0
10 3
4 10
5 3
2 2
3 6
3 1
Sample Output
3.0000
-0.5086
"""
"""
Caso de prueba positivo(invent)
Sample Input
4 13
8 -2
6 -2
10 1
12 -1
Sample Output
4
"""