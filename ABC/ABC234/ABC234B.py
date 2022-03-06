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
    N = NI()
    XY = [NLI() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            xi, yi = XY[i]
            xj, yj = XY[j]
            ans = max(ans, (xi-xj)**2 + (yi-yj)**2)
    print(math.sqrt(ans))


if __name__ == "__main__":
    main()
