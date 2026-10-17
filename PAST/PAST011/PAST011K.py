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
    S = SI()
    T = SI()
    N = len(S)
    M = len(T)
    BS = [[] for _ in range(26)]
    BT = [[] for _ in range(26)]
    for i, s in enumerate(S):
        s = ord(s) - ord("a")
        BS[s].append(i)
    for i, s in enumerate(T):
        s = ord(s) - ord("a")
        BT[s].append(i)
    for w in range(26):
        BS[w].append(N)
        BT[w].append(M)

    BS2 = [[0]*(N+1) for _ in range(26)]
    BT2 = [[0]*(M+1) for _ in range(26)]
    for w in range(26):
        for i in range(N+1):
            x = BS[w][bisect.bisect_left(BS[w], i)] + 1
            BS2[w][i] = x
        for j in range(M+1):
            x = BT[w][bisect.bisect_left(BT[w], j)] + 1
            BT2[w][j] = x

    dp = [[0]*(M+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N+1):
        for j in range(M+1):
            for w in range(26):
                ni = BS2[w][i]
                nj = BT2[w][j]
                if ni > N or nj > M:
                    continue
                dp[ni][nj] += dp[i][j]
                dp[ni][nj] %= MOD99

    dps = [0] * (N+1)
    dps[0] = 1
    for i in range(N+1):
        for w in range(26):
            ni = BS2[w][i]
            if ni > N:
                continue
            dps[ni] += dps[i]
            dps[ni] %= MOD99

    dpt = [0] * (M + 1)
    dpt[0] = 1
    for i in range(M+1):
        for w in range(26):
            ni = BT2[w][i]
            if ni > M:
                continue
            dpt[ni] += dpt[i]
            dpt[ni] %= MOD99

    res = sum(sum(row) % MOD99 for row in dp)
    ans = sum(dps) + sum(dpt) - res - 1
    print(ans % MOD99)


if __name__ == "__main__":
    main()
