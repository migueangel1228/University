from collections import deque
import sys

def convertToCuatroDigitos(numero):
    """
    Convierte un numero entero en una cadena de 4 digitos,
    agregando ceros a la izquierda si es necesario(8->0008)
    """
    strResult = str(numero)
    while len(strResult) < 4: 
        strResult = "0" + strResult
    return strResult

def generarPosibilidades(numero):
    """
    Genera y retorna un conjunto de los posibles movimientes a partir de un numero.
    Para cada digit se crean dos posibilidades; una con el digito incrementado y
    otro con el digito decrementado, ambos de forma ciclica (de 9 a 0 y viceversa)
    """
    cadenaNum = convertToCuatroDigitos(numero)
    conjuntoPosibilidades = set()
    
    for indice in range(4):
        digitoActual = int(cadenaNum[indice])
        
        # Incrementar el digito (si es 9 pasa a 0)
        nuevoDigit = (digitoActual + 1) % 10
        newStr = cadenaNum[0:indice] + str(nuevoDigit) + cadenaNum[indice +1:]
        conjuntoPosibilidades.add(int(newStr))
        
        # Decrementar el digito (si es 0 pasa a 9)
        nuevoDigit = (digitoActual - 1) % 10
        newStr = cadenaNum[0:indice] + str(nuevoDigit) + cadenaNum[indice +1:]
        conjuntoPosibilidades.add(int(newStr))
    
    return conjuntoPosibilidades

def bfs(inicio, target, listaForbiddenn):
    """
    Realiza una busqueda en amplitud (BFS) en el espacio de numeros de 4 digitos.
    Retorna el numero minimo de movimientos para transformar 'inicio' en 'objetivo'
    sin pasar por ningun numero prohibido. Si no existe camino, retorna -1.
    """
    resultado = -1
    forbiddenSet = set(listaForbiddenn)
    
    if inicio == target:
        resultado = 0
    elif inicio not in forbiddenSet and target not in forbiddenSet:
        visitados = set()
        visitados.add(inicio)
        cola = deque()
        cola.append((inicio, 0))
        encontrado = False
        
        while len(cola) > 0 and not encontrado:
            posicionActual, pasosActuales = cola.popleft()
            posibilidadesSet = generarPosibilidades(posicionActual)
            for posibilidad in posibilidadesSet:
                if posibilidad == target:
                    resultado = pasosActuales + 1
                    encontrado = True
                elif posibilidad not in forbiddenSet and posibilidad not in visitados:
                    visitados.add(posibilidad)
                    cola.append((posibilidad, pasosActuales + 1))

    return resultado

def main():
    """
    lee la entrada, procesa cada caso de prueba y escribe
    el resultado en la salida estándar.
    """
    # Lee la entrada
    datosEntrada = sys.stdin.read().split()
    puntero = 0
    
    cases = int(datosEntrada[puntero])
    puntero = puntero + 1
    
    for _ in range(cases):
        strInicial = ""
        for _ in range(4):
            strInicial = strInicial + datosEntrada[puntero]
            puntero = puntero + 1
        numeroInicial = int(strInicial)
        
        cadenaObjetivo = ""
        for _ in range(4):
            cadenaObjetivo = cadenaObjetivo + datosEntrada[puntero]
            puntero = puntero + 1
        numeroObjetivo = int(cadenaObjetivo)
        
        forbiddenNum = int(datosEntrada[puntero])
        puntero = puntero + 1
        
        listaForbiddenn = []
        for i in range(forbiddenNum):
            strForbiddenn = ""
            for j in range(4):
                strForbiddenn = strForbiddenn + datosEntrada[puntero]
                puntero = puntero + 1
            listaForbiddenn.append(int(strForbiddenn))
        
        resultado = bfs(numeroInicial, numeroObjetivo, listaForbiddenn)
        
        if resultado != -1:
            print(str(resultado))
        else:
            print(-1)

main()
