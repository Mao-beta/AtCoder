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
    N, D, P = NMI()
    F = NLI()
    F.sort()
    C = list(accumulate([0]+F))
    ans = 10**20
    for i in range(N//D + 2):
        x = i * D
        if x > N:
            x = N
        ans = min(ans, C[N-x] + i*P)
    print(ans)


if __name__ == "__main__":
    main()
