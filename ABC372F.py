import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N, M, K = NMI()
    XY = EI(M)

    if M == 0:
        print(1)
        return

    XY = [[x-1, y-1] for x, y in XY]
    X = sorted(list(set(x for x, y in XY)))
    Y = sorted(list(set(y for x, y in XY)))
    Z, UZ = compress(X + Y)
    ZN = len(Z)
    XY.sort()
    G = [[] for _ in range(ZN)]
    # jump
    for i, (x, y) in enumerate(XY):
        # print("jump", x, y, 1, file=sys.stderr)
        G[Z[x]].append([Z[y], 1])
    # next
    for i in range(ZN):
        x, nx = UZ[i], UZ[(i+1)%ZN]
        d = nx - x if nx > x else nx + N - x
        G[i].append([(i+1)%ZN, d])
        # print("next", i, i + 1, x, nx, d, file=sys.stderr)
    dp = [[0]*ZN for _ in range(K+1)]
    if UZ[0] > K:
        print(1)
        return
    dp[UZ[0]][0] = 1
    ans = 0
    # print(*G, sep="\n", file=sys.stderr)
    # print(f"{K=} {ZN=}", file=sys.stderr)
    for i in range(K):
        for j in range(ZN):
            for nj, d in G[j]:
                ni = i + d
                if ni <= K:
                    # print(ni, nj, i, j, ZN, file=sys.stderr)
                    dp[ni][nj] += dp[i][j]
                    dp[ni][nj] %= MOD99
                else:
                    ans += dp[i][j]
    for j in range(ZN):
        ans += dp[K][j]
    print(ans % MOD99)


if __name__ == "__main__":
    main()
