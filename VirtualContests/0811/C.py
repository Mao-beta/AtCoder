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
    N, H = NMI()
    AB = [NLI() for _ in range(N)]
    AB.sort(key=lambda x: -x[1])
    maxA = max([a for a, b in AB])
    # print(AB)
    ans = (H + maxA - 1) // maxA
    for i in range(N):
        b = AB[i][1]
        H -= b
        ans = min(ans, max(0, (H + maxA - 1) // maxA) + i+1)
    print(ans)


if __name__ == "__main__":
    main()
