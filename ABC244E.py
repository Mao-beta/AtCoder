import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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


def main():
    N, M, K, S, T, X = NMI()
    UV = [NLI() for _ in range(M)]
    S, T, X = S-1, T-1, X-1
    UV = [[x-1, y-1] for x, y in UV]

    # dp[x][k][i]: k回移動後、頂点iにいて、x = Xの回数 % 2
    dp = [[[0]*N for _ in range(K+1)] for _ in range(2)]
    dp[0][0][S] = 1

    for k in range(K):
        for u, v in UV:
            for x in range(2):
                nk = k+1
                for m in range(2):
                    if m == 0:
                        fr, to = u, v
                    else:
                        fr, to = v, u

                    if to == X:
                        nx = x ^ 1
                    else:
                        nx = x

                    dp[nx][nk][to] += dp[x][k][fr]
                    dp[nx][nk][to] %= MOD99

    print(dp[0][K][T])


if __name__ == "__main__":
    main()
