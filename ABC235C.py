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


def main():
    N, Q = NMI()
    A = NLI()
    XK = [NLI() for _ in range(Q)]
    C = defaultdict(int)
    D = defaultdict(int)
    for i, a in enumerate(A, start=1):
        k = C[a] + 1
        C[a] += 1
        D[(a, k)] = i

    for x, k in XK:
        ans = D[(x, k)]
        print(-1 if ans == 0 else ans)


if __name__ == "__main__":
    main()
