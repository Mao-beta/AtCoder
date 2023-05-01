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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N = NI()
    S = SI()

    for i in range(N):
        if i < N-2 and S[i] == S[i+2] and S[i] != "?":
            print(0)
            exit()

        if i < N-1 and S[i] == S[i+1] and S[i] != "?":
            print(0)
            exit()

    if N == 2:
        q = S.count("?")
        if q == 0:
            print(1)
            exit()
        elif q == 1:
            print(25)
            exit()
        else:
            print(26 * 25)
            exit()

    dp = [[[0]*26 for _ in range(26)] for _ in range(N+1)]

    if S[0] != "?" and S[1] != "?":
        s0 = ord(S[0]) - ord("a")
        s1 = ord(S[1]) - ord("a")
        dp[2][s0][s1] = 1

    elif S[0] != "?" and S[1] == "?":
        s0 = ord(S[0]) - ord("a")
        for s1 in range(26):
            if s0 != s1:
                dp[2][s0][s1] = 1

    elif S[0] == "?" and S[1] != "?":
        s1 = ord(S[1]) - ord("a")
        for s0 in range(26):
            if s0 != s1:
                dp[2][s0][s1] = 1

    else:
        for s0 in range(26):
            for s1 in range(26):
                if s0 != s1:
                    dp[2][s0][s1] = 1

    for i, s in enumerate(S[2:], start=2):
        for j in range(26):
            for k in range(26):
                if s != "?":
                    ss = ord(s) - ord("a")
                    if ss == j or ss == k:
                        continue
                    ns = ss
                    dp[i+1][k][ns] += dp[i][j][k]
                    dp[i+1][k][ns] %= MOD99
                else:
                    for ns in range(26):
                        if ns == j or ns == k:
                            continue
                        dp[i+1][k][ns] += dp[i][j][k]
                        dp[i+1][k][ns] %= MOD99

    ans = 0
    for s0 in range(26):
        for s1 in range(26):
            ans += dp[-1][s0][s1]
            ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
