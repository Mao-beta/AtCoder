import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    A = NLI()
    M = NI()
    B = NLI()
    B.sort(reverse=True)
    Bok = [[0]*(1<<N) for _ in range(M)]
    for bi in range(M):
        for case in range(1<<N):
            w = 0
            for ai in range(N):
                if (case >> ai) & 1:
                    w += A[ai]
            if B[bi] >= w:
                Bok[bi][case] = 1
    # i個箱を見て、入れたおもちゃがcaseの状態にできるか
    dp = [[0]*(1<<N) for _ in range(M+1)]
    dp[0][0] = 1
    for i in range(M):
        for case in range(1<<N):
            if dp[i][case] == 0:
                continue
            for nc in range(1<<N):
                if case & nc:
                    continue
                if Bok[i][nc] == 0:
                    continue
                dp[i+1][case | nc] = 1
    for bi in range(M+1):
        if dp[bi][-1]:
            print(bi)
            return

    print(-1)


if __name__ == "__main__":
    main()
