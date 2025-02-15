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
    L = NLI()
    Q = NI()
    K = NLI()
    ans = [0] * 500001
    hq = [[-l, 1, l] for l in L]
    heapify(hq)
    for i in range(500000):
        x, k, l = heappop(hq)
        x = -x
        ans[i+1] = x
        heappush(hq, [-l/(k+1), k+1, l])

    for k in K:
        print(ans[k])


if __name__ == "__main__":
    main()
