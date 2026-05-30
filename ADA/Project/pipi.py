import sys
sys.setrecursionlimit(10**7)

NEG = -10**18


def solve_case(n, m, q, edges, transmissions, queries):
    adj = [[] for _ in range(n)]
    has_parent = [False] * n

    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        has_parent[v] = True

    root = 0
    for i in range(n):
        if not has_parent[i]:
            root = i
            break

    isT = [0] * n
    for t in transmissions:
        isT[t] = 1

    parent = [-1] * n
    children = [[] for _ in range(n)]
    order = []
    stack = [root]
    parent[root] = root

    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            children[u].append((v, w))
            stack.append(v)

    order.reverse()

    subT = [0] * n
    for u in order:
        subT[u] = isT[u]
        for v, _ in children[u]:
            subT[u] += subT[v]

    dp = [[NEG] * (m + 1) for _ in range(n)]
    best = [[NEG] * (m + 1) for _ in range(n)]

    for u in order:
        cur = [NEG] * (m + 1)
        if isT[u]:
            cur[1] = 0
        else:
            cur[0] = 0

        for v, w in children[u]:
            nxt = cur[:]
            lim_u = min(m, subT[u])
            lim_v = subT[v]
            for k in range(lim_u + 1):
                if cur[k] == NEG:
                    continue
                max_t = min(lim_v, m - k)
                for t in range(max_t + 1):
                    if dp[v][t] == NEG:
                        continue
                    val = cur[k] + dp[v][t] + (w if t > 0 else 0)
                    if val > nxt[k + t]:
                        nxt[k + t] = val
            cur = nxt

        dp[u] = cur
        best[u] = cur

    out = []
    for x in queries:
        if x < 0 or x > m:
            out.append("0")
        else:
            val = best[root][x]
            out.append("0" if val == NEG else str(max(0, val)))
    return out


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    out = []

    while idx + 2 < len(data):
        n = data[idx]
        m = data[idx + 1]
        q = data[idx + 2]
        idx += 3

        need = (n - 1) * 3 + m + q
        if idx + need > len(data):
            break

        edges = []
        for _ in range(n - 1):
            u = data[idx]
            v = data[idx + 1]
            w = data[idx + 2]
            idx += 3
            edges.append((u, v, w))

        transmissions = data[idx:idx + m]
        idx += m

        queries = data[idx:idx + q]
        idx += q

        out.extend(solve_case(n, m, q, edges, transmissions, queries))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()