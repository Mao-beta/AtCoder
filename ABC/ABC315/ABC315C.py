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
    FS = EI(N)
    D = [[] for _ in range(N+1)]
    Ms = []
    for f, s in FS:
        D[f].append(s)
    ans = 0
    for f in range(N+1):
        D[f].sort(reverse=True)
        if D[f]:
            Ms.append(D[f][0])
        if len(D[f]) >= 2:
            ans = max(ans, D[f][0] + D[f][1] // 2)
    Ms.sort(reverse=True)
    if len(Ms) >= 2:
        ans = max(ans, Ms[0] + Ms[1])
    print(ans)


if __name__ == "__main__":
    main()
