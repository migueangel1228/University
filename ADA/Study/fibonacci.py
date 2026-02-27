from sys import stdin 

def fibo(num):
    if num == 1 or num == 0:
        ans = 1
    else:
        ans = fibo(num - 1) + fibo(num - 2)
    return ans

def fiboMemory(num,dicsito):
    if num == 1 or num == 0:
        ans = 1
    elif num in dicsito:
        ans = dicsito[num]
    else:
        ans = fiboMemory(num - 1,dicsito) + fiboMemory(num - 2,dicsito)
        dicsito[num] = ans
    return ans


def main():
    num = int(stdin.readline())
    dic = {}
    print(fiboMemory(num,dic))
    print(fibo(num))
    
main()