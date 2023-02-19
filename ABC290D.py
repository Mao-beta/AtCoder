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


def solve(N, D, K):
    g = math.gcd(D, N)
    if g == 1:
        ans = D * (K-1) % N
        return ans

    loop = N // g
    i, j = divmod((K-1), loop)
    ans = (i + D * j) % N
    return ans


def main():
    T = NI()
    for _ in range(T):
        N, D, K = NMI()
        print(solve(N, D, K))


if __name__ == "__main__":
    main()
