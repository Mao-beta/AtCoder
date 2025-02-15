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
    N, D, K = NMI()
    if sum(N-i for i in range(K)) < D:
        print(-1)
        return

    res = list(range(1, K+1))
    if sum(res) > D:
        print(-1)
        return
    rem = D - sum(res)
    for i in range(K):
        v = res[K-1-i]
        m = N-i
        if rem >= m-v:
            rem -= m-v
            res[K-1-i] = m
        else:
            res[K-1-i] += rem
            rem = 0
        if rem == 0:
            break
    print(*res)


if __name__ == "__main__":
    main()
