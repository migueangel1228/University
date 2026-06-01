import sys

NINF = float('-inf')


def fuji(u, t, web, tNode, mem, size):
    ans, k = NINF, (u, t)
    transmi = tNode[u]
    if k in mem:
        ans = mem[k]
    else:
        if len(web[u]) == 0:  # leaf
            if transmi and t == 1:
                ans = 0
            elif not transmi and t == 0:
                ans = 0
        else:
            mCases = [NINF] * (t + 1)
            if transmi:
                if t >= 1:
                    mCases[1] = 0
                tUsed = 1
            else:
                mCases[0] = 0
                tUsed = 0

            for v, w in web[u]:
                tMax = size[v]
                avilableNode = min(t, tUsed + tMax)
                # Traverse backwards to avoid double counting
                for node in range(avilableNode, -1, -1):
                    cAvilableNode = min(node, tMax)
                    for j in range(1, cAvilableNode + 1):
                        son = fuji(v, j, web, tNode, mem, size)
                        father = mCases[node - j]
                        if son != NINF and father != NINF:
                            posCoins = father + son + w
                            if posCoins > mCases[node]:
                                mCases[node] = posCoins
                tUsed += tMax
            ans = mCases[t]
        mem[k] = ans
    return ans


def findTransmi(root, web, tNodes, tSize):
    orden = []
    pila = [root]
    while pila:
        u = pila.pop()
        orden.append(u)
        for v, w in web[u]:
            pila.append(v)
    n = len(web)
    for i in range(n - 1, -1, -1):
        u = orden[i]
        ans = 1 if tNodes[u] else 0
        for v, w in web[u]:
            ans += tSize[v]
        tSize[u] = ans


def main():
    data = sys.stdin.read().split()
    i = 0
    while i < len(data):
        n = int(data[i])
        m = int(data[i + 1])
        q = int(data[i + 2])
        i += 3
        web = [[] for _ in range(n)]
        tNodes = [False] * n
        cNodes = set()
        for _ in range(n - 1):
            u = int(data[i])
            v = int(data[i + 1])
            w = int(data[i + 2])
            web[u].append((v, w))
            cNodes.add(v)
            i += 3
        for _ in range(m):
            t = int(data[i])
            tNodes[t] = True
            i += 1
        queries = [int(data[i + j]) for j in range(q)]
        i += q

        # Find the root (node without a parent)
        root = 0
        for k in range(n):
            if k not in cNodes:
                root = k
                break

        size = [0] * n
        findTransmi(root, web, tNodes, size)

        mem = {}
        for query in queries:
            maxCoins = 0
            if query <= m:
                if query <= 1:
                    maxCoins = 0
                else:
                    for posStart in range(n):
                        if tNodes[posStart]:
                            coins = fuji(posStart, query, web, tNodes, mem, size)
                            if coins != NINF:
                                maxCoins = max(maxCoins, coins)
            print(maxCoins)


if __name__ == "__main__":
    main()