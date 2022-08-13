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


# PyPyではRE（isqrtがない）
def main():
    T = NI()
    F = [0] * 10**5
    C = [0] * 10**5
    F[1] = 1
    C[1] = 1
    for x in range(2, 10**5):
        rx = math.isqrt(x)
        F[x] = C[rx]
        C[x] = C[x-1] + F[x]

    for _ in range(T):
        X = NI()
        X1 = math.isqrt(X)
        X2 = math.isqrt(X1)
        ans = 0
        for y in range(1, X2+1):
            ans += F[y] * (X1 - y**2 + 1)
        print(ans)


if __name__ == "__main__":
    main()
