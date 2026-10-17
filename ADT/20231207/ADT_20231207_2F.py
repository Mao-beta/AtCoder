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
    P = NLI()
    P2I = {p: i for i, p in enumerate(P)}
    C = [0] * N
    for i in range(N):
        idx = P2I[i]
        C[(i - idx)%N] += 1
        C[(i+1 - idx) % N] += 1
        C[(i-1 - idx) % N] += 1

    print(max(C))


if __name__ == "__main__":
    main()
