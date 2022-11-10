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
    T = NI()
    N = NI()
    LR = [NLI() for _ in range(N)]
    imos = [0] * (T+1)
    for l, r in LR:
        imos[l] += 1
        imos[r] -= 1
    ans = list(accumulate(imos))
    print(*ans[:-1], sep="\n")


if __name__ == "__main__":
    main()
