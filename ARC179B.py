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
    M, N = NMI()
    X = NLI()
    X = [x-1 for x in X]
    P = 1 << M
    dp = [0] * P
    dp[0] = 1

    njs = [[0]*M for _ in range(P)]
    for j in range(P):
        for a in range(M):
            # 次をaにする
            ok = True
            nj = j
            for b, xb in enumerate(X):
                if b == xb:
                    continue

                if (j >> b) & 1 == 0:
                    if a == b:
                        nj ^= 1 << b
                else:
                    if a == b:
                        ok = False
                        break
                    elif a == xb:
                        nj ^= 1 << b
            if ok:
                njs[j][a] = nj
            else:
                njs[j][a] = -1


    for i in range(N):
        dp2 = [0] * P
        for j in range(P):
            if dp[j] == 0:
                continue
            for a in range(M):
                # 次をaにする
                nj = njs[j][a]

                if nj != -1:
                    dp2[nj] += dp[j]
                    dp2[nj] %= MOD99

        dp, dp2 = dp2, dp

    print(sum(dp) % MOD99)


if __name__ == "__main__":
    main()
