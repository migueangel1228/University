'''
Solution Problem A - Winterim Backpacking Trip
Daniel Alejandro Posada Noguera - 8980619
15/03/2026
'''

from sys import stdin

N, K, INF, mem = int(), int(), float('inf'), dict()
distances, preffix = [-1 for _ in range(601)], [-1 for _  in range(601)]

def calc_preffix_sum():
    global distances, preffix, N
    ac = 0
    for i in range(N + 1):
        ac += distances[i]
        preffix[i] = ac

def sum_range(l, r):
    prev = preffix[l - 1] if l >= 1 else 0
    return preffix[r - 1] - prev

def phi(l, k):
    global mem, N, K, distances
    ans, c = INF, (l, k)
    if c in mem: ans = mem[c]
    else:
        if l == N: ans = distances[l] 
        elif k == 0: ans = sum_range(l, N + 1)
        else:
            low, high = l + 1, N + 1
            
            while high - low > 1:
                mid = low + ((high - low) >> 1)
                
                s, p = sum_range(l, mid), phi(mid, k - 1)
                
                if p >= s: low = mid
                else: high = mid
                ans = min(ans, max(s, p))
                
            if low == l + 1 or high == N + 1:
                s = sum_range(l, low) if low == l + 1 else sum_range(l, high - 1)
                p = phi(low, k - 1) if low == l + 1 else phi(high - 1, k - 1)
                ans = min(ans, max(s, p))
        mem[c] = ans
    return ans


def solve():
    calc_preffix_sum()
    s = phi(0, K)
    print(s)

def main():
    global N, K
    line = stdin.readline()
    while line != '':
        N, K = map(int, line.split())
        mem.clear()
        for i in range(N + 1):
            distances[i] = int(stdin.readline())
        solve()
        line = stdin.readline()

main()