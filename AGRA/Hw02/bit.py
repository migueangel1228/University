from sys import stdin

"""
AGRA   : Tarea 1 Enero 2025
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
A - Problem A - bit.cpp

Complejidad programa,

La complejidad temporal del programa en el peor caso es: [ O(n^2 \log n) ]

donde n es el tamaño de la matriz (asumiendo una matriz de tamaño n x n).
"""


def BtoD(matriz, ansList, inicioFila, inicioColumna, filasMatriz, columnasMatriz):
    result = ""
    base = matriz[inicioFila][inicioColumna]
    uniforme = True
    
    # revisa si es el caso base
    i = inicioFila
    while i < inicioFila + filasMatriz and uniforme:
        j = inicioColumna
        while j < inicioColumna + columnasMatriz and uniforme:
            if matriz[i][j] != base:
                uniforme = False
            j += 1
        i += 1
    # caso base
    if uniforme:
        result = base
    else:
            # Casos no bases
        result = "D"
        
            # Caso sub-matriz fila
        if filasMatriz == 1 and columnasMatriz > 1:
            left_cols = columnasMatriz // 2 + (columnasMatriz % 2)
            right_cols = columnasMatriz - left_cols
            
            result += BtoD(matriz, ansList, inicioFila, inicioColumna, 1, left_cols)
            result += BtoD(matriz, ansList, inicioFila, inicioColumna + left_cols, 1, right_cols)
            
            # Caso sub-matriz columna
        elif columnasMatriz == 1 and filasMatriz > 1:
            top_rows = filasMatriz // 2 + (filasMatriz % 2)
            bottom_rows = filasMatriz - top_rows
            
            result += BtoD(matriz, ansList, inicioFila, inicioColumna, top_rows, 1)
            result += BtoD(matriz, ansList, inicioFila + top_rows, inicioColumna, bottom_rows, 1)
            
            # Caso sub-matriz matriz
        else:
            top_rows = filasMatriz // 2 + (filasMatriz % 2)
            bottom_rows = filasMatriz - top_rows
            left_cols = columnasMatriz // 2 + (columnasMatriz % 2)
            right_cols = columnasMatriz - left_cols
            

            result += BtoD(matriz, ansList, inicioFila, inicioColumna, top_rows, left_cols)
            result += BtoD(matriz, ansList, inicioFila, inicioColumna + left_cols, top_rows, right_cols)
            result += BtoD(matriz, ansList, inicioFila + top_rows, inicioColumna, bottom_rows, left_cols)
            result += BtoD(matriz, ansList, inicioFila + top_rows, inicioColumna + left_cols, bottom_rows, right_cols)
    return result

def DtoB(matriz, inicioFila, inicioColumna, filasMatriz, columnasMatriz, DatoStr, indice):
    nuevoIndice = indice
    current_char = DatoStr[nuevoIndice]
    nuevoIndice += 1
    if current_char != "D":
        for i in range(inicioFila, inicioFila + filasMatriz):
            for j in range(inicioColumna, inicioColumna + columnasMatriz):
                matriz[i][j] = current_char
    else:
        if filasMatriz == 1 and columnasMatriz > 1:
            columnaIzq = columnasMatriz // 2 + (columnasMatriz % 2)
            columnaDer = columnasMatriz - columnaIzq
            nuevoIndice = DtoB(matriz, inicioFila, inicioColumna, 1, columnaIzq, DatoStr, nuevoIndice)
            nuevoIndice = DtoB(matriz, inicioFila, inicioColumna + columnaIzq, 1, columnaDer, DatoStr, nuevoIndice)
        elif columnasMatriz == 1 and filasMatriz > 1:
            top_rows = filasMatriz // 2 + (filasMatriz % 2)
            bottom_rows = filasMatriz - top_rows
            nuevoIndice = DtoB(matriz, inicioFila, inicioColumna, top_rows, 1, DatoStr, nuevoIndice)
            nuevoIndice = DtoB(matriz, inicioFila + top_rows, inicioColumna, bottom_rows, 1, DatoStr, nuevoIndice)
        else:
            top_rows = filasMatriz // 2 + (filasMatriz % 2)
            bottom_rows = filasMatriz - top_rows
            columnaIzq = columnasMatriz // 2 + (columnasMatriz % 2)
            columnaDer = columnasMatriz - columnaIzq
            nuevoIndice = DtoB(matriz, inicioFila, inicioColumna, top_rows, columnaIzq, DatoStr, nuevoIndice)
            nuevoIndice = DtoB(matriz, inicioFila, inicioColumna + columnaIzq, top_rows, columnaDer, DatoStr, nuevoIndice)
            nuevoIndice = DtoB(matriz, inicioFila + top_rows, inicioColumna, bottom_rows, columnaIzq, DatoStr, nuevoIndice)
            nuevoIndice = DtoB(matriz, inicioFila + top_rows, inicioColumna + columnaIzq, bottom_rows, columnaDer, DatoStr, nuevoIndice)
    return nuevoIndice

def main():
    lineas = stdin.read().splitlines()
    lineasSalida = []
    indiceLinea = 0
    while indiceLinea < len(lineas) and lineas[indiceLinea].strip() != "#":
        head = lineas[indiceLinea].strip()
        indiceLinea += 1
        partes = head.split()
        tipoConversion = partes[0]
        numFilas = int(partes[1])
        numColumnas = int(partes[2])
        representacion = ""
        
        if tipoConversion == "B":
            longitudEsperada = numFilas * numColumnas
            while indiceLinea < len(lineas) and len(representacion) < longitudEsperada:
                if " " not in lineas[indiceLinea]:
                    representacion += lineas[indiceLinea].strip()
                indiceLinea += 1
        else:
            while indiceLinea < len(lineas) and (" " not in lineas[indiceLinea]) and lineas[indiceLinea].strip() != "#":
                representacion += lineas[indiceLinea].strip()
                indiceLinea += 1
        if tipoConversion == "B":
            matriz = []
            for fila in range(numFilas):
                matriz.append(list(representacion[fila * numColumnas:(fila + 1) * numColumnas]))
            resultadoConversion = BtoD(matriz, [], 0, 0, numFilas, numColumnas)
            tipoSalida = "D"
        else:
            matriz = []
            for k in range(numFilas):
                matriz.append([""] * numColumnas)
            k = DtoB(matriz, 0, 0, numFilas, numColumnas, representacion, 0)
            resultadoConversion = ""
            for fila in matriz:
                resultadoConversion += "".join(fila)
            tipoSalida = "B"
            
        lineasSalida.append(f"{tipoSalida}{numFilas:4d}{numColumnas:4d}")
        indiceConversion = 0
        while indiceConversion < len(resultadoConversion):
            lineasSalida.append(resultadoConversion[indiceConversion:indiceConversion+50])
            indiceConversion += 50
    for lineaSalida in lineasSalida:
        print(lineaSalida)

main()

