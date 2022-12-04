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
    N, P = NMI()
    E = [0] * (N+1)
    E[1] = 1
    c = P * pow(100, MOD99-2, MOD99) % MOD99
    p = (100-P) * pow(100, MOD99-2, MOD99) % MOD99
    for i in range(2, N+1):
        E[i] = (E[i-1] * p + E[i-2] * c + 1) % MOD99
    print(E[-1])


if __name__ == "__main__":
    main()
