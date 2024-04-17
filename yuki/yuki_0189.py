import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 9
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
    M, D = NMI()

    def solve(N):
        # N以下の正整数における数字和の分布
        # i桁決めて数字和がjで未満確定かどうか(k)
        dp = [[[0]*2 for _ in range(1801)] for _ in range(202)]
        N = str(N).zfill(201)
        dp[0][0][0] = 1
        for i in range(201):
            s = int(N[i])
            ni = i+1
            for j in range(1801):
                for k in range(2):
                    if dp[i][j][k] == 0:
                        continue
                    lim = 9 if k else s
                    for x in range(lim+1):
                        nj = j + x
                        if k == 0 and x == lim:
                            nk = 0
                        else:
                            nk = 1
                        dp[ni][nj][nk] += dp[i][j][k]
                        dp[ni][nj][nk] %= MOD
        res = [0] * 1801
        for j in range(1801):
            res[j] = sum(dp[201][j]) % MOD
        return res

    dpM = solve(M)
    dpD = solve(D)
    ans = 0
    for j in range(1, 1801):
        ans += dpM[j] * dpD[j]
    print(ans % MOD)


if __name__ == "__main__":
    main()
