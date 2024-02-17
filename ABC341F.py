import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N, M = NMI()
    UV = EI(M)
    W = NLI()
    A = NLI()
    G = [[] for _ in range(N)]
    for u, v in UV:
        u -= 1
        v -= 1
        if W[u] > W[v]:
            G[u].append(v)
        elif W[v] > W[u]:
            G[v].append(u)

    # 頂点iから始めた1個のコマの影響が何回で消えるか
    dp = [0] * N
    WX = [(w, x) for x, w in enumerate(W)]
    WX.sort()

    for w, x in WX:
        n = len(G[x])
        sdp = [[0]*w for _ in range(n+1)]
        for si in range(n):
            y = G[x][si]
            wy = W[y]
            dy = dp[y]
            for sj in range(w):
                sdp[si+1][sj] = max(sdp[si+1][sj], sdp[si][sj])
                if sj + wy < w:
                    sdp[si+1][sj+wy] = max(sdp[si+1][sj+wy], sdp[si][sj] + dy)
        dp[x] = max(sdp[-1]) + 1

    ans = 0
    for a, d in zip(A, dp):
        ans += a * d
    print(ans)


if __name__ == "__main__":
    main()
