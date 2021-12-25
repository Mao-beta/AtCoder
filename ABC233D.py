import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate

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
    # input
    N, K = NMI()
    A = NLI()

    C = list(accumulate([0]+A))
    CC = defaultdict(int)
    ans = 0
    for c in C[::-1]:
        ans += CC[c+K]
        CC[c] += 1

    print(ans)


if __name__ == "__main__":
    main()
