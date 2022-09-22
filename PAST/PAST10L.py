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
    K, M = NMI()
    CD = [NLI() for _ in range(K)]
    B = 42
    f = [[0]*B for i in range(10)]

    P10 = [10 % M]
    for i in range(B):
        P10.append(P10[-1] * P10[-1] % M)

    for c in range(10):
        for i in range(B):
            if i == 0:
                f[c][i] = c % M
            else:
                f[c][i] = f[c][i-1] * (P10[i-1] + 1) % M

    ans = 0
    for c, d in CD:
        for i in range(B):
            if (d >> i) & 1 == 0:
                continue

            ans = ans * P10[i] % M + f[c][i]
            ans %= M

    print(ans)


if __name__ == "__main__":
    main()
