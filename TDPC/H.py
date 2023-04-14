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
    N, W, C = NMI()
    WVC = EI(N)
    C2WV = [[] for _ in range(51)]
    for w, v, c in WVC:
        C2WV[c].append([w, v])
    INF = 10**15

    dp = [[-INF]*(W+1) for _ in range(C+1)]
    dp[0][0] = 0

    for WV in C2WV:
        w2v = [-INF] * (W+1)
        w2v[0] = 0
        for w, v in WV:
            for j in range(W, -1, -1):
                if j+w <= W:
                    w2v[j+w] = max(w2v[j+w], w2v[j] + v)
        Pwv = [[w, v] for w, v in enumerate(w2v) if v > 0]

        for c in range(C-1, -1, -1):
            for i in range(W, -1, -1):
                if dp[c][i] < 0:
                    continue
                for w, v in Pwv[::-1]:
                    if i+w <= W:
                        dp[c+1][i+w] = max(dp[c+1][i+w], dp[c][i] + v)

    ans = 0
    for d in dp:
        ans = max(ans, max(d))
    print(ans)




if __name__ == "__main__":
    main()
