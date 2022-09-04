import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())



def LevelAncestor(N, G, root, querys):
    """
    :param N: 木の頂点数
    :param G: 木の隣接グラフ
    :param root: 根
    :param querys: 以下の形式のクエリのList
            (v, k): node vのk個祖先のnodeのindexを取得
    :return: クエリの解答のList O(N+Q)
    """
    q = len(querys)

    D = [[] for _ in range(N+1)]
    for i, (v, k) in enumerate(querys):
        D[v].append([k, i])

    # Pars[i][u]: uの2^i個祖先
    K = len(bin(N)[2:])
    Pars = [[N]*N for _ in range(K)]

    steps = [-1] * N
    que = deque()
    que.append(root)
    steps[root] = 0
    while que:
        now = que.popleft()
        step = steps[now]
        for goto in G[now]:
            if steps[goto] != -1:
                continue
            que.append(goto)
            Pars[0][goto] = now
            steps[goto] = step + 1

    # ダブリング
    for i in range(K-1):
        for u in range(N):
            if Pars[i][u] < N:
                Pars[i+1][u] = Pars[i][Pars[i][u]]

    # print(Pars)
    res = []

    for qi, (v, k) in enumerate(querys):
        if steps[v] < k:
            res.append(-1)
            continue

        for i in range(K):
            if (k >> i) & 1:
                # print(qi, i, v, k, steps[v])
                v = Pars[i][v]

        res.append(v)

    return res


def main():
    N = NI()
    AB = [NLI() for _ in range(N-1)]
    Q = NI()
    UK = [NLI() for _ in range(Q)]

    AB = [[x-1, y-1] for x, y in AB]
    UK = [[x-1, y] for x, y in UK]

    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)


    def bfs(s):
        dist = [-1] * N
        que = deque([s])
        dist[s] = 0
        while que:
            v = que.popleft()
            d = dist[v]
            for w in G[v]:
                if dist[w] >= 0:
                    continue
                dist[w] = d + 1
                que.append(w)
        d = max(dist)
        return dist.index(d)

    # u-vが直径
    u = bfs(0)
    v = bfs(u)

    LAU = LevelAncestor(N, G, u, UK)
    LAV = LevelAncestor(N, G, v, UK)

    # print(LAU)
    # print(LAV)

    for x, y in zip(LAU, LAV):
        if x == y == -1:
            print(-1)
        elif x == -1:
            print(y+1)
        else:
            print(x+1)


if __name__ == "__main__":
    main()
