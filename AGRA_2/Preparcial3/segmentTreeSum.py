"""
Segment Tree Implementation
Carlos Ramírez
Noviembre 7 de 2020

Update with lazy propagation
Adding on segments, range max query (RMQ)

"""

#Segment tree is represented as a list
n, MAXN = int(), 1000
tree = [None for _ in range(MAXN * 2)]
pend = [0 for _ in range(MAXN * 2)]

#build the segment tree
def build(a, v, l, r):
  if l == r: tree[v] = a[l]
  else:
    m = l + ((r - l) >> 1)
    build(a, v + 1, l, m)
    build(a, v + 2 * (m - l + 1), m + 1, r)
    tree[v] = tree[v + 1] + tree[v + 2 * (m - l + 1)]
        
#query
def query(v, L, R, l, r):
  ans = None
  if l > r: ans = 0
  elif l == L and r == R: ans = tree[v]
  else:
    m = L + ((R - L) >> 1)
    push(v, v + 1, v + 2 * (m - L + 1), L, m, R)
    ans = query(v + 1, L, m, l, min(r, m)) + query(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r)
  return ans

#update query
def update(v, L, R, l, r, h):
  if l <= r:
    if l == L and r == R: tree[v] += h * (r - l + 1) ; pend[v] += h
    else:
      m = L + ((R - L) >> 1)
      push(v, v + 1, v + 2 * (m - L + 1), L, m, R)
      update(v + 1, L, m, l, min(r, m), h)
      update(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r, h)
      tree[v] = tree[v + 1] + tree[v + 2 * (m - L + 1)]

def push(v, v1, v2, l, m, r):
  tree[v1] += pend[v] * (m - l + 1)
  pend[v1] += pend[v]
  tree[v2] += pend[v] * (r - (m + 1) + 1)
  pend[v2] += pend[v]
  pend[v] = 0
            
n = 9
build([3, 2, 5, 7, 4, 6, 2, 5, 4], 0, 0, n - 1)
print("Árbol:")
print(*tree[:2*n - 1])

print(query(0, 0, n - 1, 1, 6))
print(query(0, 0, n - 1, 4, 8))
update(0, 0, n - 1, 0, 5, 9)

print("Árbol:")
print(*tree[:2*n - 1])

print("Pendiente:")
print(*pend[:2*n - 1])

print(query(0, 0, n - 1, 1, 4))

print("Árbol:")
print(*tree[:2*n - 1])

print("Pendiente:")
print(*pend[:2*n - 1])

print(query(0, 0, n - 1, 5, 8))

print("Árbol:")
print(*tree[:2*n - 1])

print("Pendiente:")
print(*pend[:2*n - 1])

update(0, 0, n - 1, 2, 6, 4)

print("Árbol:")
print(*tree[:2*n - 1])

print("Pendiente:")
print(*pend[:2*n - 1])

print(query(0, 0, n - 1, 6, 8))

print("Árbol:")
print(*tree[:2*n - 1])

print("Pendiente:")
print(*pend[:2*n - 1])