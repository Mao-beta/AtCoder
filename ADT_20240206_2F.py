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


def main():
    N, M = NMI()
    A = NLI()
    sb = 0
    s = 0
    for i in range(M):
        sb += (i+1) * A[i]
        s += A[i]
    ans = sb
    for i in range(M, N):
        sb = sb - s + M * A[i]
        s = s + A[i] - A[i-M]
        ans = max(ans, sb)
    print(ans)


if __name__ == "__main__":
    main()
