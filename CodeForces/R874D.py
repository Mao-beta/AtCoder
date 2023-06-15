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
    T = NI()
    for _ in range(T):
        N = NI()
        P = NLI()

        if N == 1:
            print(1)
            continue

        m = P.index(N)
        if m == 0:
            m = P.index(N-1)

        # ...[...]N... -> N...[...]...
        # Nが最初のときは無理なのでN-1狙い
        Qs = []
        for l in range(m):
            Q = P[m:] + P[l:m][::-1] + P[:l]
            Qs.append(Q)

        if m == N-1:
            Q = P[m:] + P[:m]
            Qs.append(Q)

        Qs.sort(reverse=True)
        print(*Qs[0])


if __name__ == "__main__":
    main()
