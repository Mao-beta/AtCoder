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


def main():
    N, S, T = NMI()
    L = [[0, 0, 0, 0]] + EI(N)
    INF = 10**18
    ans = INF

    for P in permutations(range(1, N+1)):
        P = [0] + list(P)
        # print(P)
        dp = [[INF]*2 for _ in range(N+1)]
        dp[0][0] = 0.0
        dp[0][1] = 0.0
        for i in range(N):
            a, b, c, d = L[P[i]]
            na, nb, nc, nd = L[P[i+1]]
            # print(L[P[i]], L[P[i+1]])
            for j in range(2):
                if dp[i][j] >= INF:
                    continue
                if j:
                    x, y = c, d
                else:
                    x, y = a, b
                for nj in range(2):
                    if nj:
                        nx, ny = nc, nd
                    else:
                        nx, ny = na, nb
                    t = math.sqrt((x-nx) ** 2 + (y-ny) ** 2) / S
                    t += math.sqrt((na-nc) ** 2 + (nb-nd) ** 2) / T
                    dp[i+1][nj^1] = min(dp[i+1][nj^1], dp[i][j] + t)
        # print(*dp, sep="\n")
        ans = min(ans, min(dp[-1]))
    print(ans)


if __name__ == "__main__":
    main()
