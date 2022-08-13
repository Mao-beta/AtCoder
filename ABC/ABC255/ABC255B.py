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
    N, K = NMI()
    A = NLI()
    XY = [NLI() for _ in range(N)]
    A = [x-1 for x in A]
    ans = 0

    for i in range(N):
        if i in A:
            continue

        x, y = XY[i]
        tmp = 10**10
        for a in A:
            ax, ay = XY[a]
            tmp = min(tmp, math.sqrt((ax-x)**2 + (ay-y)**2))

        ans = max(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
