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
    N, K = NMI()
    S = SI()
    dp = [[0]*(1<<K) for _ in range(N+1)]
    # A:0 B:1
    P = set()
    for p in product("AB", repeat=K):
        if p == p[::-1]:
            x = 0
            for pp in p:
                x <<= 1
                x |= int(pp == "B")
            P.add(x)
    if S[0] == "A":
        dp[1][0] = 1
    elif S[0] == "B":
        dp[1][1] = 1
    else:
        dp[1][0] = 1
        dp[1][1] = 1

    MASK = (1<<K) - 1

    # print([bin(p)[2:].zfill(K) for p in P])

    for i in range(1, N):
        s = S[i]
        for j in range(1<<K):
            if s == "A":
                nj = (j << 1) & MASK
                if i >= K-1 and nj in P:
                    continue
                dp[i+1][nj] += dp[i][j]
                dp[i + 1][nj] %= MOD99
            elif s == "B":
                nj = ((j << 1) | 1) & MASK
                if i >= K-1 and nj in P:
                    continue
                dp[i + 1][nj] += dp[i][j]
                dp[i + 1][nj] %= MOD99
            else:
                for b in range(2):
                    nj = ((j << 1) | b) & MASK
                    if i >= K-1 and nj in P:
                        continue
                    dp[i + 1][nj] += dp[i][j]
                    dp[i + 1][nj] %= MOD99
    # print(*dp, sep="\n")
    print(sum(dp[-1]) % MOD99)


if __name__ == "__main__":
    main()
