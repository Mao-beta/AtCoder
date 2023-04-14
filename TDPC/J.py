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
    X = NLI()
    B = 0
    for x in X:
        B |= 1 << x

    def rec(bit):
        if bit == 0:
            return 0

        t = -1
        for i in range(16, -1, -1):
            if (bit >> i) & 1:
                t = i - 1
                break

        goto = []

        for tt in range(t - 1, t + 2):
            if tt < 0:
                continue
            if (bit >> tt) & 1:
                goto.append(bit ^ (1 << tt))

        ans = 3

        for g in goto:
            ans += rec(g)

        return ans / len(goto)

    print(rec(B))



if __name__ == "__main__":
    main()
