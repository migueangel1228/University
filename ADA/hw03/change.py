"""
Tarea  : ADA  Tarea 3
Fecha  : 30 Marzo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem B - Making Change
"""

from sys import stdin


INF = float('inf')
MONEDAS = [1, 2, 4, 10, 20, 40]  # valores en unidades de 5 centavos
LIMITE = 200


# recibe un precio con formato "d.cc" y lo convierte a unidades de 5 centavos
def parsing(precio):
    entero, decimal = precio.split('.')
    centavos = int(entero) * 100 + int(decimal)
    return centavos // 5


# dp ilimitado para el cambio que puede entregar el cajero
def cambioCajero():
    dp = [INF] * (LIMITE + 1)
    dp[0] = 0

    for moneda in MONEDAS:
        for monto in range(moneda, LIMITE + 1):
            dp[monto] = min(dp[monto], dp[monto - moneda] + 1)

    return dp


# dp acotado con las monedas reales de la billetera
def solution(cantidades, compra, dpCambio):
    dpCliente = [INF] * (LIMITE + 1)
    dpCliente[0] = 0

    for i in range(6):
        moneda = MONEDAS[i]

        for _ in range(cantidades[i]):
            for monto in range(LIMITE, moneda - 1, -1):
                dpCliente[monto] = min(dpCliente[monto], dpCliente[monto - moneda] + 1)

    ans = INF
    for pago in range(compra, LIMITE + 1):
        if (dpCliente[pago] != INF):
            ans = min(ans, dpCliente[pago] + dpCambio[pago - compra])

    return int(ans)


def main():
    dpCambio = cambioCajero()
    caso = stdin.readline().strip()
    
    while (caso != "0 0 0 0 0 0"):
        datos = caso.split()
        monedasDisponibles = list(map(int, datos[:-1]))
        valorCompra = parsing(datos[-1])
        
        result = solution(monedasDisponibles, valorCompra, dpCambio)
        print(f"{result:3d}")
        
        caso = stdin.readline().strip()


main()

"""
Sample Input
2 4 2 2 1 0 0.95
2 4 2 0 1 0 0.55
0 0 0 0 0 0
Sample Output
  2
  3
"""
