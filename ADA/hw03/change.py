"""
Tarea  : ADA  Tarea 3
Fecha  : 30 Marzo 2026
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878

Problem B - Making Change
"""

from sys import stdin


INF = float("inf")
# monedas en formato 5 centavos, cada unidad equivale a 5 centavos
MONEDAS = [1, 2, 4, 10, 20, 40]
MAX_PAGO = 200


# recibe un precio dolar.centimo y lo convierte a unidades de 5 centavos
def parsing(precio):
    entero, decimal = precio.split('.')
    centavos = int(entero) * 100 + int(decimal)
    return centavos // 5


# tabla de cambio de cajero
def cambioCajero(limite):
    ans = [INF] * (limite + 1)
    ans[0] = 0

    for monto in range(1, limite + 1):
        restante = monto
        monedasUsadas = 0

        for indice in range(len(MONEDAS) - 1, -1, -1):
            moneda = MONEDAS[indice]
            cantidad = restante // moneda
            monedasUsadas += cantidad
            restante -= cantidad * moneda

        if restante == 0:
            ans[monto] = monedasUsadas

    return ans


# mInimo numero de monedas que el cliente necesita para juntar ese pago
def dpMemoCliente(indice, montoRestante, cantidades, memo):
    if montoRestante == 0:
        ans = 0
    elif indice == len(MONEDAS):
        ans = INF
    else:
        clave = (indice, montoRestante)
        if clave in memo:
            ans = memo[clave]
        else:
            moneda = MONEDAS[indice]
            mejor = INF
            limite = min(cantidades[indice], montoRestante // moneda)

            for usadas in range(limite + 1):
                costo = dpMemoCliente(indice + 1, montoRestante - usadas * moneda, cantidades, memo)
                if costo != INF:
                    mejor = min(mejor, costo + usadas)

            memo[clave] = mejor
            ans = mejor

    return ans


# def dpTabCliente(montoObjetivo, cantidades):
#     n = len(MONEDAS)
#     dp = [[INF] * (montoObjetivo + 1) for _ in range(n + 1)]
#     dp[0][0] = 0

#     for i in range(1, n + 1):
#         moneda = MONEDAS[i - 1]
#         disponibles = cantidades[i - 1]

#         for monto in range(montoObjetivo + 1):
#             mejor = dp[i - 1][monto]
#             limite = min(disponibles, monto // moneda)

#             for usadas in range(1, limite + 1):
#                 anterior = dp[i - 1][monto - usadas * moneda]
#                 if anterior != INF:
#                     mejor = min(mejor, anterior + usadas)

#             dp[i][monto] = mejor

#     return dp[n][montoObjetivo]


def dpTabClienteTodos(limite, cantidades):
    dp = [INF] * (limite + 1)
    dp[0] = 0

    for i in range(len(MONEDAS)):
        moneda = MONEDAS[i]
        disponibles = min(cantidades[i], limite // moneda)

        for _ in range(disponibles):
            for monto in range(limite, moneda - 1, -1):
                previo = dp[monto - moneda]
                if previo + 1 < dp[monto]:
                    dp[monto] = previo + 1

    return dp


def solution(cantidades, compra, arrCambio):
    ans = INF
    totalCliente = 0
    for i in range(len(MONEDAS)):
        totalCliente += cantidades[i] * MONEDAS[i]

    limite = min(totalCliente, MAX_PAGO)
    dpCliente = dpTabClienteTodos(limite, cantidades)

    for pago in range(compra, limite + 1):
        monedasCliente = dpCliente[pago]
        if monedasCliente != INF:
            ans = min(ans, monedasCliente + arrCambio[pago - compra])

    if ans == INF:
        resultado = -1
    else:
        resultado = int(ans)

    return resultado


def main():
    caso = stdin.readline().strip()
    arrCambio = cambioCajero(MAX_PAGO)
    
    while (caso != "0 0 0 0 0 0"):
        datos = caso.split()
        monedasDisponibles = list(map(int, datos[:-1]))
        valorCompra = parsing(datos[-1])
        result = solution(monedasDisponibles, valorCompra, arrCambio)
        
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
