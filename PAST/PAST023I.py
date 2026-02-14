import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N, Y = NMI()
    SX = [SLI() for _ in range(N)]
    SX = [[set(s), int(x)] for s, x in SX]
    ans = 0
    for b in range(1<<N):
        w = set()
        x = 0
        for i in range(N):
            if (b >> i) & 1:
                w |= SX[i][0]
                x += SX[i][1]
        if x <= Y:
            ans = max(ans, len(w))
    print(ans)


if __name__ == '__main__':
    main()