import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    W = SLI()
    W[-1] = W[-1][:-1]
    S = ["TAKAHASHIKUN", "Takahashikun", "takahashikun"]
    ans = 0
    for s in S:
        ans += W.count(s)
    print(ans)


if __name__ == "__main__":
    main()
