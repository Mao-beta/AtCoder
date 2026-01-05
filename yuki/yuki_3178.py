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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N = SI()
    C = [0] * 10
    for i, n in enumerate(N):
        C[int(n)] += 1
    ans = 0
    S = sum(C)
    P = [0] * 200002
    P[1] = 1
    for i in range(2, 200002):
        P[i] = P[i-1] * i % MOD99

    tmp = P[S]
    for i in range(10):
        if C[i]:
            tmp = tmp * pow(P[C[i]], -1, MOD99) % MOD99
    ans += tmp

    if C[0] > 0:
        C[0] -= 1
        S = sum(C)
        tmp = P[S]
        for i in range(10):
            if C[i]:
                tmp = tmp * pow(P[C[i]], -1, MOD99) % MOD99
        ans -= tmp

    print(ans % MOD99)


if __name__ == "__main__":
    main()
