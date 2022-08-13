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
    h1, h2, h3, w1, w2, w3 = NMI()

    ans = 0
    for a11 in range(1, 29):
        for a12 in range(1, 29):
            for a21 in range(1, 29):
                for a22 in range(1, 29):
                    a31 = w1 - a11 - a21
                    a32 = w2 - a12 - a22
                    a13 = h1 - a11 - a12
                    a23 = h2 - a21 - a22
                    if a31 <= 0 or a32 <= 0 or a13 <= 0 or a23 <= 0:
                        continue

                    a33 = h3 - a31 - a32
                    if a33 != w3 - a13 - a23 or a33 <= 0:
                        continue
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
