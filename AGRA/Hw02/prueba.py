from sys import stdin

def main():
    textoEntrada = stdin.read()
    if textoEntrada != "":
        lineas = textoEntrada.splitlines()
    else:
        lineas = []
    indice = 0
    totalLineas = len(lineas)
    
    while indice < totalLineas:
        lineaActual = lineas[indice].strip()
        # Flag que indica si se procesara el caso
        casoValido = True  
        if lineaActual == "":
            # Si la linea está vacia, simplemente se incrementa el indice
            indice = indice + 1
        else:
            tokens = lineaActual.split()
            if len(tokens) == 1:
                numeroPares = int(tokens[0])
                if (indice + 1) < totalLineas and lineas[indice + 1].strip() != "":
                    fila0 = list(map(int, lineas[indice + 1].split()))
                else:
                    casoValido = False
                if (indice + 2) < totalLineas and lineas[indice + 2].strip() != "":
                    fila1 = list(map(int, lineas[indice + 2].split()))
                else:
                    casoValido = False
                indice = indice + 3
            else:
                fila0 = list(map(int, tokens))
                if (indice + 1) < totalLineas and lineas[indice + 1].strip() != "":
                    fila1 = list(map(int, lineas[indice + 1].split()))
                else:
                    casoValido = False
                numeroPares = len(fila0)
                indice = indice + 2
            
            if casoValido:
                # Construir el diccionario de ocurrencias: peso -> lista de (fila, posición)
                ocurrencias = {}
                filaIndice = 0
                while filaIndice < 2:
                    if filaIndice == 0:
                        fila = fila0
                    else:
                        fila = fila1
                    pos = 0
                    tamFila = len(fila)
                    while pos < tamFila:
                        peso = fila[pos]
                        if peso not in ocurrencias:
                            ocurrencias[peso] = []
                        ocurrencias[peso].append((filaIndice, pos))
                        pos = pos + 1
                    filaIndice = filaIndice + 1

                # Para cada fila se determina si se requiere mover alguna pesa (pares no consecutivos)
                necesitaMovimiento = [False, False]
                costoExtra = [float('inf'), float('inf')]
                paresDivididos = []
                for peso in ocurrencias:
                    listaOcurrencias = ocurrencias[peso]
                    if len(listaOcurrencias) == 2:
                        filaA = listaOcurrencias[0][0]
                        posA = listaOcurrencias[0][1]
                        filaB = listaOcurrencias[1][0]
                        posB = listaOcurrencias[1][1]
                        if filaA == filaB:
                            if abs(posA - posB) != 1:
                                necesitaMovimiento[filaA] = True
                                if peso < costoExtra[filaA]:
                                    costoExtra[filaA] = peso
                        else:
                            paresDivididos.append(peso)
                paresDivididos.sort()
                
                # Calcular el costo para liberar cada fila (costoGap)
                costoGap = 0
                if (not necesitaMovimiento[0]) and (not necesitaMovimiento[1]):
                    costoGap = 0
                elif necesitaMovimiento[0] and (not necesitaMovimiento[1]):
                    if len(paresDivididos) > 0:
                        if paresDivididos[0] < costoExtra[0]:
                            costoGap = paresDivididos[0]
                        else:
                            costoGap = costoExtra[0]
                    else:
                        costoGap = costoExtra[0]
                elif necesitaMovimiento[1] and (not necesitaMovimiento[0]):
                    if len(paresDivididos) > 0:
                        if paresDivididos[0] < costoExtra[1]:
                            costoGap = paresDivididos[0]
                        else:
                            costoGap = costoExtra[1]
                    else:
                        costoGap = costoExtra[1]
                else:
                    if len(paresDivididos) >= 2:
                        a = paresDivididos[0]
                        b = paresDivididos[1]
                        if a > costoExtra[1]:
                            opcion1 = a
                        else:
                            opcion1 = costoExtra[1]
                        if costoExtra[0] > b:
                            opcion2 = costoExtra[0]
                        else:
                            opcion2 = b
                        if opcion1 < opcion2:
                            costoGap = opcion1
                        else:
                            costoGap = opcion2
                    elif len(paresDivididos) == 1:
                        if paresDivididos[0] > costoExtra[1]:
                            opcion1 = paresDivididos[0]
                        else:
                            opcion1 = costoExtra[1]
                        if costoExtra[0] > paresDivididos[0]:
                            opcion2 = costoExtra[0]
                        else:
                            opcion2 = paresDivididos[0]
                        if opcion1 < opcion2:
                            costoGap = opcion1
                        else:
                            costoGap = opcion2
                    else:
                        if costoExtra[0] > costoExtra[1]:
                            costoGap = costoExtra[0]
                        else:
                            costoGap = costoExtra[1]
                
                # Cada par dividido implica mover una pesa; se toma el mayor de ellos
                costoMaximoParDividido = 0
                if len(paresDivididos) > 0:
                    costoMaximoParDividido = paresDivididos[len(paresDivididos) - 1]
                if costoMaximoParDividido > costoGap:
                    costoFinal = costoMaximoParDividido
                else:
                    costoFinal = costoGap
                
                print(costoFinal)

main()
