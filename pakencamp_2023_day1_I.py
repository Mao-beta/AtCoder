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
    ans = []
    for i in range(N):
        m = A[-1]
        t = N-1
        for j in range(N-1, i-1, -1):
            if A[j] < m:
                m = A[j]
                t = j
        now = t
        while now > i:
            ans.append(now)
            A[now-1], A[now] = A[now], A[now-1]
            A[now] += K
            now -= 1
    # print(A)
    print(len(ans))
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
