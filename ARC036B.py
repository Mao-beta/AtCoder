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
    N = NI()
    H = [NI() for _ in range(N)]
    if N == 1:
        print(1)
        return

    A = [1] * N
    for i in range(1, N):
        if H[i-1] < H[i]:
            A[i] = A[i-1] + 1
        else:
            A[i] = 1
    B = [1] * N
    for i in range(N-2, -1, -1):
        if H[i] > H[i+1]:
            B[i] = B[i+1] + 1
        else:
            B[i] = 1

    ans = 1
    for a, b in zip(A, B):
        ans = max(ans, a+b-1)
    print(ans)


if __name__ == "__main__":
    main()
