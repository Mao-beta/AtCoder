import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 9
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def div_sparse_one(f: list, k, M):
    """(1-x^k)で割る x^Mまで"""
    res = f.copy()
    for i in range(M+1):
        if i+k <= M:
            res[i+k] += res[i]
            res[i+k] %= MOD
    return res


def main():
    T = NI()
    D = 10**5
    f = [0] * (D+1)
    f[0] = 1
    for k in range(1, 10):
        f = div_sparse_one(f, k, D)

    for _ in range(T):
        M = NI()
        ans = 0
        for i in range(M+1):
            if i * 111111 > M:
                break
            ans = (ans + f[i]) % MOD
        print(ans)


if __name__ == "__main__":
    main()
