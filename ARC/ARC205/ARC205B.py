import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    N, M = NMI()
    UV = EI(M)
    UV = [[x-1, y-1] for x, y in UV]
    D = [0] * N
    for u, v in UV:
        D[u] += 1
        D[v] += 1
    ans = N * (N-1) // 2 - sum([(N-1-d)%2 for d in D]) // 2
    print(ans)


if __name__ == "__main__":
    main()
