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
    E = [0] * (N+1)
    E[N-1] = (N**2-N) * pow(2*N-1, MOD99-2, MOD99) % MOD99
    for i in range(N-2, -1, -1):
        E[i] = pow(N**2-i**2, MOD99-2, MOD99) * (
            (N-i)*(N-i-1)*E[i+2] + (N-i)*(i+1)*E[i+1] + i*(N-i)*(E[i+1]+1) + i**2) % MOD99
    print(E[0], E[1])


if __name__ == "__main__":
    main()
