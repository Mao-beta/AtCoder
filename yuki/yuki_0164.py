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


def f(s):
    try:
        return int(s)
    except:
        return ord(s) - ord("A") + 10


def main():
    N = NI()
    V = [[f(s) for s in SI()] for _ in range(N)]

    ans = 36**12

    for v in V:
        tmp = 0
        M = max(v) + 1
        for i, x in enumerate(v[::-1]):
            tmp += x * M**i
        ans = min(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
