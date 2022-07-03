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
    N, X = NMI()
    AB = [NLI() for _ in range(N)]
    ans = 10**20
    cum_a = 0
    cum_b = 0
    min_b = 10**20
    base_x = 0

    for a, b in AB:
        cum_a += a
        cum_b += b
        min_b = min(min_b, b)
        base = cum_a + cum_b
        base_x += 1

        rem = X - base_x
        # print(cum_a, cum_b, base_x, rem, min_b)
        if rem <= 0:
            ans = min(ans, base)
            break

        ans = min(ans, base + rem * min_b)

    print(ans)


if __name__ == "__main__":
    main()
