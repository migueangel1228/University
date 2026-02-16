def algoritmo3 (A):
    m = None
    r = 0
    j = len(A) - 1
    while j >= 0:
        i, ac = 0, 0
        while i < j:
            if A[i] <= A[j]:
                ac = ac + 1
            i = i + 1
        if ac > r:
            r = ac
            m = A[j]
        j = j - 1
            
    return m
def main():
    b = [1,2,6,2,3]
    resultado = algoritmo3(b) 
    print(resultado)
    
main()