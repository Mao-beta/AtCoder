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
    N, L, W = NMI()
    A = NLI() + [L]
    if A[0] % W:
        ans = A[0] // W + 1
    else:
        ans = A[0] // W

    for i in range(N):
        gap = A[i+1] - A[i] - W
        if gap < 0:
            continue
        if gap % W:
            ans += gap // W + 1
        else:
            ans += gap // W

    print(ans)



if __name__ == "__main__":
    main()
