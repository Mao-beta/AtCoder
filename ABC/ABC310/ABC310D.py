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
    N, T, M = NMI()
    AB = EI(M)
    AB = [[x-1, y-1] for x, y in AB]
    ng = [[0]*N for _ in range(N)]
    for a, b in AB:
        ng[a][b] = 1
        ng[b][a] = 1

    # print(*ng, sep="\n")
    # 既にi組できていて既に属している人の集合がj
    dp = [[0]*(1<<N) for _ in range(T+1)]
    dp[0][0] = 1
    for j in range(1<<N):
        target = 0
        for t in range(N):
            if (j>>t) & 1 == 0:
                target = t
                break
        tb = 1 << target
        for p in range(1<<(N-target-1)):
            p = (p << (target+1)) | tb
            if (j | p) != j + p:
                continue
            ok = True
            for a, b in AB:
                if (p>>a)&1 and (p>>b)&1 and ng[a][b]:
                    # print(a, b, bin(j), bin(p), "#")
                    ok = False
            if not ok:
                continue
            # print(bin(j), bin(p))
            nj = j | p
            for i in range(T):
                dp[i+1][nj] += dp[i][j]

    # print(*dp, sep="\n")
    print(dp[T][-1])


if __name__ == "__main__":
    main()
