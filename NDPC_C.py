import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    N = NI()
    S = SLI()
    S = [[ord(ss)-ord("a") for ss in s] for s in S]
    Ms = [len(s) for s in S]
    dp = [[[[0]*(Ms[2]+1) for _ in range(Ms[1]+1)] for _ in range(Ms[0]+1)] for _ in range(N+1)]
    dp[0][0][0][0] = 1
    for i in range(N):
        for j0 in range(Ms[0]):
            s0 = S[0][j0]
            for j1 in range(Ms[1]):
                s1 = S[1][j1]
                for j2 in range(Ms[2]):
                    s2 = S[2][j2]
                    d = dp[i][j0][j1][j2]
                    for x in range(26):
                        nj0 = j0 if s0 != x else j0+1
                        nj1 = j1 if s1 != x else j1+1
                        nj2 = j2 if s2 != x else j2+1
                        if nj0 == Ms[0] or nj1 == Ms[1] or nj2 == Ms[2]:
                            continue
                        dp[i+1][nj0][nj1][nj2] += d
                        dp[i+1][nj0][nj1][nj2] %= MOD99
    ans = 0
    for j0 in range(Ms[0]):
        for j1 in range(Ms[1]):
            for j2 in range(Ms[2]):
                ans += dp[N][j0][j1][j2]
                ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
