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


def main(N, K):

    S = str(K)
    RS = S[::-1]
    R = int(RS)

    ans = 0
    if K == R:
        now = K
        while now <= N:
            ans += 1
            now *= 10

    elif K % 10 == 0:
        ans = 0

    elif K > R:
        ans = 0

    else:
        now = K
        while now <= N:
            ans += 1
            now *= 10

        now = R
        while now <= N:
            ans += 1
            now *= 10

    return ans


def calc(K):
    res = 10**20
    for i in range(10):
        res = min(res, K)
        K = int(str(K)[::-1])
    return res


if __name__ == "__main__":
    # N = 1000
    # MX = 1000
    # ans = [0] * (N+1)
    # for x in range(1, N+1):
    #     ans[calc(x)] += 1
    #
    # for K in range(1, N+1):
    #     if ans[K] != main(N, K):
    #         print(K)
    N, K = NMI()
    print(main(N, K))

