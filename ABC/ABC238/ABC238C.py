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
    K = len(str(N))
    ans = 0
    for k in range(K):
        start = pow(10, k)
        if k < K-1:
            end = start * 10 - 1
            end -= start - 1
            start = 1
            ans += (start + end) * (end - start + 1) // 2
        else:
            end = N
            end -= start - 1
            start = 1
            ans += (start + end) * (end - start + 1) // 2
        ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
