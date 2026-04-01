"""
Tarea  : ADA  Tarea 3
Fecha  : 30 Marzo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem B - Making Change
"""

from sys import stdin


INF = float('inf')
MONEDAS = [5, 10, 20, 50, 100, 200] 
LIMITE = 1000


# recibe un precio con formato "d.cc" y lo convierte a unidades de 5 centavos
def parsing(precio):
    entero, decimal = precio.split('.')
    centavos = int(entero) * 100 + int(decimal)
    return centavos


# tabla de cambio del cajero construida con estrategia greedy
def cambioCajero():
    greedy = [INF] * (LIMITE + 1)
    greedy[0] = 0

    for monto in range(1, LIMITE + 1):
        restante = monto
        monedasUsadas = 0

        for moneda in reversed(MONEDAS):
            if restante == 0:
                break

            cantidad = restante // moneda
            monedasUsadas += cantidad
            restante -= cantidad * moneda

        if restante == 0:
            greedy[monto] = monedasUsadas

    return greedy


# dp acotado con memoización para las monedas reales de la billetera
def solution(cantidades, compra, dpCambio):
    memo = {}

    def dp(indice, montoRestante):
        if montoRestante == 0:
            return 0

        if indice == len(MONEDAS):
            return INF

        clave = (indice, montoRestante)
        if clave in memo:
            return memo[clave]

        moneda = MONEDAS[indice]
        mejor = INF
        limite = min(cantidades[indice], montoRestante // moneda)

        for usadas in range(limite + 1):
            costo = dp(indice + 1, montoRestante - usadas * moneda)
            if costo != INF:
                mejor = min(mejor, costo + usadas)

        memo[clave] = mejor
        return mejor

    ans = INF
    for pago in range(compra, LIMITE + 1):
        monedasCliente = dp(0, pago)
        if monedasCliente != INF:
            ans = min(ans, monedasCliente + dpCambio[pago - compra])

    return int(ans)


def main():
    dpCambio = cambioCajero()
    caso = stdin.readline().strip()
    
    while (caso != "0 0 0 0 0 0"):
        datos = caso.split()
        monedasDisponibles = list(map(int, datos[:-1]))
        valorCompra = parsing(datos[-1])
        
        result = solution(monedasDisponibles, valorCompra, dpCambio)
        print(result)
        
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
