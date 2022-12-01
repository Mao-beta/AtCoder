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
    N, D = NMI()
    XY = [NLI() for _ in range(N)]
    heapify(XY)
    Y = []
    ans = 0
    for day in range(1, D+1):
        while XY and XY[0][0] <= day:
            x, y = heappop(XY)
            heappush(Y, -y)
        if Y:
            ans += heappop(Y) * (-1)
    print(ans)


if __name__ == "__main__":
    main()
