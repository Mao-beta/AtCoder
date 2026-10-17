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
    N = NI()
    XY = EI(N)
    for i in range(N):
        xi, yi = XY[i]
        ans = N
        D = -1
        for j in range(N-1, -1, -1):
            if i == j:
                continue
            xj, yj = XY[j]
            d2 = (xi-xj)**2 + (yi-yj)**2
            if d2 >= D:
                D = d2
                ans = j+1
        print(ans)


if __name__ == "__main__":
    main()
