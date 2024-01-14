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
    if K % 2:
        ans = 0
        for i in range(K // 2):
            ans += abs(A[i * 2] - A[i * 2 + 1])
        tmp = ans
        for i in range(-3, -K-1, -2):
            tmp -= abs(A[i]-A[i+1])
            tmp += abs(A[i+1]-A[i+2])
            ans = min(ans, tmp)
        print(ans)

    else:
        ans = 0
        for i in range(K//2):
            ans += abs(A[i*2] - A[i*2+1])
        print(ans)


if __name__ == "__main__":
    main()
