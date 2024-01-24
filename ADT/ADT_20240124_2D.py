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
    N, S, M, L = NMI()
    ans = 10**18
    for i in range(101):
        for j in range(101):
            for k in range(101):
                egg = i*6 + j*8 + k*12
                m = i*S + j*M + k*L
                if egg >= N:
                    ans = min(ans, m)
    print(ans)


if __name__ == "__main__":
    main()
