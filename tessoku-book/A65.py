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
    N = NI()
    A = [0, 0] + NLI()
    C = [[] for _ in range(N+1)]
    for i, a in enumerate(A):
        C[a].append(i)

    ans = [0] * (N+1)

    def rec(i):
        res = 0
        for c in C[i]:
            x = rec(c)
            res += x
        ans[i] = res
        return res + 1

    rec(1)
    print(*ans[1:])


if __name__ == "__main__":
    main()
