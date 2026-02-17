"""
Segment Tree Implementation
Carlos Ramírez
Noviembre 7 de 2020

Update with lazy propagation
Adding on segments, range max query (RMQ)

"""

from sys import stdin

#Segment tree is represented as a list

#build the segment tree max
def buildMax(a, v, l, r,tree):
  if l == r: tree[v] = a[l]
  else:
    m = l + ((r - l) >> 1)
    buildMax(a, v + 1, l, m,tree)
    buildMax(a, v + 2 * (m - l + 1), m + 1, r,tree)
    tree[v] = max(tree[v + 1], tree[v + 2 * (m - l + 1)])

#build the segment tree min
def buildMin(a, v, l, r, tree):
    if l == r:
        tree[v] = a[l]
    else:
        m = l + ((r - l) >> 1)
        buildMin(a, v + 1, l,m,tree)
        buildMin(a,v + 2 * (m - l + 1), m + 1, r,tree)
        tree[v] = min(tree[v + 1], tree[v + 2 * (m - l + 1)])
        
#query max
def queryMax(v, L, R, l, r, tree, pend):
  ans = None
  if l > r: ans = float('-inf')
  elif l == L and r == R: ans = tree[v]
  else:
    m = L + ((R - L) >> 1)
    push(v, v + 1, v + 2 * (m - L + 1), tree, pend)
    ans = max(queryMax(v + 1, L, m, l, min(r, m), tree, pend), queryMax(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r, tree, pend))
  return ans

#query min
def queryMin(v, L, R, l, r, tree, pend):
  ans = None
  if l > r: ans = float('inf')
  elif l == L and r == R: ans = tree[v]
  else:
    m = L + ((R - L) >> 1)
    push(v, v + 1, v + 2 * (m - L + 1), tree, pend)
    ans = min(queryMin(v + 1, L, m, l, min(r, m), tree, pend), queryMin(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r, tree, pend))
  return ans


#update query max
def updateMax(v, L, R,
              l, r, h, tree, pend):
  if l <= r:
    if l == L and r == R: tree[v] += h ; pend[v] += h
    else:
      m = L + ((R - L) >> 1)
      push(v, v + 1, v + 2 * (m - L + 1), tree, pend)
      updateMax(v + 1, L, m, l, min(r, m), h, tree, pend)
      updateMax(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r, h, tree, pend)
      tree[v] = max(tree[v + 1], tree[v + 2 * (m - L + 1)])
      
#update query min
def updateMin(v, L, R, l, r, h, tree, pend):
  if l <= r:
    if l == L and r == R: tree[v] += h ; pend[v] += h
    else:
      m = L + ((R - L) >> 1)
      push(v, v + 1, v + 2 * (m - L + 1), tree, pend)
      updateMin(v + 1, L, m, l, min(r, m), h, tree, pend)
      updateMin(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r, h, tree, pend)
      tree[v] = min(tree[v + 1], tree[v + 2 * (m - L + 1)])

def push(v, v1, v2, tree, pend):
  tree[v1] += pend[v]
  pend[v1] += pend[v]
  tree[v2] += pend[v]
  pend[v2] += pend[v]
  pend[v] = 0
            
def arregloCircular(arr, x):
    """
    Genera un arreglo circular agregando los ultimos x-1 elementos al inicio
    y los primeros x-1 elementos al final
    """
    n = len(arr)
    result = []
    
    if x > 1 and n > 0:
        elementsAgregar = x - 1
        ultimos = n - elementsAgregar
        inicio = elementsAgregar
        
        # Agregar los ultimos x-1 elementos al inicio
        result.extend(arr[ultimos:n])
        # Agregar el arreglo original
        result.extend(arr)
        # Agregar los primeros x-1 elementos al final
        result.extend(arr[0:inicio])
    else:
        result = arr[:]
    
    return result

def main():
    n , x = map(int, stdin.readline().split())
    original = list(map(int, stdin.readline().split()))
    circular = arregloCircular(original, x)
    n = len(circular)
    MAXN = 1000
    tree = [None for _ in range(MAXN * 2)]
    pend = [0 for _ in range(MAXN * 2)]
    
    buildMin(circular,0,0,n - 1,tree)
    print("Árbol:")
    print(*tree[:2*n - 1])
    maxi = 0
    
    for i in range(n - x + 1):
        l = i
        r = i + x - 1
        aux = queryMin(0, 0, n - 1, l, r, tree, pend)
        if aux > maxi:
            maxi = aux
    
    print(maxi)
    
main()



"""
Sample Imput:
7 3
5 4 1 2 6 3 7
Sample Output:
4

"""