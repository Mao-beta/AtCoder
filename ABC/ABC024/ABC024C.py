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
    N, D, K = NMI()
    LR = [NLI() for _ in range(D)]
    ST = [NLI() for _ in range(K)]
    for s, t in ST:
        for i, (l, r) in enumerate(LR, start=1):

            if not (l <= s <= r):
                continue

            if s < t:
                s = r
                if s >= t:
                    print(i)
                    break
            else:
                s = l
                if s <= t:
                    print(i)
                    break


if __name__ == "__main__":
    main()
