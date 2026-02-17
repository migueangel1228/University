from sys import stdin

"""
    AGRA  Tarea 6
Fecha  : 22/11/25
Nombre : Miguel Angel Padilla Rosero
Cod    : 8988878
Problem C  preinpos.py

Complejidad computacional "Big-O":

Función generatePosOrder:

Recorre el árbol recursivamente visitando cada nodo una vez.
En cada llamada recursiva:

Búsqueda del indice de la raiz en inOrder: O(n).
División de strings y llamadas recursivas para subárboles.

Complejidad global:
    Tiempo: O(n log n) en el caso promedio (árbol balanceado):
        Porque hay O(log n) niveles en un árbol balanceado
        En cada nivel hacemos trabajo O(n) total
        Complejidad total: O(n) x O(log n) = O(n log n)
  
    Espacio: O(n) para la pila de recursión y strings temporales
"""

# PreOrder: root [izquierdo] [derecho]
# InOrder: [izquierdo] root [derecho]
# PosOrder [izquierda] [derecha] root

def generatePosOrder(preOrder, inOrder):
    # Caso base: un solo nodo( es su propio root)
    if len(preOrder) <= 1:
        return preOrder
    else:
        # El primer elemento del preOrder es la raíz
        root = preOrder[0]
        
        # Encontrar la posicion de la raíz en el inOrder
        rootIdx = 0
        for i in range(len(inOrder)):
            if inOrder[i] == root:
                rootIdx = i
        
        # Dividir izquierda de derecha
        # InOrder
        leftInorder = inOrder[:rootIdx]
        rightInorder = inOrder[rootIdx + 1:]
        
        # PreOrder
        tamanoIzq = len(leftInorder)
        leftPreorder = preOrder[1:1 + tamanoIzq]
        rightPreorder = preOrder[1 + tamanoIzq:]
        
        ramaIzq = generatePosOrder(leftPreorder, leftInorder)
        ramaDer = generatePosOrder(rightPreorder, rightInorder)
        
        # PosOrder [izquierda] [derecha] root
        return ''.join([ramaIzq, ramaDer, root]) 

def main():
    casos = int(stdin.readline())
    for i in range(casos):
        entrada = stdin.readline().split()
        sPreOrder = entrada[1]
        sInOrder = entrada[2]
        
        resultado = generatePosOrder(sPreOrder, sInOrder)
        print(resultado)
        
    
main()


"""
Sample Input
3
3 xYz Yxz
3 abc cba
6 ABCDEF CBAEDF
Sample Output
Yzx
cba
CBEFDA
"""

"""
Sample Input
1
9 ABDECFHIG DBEAHFICG
Sample Output
DEBHIFGCA
"""

"""
Sample Input
1
9 ABDCEGFHI DBAEGCHFI
Sample Output
DBGEHIFCA
"""