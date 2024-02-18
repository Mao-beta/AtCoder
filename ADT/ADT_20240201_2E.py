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
    N, K = NMI()
    A = NLI()
    if K % 2 == 0:
        ans = 0
        for i in range(K//2):
            ans += A[2*i+1] - A[2*i]
        print(ans)

    else:
        ans = 0
        res = 0
        for i in range(K // 2):
            res += A[2 * i + 1] - A[2 * i]
        ans = res
        for i in range(K//2-1, -1, -1):
            a, b, c = 2*i, 2*i+1, 2*i+2
            res = res - (A[b]-A[a]) + (A[c]-A[b])
            ans = min(ans, res)
        print(ans)


if __name__ == "__main__":
    main()
